from __future__ import annotations

import argparse
import asyncio
import json
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from groundtruth.answer import answer, dataset_id as resolve_dataset_id
from groundtruth.contradictions import memory_data_ids
from groundtruth.registry import (
    DATASETS,
    load_claims,
    load_json,
    write_json,
)
from groundtruth.runtime import DATA_DIR, DOCS_DIR, import_cognee, is_quota_error
from groundtruth.watcher import process_retraction


BENCHMARK_QUESTIONS_PATH = DATA_DIR / "benchmark_questions.json"
BENCHMARK_RESULTS_PATH = DATA_DIR / "benchmark_results.json"
BENCHMARK_DOC_PATH = DOCS_DIR / "BENCHMARK.md"
RESULTS_FIX_PATH = DOCS_DIR / "RESULTS-FIX.md"
V2_RESULTS_PATH = DATA_DIR / "v2_results.json"
METRIC_DEFINITION = (
    "The headline metric is the fraction of answers whose relevance-ranked "
    "Cognee GRAPH_COMPLETION references include a still-present original claim "
    'from `cohort == "retracted_original"`. Raw graph references remain in '
    "the JSON for audit."
)


class QuotaStop(RuntimeError):
    def __init__(self, prepared: list[dict[str, Any]], error: BaseException):
        super().__init__(str(error))
        self.prepared = prepared
        self.error = error


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


def all_retracted_claim_ids(claims: list[dict[str, Any]] | None = None) -> list[str]:
    entries = claims if claims is not None else load_claims()
    return [
        claim["claim_id"]
        for claim in entries
        if claim.get("cohort") == "retracted_original"
    ]


