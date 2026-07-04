from __future__ import annotations

from groundtruth.answer import answer_text, superseded_references
from groundtruth.contradictions import judge_retraction_contradiction, judge_retraction_supersession
from groundtruth.v2 import (
    heuristic_judge,
    semantic_metrics,
    spot_check_claims,
    vector_candidate_pairs,
)


def test_tier_a_retraction_supersession_keeps_doi_lookup_behavior() -> None:
    claim = {"doi": "10.5555/original"}
    retraction = {"original_doi": "10.5555/original", "reason": "Unreliable data"}

    decision = judge_retraction_supersession(claim, retraction)
    legacy = judge_retraction_contradiction(claim, retraction)

    assert decision.contradicts is True
    assert decision.superseded_doi == "10.5555/original"
    assert legacy == decision


def test_spot_check_rejects_title_echo_claims() -> None:
    checks = spot_check_claims(
        [
            {
                "claim_id": "bad",
                "claim_text": "The paper claimed that Vitamin D Supplementation and Prevention of Type 2 Diabetes.",
            },
            {
                "claim_id": "good",
                "claim_text": "Vitamin D supplementation does not significantly lower diabetes risk versus placebo.",
            },
        ],
        count=2,
    )

    assert checks[0]["real_assertion"] is False
    assert checks[1]["real_assertion"] is True


def test_heuristic_judge_flags_same_subject_positive_negative_claims() -> None:
    claim_a = {
        "claim_id": "a",
        "claim_text": "Vitamin D supplementation does not significantly lower diabetes risk.",
        "source": {
            "subject": "vitamin D and type 2 diabetes prevention",
            "title": "A",
            "year": 2019,
            "doi": "10.1/a",
        },
    }
    claim_b = {
        "claim_id": "b",
        "claim_text": "Vitamin D supplementation appears to reduce progression to type 2 diabetes.",
        "source": {
            "subject": "vitamin D and type 2 diabetes prevention",
            "title": "B",
            "year": 2020,
            "doi": "10.1/b",
        },
    }

    decision = heuristic_judge(claim_a, claim_b)

    assert decision.conflicts is True
    assert decision.confidence >= 0.7


def test_semantic_metrics_counts_precision_and_recall() -> None:
    rows = [
        {
            "expected_conflict": True,
            "decision": {"conflicts": True, "confidence": 0.9},
        },
        {
            "expected_conflict": True,
            "decision": {"conflicts": False, "confidence": 0.2},
        },
        {
            "expected_conflict": False,
            "decision": {"conflicts": True, "confidence": 0.8},
        },
        {
            "expected_conflict": False,
            "decision": {"conflicts": False, "confidence": 0.1},
        },
    ]

    metrics = semantic_metrics(rows)

    assert metrics["true_positive"] == 1
    assert metrics["false_negative"] == 1
    assert metrics["false_positive"] == 1
    assert metrics["true_negative"] == 1
    assert metrics["precision"] == 0.5
    assert metrics["recall"] == 0.5


def test_vector_candidate_pairs_has_resumable_pair_keys(monkeypatch) -> None:
    monkeypatch.setenv("GROUNDTRUTH_V2_DISABLE_FASTEMBED", "true")
    claims = [
        {"claim_id": "a", "claim_text": "Vitamin D lowers diabetes risk"},
        {"claim_id": "b", "claim_text": "Vitamin D does not lower diabetes risk"},
    ]

    result = vector_candidate_pairs(claims, neighbors_per_claim=1)

    assert result["pairs"]
    assert {result["pairs"][0]["claim_a_id"], result["pairs"][0]["claim_b_id"]} == {"a", "b"}


def test_superseded_warning_follows_retrieved_reference_order() -> None:
    references = [
        {
            "claim_id": "V2C004",
            "kind": "original_claim",
            "doi": "10.2/omega",
            "data_id": "omega-data-id",
        },
        {
            "claim_id": "V2C001",
            "kind": "original_claim",
            "doi": "10.1/vitamin-d",
            "data_id": "vitamin-data-id",
        },
    ]
    reference_edges = {
        "V2C001:original_claim": [
            {
                "relationship_name": "contradicts",
                "attributes": {
                    "target_data_id": "vitamin-data-id",
                    "basis": "vitamin basis",
                },
            }
        ],
        "V2C004:original_claim": [
            {
                "relationship_name": "contradicts",
                "attributes": {
                    "target_data_id": "omega-data-id",
                    "basis": "omega basis",
                },
            }
        ],
    }

    superseded = superseded_references(references, reference_edges)
    text = answer_text("dataset", references, "synthesized answer", superseded)

    assert superseded[0]["reference"]["claim_id"] == "V2C004"
    assert "10.2/omega" in text
    assert "omega basis" in text
