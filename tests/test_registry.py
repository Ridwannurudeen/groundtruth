from __future__ import annotations

from uuid import UUID

import pytest

from groundtruth.registry import DATASETS, load_claims, validate_claims
from groundtruth.runtime import import_cognee


def test_claims_registry_is_complete_and_unique() -> None:
    claims = load_claims()
    validate_claims(claims)

    data_items = [
        (
            claim["datasets"][dataset_name]["dataset_id"],
            claim["datasets"][dataset_name]["data_id"],
        )
        for claim in claims
        for dataset_name in DATASETS
    ]
    assert len(data_items) == 80
    assert len(set(data_items)) == 80
    assert {claim["belief_state"] for claim in claims} == {"active", "retracted"}
    assert all(claim["state_history"] for claim in claims)
    assert sum(claim["belief_state"] == "retracted" for claim in claims) == 25


@pytest.mark.asyncio
async def test_registry_data_ids_exist_in_cognee() -> None:
    cognee = import_cognee()
    claims = load_claims()
    for claim in [claims[0], claims[2], claims[-1]]:
        for dataset_name in DATASETS:
            dataset_entry = claim["datasets"][dataset_name]
            dataset_id = UUID(dataset_entry["dataset_id"])
            data_id = UUID(dataset_entry["data_id"])
            data_ids = {item.id for item in await cognee.datasets.list_data(dataset_id)}
            assert data_id in data_ids
