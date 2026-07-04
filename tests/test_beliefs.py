from __future__ import annotations

from groundtruth.beliefs import cites_by_state, transition_belief


def test_transition_belief_records_classed_evidence() -> None:
    claim = {
        "claim_id": "T001",
        "doi": "10.5555/original",
        "status": "active",
        "source": {"doi": "10.5555/original", "year": 2020},
    }

    transition_belief(
        claim,
        "contested",
        "semantic_inference",
        "pair:T001:T002",
        "Structured judge confidence landed in the contested band.",
        at="2026-07-04T00:00:00+00:00",
    )

    assert claim["belief_state"] == "contested"
    assert claim["state_history"][-1] == {
        "state": "contested",
        "at": "2026-07-04T00:00:00+00:00",
        "evidence_class": "semantic_inference",
        "evidence_ref": "pair:T001:T002",
        "basis": "Structured judge confidence landed in the contested band.",
    }


def test_cites_by_state_counts_all_known_states() -> None:
    counts = cites_by_state(
        [
            {"belief_state": "active"},
            {"belief_state": "retracted"},
            {"belief_state": "retracted"},
        ]
    )

    assert counts == {
        "active": 1,
        "contested": 0,
        "superseded": 0,
        "retracted": 2,
        "purged": 0,
    }
