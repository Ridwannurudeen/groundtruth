from __future__ import annotations

import json

import pytest

from groundtruth.answer import answer_text, superseded_references
from groundtruth.contradictions import (
    judge_retraction_contradiction,
    judge_retraction_supersession,
)
from groundtruth.v2 import (
    all_pair_total,
    heuristic_judge,
    judge_pairs,
    labeled_candidate_pairs,
    load_v2_corpus,
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


def test_spot_check_defaults_to_all_claims() -> None:
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
    )

    assert [check["claim_id"] for check in checks] == ["bad", "good"]


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
    assert {result["pairs"][0]["claim_a_id"], result["pairs"][0]["claim_b_id"]} == {
        "a",
        "b",
    }


def test_vector_candidate_pairs_defaults_to_all_pairs(monkeypatch) -> None:
    monkeypatch.setenv("GROUNDTRUTH_V2_DISABLE_FASTEMBED", "true")
    claims = [
        {"claim_id": "a", "claim_text": "Vitamin D lowers diabetes risk"},
        {"claim_id": "b", "claim_text": "Vitamin D does not lower diabetes risk"},
        {"claim_id": "c", "claim_text": "Sodium reduction lowers blood pressure"},
    ]

    result = vector_candidate_pairs(claims)

    assert len(result["pairs"]) == all_pair_total(claims)


def test_committed_v2_manifest_labels_every_all_pair() -> None:
    corpus = load_v2_corpus()
    claims = corpus["claims"]
    candidate_pairs = [
        {
            "claim_a_id": claims[index]["claim_id"],
            "claim_b_id": claims[other_index]["claim_id"],
            "similarity": 0.0,
        }
        for index in range(len(claims))
        for other_index in range(index + 1, len(claims))
    ]

    labeled = labeled_candidate_pairs(candidate_pairs, corpus["evaluation_pairs"])

    assert len(labeled) == all_pair_total(claims) == 28
    assert sum(pair["expected_conflict"] for pair in labeled) == 3


def test_labeled_candidate_pairs_fails_closed_on_missing_label() -> None:
    with pytest.raises(ValueError, match="Missing V2 evaluation labels"):
        labeled_candidate_pairs(
            [
                {
                    "claim_a_id": "a",
                    "claim_b_id": "b",
                    "similarity": 0.5,
                }
            ],
            [],
        )


@pytest.mark.asyncio
async def test_judge_cache_invalidates_when_claim_input_changes(
    monkeypatch, tmp_path
) -> None:
    monkeypatch.setattr(
        "groundtruth.v2.V2_JUDGE_CACHE_PATH", tmp_path / "judgments.json"
    )
    claims = [
        {
            "claim_id": "a",
            "claim_text": "Vitamin D supplementation does not significantly lower diabetes risk.",
            "cohort": "semantic_conflict",
            "source": {
                "subject": "vitamin D and type 2 diabetes prevention",
                "title": "A",
                "year": 2019,
                "doi": "10.1/a",
            },
        },
        {
            "claim_id": "b",
            "claim_text": "Vitamin D supplementation appears to reduce progression to type 2 diabetes.",
            "cohort": "semantic_conflict",
            "source": {
                "subject": "vitamin D and type 2 diabetes prevention",
                "title": "B",
                "year": 2020,
                "doi": "10.1/b",
            },
        },
    ]
    pairs = [{"claim_a_id": "a", "claim_b_id": "b", "expected_conflict": True}]

    first = await judge_pairs(claims, pairs, use_llm=False)
    second = await judge_pairs(claims, pairs, use_llm=False)
    claims[1] = {
        **claims[1],
        "claim_text": "Vitamin D supplementation has mixed diabetes evidence.",
    }
    third = await judge_pairs(claims, pairs, use_llm=False)

    assert first[0]["cached"] is False
    assert second[0]["cached"] is True
    assert third[0]["cached"] is False
    assert third[0]["pair_signature"] != first[0]["pair_signature"]


@pytest.mark.asyncio
async def test_judge_pairs_records_provider_partial_stop(monkeypatch, tmp_path) -> None:
    cache_path = tmp_path / "judgments.json"
    monkeypatch.setattr("groundtruth.v2.V2_JUDGE_CACHE_PATH", cache_path)

    async def fail_provider(*args, **kwargs):
        raise RuntimeError(
            "Cannot connect to host generativelanguage.googleapis.com:443 [getaddrinfo failed]"
        )

    claims = [
        {
            "claim_id": "a",
            "claim_text": "Vitamin D supplementation does not significantly lower diabetes risk.",
            "cohort": "semantic_conflict",
            "source": {
                "subject": "vitamin D and type 2 diabetes prevention",
                "title": "A",
                "year": 2019,
                "doi": "10.1/a",
            },
        },
        {
            "claim_id": "b",
            "claim_text": "Vitamin D supplementation appears to reduce progression to type 2 diabetes.",
            "cohort": "semantic_conflict",
            "source": {
                "subject": "vitamin D and type 2 diabetes prevention",
                "title": "B",
                "year": 2020,
                "doi": "10.1/b",
            },
        },
    ]

    monkeypatch.setattr("groundtruth.v2.judge_semantic_conflict", fail_provider)
    with pytest.raises(RuntimeError, match="Cannot connect"):
        await judge_pairs(
            claims,
            [{"claim_a_id": "a", "claim_b_id": "b", "expected_conflict": True}],
            use_llm=True,
        )

    payload = json.loads(cache_path.read_text(encoding="utf-8"))
    assert payload["_partial_stop"]["stop_reason"] == "provider_error"
    assert payload["_partial_stop"]["completed_pairs"] == 0


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
