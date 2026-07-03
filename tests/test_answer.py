from __future__ import annotations

import pytest

from groundtruth.answer import answer


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
    assert any(reference["kind"] == "original_claim" for reference in naive["references"])
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
