from __future__ import annotations

import pytest

from groundtruth.adapters import EvidenceItem
from groundtruth.adapters.retraction_watch import (
    RetractionWatchAdapter,
    evidence_from_retraction,
)


def test_evidence_item_requires_authority_feed_match_key_and_basis() -> None:
    item = EvidenceItem(
        adapter="test",
        match_key={"kind": "doi", "doi": "10.5555/original"},
        evidence_ref="10.5555/notice",
        basis="Authority notice supersedes the original.",
        target_state="retracted",
        relationship_name="contradicts",
    )

    assert item.to_dict()["evidence_class"] == "authority_feed"

    with pytest.raises(ValueError, match="authority_feed"):
        EvidenceItem(
            adapter="test",
            match_key={"kind": "doi", "doi": "10.5555/original"},
            evidence_ref="10.5555/notice",
            basis="Authority notice supersedes the original.",
            target_state="retracted",
            relationship_name="contradicts",
            evidence_class="user_assertion",
        )

    with pytest.raises(ValueError, match="match_key"):
        EvidenceItem(
            adapter="test",
            match_key={},
            evidence_ref="10.5555/notice",
            basis="Authority notice supersedes the original.",
            target_state="retracted",
            relationship_name="contradicts",
        )

    with pytest.raises(ValueError, match="basis"):
        EvidenceItem(
            adapter="test",
            match_key={"kind": "doi", "doi": "10.5555/original"},
            evidence_ref="10.5555/notice",
            basis="",
            target_state="retracted",
            relationship_name="contradicts",
        )


def test_retraction_watch_adapter_maps_seed_retraction_to_evidence_item() -> None:
    row = {
        "original_doi": "10.5555/Test-Blood-Pressure",
        "retraction_doi": "10.5555/test-blood-pressure-retraction",
        "retraction_date": "2024-01-02",
        "reason": "Data were unreliable and the results should not be used.",
    }

    item = evidence_from_retraction(row)

    assert item.adapter == "retraction_watch"
    assert item.match_key == {
        "kind": "doi",
        "doi": "10.5555/test-blood-pressure",
    }
    assert item.target_state == "retracted"
    assert item.relationship_name == "contradicts"
    assert item.evidence_ref == "10.5555/test-blood-pressure-retraction"
    assert item.at == "2024-01-02T00:00:00+00:00"
    assert "Retraction Watch record" in item.basis


def test_retraction_watch_adapter_polls_matching_claims_only() -> None:
    adapter = RetractionWatchAdapter(
        [
            {
                "original_doi": "10.5555/matching",
                "retraction_doi": "10.5555/matching-notice",
                "reason": "Unreliable data.",
            },
            {
                "original_doi": "10.5555/not-held",
                "retraction_doi": "10.5555/not-held-notice",
                "reason": "Unreliable data.",
            },
        ]
    )

    items = adapter.poll(
        [
            {
                "claim_id": "T001",
                "doi": "10.5555/matching",
                "source": {"doi": "10.5555/matching"},
            }
        ]
    )

    assert [item.evidence_ref for item in items] == ["10.5555/matching-notice"]
