from __future__ import annotations

import json

import pytest

from groundtruth.timeline import (
    answer_as_of,
    render_results_markdown,
    scripted_run,
    state_at,
    timeline_diff,
    write_artifacts,
)


def retracted_claim() -> dict:
    return {
        "claim_id": "R001",
        "doi": "10.1056/nejmoa2023386",
        "claim_text": "The paper claimed that avacopan treats ANCA-associated vasculitis.",
        "status": "retracted_forgotten",
        "belief_state": "retracted",
        "source": {
            "doi": "10.1056/nejmoa2023386",
            "journal": "NEJM",
            "title": "Avacopan for the Treatment of ANCA-Associated Vasculitis",
            "year": 2021,
        },
        "cohort": "retracted_original",
        "datasets": {
            "groundtruth_memory": {
                "data_id": "original-data",
                "dataset_id": "dataset",
                "status": "retracted_forgotten",
                "retraction_notice_data_id": "notice-data",
            }
        },
        "state_history": [
            {
                "state": "active",
                "at": "2021-01-01T00:00:00+00:00",
                "evidence_class": "user_assertion",
                "evidence_ref": "10.1056/nejmoa2023386",
                "basis": "Seed corpus imported this claim as an active memory claim.",
            },
            {
                "state": "retracted",
                "at": "2026-06-29T00:00:00+00:00",
                "evidence_class": "authority_feed",
                "evidence_ref": "10.1056/nejme2608684",
                "basis": "Retraction Watch record supersedes original DOI.",
            },
        ],
    }


def contested_claim() -> dict:
    claim = retracted_claim()
    claim["claim_id"] = "V2C003"
    claim["doi"] = "10.1056/NEJMoa1811403"
    claim["status"] = "active"
    claim["belief_state"] = "superseded"
    claim["source"]["title"] = "Marine n-3 Fatty Acids and Prevention"
    claim["source"]["journal"] = "New England Journal of Medicine"
    claim["datasets"]["groundtruth_memory"]["status"] = "active"
    claim["state_history"] = [
        {
            "state": "active",
            "at": "2019-01-01T00:00:00+00:00",
            "evidence_class": "user_assertion",
            "evidence_ref": "10.1056/NEJMoa1811403",
            "basis": "Seed corpus imported this claim as an active memory claim.",
        },
        {
            "state": "contested",
            "at": "2026-07-04T00:00:00+00:00",
            "evidence_class": "semantic_inference",
            "evidence_ref": "pair:V2C003::V2C004",
            "basis": "Semantic inference marked competing omega-3 claims contested.",
        },
        {
            "state": "superseded",
            "at": "2026-07-05T00:00:00+00:00",
            "evidence_class": "user_assertion",
            "evidence_ref": "adjudication:V2C003::V2C004",
            "basis": "User adjudication resolved the conflict.",
        },
    ]
    return claim


def write_claims(tmp_path, claims: list[dict]) -> str:
    path = tmp_path / "claims.json"
    path.write_text(json.dumps(claims) + "\n", encoding="utf-8")
    return path


def test_state_at_returns_latest_event_before_date() -> None:
    claim = retracted_claim()

    assert state_at(claim, "2023-01-01")["state"] == "active"
    assert state_at(claim, "2026-06-30")["state"] == "retracted"


def test_state_at_returns_none_before_claim_exists() -> None:
    assert state_at(retracted_claim(), "2020-12-31") is None


def test_answer_as_of_switches_original_to_retraction_notice(tmp_path) -> None:
    registry_path = write_claims(tmp_path, [retracted_claim()])
    question = "What did we believe about Avacopan treatment?"

    before = answer_as_of(question, "2023-01-01", registry_path=registry_path)
    after = answer_as_of(question, "2026-07-04", registry_path=registry_path)

    assert before["references"][0]["kind"] == "original_claim"
    assert before["references"][0]["belief_state"] == "active"
    assert before["cites_retracted"] is False
    assert after["references"][0]["kind"] == "retraction_notice"
    assert after["cites_by_state"]["retracted"] == 1
    assert after["cites_retracted"] is False
    assert after["text"].startswith("As of 2026-07-04T00:00:00+00:00")


def test_timeline_diff_groups_retraction_as_revised_and_purged(tmp_path) -> None:
    registry_path = write_claims(tmp_path, [retracted_claim()])

    diff = timeline_diff("2026-06-28", "2026-06-30", registry_path=registry_path)

    assert diff["changes"]["revised"][0]["evidence_class"] == "authority_feed"
    assert diff["changes"]["purged"][0]["memory_status"] == "retracted_forgotten"


def test_timeline_diff_groups_contested_then_resolved(tmp_path) -> None:
    registry_path = write_claims(tmp_path, [contested_claim()])

    contested = timeline_diff("2026-07-03", "2026-07-04", registry_path=registry_path)
    resolved = timeline_diff("2026-07-04", "2026-07-06", registry_path=registry_path)

    assert contested["changes"]["contested"][0]["claim_id"] == "V2C003"
    assert resolved["changes"]["revised"][0]["from_state"] == "contested"
    assert resolved["changes"]["revised"][0]["to_state"] == "superseded"


def test_answer_as_of_includes_chain_for_each_reference(tmp_path) -> None:
    registry_path = write_claims(tmp_path, [retracted_claim()])

    result = answer_as_of(
        "What did we believe about Avacopan treatment?",
        "2023-01-01",
        registry_path=registry_path,
    )

    chain = result["chains"][0]["state_history"]
    assert [event["state"] for event in chain] == ["active"]
    assert all(event["at"] <= "2023-01-01T00:00:00+00:00" for event in chain)


def test_timeline_diff_rejects_reversed_range(tmp_path) -> None:
    registry_path = write_claims(tmp_path, [retracted_claim()])

    with pytest.raises(ValueError, match="from date"):
        timeline_diff("2026-07-04", "2023-01-01", registry_path=registry_path)


def test_results_artifacts_render_raw_run(tmp_path) -> None:
    registry_path = write_claims(tmp_path, [retracted_claim()])
    run = scripted_run(
        question="What did we believe about Avacopan treatment?",
        from_date="2023-01-01",
        to_date="2026-07-04",
        registry_path=registry_path,
    )
    timeline_run_path = tmp_path / "timeline_run.json"
    results_path = tmp_path / "RESULTS-V3-P4.md"

    write_artifacts(run, timeline_run_path=timeline_run_path, results_path=results_path)

    assert json.loads(timeline_run_path.read_text())["timeline"]["changes"]["revised"]
    markdown = results_path.read_text()
    assert "GroundTruth V3 P4 Results" in markdown
    assert "python.exe -m groundtruth.timeline --results-v3-p4" in markdown
    assert "Raw Run" in markdown
    assert render_results_markdown(run) == markdown
