from __future__ import annotations

import argparse
import asyncio
import json
import math
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import UUID

from groundtruth.answer import answer, tokens
from groundtruth.contradictions import (
    SemanticConflictDecision,
    add_semantic_conflict_edges,
    judge_semantic_conflict,
    ledger_edges,
)
from groundtruth.ingest import dataset_id, store_claim_deterministic
from groundtruth.registry import load_json, write_json
from groundtruth.runtime import DATA_DIR, DOCS_DIR, import_cognee, is_quota_error


V2_DATASET = "groundtruth_v2_semantic_memory"
V2_CORPUS_PATH = DATA_DIR / "v2_semantic_claims.json"
V2_REGISTRY_PATH = DATA_DIR / "v2_claims.json"
V2_RESULTS_PATH = DATA_DIR / "v2_results.json"
V2_DOC_PATH = DOCS_DIR / "RESULTS-V2.md"
V2_JUDGE_CACHE_PATH = DATA_DIR / "v2_semantic_judgments.json"
CONFIDENCE_THRESHOLD = 0.7


BASELINE_NOTES = [
    "Full baseline `pytest -q` timed out twice before code changes: first at 180s, then at 360s.",
    "Split baseline before code changes: `tests/test_benchmark.py -q` passed 3 tests; `tests/test_web.py -q` passed 5 tests.",
    "Split baseline `tests/test_watcher.py -q` timed out at 240s even after stopping stale pytest/uvicorn workers.",
]


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def compact_json(value: Any) -> Any:
    if hasattr(value, "model_dump"):
        return compact_json(value.model_dump(mode="json"))
    if isinstance(value, dict):
        return {str(key): compact_json(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [compact_json(item) for item in value]
    if isinstance(value, (Path, UUID)):
        return str(value)
    return value


def write_v2_json(path: Path, value: Any) -> None:
    write_json(path, compact_json(value))


def load_v2_corpus() -> dict[str, Any]:
    return load_json(V2_CORPUS_PATH)


def load_v2_registry() -> list[dict[str, Any]]:
    if V2_REGISTRY_PATH.exists():
        return load_json(V2_REGISTRY_PATH)
    return []


def claim_index(claims: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {claim["claim_id"]: claim for claim in claims}


def spot_check_claims(claims: list[dict[str, Any]], count: int = 5) -> list[dict[str, Any]]:
    checks = []
    for claim in claims[:count]:
        text = claim["claim_text"]
        checks.append(
            {
                "claim_id": claim["claim_id"],
                "claim_text": text,
                "real_assertion": (
                    not text.lower().startswith("the paper claimed that")
                    and not text.lower().startswith("the active control paper reports")
                    and any(
                        marker in text.lower()
                        for marker in [
                            "does not",
                            "lowers",
                            "reduce",
                            "shows",
                            "modulate",
                        ]
                    )
                ),
            }
        )
    return checks


def pair_key(claim_a_id: str, claim_b_id: str) -> str:
    return "::".join(sorted([claim_a_id, claim_b_id]))


def cosine(left: list[float], right: list[float]) -> float:
    numerator = sum(a * b for a, b in zip(left, right))
    left_norm = math.sqrt(sum(a * a for a in left))
    right_norm = math.sqrt(sum(b * b for b in right))
    if not left_norm or not right_norm:
        return 0.0
    return numerator / (left_norm * right_norm)


def lexical_similarity(left: str, right: str) -> float:
    left_tokens = tokens(left)
    right_tokens = tokens(right)
    if not left_tokens or not right_tokens:
        return 0.0
    return len(left_tokens & right_tokens) / len(left_tokens | right_tokens)


def vector_candidate_pairs(
    claims: list[dict[str, Any]],
    *,
    neighbors_per_claim: int = 3,
) -> dict[str, Any]:
    texts = [claim["claim_text"] for claim in claims]
    try:
        if os.environ.get("GROUNDTRUTH_V2_DISABLE_FASTEMBED") == "true":
            raise RuntimeError("disabled by GROUNDTRUTH_V2_DISABLE_FASTEMBED")
        from fastembed import TextEmbedding

        embedder = TextEmbedding(model_name="BAAI/bge-small-en")
        vectors = [list(map(float, vector)) for vector in embedder.embed(texts)]
        method = "fastembed:BAAI/bge-small-en cosine"
        score = lambda a, b: cosine(vectors[a], vectors[b])
    except Exception as error:
        method = f"lexical fallback after FastEmbed error: {type(error).__name__}: {error}"
        score = lambda a, b: lexical_similarity(texts[a], texts[b])

    candidates: dict[str, dict[str, Any]] = {}
    for index, claim in enumerate(claims):
        scored = []
        for other_index, other in enumerate(claims):
            if index == other_index:
                continue
            scored.append((score(index, other_index), other["claim_id"]))
        scored.sort(reverse=True)
        for similarity, other_id in scored[:neighbors_per_claim]:
            key = pair_key(claim["claim_id"], other_id)
            candidates[key] = {
                "claim_a_id": claim["claim_id"],
                "claim_b_id": other_id,
                "similarity": round(float(similarity), 6),
            }

    return {
        "method": method,
        "pairs": sorted(candidates.values(), key=lambda item: item["similarity"], reverse=True),
    }


def load_judge_cache() -> dict[str, Any]:
    if V2_JUDGE_CACHE_PATH.exists():
        return load_json(V2_JUDGE_CACHE_PATH)
    return {}


def heuristic_judge(
    claim_a: dict[str, Any],
    claim_b: dict[str, Any],
) -> SemanticConflictDecision:
    subject_match = claim_a["source"]["subject"] == claim_b["source"]["subject"]
    text = f"{claim_a['claim_text']} {claim_b['claim_text']}".lower()
    has_negative = any(marker in text for marker in ["does not", "no beneficial", "not significantly"])
    has_positive = any(marker in text for marker in ["lowers", "reduce", "positively", "appears to reduce"])
    conflicts = subject_match and has_negative and has_positive
    return SemanticConflictDecision(
        conflicts=conflicts,
        direction="mutual" if conflicts else "none",
        basis=(
            "Heuristic detected same-subject positive and negative effect claims."
            if conflicts
            else "Heuristic did not find same-subject incompatible effect claims."
        ),
        confidence=0.75 if conflicts else 0.2,
    )


async def judge_pairs(
    claims: list[dict[str, Any]],
    pairs: list[dict[str, Any]],
    *,
    use_llm: bool,
) -> list[dict[str, Any]]:
    claims_by_id = claim_index(claims)
    cache = load_judge_cache()
    rows = []
    for pair in pairs:
        key = pair_key(pair["claim_a_id"], pair["claim_b_id"])
        cached = cache.get(key)
        expected_judge = "LLMGateway.acreate_structured_output" if use_llm else "heuristic_test_mode"
        if cached and cached.get("judge") == expected_judge:
            decision = SemanticConflictDecision(**cache[key]["decision"])
            row = {**pair, "decision": decision.model_dump(), "cached": True}
            rows.append(row)
            continue

        claim_a = claims_by_id[pair["claim_a_id"]]
        claim_b = claims_by_id[pair["claim_b_id"]]
        try:
            decision = (
                await judge_semantic_conflict(claim_a, claim_b)
                if use_llm
                else heuristic_judge(claim_a, claim_b)
            )
        except Exception as error:
            if is_quota_error(error):
                write_json(
                    V2_JUDGE_CACHE_PATH,
                    {
                        **cache,
                        "_partial_stop": {
                            "pair": pair,
                            "error": str(error)[:1000],
                            "generated_at": now(),
                        },
                    },
                )
            raise

        cache[key] = {
            "claim_a_id": pair["claim_a_id"],
            "claim_b_id": pair["claim_b_id"],
            "decision": decision.model_dump(),
            "generated_at": now(),
            "judge": "LLMGateway.acreate_structured_output" if use_llm else "heuristic_test_mode",
        }
        write_json(V2_JUDGE_CACHE_PATH, cache)
        rows.append({**pair, "decision": decision.model_dump(), "cached": False})
    return rows


def semantic_metrics(rows: list[dict[str, Any]]) -> dict[str, Any]:
    tp = fp = tn = fn = 0
    for row in rows:
        expected = bool(row["expected_conflict"])
        predicted = (
            row["decision"]["conflicts"]
            and row["decision"]["confidence"] >= CONFIDENCE_THRESHOLD
        )
        if expected and predicted:
            tp += 1
        elif expected and not predicted:
            fn += 1
        elif not expected and predicted:
            fp += 1
        else:
            tn += 1
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    return {
        "true_positive": tp,
        "false_positive": fp,
        "true_negative": tn,
        "false_negative": fn,
        "precision": precision,
        "recall": recall,
        "evaluated_pairs": len(rows),
    }


async def ensure_v2_registry(claims: list[dict[str, Any]], *, skip_ingest: bool) -> list[dict[str, Any]]:
    registry = load_v2_registry()
    registry_by_id = claim_index(registry)
    if all(claim["claim_id"] in registry_by_id for claim in claims):
        return registry
    if skip_ingest:
        return registry

    os.environ["COGNEE_SKIP_CONNECTION_TEST"] = "true"
    cognee = import_cognee()
    entries = registry[:]
    entries_by_id = claim_index(entries)
    for claim in claims:
        existing = entries_by_id.get(claim["claim_id"])
        if existing and V2_DATASET in existing.get("datasets", {}):
            continue
        dataset_entry = await store_claim_deterministic(cognee, claim, V2_DATASET)
        entry = {
            "claim_id": claim["claim_id"],
            "doi": claim["source"]["doi"],
            "claim_text": claim["claim_text"],
            "source": claim["source"],
            "status": "active",
            "cohort": claim["cohort"],
            "ingestion_mode": "v2_semantic_deterministic_graph",
            "datasets": {V2_DATASET: dataset_entry},
        }
        if existing:
            entries[entries.index(existing)] = entry
        else:
            entries.append(entry)
        entries_by_id[claim["claim_id"]] = entry
        write_json(V2_REGISTRY_PATH, entries)
    return entries


async def reset_v2_dataset() -> None:
    cognee = import_cognee()
    if await dataset_id(cognee, V2_DATASET):
        await cognee.forget(dataset=V2_DATASET)
    if V2_REGISTRY_PATH.exists():
        V2_REGISTRY_PATH.unlink()


async def write_confirmed_edges(
    registry: list[dict[str, Any]],
    rows: list[dict[str, Any]],
    *,
    skip_ingest: bool,
) -> list[dict[str, Any]]:
    if skip_ingest or not registry:
        return []
    cognee = import_cognee()
    dataset = await dataset_id(cognee, V2_DATASET)
    if dataset is None:
        return []
    registry_by_id = claim_index(registry)
    existing_edges = await ledger_edges(dataset)
    existing_pair_keys = {
        pair_key(
            (edge.attributes or {}).get("claim_a_id", ""),
            (edge.attributes or {}).get("claim_b_id", ""),
        )
        for edge in existing_edges
        if edge.relationship_name in {"contradicts", "supersedes"}
        and (edge.attributes or {}).get("claim_a_id")
        and (edge.attributes or {}).get("claim_b_id")
    }
    edge_rows = []
    for row in rows:
        decision = SemanticConflictDecision(**row["decision"])
        if not decision.conflicts or decision.confidence < CONFIDENCE_THRESHOLD:
            continue
        current_pair_key = pair_key(row["claim_a_id"], row["claim_b_id"])
        if current_pair_key in existing_pair_keys:
            edge_rows.append(
                {
                    "pair": [row["claim_a_id"], row["claim_b_id"]],
                    "action": "already_exists",
                    "edges": [],
                }
            )
            continue
        entry_a = registry_by_id[row["claim_a_id"]]
        entry_b = registry_by_id[row["claim_b_id"]]
        edge_rows.append(
            {
                "pair": [row["claim_a_id"], row["claim_b_id"]],
                "edges": await add_semantic_conflict_edges(
                    cognee,
                    dataset_id=dataset,
                    claim_a_data_id=UUID(entry_a["datasets"][V2_DATASET]["data_id"]),
                    claim_b_data_id=UUID(entry_b["datasets"][V2_DATASET]["data_id"]),
                    claim_a_id=row["claim_a_id"],
                    claim_b_id=row["claim_b_id"],
                    decision=decision,
                ),
            }
        )
    return edge_rows


async def answer_probes(
    questions: list[dict[str, Any]],
    *,
    skip_answers: bool,
) -> list[dict[str, Any]]:
    if skip_answers or not V2_REGISTRY_PATH.exists():
        return []
    rows = []
    for question in questions:
        try:
            result = await answer(
                question["question"],
                V2_DATASET,
                registry_path=V2_REGISTRY_PATH,
                record_session=False,
                synthesize=True,
            )
        except Exception as error:
            if is_quota_error(error):
                rows.append(
                    {
                        "question_id": question["id"],
                        "question": question["question"],
                        "status": "skipped_quota_error",
                        "error": str(error)[:1000],
                    }
                )
                continue
            raise
        rows.append(
            {
                "question_id": question["id"],
                "question": question["question"],
                "status": "completed",
                "text": result["text"],
                "references": result["references"],
                "reference_edges": result["reference_edges"],
                "cites_retracted": result["cites_retracted"],
                "cites_superseded": result["cites_superseded"],
                "superseded_dois": result["superseded_dois"],
                "superseded_references": result["superseded_references"],
                "synthesis_mode": result["synthesis_mode"],
            }
        )
    return rows


def write_results_doc(payload: dict[str, Any]) -> None:
    payload = compact_json(payload)
    lines = [
        "# GroundTruth V2 Results",
        "",
        f"Generated: {payload['generated_at']}",
        f"Status: `{payload['status']}`",
        "",
        "## Baseline Before V2",
        "",
    ]
    lines.extend(f"- {note}" for note in BASELINE_NOTES)
    lines.extend(
        [
            "",
            "## V2-4 Concrete Claim Spot Check",
            "",
            "```json",
            json.dumps(payload["spot_checks"], indent=2, sort_keys=True),
            "```",
            "",
            "## V2-1 Semantic Conflict Detection",
            "",
            f"- Candidate method: `{payload['candidate_method']}`",
            f"- Judge: `{payload['judge']}`",
            "",
            "Metrics:",
            "",
            "```json",
            json.dumps(payload.get("semantic_metrics"), indent=2, sort_keys=True),
            "```",
            "",
            "Pairs:",
            "",
            "```json",
            json.dumps(payload.get("semantic_rows"), indent=2, sort_keys=True),
            "```",
            "",
            "## V2-2 Graph-Aware Answer Probes",
            "",
            "```json",
            json.dumps(payload.get("answer_probes"), indent=2, sort_keys=True),
            "```",
            "",
            "## Edge Writes",
            "",
            "```json",
            json.dumps(payload.get("edge_writes"), indent=2, sort_keys=True),
            "```",
            "",
        ]
    )
    if payload.get("quota_error"):
        lines.extend(
            [
                "## Quota Stop",
                "",
                "The pass stopped on a quota/rate-limit error. Cached judgments and ingested claims were preserved for resume.",
                "",
                "```text",
                payload["quota_error"],
                "```",
                "",
            ]
        )
    V2_DOC_PATH.write_text("\n".join(lines), encoding="utf-8")


async def run_v2(
    *,
    use_llm: bool,
    skip_ingest: bool,
    skip_answers: bool,
    reset_v2: bool,
) -> dict[str, Any]:
    corpus = load_v2_corpus()
    claims = corpus["claims"]
    spot_checks = spot_check_claims(claims)
    candidates = vector_candidate_pairs(claims)
    eval_pairs = corpus["evaluation_pairs"]
    if reset_v2:
        await reset_v2_dataset()
    registry = await ensure_v2_registry(claims, skip_ingest=skip_ingest)
    status = "complete"
    quota_error = None
    semantic_rows: list[dict[str, Any]] = []
    edge_writes: list[dict[str, Any]] = []
    answer_rows: list[dict[str, Any]] = []
    try:
        semantic_rows = await judge_pairs(claims, eval_pairs, use_llm=use_llm)
        edge_writes = await write_confirmed_edges(
            registry,
            semantic_rows,
            skip_ingest=skip_ingest,
        )
        answer_rows = await answer_probes(corpus["question_probes"], skip_answers=skip_answers)
    except Exception as error:
        if not is_quota_error(error):
            raise
        status = "partial_quota_stop"
        quota_error = str(error)[:1000]

    payload = {
        "generated_at": now(),
        "status": status,
        "dataset": V2_DATASET,
        "corpus_path": str(V2_CORPUS_PATH),
        "registry_path": str(V2_REGISTRY_PATH),
        "spot_checks": spot_checks,
        "candidate_method": candidates["method"],
        "candidate_pairs": candidates["pairs"],
        "judge": "LLMGateway.acreate_structured_output" if use_llm else "heuristic_test_mode",
        "semantic_rows": semantic_rows,
        "semantic_metrics": semantic_metrics(semantic_rows) if semantic_rows else None,
        "edge_writes": edge_writes,
        "answer_probes": answer_rows,
        "quota_error": quota_error,
    }
    write_v2_json(V2_RESULTS_PATH, payload)
    write_results_doc(payload)
    return payload


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="GroundTruth V2 semantic memory pass")
    parser.add_argument("--no-llm", action="store_true", help="Use deterministic test heuristic")
    parser.add_argument("--skip-ingest", action="store_true", help="Do not ingest V2 claims")
    parser.add_argument("--skip-answers", action="store_true", help="Do not run synthesized answers")
    parser.add_argument(
        "--reset-v2",
        action="store_true",
        help="Forget only the V2 semantic dataset and rebuild its registry",
    )
    return parser.parse_args()


async def main() -> int:
    args = parse_args()
    payload = await run_v2(
        use_llm=not args.no_llm,
        skip_ingest=args.skip_ingest,
        skip_answers=args.skip_answers,
        reset_v2=args.reset_v2,
    )
    print(json.dumps(payload["semantic_metrics"], indent=2, sort_keys=True))
    print(f"Wrote {V2_RESULTS_PATH}")
    print(f"Wrote {V2_DOC_PATH}")
    return 0 if payload["status"] == "complete" else 1


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
