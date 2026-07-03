from __future__ import annotations

import os
from uuid import uuid4

import pytest_asyncio

from groundtruth.ingest import dataset_id, store_claim_deterministic
from groundtruth.registry import write_json
from groundtruth.runtime import import_cognee
from groundtruth.watcher import process_retraction


@pytest_asyncio.fixture
async def retraction_lifecycle(tmp_path):
    os.environ["COGNEE_SKIP_CONNECTION_TEST"] = "true"
    cognee = import_cognee()
    suffix = uuid4().hex[:8]
    dataset_names = (f"test_naive_{suffix}", f"test_groundtruth_{suffix}")
    claim = {
        "claim_id": "T001",
        "claim_text": (
            "The paper claimed that Test Compound lowers systolic blood pressure in adults."
        ),
        "status_at_seed": "active",
        "source": {
            "title": "Test Compound lowers systolic blood pressure in adults",
            "journal": "Journal of Test Medicine",
            "year": 2020,
            "doi": "10.5555/test-blood-pressure",
            "subject": "blood pressure",
        },
        "cohort": "retracted_original",
    }
    retraction = {
        "claim_id": "T001",
        "original_doi": claim["source"]["doi"],
        "retraction_doi": "10.5555/test-blood-pressure-retraction",
        "retraction_date": "2024-01-02",
        "reason": "Data were unreliable and the results should not be used.",
        "nature": "Retraction",
    }
    registry_path = tmp_path / "claims.json"
    seed_path = tmp_path / "seed_corpus.json"
    audit_log_path = tmp_path / "audit_log.jsonl"

    for name in dataset_names:
        if await dataset_id(cognee, name):
            await cognee.forget(dataset=name)

    datasets = {}
    for name in dataset_names:
        datasets[name] = await store_claim_deterministic(cognee, claim, name)

    write_json(
        registry_path,
        [
            {
                "claim_id": claim["claim_id"],
                "doi": claim["source"]["doi"],
                "claim_text": claim["claim_text"],
                "source": claim["source"],
                "status": "active",
                "cohort": claim["cohort"],
                "retraction_doi": retraction["retraction_doi"],
                "datasets": datasets,
            }
        ],
    )
    write_json(
        seed_path,
        {
            "subject_area": "test blood pressure",
            "claims": [claim],
            "held_back_retractions": [retraction],
        },
    )

    try:
        result = await process_retraction(
            claim["source"]["doi"],
            registry_path=registry_path,
            seed_path=seed_path,
            audit_log_path=audit_log_path,
            dataset_names=dataset_names,
        )
        yield {
            "dataset_names": dataset_names,
            "claim": claim,
            "registry_path": registry_path,
            "seed_path": seed_path,
            "audit_log_path": audit_log_path,
            "result": result,
            "question": "what does the research say about Test Compound blood pressure?",
        }
    finally:
        for name in dataset_names:
            if await dataset_id(cognee, name):
                await cognee.forget(dataset=name)