def retraction_progress(claims: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    entries = claims if claims is not None else load_claims()
    retracted = [
        claim for claim in entries if claim.get("cohort") == "retracted_original"
    ]
    forgotten = [
        claim
        for claim in retracted
        if claim.get("status") == "retracted_forgotten"
        and claim.get("datasets", {}).get("groundtruth_memory", {}).get("status")
        == "retracted_forgotten"
    ]
    pending = [claim["claim_id"] for claim in retracted if claim not in forgotten]
    return {
        "retracted_cohort_total": len(retracted),
        "groundtruth_forgotten": len(forgotten),
        "pending": pending,
    }


async def memory_integrity_report(
    claims: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    entries = claims if claims is not None else load_claims()
    cognee = import_cognee()
    memory_ids_by_dataset = {}
    for dataset in DATASETS:
        resolved_dataset_id = await resolve_dataset_id(cognee, dataset)
        memory_ids_by_dataset[dataset] = await memory_data_ids(resolved_dataset_id)

    violations: list[dict[str, str]] = []
    for claim in entries:
        datasets = claim.get("datasets", {})
        if claim.get("cohort") == "retracted_original":
            groundtruth_entry = datasets.get("groundtruth_memory", {})
            naive_entry = datasets.get("naive_memory", {})
            if (
                groundtruth_entry.get("data_id")
                in memory_ids_by_dataset["groundtruth_memory"]
            ):
                violations.append(
                    {
                        "claim_id": claim["claim_id"],
                        "dataset": "groundtruth_memory",
                        "problem": "retracted_original_present",
                    }
                )
            if naive_entry.get("data_id") not in memory_ids_by_dataset["naive_memory"]:
                violations.append(
                    {
                        "claim_id": claim["claim_id"],
                        "dataset": "naive_memory",
                        "problem": "retracted_original_missing_from_naive",
                    }
                )
        elif claim.get("cohort") == "active_control":
            for dataset in DATASETS:
                dataset_entry = datasets.get(dataset, {})
                if dataset_entry.get("data_id") not in memory_ids_by_dataset[dataset]:
                    violations.append(
                        {
                            "claim_id": claim["claim_id"],
                            "dataset": dataset,
                            "problem": "active_control_missing",
                        }
                    )

    return {
        "violations": violations,
        "retracted_original_total": sum(
            claim.get("cohort") == "retracted_original" for claim in entries
        ),
        "active_control_total": sum(
            claim.get("cohort") == "active_control" for claim in entries
        ),
    }


async def prepare_retractions(
    questions: list[dict[str, Any]],
    *,
    skip_prepare: bool,
) -> list[dict[str, Any]]:
    del questions
    if skip_prepare:
        return []

    prepared: list[dict[str, Any]] = []
    for claim_id in all_retracted_claim_ids():
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
        try:
            result = await process_retraction(claim["doi"])
        except Exception as error:
            if is_quota_error(error):
                prepared.append(
                    {
                        "claim_id": claim_id,
                        "doi": claim["doi"],
                        "action": "quota_error",
                        "error": str(error)[:1000],
                    }
                )
                raise QuotaStop(prepared, error) from error
            raise
        prepared.append(
            {
                "claim_id": claim_id,
                "doi": claim["doi"],
                "action": result.get("action", "processed"),
                "result": result,
            }
        )
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
        "reference_cross_check": result["reference_cross_check"],
        "control_retained": control_retained(question, result),
        "correctness_score": None,
        "correctness_judge": "skipped_quota_disclosed",
        "text": result["text"],
        "recall_mode": result["recall_mode"],
        "recall_context_excerpt": result["recall_context"][:1200],
    }


async def demo_synthesis(questions: list[dict[str, Any]]) -> dict[str, Any]:
    question = next(item for item in questions if item["id"] == "Q01")
    answers: dict[str, Any] = {}
    for dataset in DATASETS:
        try:
            result = await answer(question["question"], dataset, synthesize=True)
        except Exception as error:
            if is_quota_error(error):
                answers[dataset] = {
                    "status": "skipped_quota_error",
                    "error": str(error)[:1000],
                }
                continue
            raise
        answers[dataset] = {
            "status": "completed",
            "text": result["text"],
            "references": result["references"],
            "cites_retracted": result["cites_retracted"],
            "retracted_dois": result["retracted_dois"],
        }
    return {
        "question_id": question["id"],
        "question": question["question"],
        "answers": answers,
    }


async def run_benchmark(
    skip_prepare: bool = False,
    *,
    synthesize_demo: bool = False,
) -> dict[str, Any]:
    os.environ["COGNEE_SKIP_CONNECTION_TEST"] = "true"
    questions = load_questions()
    try:
        prepared = await prepare_retractions(questions, skip_prepare=skip_prepare)
    except QuotaStop as stop:
        payload = {
            "generated_at": now(),
            "status": "partial_quota_stop",
            "metric_definition": METRIC_DEFINITION,
            "prepared_retractions": stop.prepared,
            "retraction_progress": retraction_progress(),
            "quota_error": str(stop.error)[:1000],
            "summary": None,
            "rows": [],
        }
        write_results_fix_doc(payload)
        raise

    integrity = await memory_integrity_report()
    progress = retraction_progress()
    if integrity["violations"]:
        payload = {
            "generated_at": now(),
            "status": "memory_integrity_failed",
            "metric_definition": METRIC_DEFINITION,
            "prepared_retractions": prepared,
            "retraction_progress": progress,
            "memory_integrity": integrity,
            "summary": None,
            "rows": [],
        }
        write_results_fix_doc(payload)
        raise RuntimeError(f"Memory integrity violations: {integrity['violations']}")

    rows: list[dict[str, Any]] = []
    for question in questions:
        for dataset in DATASETS:
            rows.append(await run_question(question, dataset))

    summary = summarize(rows)
    payload = {
        "generated_at": now(),
        "status": "complete",
        "metric_definition": METRIC_DEFINITION,
        "questions_path": str(BENCHMARK_QUESTIONS_PATH),
        "results_path": str(BENCHMARK_RESULTS_PATH),
        "prepared_retractions": prepared,
        "retraction_progress": progress,
        "memory_integrity": integrity,
        "demo_synthesis": await demo_synthesis(questions) if synthesize_demo else None,
        "summary": summary,
        "rows": rows,
    }
    write_json(BENCHMARK_RESULTS_PATH, payload)
    write_benchmark_doc(payload)
    write_results_fix_doc(payload)
    return payload


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    by_dataset = {
        dataset: [row for row in rows if row["dataset"] == dataset]
        for dataset in DATASETS
    }
    control_rows = [
        row for row in by_dataset["groundtruth_memory"] if row["kind"] == "control"
    ]
    return {
        "total_questions": len({row["question_id"] for row in rows}),
        "rows": len(rows),
        "naive_cites_retracted": sum(
            row["cites_retracted"] for row in by_dataset["naive_memory"]
        ),
        "groundtruth_cites_retracted": sum(
            row["cites_retracted"] for row in by_dataset["groundtruth_memory"]
        ),
        "control_claim_retention": sum(row["control_retained"] for row in control_rows),
        "control_claim_total": len(control_rows),
        "correctness_judge": "skipped_quota_disclosed",
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


def v2_addendum_lines(path: Path = V2_RESULTS_PATH) -> list[str]:
    if not path.exists():
        return []
    payload = load_json(path)
    metrics = payload.get("semantic_metrics") or {}
    coverage = payload.get("evaluation_coverage") or {}
    answer_rows = payload.get("answer_probes") or []
    completed_answers = sum(row.get("status") == "completed" for row in answer_rows)
    superseded_answers = sum(
        row.get("status") == "completed" and row.get("cites_superseded")
        for row in answer_rows
    )
    lines = [
        "",
        "## V2 Semantic Conflict Addendum",
        "",
        "The V2 semantic pass is separate from the retraction-forgetting headline metric.",
        "",
        f"- Status: `{payload.get('status')}`.",
        f"- Protocol: `{coverage.get('protocol', 'unknown')}`.",
        (
            f"- Coverage: {coverage.get('evaluated_pairs', metrics.get('evaluated_pairs', 0))}/"
            f"{coverage.get('all_pair_total', 'unknown')} committed claim pairs evaluated."
        ),
        (
            f"- Confusion matrix: TP {metrics.get('true_positive', 0)}, "
            f"TN {metrics.get('true_negative', 0)}, FP {metrics.get('false_positive', 0)}, "
            f"FN {metrics.get('false_negative', 0)}."
        ),
        (
            f"- Precision: {metrics.get('precision', 0):.2f}; "
            f"recall: {metrics.get('recall', 0):.2f}."
        ),
        f"- Judge: `{payload.get('judge')}`.",
    ]
    if answer_rows:
        lines.append(
            f"- Graph-aware answer probes: {completed_answers}/{len(answer_rows)} completed; "
            f"{superseded_answers}/{len(answer_rows)} surfaced conflicted graph references."
        )
    else:
        lines.append(
            "- Graph-aware answer probes: not run; V2 stopped before the answer-probe phase."
        )
    try:
        display_path = path.relative_to(DATA_DIR.parent).as_posix()
    except ValueError:
        display_path = path.as_posix()
    lines.append(
        f"- Full V2 output: [docs/RESULTS-V2.md](RESULTS-V2.md) and `{display_path}`."
    )
    if payload.get("quota_error"):
        lines.append("- Quota stop: present; numbers above are partial and resumable.")
    if payload.get("provider_error"):
        lines.append(
            "- Provider stop: present; numbers above are partial and resumable."
        )
    return lines


def write_benchmark_doc(payload: dict[str, Any]) -> None:
    summary = payload["summary"]
    prepared = payload["prepared_retractions"]
    progress = payload["retraction_progress"]
    rows = payload["rows"]
    lines = [
        "# GroundTruth Benchmark",
        "",
        f"Generated: {payload['generated_at']}",
        "",
        "## Headline",
        "",
        (
            f"- Naive memory retrieves retracted originals in "
            f"{summary['naive_cites_retracted']}/{summary['total_questions']} answers."
        ),
        (
            f"- GroundTruth retrieves retracted originals in "
            f"{summary['groundtruth_cites_retracted']}/{summary['total_questions']} answers."
        ),
        (
            f"- Control-claim retention: "
            f"{summary['control_claim_retention']}/{summary['control_claim_total']}."
        ),
        (
            f"- Retraction coverage: {progress['groundtruth_forgotten']}/"
            f"{progress['retracted_cohort_total']} retracted-cohort originals forgotten "
            "from GroundTruth memory."
        ),
        "- Correctness judge: skipped with disclosure; the primary metric is relevance-ranked graph references containing a still-present retracted original.",
        *v2_addendum_lines(),
        "",
        "## Metric Definition",
        "",
        METRIC_DEFINITION,
        "",
        "## Reproduction",
        "",
        "```powershell",
        "$env:PYTHONIOENCODING='utf-8'; .\\.venv\\Scripts\\python.exe -m groundtruth.benchmark",
        "```",
        "",
        "## Memory Integrity",
        "",
        "```json",
        json.dumps(payload["memory_integrity"], indent=2, sort_keys=True),
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
        "| Q | Kind | Dataset | Retrieves Retracted Original | Control Retained | Correctness | Retrieved References |",
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


def sample_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    selected_ids = {"Q01", "Q13", "Q18"}
    return [row for row in rows if row["question_id"] in selected_ids]


def write_results_fix_doc(payload: dict[str, Any]) -> None:
    summary = payload.get("summary")
    progress = payload.get("retraction_progress", {})
    lines = [
        "# Fix Pass Results",
        "",
        f"Generated: {payload['generated_at']}",
        f"Status: `{payload['status']}`",
        "",
        "## Retraction Pass",
        "",
        (
            f"- GroundTruth forgotten: {progress.get('groundtruth_forgotten', 0)}/"
            f"{progress.get('retracted_cohort_total', 0)} retracted-cohort originals."
        ),
        f"- Pending: {progress.get('pending', [])}",
        "",
    ]
    if payload.get("quota_error"):
        lines.extend(
            [
                "## Quota Stop",
                "",
                "The pass stopped on a provider quota/rate-limit error. No pending claim was marked forgotten.",
                "",
                "```text",
                payload["quota_error"],
                "```",
                "",
            ]
        )
    if payload.get("memory_integrity"):
        lines.extend(
            [
                "## Memory Integrity",
                "",
                "```json",
                json.dumps(payload["memory_integrity"], indent=2, sort_keys=True),
                "```",
                "",
            ]
        )
    if summary:
        lines.extend(
            [
                "## Regenerated Numbers",
                "",
                (
                    f"- Naive memory retrieves retracted originals in "
                    f"{summary['naive_cites_retracted']}/{summary['total_questions']} answers."
                ),
                (
                    f"- GroundTruth retrieves retracted originals in "
                    f"{summary['groundtruth_cites_retracted']}/{summary['total_questions']} answers."
                ),
                (
                    f"- Control retention: {summary['control_claim_retention']}/"
                    f"{summary['control_claim_total']}."
                ),
                "",
                "## Metric",
                "",
                METRIC_DEFINITION,
                "",
                "## Sample Recall References",
                "",
            ]
        )
        for row in sample_rows(payload["rows"]):
            refs = [
                {
                    "claim_id": ref["claim_id"],
                    "kind": ref["kind"],
                    "cohort": ref.get("cohort"),
                    "retracted": ref["retracted"],
                    "data_id": ref["data_id"],
                }
                for ref in row["references"]
            ]
            lines.extend(
                [
                    f"### {row['question_id']} - {row['dataset']}",
                    "",
                    f"- `cites_retracted`: `{row['cites_retracted']}`",
                    f"- `retracted_dois`: `{row['retracted_dois']}`",
                    "",
                    "```json",
                    json.dumps(refs, indent=2, sort_keys=True),
                    "```",
                    "",
                ]
            )
    if payload.get("demo_synthesis"):
        lines.extend(
            [
                "## Demo Synthesis",
                "",
                "```json",
                json.dumps(payload["demo_synthesis"], indent=2, sort_keys=True),
                "```",
                "",
            ]
        )
    RESULTS_FIX_PATH.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="GroundTruth benchmark")
    parser.add_argument(
        "--skip-prepare",
        action="store_true",
        help="Do not trigger benchmark target retractions before scoring",
    )
    parser.add_argument(
        "--synthesize-demo",
        action="store_true",
        help="Run one small synthesized-answer demo after deterministic scoring",
    )
    return parser.parse_args()


async def main() -> int:
    args = parse_args()
    try:
        payload = await run_benchmark(
            skip_prepare=args.skip_prepare,
            synthesize_demo=args.synthesize_demo,
        )
    except QuotaStop:
        print(f"Wrote {RESULTS_FIX_PATH}")
        return 1
    print(json.dumps(payload["summary"], indent=2, sort_keys=True))
    print(f"Wrote {BENCHMARK_RESULTS_PATH}")
    print(f"Wrote {BENCHMARK_DOC_PATH}")
    print(f"Wrote {RESULTS_FIX_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
