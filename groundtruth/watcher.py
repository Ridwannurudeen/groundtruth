from __future__ import annotations

import argparse
import asyncio
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import UUID

from groundtruth.answer import answer
from groundtruth.contradictions import (
    add_contradiction_edge,
    graph_contradiction_edges,
    judge_retraction_contradiction,
    ledger_edges,
)
from groundtruth.ingest import normalize_doi, parse_year, store_claim_deterministic
from groundtruth.registry import (
    CLAIMS_PATH,
    DATASETS,
    SEED_CORPUS_PATH,
    claim_topic,
    load_claims,
    load_seed,
    save_claims,
    write_json,
)
from groundtruth.runtime import DATA_DIR, DOCS_DIR, import_cognee


AUDIT_LOG_PATH = DATA_DIR / "audit_log.jsonl"
GROUNDTRUTH_DATASET = "groundtruth_memory"
NAIVE_DATASET = "naive_memory"


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def compact_json(value: Any) -> Any:
    if hasattr(value, "model_dump"):
        return value.model_dump(mode="json")
    if isinstance(value, list):
        return [compact_json(item) for item in value]
    if isinstance(value, tuple):
        return [compact_json(item) for item in value]
    if isinstance(value, dict):
        return {str(key): compact_json(item) for key, item in value.items()}
    if isinstance(value, UUID):
        return str(value)
    return value


