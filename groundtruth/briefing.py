from __future__ import annotations

import argparse
import asyncio
import json
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from groundtruth.beliefs import latest_state_change, migrate_claim_belief
from groundtruth.contest import CONTESTED_PAIRS_PATH, list_contested_pairs
from groundtruth.registry import CLAIMS_PATH, load_claims, load_json, write_json
from groundtruth.runtime import DATA_DIR, DOCS_DIR, ROOT, import_cognee


GROUNDTRUTH_DATASET = "groundtruth_memory"
V2_CLAIMS_PATH = DATA_DIR / "v2_claims.json"
BRIEFING_RUN_PATH = DATA_DIR / "briefing_run.json"
MORNING_BRIEFING_PATH = ROOT / "MORNING_BRIEFING.md"
RESULTS_V3_P3_PATH = DOCS_DIR / "RESULTS-V3-P3.md"


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def compact_json(value: Any) -> Any:
    if hasattr(value, "model_dump"):
        return value.model_dump(mode="json")
    if hasattr(value, "to_dict"):
        return compact_json(value.to_dict())
    if isinstance(value, list):
        return [compact_json(item) for item in value]
    if isinstance(value, tuple):
        return [compact_json(item) for item in value]
    if isinstance(value, dict):
        return {str(key): compact_json(item) for key, item in value.items()}
    return value


def item_from_claim(claim: dict[str, Any]) -> dict[str, Any]:
    migrated = migrate_claim_belief(claim)
    source = migrated.get("source") or {}
    latest = latest_state_change(migrated)
    dataset_entry = (migrated.get("datasets") or {}).get(GROUNDTRUTH_DATASET) or {}
    return {
        "claim_id": migrated["claim_id"],
        "doi": migrated.get("doi") or source.get("doi"),
        "title": source.get("title"),
        "journal": source.get("journal"),
        "belief_state": migrated["belief_state"],
        "status": migrated.get("status"),
        "memory_status": dataset_entry.get("status"),
        "evidence_class": latest["evidence_class"],
        "evidence_ref": latest["evidence_ref"],
        "basis": latest["basis"],
        "changed_at": latest["at"],
    }


