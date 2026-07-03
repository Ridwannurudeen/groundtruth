from __future__ import annotations

import argparse
import asyncio
import json
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from groundtruth.answer import answer
from groundtruth.registry import (
    DATASETS,
    load_claims,
    load_json,
    write_json,
)
from groundtruth.runtime import DATA_DIR, DOCS_DIR
from groundtruth.watcher import process_retraction


BENCHMARK_QUESTIONS_PATH = DATA_DIR / "benchmark_questions.json"
BENCHMARK_RESULTS_PATH = DATA_DIR / "benchmark_results.json"
BENCHMARK_DOC_PATH = DOCS_DIR / "BENCHMARK.md"


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_questions(path: Path = BENCHMARK_QUESTIONS_PATH) -> list[dict[str, Any]]:
    questions = load_json(path)
    validate_questions(questions)
    return questions


def validate_questions(questions: list[dict[str, Any]]) -> None:
    if len(questions) != 20:
        raise ValueError(f"Expected 20 benchmark questions, found {len(questions)}")
    ids = [question["id"] for question in questions]
    if len(set(ids)) != len(ids):
        raise ValueError("Benchmark question IDs must be unique")
    counts = Counter(question["kind"] for question in questions)
    expected = {"retracted": 12, "control": 5, "mixed": 3}
    if counts != expected:
        raise ValueError(f"Expected question mix {expected}, found {dict(counts)}")


def claim_index() -> dict[str, dict[str, Any]]:
    return {claim["claim_id"]: claim for claim in load_claims()}


def target_retracted_claim_ids(questions: list[dict[str, Any]]) -> list[str]:
    claim_ids: list[str] = []
    for question in questions:
        for claim_id in question["target_claim_ids"]:
            if claim_id.startswith("R") and claim_id not in claim_ids:
                claim_ids.append(claim_id)
    return claim_ids


async def prepare_retractions(
    questions: list[dict[str, Any]],
    *,
    skip_prepare: bool,
) -> list[dict[str, Any]]:
    if skip_prepare:
        return []

    prepared: list[dict[str, Any]] = []
    for claim_id in target_retracted_claim_ids(questions):
        claims = claim_index()
        claim = claims[claim_id]
        if claim["status"] != "active":
            prepared.append(
                {
                    "claim_id": claim_id,
                    "doi": claim["doi"],
                    "action": "already_prepared",
                    "status": claim["status"],
                }
            )
            continue
        result = await process_retraction(claim["doi"])
        prepared.append({"claim_id": claim_id, "doi": claim["doi"], "action": "processed", "result": result})
    return prepared


def reference_claim_ids(result: dict[str, Any]) -> list[str]:
    return [reference["claim_id"] for reference in result["references"]]


def control_retained(question: dict[str, Any], result: dict[str, Any]) -> bool:
    if question["kind"] != "control" or result["cites_retracted"]:
        return False
    references = set(reference_claim_ids(result))
    return any(claim_id in references for claim_id in question["target_claim_ids"])


async def run_question(question: dict[str, Any], dataset: str) -> dict[str, Any]:
    result = await answer(question["question"], dataset)
    return {
        "question_id": question["id"],
        "kind": question["kind"],
        "dataset": dataset,
        "question": question["question"],
        "target_claim_ids": question["target_claim_ids"],
        "cites_retracted": result["cites_retracted"],
        "retracted_dois": result["retracted_dois"],
        "reference_claim_ids": reference_claim_ids(result),
        "references": result["references"],
        "control_retained": control_retained(question, result),
        "correctness_score": None,
        "correctness_judge": "skipped_gemini_quota_fallback",
        "text": result["text"],
        "recall_context_excerpt": result["recall_context"][:1200],
    }


