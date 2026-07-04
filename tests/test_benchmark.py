from __future__ import annotations

import pytest

from groundtruth.registry import write_json
from groundtruth.benchmark import (
    load_questions,
    memory_integrity_report,
    summarize,
    v2_addendum_lines,
)


def test_benchmark_question_manifest_shape() -> None:
    questions = load_questions()
    assert len(questions) == 20
    assert sum(question["kind"] == "retracted" for question in questions) == 12
    assert sum(question["kind"] == "control" for question in questions) == 5
    assert sum(question["kind"] == "mixed" for question in questions) == 3


def test_benchmark_summary_counts() -> None:
    rows = [
        {
            "question_id": "Q01",
            "dataset": "naive_memory",
            "kind": "retracted",
            "cites_retracted": True,
            "control_retained": False,
        },
        {
            "question_id": "Q01",
            "dataset": "groundtruth_memory",
            "kind": "retracted",
            "cites_retracted": False,
            "control_retained": False,
        },
        {
            "question_id": "Q13",
            "dataset": "naive_memory",
            "kind": "control",
            "cites_retracted": False,
            "control_retained": True,
        },
        {
            "question_id": "Q13",
            "dataset": "groundtruth_memory",
            "kind": "control",
            "cites_retracted": False,
            "control_retained": True,
        },
    ]

    summary = summarize(rows)
    assert summary["total_questions"] == 2
    assert summary["naive_cites_retracted"] == 1
    assert summary["groundtruth_cites_retracted"] == 0
    assert summary["control_claim_retention"] == 1
    assert summary["control_claim_total"] == 1


def test_v2_addendum_lines_uses_results_payload(tmp_path) -> None:
    path = tmp_path / "v2_results.json"
    write_json(
        path,
        {
            "status": "complete",
            "judge": "heuristic_test_mode",
            "evaluation_coverage": {
                "protocol": "exhaustive_all_pairs_over_committed_v2_claims",
                "all_pair_total": 28,
                "evaluated_pairs": 28,
            },
            "semantic_metrics": {
                "evaluated_pairs": 28,
                "true_positive": 3,
                "true_negative": 25,
                "false_positive": 0,
                "false_negative": 0,
                "precision": 1.0,
                "recall": 1.0,
            },
            "answer_probes": [
                {"status": "completed", "cites_superseded": True},
                {"status": "skipped_quota_error"},
            ],
            "quota_error": None,
        },
    )

    lines = "\n".join(v2_addendum_lines(path))

    assert "28/28 committed claim pairs evaluated" in lines
    assert "TP 3, TN 25, FP 0, FN 0" in lines
    assert "1/2 completed; 1/2 surfaced conflicted graph references" in lines


@pytest.mark.asyncio
async def test_committed_corpus_memory_integrity_guard() -> None:
    report = await memory_integrity_report()
    assert report["retracted_original_total"] == 25
    assert report["active_control_total"] == 15
    assert report["violations"] == []
