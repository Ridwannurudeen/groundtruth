from __future__ import annotations

import json
from pathlib import Path
from typing import Any
from uuid import UUID

from groundtruth.beliefs import BELIEF_STATES, EVIDENCE_CLASSES
from groundtruth.runtime import DATA_DIR


SEED_CORPUS_PATH = DATA_DIR / "seed_corpus.json"
CLAIMS_PATH = DATA_DIR / "claims.json"
DATASETS = ("naive_memory", "groundtruth_memory")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def load_seed(path: Path = SEED_CORPUS_PATH) -> dict[str, Any]:
    return load_json(path)


def load_claims(path: Path = CLAIMS_PATH) -> list[dict[str, Any]]:
    return load_json(path)


def save_claims(entries: list[dict[str, Any]], path: Path = CLAIMS_PATH) -> None:
    write_json(path, entries)


def claim_topic(claim: dict[str, Any]) -> str:
    title = claim["source"]["title"]
    topic = title.split(":", 1)[0].split(" - ", 1)[0].strip()
    return topic[:140]


def claim_document(claim: dict[str, Any]) -> str:
    source = claim["source"]
    return "\n".join(
        [
            f"GROUNDTRUTH CLAIM ID: {claim['claim_id']}",
            f"Status at seed: {claim['status_at_seed']}",
            f"Source DOI: {source['doi']}",
            f"Journal: {source['journal']}",
            f"Year: {source['year']}",
            f"Title: {source['title']}",
            f"Claim: {claim['claim_text']}",
        ]
    )


def validate_claims(entries: list[dict[str, Any]]) -> None:
    if len(entries) != 40:
        raise ValueError(f"Expected 40 claims, found {len(entries)}")

    seen_claim_ids: set[str] = set()
    seen_data_ids: set[tuple[str, str]] = set()
    for entry in entries:
        claim_id = entry["claim_id"]
        if claim_id in seen_claim_ids:
            raise ValueError(f"Duplicate claim_id: {claim_id}")
        seen_claim_ids.add(claim_id)

        belief_state = entry.get("belief_state")
        if belief_state not in BELIEF_STATES:
            raise ValueError(f"{claim_id} has invalid belief_state: {belief_state}")

        state_history = entry.get("state_history")
        if not state_history:
            raise ValueError(f"{claim_id} missing state_history")
        if state_history[-1].get("state") != belief_state:
            raise ValueError(f"{claim_id} latest state_history does not match state")
        for event in state_history:
            if event.get("state") not in BELIEF_STATES:
                raise ValueError(f"{claim_id} has invalid history state: {event}")
            if event.get("evidence_class") not in EVIDENCE_CLASSES:
                raise ValueError(f"{claim_id} has invalid evidence class: {event}")
            for field in ("at", "evidence_ref", "basis"):
                if not event.get(field):
                    raise ValueError(f"{claim_id} history event missing {field}")

        datasets = entry.get("datasets") or {}
        for dataset_name in DATASETS:
            dataset_entry = datasets.get(dataset_name)
            if not dataset_entry:
                raise ValueError(f"{claim_id} missing dataset {dataset_name}")
            dataset_id = UUID(dataset_entry["dataset_id"])
            data_id = UUID(dataset_entry["data_id"])
            key = (str(dataset_id), str(data_id))
            if key in seen_data_ids:
                raise ValueError(f"Duplicate data_id in registry: {key}")
            seen_data_ids.add(key)

    if len(seen_data_ids) != len(entries) * len(DATASETS):
        raise ValueError(
            "Registry does not contain one data item per claim and dataset"
        )