async def run_benchmark(skip_prepare: bool = False) -> dict[str, Any]:
    os.environ["COGNEE_SKIP_CONNECTION_TEST"] = "true"
    questions = load_questions()
    prepared = await prepare_retractions(questions, skip_prepare=skip_prepare)
    rows: list[dict[str, Any]] = []
    for question in questions:
        for dataset in DATASETS:
            rows.append(await run_question(question, dataset))

    summary = summarize(rows)
    payload = {
        "generated_at": now(),
        "questions_path": str(BENCHMARK_QUESTIONS_PATH),
        "results_path": str(BENCHMARK_RESULTS_PATH),
        "prepared_retractions": prepared,
        "summary": summary,
        "rows": rows,
    }
    write_json(BENCHMARK_RESULTS_PATH, payload)
    write_benchmark_doc(payload)
    return payload


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    by_dataset = {dataset: [row for row in rows if row["dataset"] == dataset] for dataset in DATASETS}
    control_rows = [
        row
        for row in by_dataset["groundtruth_memory"]
        if row["kind"] == "control"
    ]
    return {
        "total_questions": len({row["question_id"] for row in rows}),
        "rows": len(rows),
        "naive_cites_retracted": sum(row["cites_retracted"] for row in by_dataset["naive_memory"]),
        "groundtruth_cites_retracted": sum(
            row["cites_retracted"] for row in by_dataset["groundtruth_memory"]
        ),
        "control_claim_retention": sum(row["control_retained"] for row in control_rows),
        "control_claim_total": len(control_rows),
        "correctness_judge": "skipped_gemini_quota_fallback",
    }


def table_row(row: dict[str, Any]) -> str:
    refs = ", ".join(row["reference_claim_ids"]) or "-"
    correctness = (
        str(row["correctness_score"])
        if row["correctness_score"] is not None
        else row["correctness_judge"]
    )
    return (
        f"| {row['question_id']} | {row['kind']} | {row['dataset']} | "
        f"{row['cites_retracted']} | {row['control_retained']} | {correctness} | {refs} |"
    )


def write_benchmark_doc(payload: dict[str, Any]) -> None:
    summary = payload["summary"]
    prepared = payload["prepared_retractions"]
    rows = payload["rows"]
    lines = [
        "# GroundTruth Benchmark",
        "",
        f"Generated: {payload['generated_at']}",
        "",
        "## Headline",
        "",
        (
            f"- Naive memory cites retracted sources in "
            f"{summary['naive_cites_retracted']}/{summary['total_questions']} answers."
        ),
        (
            f"- GroundTruth cites retracted sources in "
            f"{summary['groundtruth_cites_retracted']}/{summary['total_questions']} answers."
        ),
        (
            f"- Control-claim retention: "
            f"{summary['control_claim_retention']}/{summary['control_claim_total']}."
        ),
        "- Correctness judge: skipped because Gemini free-tier quota is exhausted; primary metric is deterministic citation status.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        "$env:PYTHONIOENCODING='utf-8'; .\\.venv\\Scripts\\python.exe -m groundtruth.benchmark",
        "```",
        "",
        "## Retraction Preparation",
        "",
        "```json",
        json.dumps(prepared, indent=2, sort_keys=True),
        "```",
        "",
        "## Results",
        "",
        "| Q | Kind | Dataset | Cites Retracted | Control Retained | Correctness | References |",
        "|---|---|---|---:|---:|---|---|",
    ]
    lines.extend(table_row(row) for row in rows)
    lines.extend(
        [
            "",
            "## Raw Results",
            "",
            f"Raw JSON: `{BENCHMARK_RESULTS_PATH.as_posix()}`",
            "",
        ]
    )
    BENCHMARK_DOC_PATH.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="GroundTruth benchmark")
    parser.add_argument(
        "--skip-prepare",
        action="store_true",
        help="Do not trigger benchmark target retractions before scoring",
    )
    return parser.parse_args()


async def main() -> int:
    args = parse_args()
    payload = await run_benchmark(skip_prepare=args.skip_prepare)
    print(json.dumps(payload["summary"], indent=2, sort_keys=True))
    print(f"Wrote {BENCHMARK_RESULTS_PATH}")
    print(f"Wrote {BENCHMARK_DOC_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
