from __future__ import annotations

import json
from uuid import UUID

import pytest

from groundtruth.contradictions import ledger_nodes


@pytest.mark.asyncio
async def test_watcher_retraction_lifecycle(retraction_lifecycle):
    context = retraction_lifecycle
    naive_dataset, groundtruth_dataset = context["dataset_names"]
    result = context["result"]

    assert result["claim_id"] == "T001"
    assert result["decision"]["contradicts"] is True
    assert result["graph_edges_before_forget"] >= 1
    assert result["ledger_edges_before_forget"] >= 1
    assert result["graph_edges_after_forget"] == 0

    registry = json.loads(context["registry_path"].read_text(encoding="utf-8"))
    claim = registry[0]
    assert claim["status"] == "retracted_forgotten"
    assert claim["datasets"][groundtruth_dataset]["status"] == "retracted_forgotten"
    assert claim["datasets"][naive_dataset]["status"] == "retracted_retained"

    groundtruth_entry = claim["datasets"][groundtruth_dataset]
    naive_entry = claim["datasets"][naive_dataset]
    groundtruth_dataset_id = UUID(groundtruth_entry["dataset_id"])
    naive_dataset_id = UUID(naive_entry["dataset_id"])

    groundtruth_original_nodes = await ledger_nodes(
        groundtruth_dataset_id,
        UUID(groundtruth_entry["data_id"]),
    )
    groundtruth_notice_nodes = await ledger_nodes(
        groundtruth_dataset_id,
        UUID(groundtruth_entry["retraction_notice_data_id"]),
    )
    naive_original_nodes = await ledger_nodes(
        naive_dataset_id,
        UUID(naive_entry["data_id"]),
    )

    assert groundtruth_original_nodes == []
    assert groundtruth_notice_nodes
    assert naive_original_nodes

    audit_events = [
        json.loads(line)
        for line in context["audit_log_path"].read_text(encoding="utf-8").splitlines()
    ]
    actions = {event["action"] for event in audit_events}
    assert "detected_retraction" in actions
    assert "remembered_retraction_notice" in actions
    assert "added_contradiction_edge" in actions
    assert "forgot_superseded_claim" in actions
