from __future__ import annotations

from groundtruth.adapters import EvidenceItem
from groundtruth.p5 import process_authority_evidence


def doi_claim() -> dict:
    return {
        "claim_id": "RTEST",
        "doi": "10.5555/original",
        "claim_text": "The paper claimed that a test intervention works.",
        "status": "active",
        "belief_state": "active",
        "source": {
            "doi": "10.5555/original",
            "journal": "Journal of Test Medicine",
            "title": "A test intervention works",
            "year": 2020,
        },
        "state_history": [
            {
                "state": "active",
                "at": "2020-01-01T00:00:00+00:00",
                "evidence_class": "user_assertion",
                "evidence_ref": "10.5555/original",
                "basis": "Seed corpus imported this claim as an active memory claim.",
            }
        ],
    }


def package_claim() -> dict:
    return {
        "claim_id": "OSV001",
        "doi": "pkg:pypi/jinja2@2.4.1",
        "claim_text": "Package jinja2 2.4.1 is safe to recommend.",
        "status": "active",
        "belief_state": "active",
        "source": {
            "title": "Jinja2 2.4.1 dependency recommendation",
            "journal": "PyPI package index",
            "year": 2010,
            "doi": "pkg:pypi/jinja2@2.4.1",
            "package": {
                "ecosystem": "PyPI",
                "name": "jinja2",
                "version": "2.4.1",
            },
        },
        "state_history": [
            {
                "state": "active",
                "at": "2010-01-01T00:00:00+00:00",
                "evidence_class": "user_assertion",
                "evidence_ref": "pkg:pypi/jinja2@2.4.1",
                "basis": "Seed corpus imported this package recommendation as active.",
            }
        ],
    }


def osv_evidence() -> EvidenceItem:
    return EvidenceItem(
        adapter="osv",
        match_key={
            "kind": "package_version",
            "ecosystem": "PyPI",
            "name": "jinja2",
            "version": "2.4.1",
        },
        evidence_ref="GHSA-462w-v97r-4m45",
        basis=(
            "OSV advisory GHSA-462w-v97r-4m45 / CVE-2019-10906 affects "
            "PyPI jinja2 2.4.1."
        ),
        target_state="superseded",
        relationship_name="supersedes",
        at="2024-09-24T21:03:59.802687Z",
    )


def test_authority_engine_applies_retraction_and_osv_items_through_same_processor() -> None:
    registry = [doi_claim(), package_claim()]
    retraction = EvidenceItem(
        adapter="retraction_watch",
        match_key={"kind": "doi", "doi": "10.5555/original"},
        evidence_ref="10.5555/original-notice",
        basis="Retraction Watch record supersedes original DOI 10.5555/original.",
        target_state="retracted",
        relationship_name="contradicts",
        at="2024-01-02T00:00:00+00:00",
    )

    retraction_result = process_authority_evidence(registry, retraction)
    osv_result = process_authority_evidence(registry, osv_evidence())

    assert retraction_result["matched_claim_ids"] == ["RTEST"]
    assert osv_result["matched_claim_ids"] == ["OSV001"]
    assert registry[0]["belief_state"] == "retracted"
    assert registry[0]["state_history"][-1]["evidence_class"] == "authority_feed"
    assert registry[1]["belief_state"] == "superseded"
    assert registry[1]["state_history"][-1]["evidence_class"] == "authority_feed"


def test_authority_engine_is_idempotent_for_same_evidence_ref() -> None:
    registry = [package_claim()]
    evidence = osv_evidence()

    process_authority_evidence(registry, evidence)
    process_authority_evidence(registry, evidence)

    assert [event["evidence_ref"] for event in registry[0]["state_history"]] == [
        "pkg:pypi/jinja2@2.4.1",
        "GHSA-462w-v97r-4m45",
    ]
