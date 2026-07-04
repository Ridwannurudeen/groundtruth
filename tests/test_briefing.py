from __future__ import annotations

import json

import pytest

from groundtruth.briefing import (
    after_answer_text,
    before_answer_text,
    diff_snapshots,
    make_fixture_transition,
    remember_evening_evidence,
    render_briefing_markdown,
    snapshot_registry,
    scripted_run,
)


def sample_claim() -> dict:
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
        "datasets": {
            "groundtruth_memory": {
                "data_id": "original-data",
                "dataset_id": "dataset",
                "status": "retracted_forgotten",
            }
        },
        "retraction": {
            "retraction_doi": "10.1056/nejme2608684",
            "reason": "Manipulation of Results;",
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


def test_diff_snapshots_groups_revised_and_purged_claims() -> None:
    before_claim, after_claim = make_fixture_transition(sample_claim())

    diff = diff_snapshots(
        snapshot_registry([before_claim]),
        snapshot_registry([after_claim]),
    )

    assert diff["learned_last_night"] == []
    assert diff["now_contested"] == []
    assert diff["revised"][0]["claim_id"] == "R001"
    assert diff["revised"][0]["evidence_class"] == "authority_feed"
    assert diff["purged"][0]["memory_status"] == "retracted_forgotten"


def test_render_briefing_markdown_contains_p3_sections() -> None:
    claim = sample_claim()
    briefing = {
        "generated_at": "2026-07-04T08:00:00+00:00",
        "status": "complete_session_executed_fixture",
        "session_id": "analyst-2026-07-04",
        "dataset": "groundtruth_memory",
        "learned_last_night": [
            {
                "claim_id": "R001",
                "doi": "10.1056/nejme2608684",
                "title": "Retraction notice",
                "belief_state": "active",
                "evidence_class": "authority_feed",
                "evidence_ref": "10.1056/nejme2608684",
                "basis": "Retraction arrived in session.",
            }
        ],
        "now_contested": [],
        "revised": [snapshot_registry([claim])["R001"]],
        "purged": [snapshot_registry([claim])["R001"]],
        "question": "What does the memory say?",
        "before_answer": before_answer_text(make_fixture_transition(claim)[0]),
        "after_answer": after_answer_text(claim),
    }

    markdown = render_briefing_markdown(briefing)

    assert "## Learned Last Night" in markdown
    assert "## Now Contested" in markdown
    assert "## Revised" in markdown
    assert "## Purged" in markdown
    assert "## Before Answer" in markdown
    assert "## After Answer" in markdown
    assert "groundtruth_memory still cites" in markdown
    assert "no longer cites" in markdown


@pytest.mark.asyncio
async def test_remember_evening_evidence_disables_self_improvement() -> None:
    calls = []

    class FakeCognee:
        async def remember(self, text, **kwargs):
            calls.append((text, kwargs))
            return {
                "status": "session_stored",
                "dataset_name": kwargs["dataset_name"],
                "session_ids": [kwargs["session_id"]],
            }

    result = await remember_evening_evidence(
        ["Retraction notice text"],
        dataset_name="groundtruth_memory",
        session_id="analyst-2026-07-04",
        cognee_client=FakeCognee(),
    )

    assert result[0]["status"] == "session_stored"
    assert calls == [
        (
            "Retraction notice text",
            {
                "dataset_name": "groundtruth_memory",
                "session_id": "analyst-2026-07-04",
                "self_improvement": False,
            },
        )
    ]


@pytest.mark.asyncio
async def test_scripted_run_retains_session_evidence_trace(monkeypatch, tmp_path) -> None:
    claims_path = tmp_path / "claims.json"
    claims_path.write_text(json.dumps([sample_claim()]) + "\n")

    async def fake_remember(texts, *, dataset_name, session_id):
        return [
            {
                "status": "session_stored",
                "dataset_name": dataset_name,
                "session_ids": [session_id],
                "text_count": len(texts),
            }
        ]

    monkeypatch.setattr("groundtruth.briefing.remember_evening_evidence", fake_remember)
    monkeypatch.setattr("groundtruth.briefing.current_contested_items", lambda: [])
    monkeypatch.setattr("groundtruth.briefing.current_revised_items", lambda: [])

    run = await scripted_run(
        session_id="analyst-2026-07-04",
        claim_id="R001",
        live_session=True,
        claims_path=claims_path,
    )

    session = run["session_remember"]
    assert session["status"] == "executed"
    assert session["source_claim_id"] == "R001"
    assert session["source_registry_path"] == str(claims_path)
    assert session["self_improvement"] is False
    assert session["texts"] == [
        "Retraction Watch notice 10.1056/nejme2608684 says original DOI "
        "10.1056/nejmoa2023386 was retracted. Reason: Manipulation of Results;"
    ]
    assert run["briefing"]["status"] == "complete_session_executed_fixture"