def append_audit(path: Path, event: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    event = {"timestamp": now(), **event}
    with path.open("a", encoding="utf-8") as audit_file:
        audit_file.write(json.dumps(compact_json(event), sort_keys=True) + "\n")


def load_registry(path: Path = CLAIMS_PATH) -> list[dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def save_registry(entries: list[dict[str, Any]], path: Path = CLAIMS_PATH) -> None:
    if path == CLAIMS_PATH:
        save_claims(entries)
    else:
        write_json(path, entries)


def retraction_index(seed: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        normalize_doi(item["original_doi"]): item
        for item in seed.get("held_back_retractions", [])
        if normalize_doi(item.get("original_doi"))
    }


def find_claim(claims: list[dict[str, Any]], doi: str) -> dict[str, Any]:
    normalized = normalize_doi(doi)
    for claim in claims:
        if normalize_doi(claim["doi"]) == normalized:
            return claim
    raise RuntimeError(f"Claim not found for DOI: {doi}")


def retraction_notice_claim(claim: dict[str, Any], retraction: dict[str, Any]) -> dict[str, Any]:
    retraction_doi = normalize_doi(retraction.get("retraction_doi")) or (
        f"retraction:{claim['doi']}"
    )
    retraction_year = parse_year(retraction.get("retraction_date")) or claim["source"]["year"]
    reason = str(retraction.get("reason") or "No reason supplied").strip()
    title = claim["source"]["title"]
    return {
        "claim_id": f"{claim['claim_id']}-NOTICE",
        "claim_text": (
            f"The retraction notice says that {title} (DOI {claim['doi']}) "
            f"was retracted. Reason: {reason}."
        ),
        "status_at_seed": "retraction_notice",
        "supersedes_doi": claim["doi"],
        "source": {
            "title": f"Retraction notice for {title}",
            "journal": "Retraction Watch / Crossref",
            "year": retraction_year,
            "doi": retraction_doi,
            "subject": claim["source"].get("subject", ""),
            "source_type": "retraction_notice",
        },
        "cohort": "retraction_notice",
    }


def active_retracted_claims(
    claims: list[dict[str, Any]],
    seed: dict[str, Any],
    dataset_names: tuple[str, str] = DATASETS,
) -> list[dict[str, Any]]:
    indexed = retraction_index(seed)
    selected = []
    for claim in claims:
        if normalize_doi(claim["doi"]) not in indexed:
            continue
        if not all(name in claim.get("datasets", {}) for name in dataset_names):
            continue
        if str(claim.get("status")) == "active":
            selected.append(claim)
    return selected


async def check(
    doi: str,
    *,
    seed_path: Path = SEED_CORPUS_PATH,
) -> dict[str, Any] | None:
    return retraction_index(load_seed(seed_path)).get(normalize_doi(doi))


async def process_retraction(
    doi: str,
    *,
    registry_path: Path = CLAIMS_PATH,
    seed_path: Path = SEED_CORPUS_PATH,
    audit_log_path: Path = AUDIT_LOG_PATH,
    dataset_names: tuple[str, str] = DATASETS,
) -> dict[str, Any]:
    naive_dataset, groundtruth_dataset = dataset_names
    os.environ["COGNEE_SKIP_CONNECTION_TEST"] = "true"
    cognee = import_cognee()
    claims = load_registry(registry_path)
    seed = load_seed(seed_path)
    retraction = await check(doi, seed_path=seed_path)
    if retraction is None:
        raise RuntimeError(f"No held-back retraction found for DOI: {doi}")

    claim = find_claim(claims, doi)
    append_audit(
        audit_log_path,
        {
            "claim_id": claim["claim_id"],
            "doi": claim["doi"],
            "action": "detected_retraction",
            "retraction": retraction,
        },
    )

    notice_claim = retraction_notice_claim(claim, retraction)
    notice_entries: dict[str, dict[str, str]] = {}
    for dataset_name in dataset_names:
        dataset_entry = claim["datasets"][dataset_name]
        if "retraction_notice_data_id" in dataset_entry:
            notice_entries[dataset_name] = {
                "dataset_id": dataset_entry["dataset_id"],
                "data_id": dataset_entry["retraction_notice_data_id"],
            }
            continue
        notice_entry = await store_claim_deterministic(cognee, notice_claim, dataset_name)
        dataset_entry["retraction_notice_data_id"] = notice_entry["data_id"]
        dataset_entry["retraction_notice_doi"] = notice_claim["source"]["doi"]
        notice_entries[dataset_name] = notice_entry
        append_audit(
            audit_log_path,
            {
                "claim_id": claim["claim_id"],
                "doi": claim["doi"],
                "dataset": dataset_name,
                "action": "remembered_retraction_notice",
                "notice_data_id": notice_entry["data_id"],
            },
        )

    decision = judge_retraction_contradiction(claim, retraction)
    if not decision.contradicts or decision.confidence < 0.7:
        append_audit(
            audit_log_path,
            {
                "claim_id": claim["claim_id"],
                "doi": claim["doi"],
                "action": "skipped_low_confidence_contradiction",
                "decision": decision.model_dump(mode="json"),
            },
        )
        save_registry(claims, registry_path)
        return {"claim_id": claim["claim_id"], "decision": decision.model_dump(mode="json")}

    groundtruth_entry = claim["datasets"][groundtruth_dataset]
    groundtruth_dataset_id = UUID(groundtruth_entry["dataset_id"])
    edge_result = await add_contradiction_edge(
        cognee,
        dataset_id=groundtruth_dataset_id,
        superseding_data_id=UUID(groundtruth_entry["retraction_notice_data_id"]),
        superseded_data_id=UUID(groundtruth_entry["data_id"]),
        decision=decision,
    )
    graph_edges_before_forget = await graph_contradiction_edges(groundtruth_dataset_id)
    ledger_edges_before_forget = await ledger_edges(
        groundtruth_dataset_id,
        UUID(groundtruth_entry["retraction_notice_data_id"]),
        "contradicts",
    )
    append_audit(
        audit_log_path,
        {
            "claim_id": claim["claim_id"],
            "doi": claim["doi"],
            "dataset": groundtruth_dataset,
            "action": "added_contradiction_edge",
            "edge": edge_result,
            "graph_edge_count": len(graph_edges_before_forget),
            "ledger_edge_count": len(ledger_edges_before_forget),
        },
    )

    forget_result = await cognee.forget(
        data_id=UUID(groundtruth_entry["data_id"]),
        dataset_id=groundtruth_dataset_id,
        memory_only=True,
    )
    graph_edges_after_forget = await graph_contradiction_edges(groundtruth_dataset_id)
    claim["status"] = "retracted_forgotten"
    claim["retraction"] = retraction
    claim["datasets"][groundtruth_dataset]["status"] = "retracted_forgotten"
    if naive_dataset in claim["datasets"]:
        claim["datasets"][naive_dataset]["status"] = "retracted_retained"
    save_registry(claims, registry_path)

    append_audit(
        audit_log_path,
        {
            "claim_id": claim["claim_id"],
            "doi": claim["doi"],
            "dataset": groundtruth_dataset,
            "action": "forgot_superseded_claim",
            "forget_result": forget_result,
            "graph_edges_after_forget": len(graph_edges_after_forget),
        },
    )
    return {
        "claim_id": claim["claim_id"],
        "doi": claim["doi"],
        "decision": decision.model_dump(mode="json"),
        "notice_entries": notice_entries,
        "edge_result": compact_json(edge_result),
        "graph_edges_before_forget": len(graph_edges_before_forget),
        "ledger_edges_before_forget": len(ledger_edges_before_forget),
        "forget_result": forget_result,
        "graph_edges_after_forget": len(graph_edges_after_forget),
    }


async def scripted_run(count: int = 3) -> list[dict[str, Any]]:
    claims = load_claims()
    seed = load_seed()
    selected = active_retracted_claims(claims, seed)[:count]
    if len(selected) != count:
        raise RuntimeError(f"Only found {len(selected)} active retracted claims")

    runs = []
    for claim in selected:
        question = f"what does the research say about {claim_topic(claim)}?"
        before = {
            dataset_name: await answer(question, dataset_name) for dataset_name in DATASETS
        }
        watcher_result = await process_retraction(claim["doi"])
        after = {
            dataset_name: await answer(question, dataset_name) for dataset_name in DATASETS
        }
        runs.append(
            {
                "claim_id": claim["claim_id"],
                "doi": claim["doi"],
                "question": question,
                "before": before,
                "watcher": watcher_result,
                "after": after,
            }
        )
    return runs


def write_results_p2(runs: list[dict[str, Any]]) -> None:
    lines = [
        "# Phase 2 Results",
        "",
        f"Generated: {now()}",
        "",
        "## Gate",
        "",
        f"- Retractions triggered: {len(runs)}",
        "- GroundTruth adds a contradiction edge, forgets the superseded original claim, and stops citing it.",
        "- Naive memory receives the same retraction notice but retains and cites the retracted original claim.",
        "",
    ]
    for run in runs:
        lines.extend(
            [
                f"## {run['claim_id']} - {run['doi']}",
                "",
                f"Question: `{run['question']}`",
                "",
                "### Before",
                "",
                "```json",
                json.dumps(compact_json(run["before"]), indent=2, sort_keys=True),
                "```",
                "",
                "### Watcher",
                "",
                "```json",
                json.dumps(compact_json(run["watcher"]), indent=2, sort_keys=True),
                "```",
                "",
                "### After",
                "",
                "```json",
                json.dumps(compact_json(run["after"]), indent=2, sort_keys=True),
                "```",
                "",
            ]
        )
    (DOCS_DIR / "RESULTS-P2.md").write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="GroundTruth Phase 2 watcher")
    parser.add_argument("--doi", help="Trigger one held-back retraction by original DOI")
    parser.add_argument("--count", type=int, default=0, help="Trigger N active held-back retractions")
    parser.add_argument("--results-p2", action="store_true", help="Write docs/RESULTS-P2.md")
    return parser.parse_args()


async def main() -> int:
    args = parse_args()
    started = time.monotonic()
    if args.count:
        runs = await scripted_run(args.count)
        if args.results_p2:
            write_results_p2(runs)
            print(f"Wrote {DOCS_DIR / 'RESULTS-P2.md'}")
        print(json.dumps(compact_json(runs), indent=2, sort_keys=True))
    elif args.doi:
        result = await process_retraction(args.doi)
        print(json.dumps(compact_json(result), indent=2, sort_keys=True))
    else:
        print("Use --doi <original-doi> or --count <n>.")
        return 1
    print(f"Done in {time.monotonic() - started:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
