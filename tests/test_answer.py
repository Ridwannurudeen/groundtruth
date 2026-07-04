from __future__ import annotations

import pytest

from groundtruth.answer import answer, rank_graph_references, reference_for_claim


def test_reference_for_claim_uses_ground_truth_cohort() -> None:
    claim = {
        "claim_id": "R999",
        "doi": "10.5555/retracted-but-active",
        "status": "active",
        "cohort": "retracted_original",
        "source": {"journal": "Test Journal"},
    }
    dataset_entry = {"dataset_id": "dataset-1", "data_id": "data-1", "status": "active"}

    reference = reference_for_claim(
        claim,
        "groundtruth_memory",
        dataset_entry,
        kind="original_claim",
        data_id="data-1",
        score=1,
    )

    assert reference["retracted"] is True
    assert reference["cohort"] == "retracted_original"
    assert reference["belief_state"] == "active"
    assert reference["belief_evidence_class"] == "user_assertion"


def test_rank_graph_references_filters_full_graph_noise() -> None:
    claims = [
        {
            "claim_id": "V2C004",
            "claim_text": "Marine omega-3 supplementation lowers cardiovascular disease risk.",
            "doi": "10.2/omega",
            "source": {
                "title": "Marine Omega-3 Supplementation and Cardiovascular Disease",
                "journal": "Journal",
            },
        },
        {
            "claim_id": "V2C007",
            "claim_text": "Reduced dietary sodium lowers blood pressure.",
            "doi": "10.2/sodium",
            "source": {
                "title": "Reduced Dietary Sodium and Blood Pressure",
                "journal": "Journal",
            },
        },
    ]
    references = [
        {"claim_id": "V2C007", "kind": "original_claim", "retrieval_rank": 1},
        {"claim_id": "V2C004", "kind": "original_claim", "retrieval_rank": 2},
    ]

    ranked = rank_graph_references(
        "Should omega-3 supplementation reduce cardiovascular disease events?",
        references,
        claims,
    )

    assert [reference["claim_id"] for reference in ranked] == ["V2C004"]
    assert ranked[0]["graph_retrieval_rank"] == 2
    assert ranked[0]["graph_relevance_score"] > 0


@pytest.mark.asyncio
async def test_answer_flags_retracted_sources(retraction_lifecycle):
    context = retraction_lifecycle
    naive_dataset, groundtruth_dataset = context["dataset_names"]

    naive = await answer(
        context["question"],
        naive_dataset,
        registry_path=context["registry_path"],
    )
    groundtruth = await answer(
        context["question"],
        groundtruth_dataset,
        registry_path=context["registry_path"],
    )

    assert naive["cites_retracted"] is True
    assert naive["cites_by_state"]["retracted"] >= 1
    assert any(
        reference["kind"] == "original_claim" for reference in naive["references"]
    )
    assert naive["retracted_dois"] == [context["claim"]["source"]["doi"]]

    assert groundtruth["cites_retracted"] is False
    assert groundtruth["cites_by_state"]["retracted"] >= 1
    assert any(
        reference["kind"] == "retraction_notice"
        for reference in groundtruth["references"]
    )
    assert all(
        reference["kind"] != "original_claim" or not reference["retracted"]
        for reference in groundtruth["references"]
    )