def snapshot_registry(claims: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {claim["claim_id"]: item_from_claim(claim) for claim in claims}


def is_memory_purged(item: dict[str, Any]) -> bool:
    return item.get("belief_state") == "purged" or item.get("memory_status") in {
        "retracted_forgotten",
        "purged",
    }


def diff_snapshots(
    before: dict[str, dict[str, Any]],
    after: dict[str, dict[str, Any]],
) -> dict[str, list[dict[str, Any]]]:
    diff = {
        "learned_last_night": [],
        "now_contested": [],
        "revised": [],
        "purged": [],
    }
    for claim_id, current in sorted(after.items()):
        previous = before.get(claim_id)
        if previous is None:
            diff["learned_last_night"].append(current)
            continue

        changed = (
            previous.get("belief_state") != current.get("belief_state")
            or previous.get("evidence_ref") != current.get("evidence_ref")
            or previous.get("memory_status") != current.get("memory_status")
        )
        if not changed:
            continue

        if current["belief_state"] == "contested":
            diff["now_contested"].append(current)
        elif current["belief_state"] in {"superseded", "retracted"}:
            diff["revised"].append(current)

        if is_memory_purged(current) and not is_memory_purged(previous):
            diff["purged"].append(current)
    return diff


async def remember_evening_evidence(
    texts: list[str],
    *,
    dataset_name: str,
    session_id: str,
    cognee_client: Any | None = None,
) -> list[dict[str, Any]]:
    cognee = cognee_client or import_cognee()
    results = []
    for text in texts:
        result = await cognee.remember(
            text,
            dataset_name=dataset_name,
            session_id=session_id,
            self_improvement=False,
        )
        results.append(compact_json(result))
    return results


def recorded_bridge(dataset_name: str, session_id: str) -> dict[str, Any]:
    return {
        "status": "recorded_not_executed",
        "dataset": dataset_name,
        "session_ids": [session_id],
        "call_shape": (
            "cognee.improve(dataset=dataset_name, session_ids=[session_id])"
        ),
        "reason": (
            "Cognee 1.2.2 public improve(session_ids=...) was source-verified to "
            "run session persistence, distillation, and default enrichment stages "
            "that can consume LLM quota. The scripted P3 artifact records the "
            "bridge boundary and performs deterministic registry reconciliation."
        ),
    }


def notice_text_for_claim(claim: dict[str, Any]) -> str:
    retraction = claim["retraction"]
    return (
        f"Retraction Watch notice {retraction['retraction_doi']} says original "
        f"DOI {claim['doi']} was retracted. Reason: {retraction['reason']}"
    )


def before_answer_text(claim: dict[str, Any]) -> str:
    source = claim["source"]
    return (
        f"{GROUNDTRUTH_DATASET} still cites the active claim {claim['doi']} from "
        f"{source['journal']}: {claim['claim_text']}"
    )


def after_answer_text(claim: dict[str, Any]) -> str:
    retraction = claim["retraction"]
    return (
        f"{GROUNDTRUTH_DATASET} no longer cites original DOI {claim['doi']}. "
        f"The belief is retracted by authority_feed evidence "
        f"{retraction['retraction_doi']}: {retraction['reason']}"
    )


def make_fixture_transition(claim: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    before = deepcopy(claim)
    before["status"] = "active"
    before["belief_state"] = "active"
    before["state_history"] = [before["state_history"][0]]
    for dataset_entry in (before.get("datasets") or {}).values():
        dataset_entry["status"] = "active"

    after = deepcopy(claim)
    return before, after


def current_revised_items(v2_registry_path: Path = V2_CLAIMS_PATH) -> list[dict[str, Any]]:
    if not v2_registry_path.exists():
        return []
    claims = load_json(v2_registry_path)
    items = [
        item_from_claim(claim)
        for claim in claims
        if migrate_claim_belief(claim)["belief_state"] in {"superseded", "retracted"}
    ]
    return sorted(items, key=lambda item: item["claim_id"])


def current_contested_items(
    queue_path: Path = CONTESTED_PAIRS_PATH,
    v2_registry_path: Path = V2_CLAIMS_PATH,
) -> list[dict[str, Any]]:
    if not queue_path.exists():
        return []
    items = list_contested_pairs(queue_path, registry_path=v2_registry_path)
    return [
        {
            "pair": item["pair"],
            "claim_id": item["pair"],
            "doi": None,
            "title": " vs ".join(claim.get("title") or "" for claim in item["claims"]),
            "belief_state": "contested",
            "evidence_class": "semantic_inference",
            "evidence_ref": item["evidence_ref"],
            "basis": item["basis"],
            "changed_at": item["updated_at"],
            "claims": item["claims"],
        }
        for item in items
    ]


def build_current_briefing() -> dict[str, Any]:
    return {
        "generated_at": now(),
        "status": "current_projection",
        "session_id": None,
        "dataset": GROUNDTRUTH_DATASET,
        "learned_last_night": [],
        "now_contested": current_contested_items(),
        "revised": current_revised_items(),
        "purged": [],
        "question": None,
        "before_answer": None,
        "after_answer": None,
        "bridge": recorded_bridge(GROUNDTRUTH_DATASET, "analyst-session"),
    }


def merge_items(
    artifact_items: list[dict[str, Any]],
    current_items: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    merged: dict[str, dict[str, Any]] = {}
    for item in artifact_items + current_items:
        key = str(item.get("pair") or item.get("claim_id") or item.get("doi"))
        merged[key] = item
    return [merged[key] for key in sorted(merged)]


def read_artifact_briefing(run_path: Path = BRIEFING_RUN_PATH) -> dict[str, Any] | None:
    if not run_path.exists():
        return None
    return load_json(run_path)["briefing"]


def build_briefing(run_path: Path = BRIEFING_RUN_PATH) -> dict[str, Any]:
    current = build_current_briefing()
    artifact = read_artifact_briefing(run_path)
    if artifact is None:
        return current

    return {
        **artifact,
        "generated_at": current["generated_at"],
        "status": f"{artifact['status']}_with_current_projection",
        "now_contested": current["now_contested"],
        "revised": merge_items(artifact.get("revised", []), current["revised"]),
        "purged": merge_items(artifact.get("purged", []), current["purged"]),
    }


def render_item(item: dict[str, Any]) -> str:
    subject = item.get("pair") or item.get("claim_id")
    doi = item.get("doi") or "n/a"
    return (
        f"- `{subject}` / `{item.get('belief_state')}` / DOI `{doi}`\n"
        f"  - Evidence: `{item.get('evidence_class')}` `{item.get('evidence_ref')}`\n"
        f"  - Basis: {item.get('basis')}"
    )


def render_section(title: str, items: list[dict[str, Any]]) -> list[str]:
    lines = [f"## {title}", ""]
    if not items:
        lines.extend(["- None.", ""])
        return lines
    for item in items:
        lines.extend([render_item(item), ""])
    return lines


def render_briefing_markdown(briefing: dict[str, Any]) -> str:
    lines = [
        "# Morning Briefing",
        "",
        f"Generated: {briefing['generated_at']}",
        f"Status: `{briefing['status']}`",
        f"Session: `{briefing.get('session_id') or 'n/a'}`",
        f"Dataset: `{briefing.get('dataset')}`",
        "",
    ]
    lines.extend(render_section("Learned Last Night", briefing["learned_last_night"]))
    lines.extend(render_section("Now Contested", briefing["now_contested"]))
    lines.extend(render_section("Revised", briefing["revised"]))
    lines.extend(render_section("Purged", briefing["purged"]))
    if briefing.get("question"):
        lines.extend(
            [
                "## Before Answer",
                "",
                f"Question: `{briefing['question']}`",
                "",
                "```text",
                briefing["before_answer"],
                "```",
                "",
                "## After Answer",
                "",
                "```text",
                briefing["after_answer"],
                "```",
                "",
            ]
        )
    return "\n".join(lines)


def render_results_markdown(run: dict[str, Any]) -> str:
    lines = [
        "# GroundTruth V3 P3 Results",
        "",
        f"Generated: {run['generated_at']}",
        f"Status: `{run['briefing']['status']}`",
        "",
        "## Gate",
        "",
        "- Evening evidence is represented as a session-only Cognee `remember` call with `self_improvement=False`.",
        "- The public Cognee `improve(dataset, session_ids=[...])` bridge is recorded but not executed in the scripted artifact because installed Cognee 1.2.2 can enter LLM-backed session distillation/cognify stages.",
        "- The before/after answer transcript is a deterministic fixture over an isolated registry transition, preserving committed P0-P2 data.",
        "- The briefing artifact is written to `MORNING_BRIEFING.md`; `GET /briefing` exposes a current projection seeded by the artifact transcript.",
        "",
        "## Command",
        "",
        "```powershell",
        ".\\.venv\\Scripts\\python.exe -m groundtruth.briefing --results-v3-p3",
        "```",
        "",
        "## Session And Bridge",
        "",
        "```json",
        json.dumps(
            {
                "session_remember": run["session_remember"],
                "bridge": run["briefing"]["bridge"],
            },
            indent=2,
            sort_keys=True,
        ),
        "```",
        "",
        "## Deterministic Before/After Transcript",
        "",
        f"Question: `{run['briefing']['question']}`",
        "",
        "Before:",
        "",
        "```text",
        run["briefing"]["before_answer"],
        "```",
        "",
        "After:",
        "",
        "```text",
        run["briefing"]["after_answer"],
        "```",
        "",
        "## Briefing JSON",
        "",
        "```json",
        json.dumps(run["briefing"], indent=2, sort_keys=True),
        "```",
        "",
        "## Verification So Far",
        "",
        "- Run the focused tests, static checks, and full suite after generation; the committed results document records the final local outputs.",
        "",
    ]
    return "\n".join(lines)


async def scripted_run(
    *,
    session_id: str,
    claim_id: str,
    dataset_name: str = GROUNDTRUTH_DATASET,
    live_session: bool = True,
    claims_path: Path = CLAIMS_PATH,
) -> dict[str, Any]:
    claims = load_claims(claims_path)
    target = next(claim for claim in claims if claim["claim_id"] == claim_id)
    before_claim, after_claim = make_fixture_transition(target)
    before_snapshot = snapshot_registry([before_claim])
    after_snapshot = snapshot_registry([after_claim])
    diff = diff_snapshots(before_snapshot, after_snapshot)
    notice_text = notice_text_for_claim(target)
    session_remember = {
        "status": "recorded_not_executed",
        "dataset": dataset_name,
        "session_id": session_id,
        "self_improvement": False,
        "source_claim_id": target["claim_id"],
        "source_registry_path": str(claims_path),
        "texts": [notice_text],
    }
    if live_session:
        try:
            session_remember["status"] = "executing"
            session_remember = {
                **session_remember,
                "status": "executed",
                "dataset": dataset_name,
                "session_id": session_id,
                "self_improvement": False,
                "source_claim_id": target["claim_id"],
                "source_registry_path": str(claims_path),
                "texts": [notice_text],
                "results": await remember_evening_evidence(
                    [notice_text],
                    dataset_name=dataset_name,
                    session_id=session_id,
                ),
            }
        except Exception as error:
            session_remember = {
                **session_remember,
                "status": "failed_recorded_fallback",
                "error": f"{type(error).__name__}: {error}",
            }

    status_by_session = {
        "executed": "complete_session_executed_fixture",
        "recorded_not_executed": "complete_recorded_fixture",
        "failed_recorded_fallback": "partial_session_fallback_fixture",
    }
    question = f"What does the memory say about {target['source']['title']}?"
    learned = [
        {
            "claim_id": target["claim_id"],
            "doi": target["retraction"]["retraction_doi"],
            "title": f"Retraction notice for {target['source']['title']}",
            "belief_state": "active",
            "evidence_class": "authority_feed",
            "evidence_ref": target["retraction"]["retraction_doi"],
            "basis": notice_text,
            "changed_at": target["state_history"][-1]["at"],
            "session_id": session_id,
        }
    ]
    briefing = {
        "generated_at": now(),
        "status": status_by_session.get(
            session_remember["status"], "partial_session_fallback_fixture"
        ),
        "session_id": session_id,
        "dataset": dataset_name,
        "learned_last_night": learned,
        "now_contested": current_contested_items(),
        "revised": diff["revised"] + current_revised_items(),
        "purged": diff["purged"],
        "question": question,
        "before_answer": before_answer_text(before_claim),
        "after_answer": after_answer_text(after_claim),
        "bridge": recorded_bridge(dataset_name, session_id),
    }
    return {
        "generated_at": briefing["generated_at"],
        "fixture_claim_id": claim_id,
        "session_remember": session_remember,
        "before_snapshot": before_snapshot,
        "after_snapshot": after_snapshot,
        "diff": diff,
        "briefing": briefing,
    }


def write_artifacts(run: dict[str, Any]) -> None:
    write_json(BRIEFING_RUN_PATH, run)
    MORNING_BRIEFING_PATH.write_text(
        render_briefing_markdown(run["briefing"]), encoding="utf-8"
    )
    RESULTS_V3_P3_PATH.write_text(render_results_markdown(run), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="GroundTruth V3 morning briefing")
    parser.add_argument("--claim-id", default="R001")
    parser.add_argument("--session-id", default="analyst-2026-07-04")
    parser.add_argument("--dataset", default=GROUNDTRUTH_DATASET)
    parser.add_argument(
        "--record-only",
        action="store_true",
        help="Record the session remember call shape without touching local Cognee.",
    )
    parser.add_argument(
        "--results-v3-p3",
        action="store_true",
        help="Write data/briefing_run.json, MORNING_BRIEFING.md, and docs/RESULTS-V3-P3.md.",
    )
    return parser.parse_args()


async def main() -> int:
    args = parse_args()
    run = await scripted_run(
        session_id=args.session_id,
        claim_id=args.claim_id,
        dataset_name=args.dataset,
        live_session=not args.record_only,
    )
    if args.results_v3_p3:
        write_artifacts(run)
        print(f"Wrote {MORNING_BRIEFING_PATH}")
        print(f"Wrote {RESULTS_V3_P3_PATH}")
    print(json.dumps(compact_json(run), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
