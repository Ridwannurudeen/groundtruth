from __future__ import annotations

import pytest

from groundtruth.answer import answer, reference_for_claim


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
    assert any(
        reference["kind"] == "original_claim" for reference in naive["references"]
    )
    assert naive["retracted_dois"] == [context["claim"]["source"]["doi"]]

    assert groundtruth["cites_retracted"] is False
    assert any(
        reference["kind"] == "retraction_notice"
        for reference in groundtruth["references"]
    )
    assert all(
        reference["kind"] != "original_claim" or not reference["retracted"]
        for reference in groundtruth["references"]
    )
