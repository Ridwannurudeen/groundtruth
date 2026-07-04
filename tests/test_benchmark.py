from __future__ import annotations

import pytest

from groundtruth.benchmark import load_questions, memory_integrity_report, summarize


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


@pytest.mark.asyncio
async def test_committed_corpus_memory_integrity_guard() -> None:
    report = await memory_integrity_report()
    assert report["retracted_original_total"] == 25
    assert report["active_control_total"] == 15
    assert report["violations"] == []
