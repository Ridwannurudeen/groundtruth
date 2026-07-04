from __future__ import annotations

from uuid import uuid4

import pytest

from groundtruth.contest import (
    adjudicate_pair,
    list_contested_pairs,
    mark_contested,
    pair_key,
    semantic_action,
)
from groundtruth.registry import load_json, write_json


DATASET = "groundtruth_v2_semantic_memory"


def semantic_row(
    confidence: float, *, conflicts: bool = True, direction: str = "mutual"
):
    return {
        "claim_a_id": "V2C003",
        "claim_b_id": "V2C004",
        "decision": {
            "conflicts": conflicts,
            "direction": direction,
            "basis": "Omega-3 claims disagree on cardiovascular outcomes.",
            "confidence": confidence,
        },
    }


def registry_entries() -> list[dict]:
    dataset_id = str(uuid4())
    return [
        {
            "claim_id": "V2C003",
            "claim_text": "Omega-3 supplementation does not lower major events.",
            "doi": "10.5555/omega-negative",
            "status": "active",
            "cohort": "semantic_conflict",
            "source": {
                "doi": "10.5555/omega-negative",
                "journal": "Journal",
                "title": "Omega negative",
                "year": 2019,
            },
            "datasets": {DATASET: {"dataset_id": dataset_id, "data_id": str(uuid4())}},
        },
        {
            "claim_id": "V2C004",
            "claim_text": "Omega-3 supplementation lowers cardiovascular risk.",
            "doi": "10.5555/omega-positive",
            "status": "active",
            "cohort": "semantic_conflict",
            "source": {
                "doi": "10.5555/omega-positive",
                "journal": "Journal",
                "title": "Omega positive",
                "year": 2019,
            },
            "datasets": {DATASET: {"dataset_id": dataset_id, "data_id": str(uuid4())}},
        },
    ]


def test_semantic_action_confidence_bands() -> None:
    assert semantic_action(semantic_row(1.0, conflicts=False)["decision"]) == "log_only"
    assert semantic_action(semantic_row(0.69)["decision"]) == "log_only"
    assert semantic_action(semantic_row(0.75)["decision"]) == "contested"
    assert semantic_action(semantic_row(1.0)["decision"]) == "contested"
    assert (
        semantic_action(semantic_row(0.9, direction="a_supersedes_b")["decision"])
        == "auto_act"
    )


def test_mark_contested_is_idempotent_and_lists_open_queue(tmp_path) -> None:
    registry_path = tmp_path / "claims.json"
    queue_path = tmp_path / "contested_pairs.json"
    registry = registry_entries()
    write_json(registry_path, registry)

    first = mark_contested(
        registry,
        semantic_row(1.0),
        dataset=DATASET,
        registry_path=registry_path,
        queue_path=queue_path,
        at="2026-07-04T00:00:00+00:00",
    )
    second = mark_contested(
        load_json(registry_path),
        semantic_row(1.0),
        dataset=DATASET,
        registry_path=registry_path,
        queue_path=queue_path,
        at="2026-07-04T00:01:00+00:00",
    )

    saved_registry = load_json(registry_path)
    open_items = list_contested_pairs(queue_path)

    assert first["pair"] == pair_key("V2C003", "V2C004")
    assert second["pair"] == first["pair"]
    assert len(load_json(queue_path)) == 1
    assert {entry["belief_state"] for entry in saved_registry} == {"contested"}
    assert [len(entry["state_history"]) for entry in saved_registry] == [2, 2]
    assert len(open_items) == 1
    assert open_items[0]["claims"][0]["belief_state"] == "contested"


@pytest.mark.asyncio
async def test_adjudicate_pair_resolves_with_user_assertion(tmp_path) -> None:
    registry_path = tmp_path / "claims.json"
    queue_path = tmp_path / "contested_pairs.json"
    registry = registry_entries()
    write_json(registry_path, registry)
    mark_contested(
        registry,
        semantic_row(1.0),
        dataset=DATASET,
        registry_path=registry_path,
        queue_path=queue_path,
        at="2026-07-04T00:00:00+00:00",
    )

    result = await adjudicate_pair(
        pair_key("V2C003", "V2C004"),
        "none",
        basis="Reviewer found the apparent conflict was endpoint mismatch.",
        queue_path=queue_path,
        apply_forget=False,
    )
    saved_registry = load_json(registry_path)

    assert result["status"] == "resolved"
    assert result["forget_results"] == []
    assert [change["evidence_class"] for change in result["state_changes"]] == [
        "user_assertion",
        "user_assertion",
    ]
    assert {entry["belief_state"] for entry in saved_registry} == {"active"}
    assert list_contested_pairs(queue_path) == []
