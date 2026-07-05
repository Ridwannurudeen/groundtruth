from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Literal
from uuid import UUID

from groundtruth.beliefs import (
    latest_state_change,
    migrate_claim_belief,
    transition_belief,
)
from groundtruth.registry import load_json, write_json
from groundtruth.runtime import DATA_DIR, import_cognee


CONTESTED_PAIRS_PATH = DATA_DIR / "contested_pairs.json"
SemanticAction = Literal["log_only", "contested", "auto_act"]
AdjudicationVerdict = Literal["a_supersedes_b", "b_supersedes_a", "mutual", "none"]


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def decision_dict(decision: Any) -> dict[str, Any]:
    if hasattr(decision, "model_dump"):
        return decision.model_dump(mode="json")
    return dict(decision)


def pair_key(claim_a_id: str, claim_b_id: str) -> str:
    return "::".join(sorted([claim_a_id, claim_b_id]))


def resolve_registry_path(
    record: dict[str, Any], queue_path: Path, override: Path | None
) -> Path:
    """Resolve a queue record's registry file. Historical records may hold a full
    path (from either OS); normalize backslashes so ``.name`` works on POSIX too,
    and resolve it next to the queue file where the registry always lives."""
    if override is not None:
        return override
    stored = str(record.get("registry_path", "")).replace("\\", "/")
    return queue_path.parent / Path(stored).name


def evidence_ref(pair: str) -> str:
    return f"pair:{pair}"


def semantic_action(decision: Any) -> SemanticAction:
    payload = decision_dict(decision)
    if not payload.get("conflicts") or float(payload.get("confidence") or 0.0) < 0.7:
        return "log_only"
    if float(payload.get("confidence") or 0.0) >= 0.9 and payload.get("direction") in {
        "a_supersedes_b",
        "b_supersedes_a",
    }:
        return "auto_act"
    return "contested"


def load_queue(path: Path = CONTESTED_PAIRS_PATH) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return load_json(path)


def save_queue(
    records: list[dict[str, Any]], path: Path = CONTESTED_PAIRS_PATH
) -> None:
    write_json(path, records)


def claims_by_id(entries: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {entry["claim_id"]: entry for entry in entries}


def transition_once(
    claim: dict[str, Any],
    state: str,
    evidence_class: str,
    ref: str,
    basis: str,
    *,
    at: str,
) -> dict[str, Any]:
    latest = latest_state_change(migrate_claim_belief(claim))
    if (
        latest.get("state") == state
        and latest.get("evidence_class") == evidence_class
        and latest.get("evidence_ref") == ref
        and latest.get("basis") == basis
    ):
        return claim
    return transition_belief(claim, state, evidence_class, ref, basis, at=at)


def semantic_basis(row: dict[str, Any]) -> str:
    decision = decision_dict(row["decision"])
    pair = pair_key(row["claim_a_id"], row["claim_b_id"])
    return (
        f"Semantic inference for {pair} landed in the contested band "
        f"(confidence {float(decision.get('confidence') or 0.0):.2f}, "
        f"direction {decision.get('direction')}); basis: {decision.get('basis')}"
    )


def upsert_contested_record(
    records: list[dict[str, Any]],
    record: dict[str, Any],
) -> dict[str, Any]:
    for index, existing in enumerate(records):
        if existing["pair"] != record["pair"]:
            continue
        merged = {
            **existing,
            **record,
            "created_at": existing.get("created_at") or record["created_at"],
            "status": (
                existing.get("status")
                if existing.get("status") == "resolved"
                else "open"
            ),
        }
        records[index] = merged
        return merged
    records.append(record)
    return record


def mark_contested(
    registry: list[dict[str, Any]],
    row: dict[str, Any],
    *,
    dataset: str,
    registry_path: Path,
    queue_path: Path = CONTESTED_PAIRS_PATH,
    at: str | None = None,
) -> dict[str, Any]:
    action = semantic_action(row["decision"])
    if action != "contested":
        raise ValueError(f"Semantic decision is {action}, not contested")

    timestamp = at or now()
    pair = pair_key(row["claim_a_id"], row["claim_b_id"])
    ref = evidence_ref(pair)
    basis = semantic_basis(row)
    indexed = claims_by_id(registry)
    state_changes = []
    for claim_id in (row["claim_a_id"], row["claim_b_id"]):
        claim = migrate_claim_belief(indexed[claim_id])
        transition_once(
            claim,
            "contested",
            "semantic_inference",
            ref,
            basis,
            at=timestamp,
        )
        indexed[claim_id].update(claim)
        state_changes.append(
            {
                "claim_id": claim_id,
                "state": "contested",
                "evidence_class": "semantic_inference",
                "evidence_ref": ref,
                "basis": basis,
            }
        )

    claim_a = indexed[row["claim_a_id"]]
    claim_b = indexed[row["claim_b_id"]]
    record = {
        "pair": pair,
        "status": "open",
        "dataset": dataset,
        "registry_path": registry_path.name,
        "claim_a_id": row["claim_a_id"],
        "claim_b_id": row["claim_b_id"],
        "claim_a_data_id": claim_a["datasets"][dataset]["data_id"],
        "claim_b_data_id": claim_b["datasets"][dataset]["data_id"],
        "decision": decision_dict(row["decision"]),
        "evidence_ref": ref,
        "basis": basis,
        "created_at": timestamp,
        "updated_at": timestamp,
        "state_changes": state_changes,
    }
    queue = load_queue(queue_path)
    saved = upsert_contested_record(queue, record)
    write_json(registry_path, registry)
    save_queue(queue, queue_path)
    return saved


def mark_auto_superseded(
    registry: list[dict[str, Any]],
    row: dict[str, Any],
    *,
    registry_path: Path,
    at: str | None = None,
) -> dict[str, Any]:
    decision = decision_dict(row["decision"])
    action = semantic_action(decision)
    if action != "auto_act":
        raise ValueError(f"Semantic decision is {action}, not auto_act")

    winner_id, loser_id = (
        (row["claim_a_id"], row["claim_b_id"])
        if decision["direction"] == "a_supersedes_b"
        else (row["claim_b_id"], row["claim_a_id"])
    )
    timestamp = at or now()
    pair = pair_key(row["claim_a_id"], row["claim_b_id"])
    ref = evidence_ref(pair)
    basis = (
        f"Semantic inference for {pair} auto-superseded {loser_id} with "
        f"confidence {float(decision.get('confidence') or 0.0):.2f}; "
        f"basis: {decision.get('basis')}"
    )
    indexed = claims_by_id(registry)
    winner = migrate_claim_belief(indexed[winner_id])
    loser = migrate_claim_belief(indexed[loser_id])
    transition_once(
        winner,
        "active",
        "semantic_inference",
        ref,
        basis,
        at=timestamp,
    )
    transition_once(
        loser,
        "superseded",
        "semantic_inference",
        ref,
        basis,
        at=timestamp,
    )
    indexed[winner_id].update(winner)
    indexed[loser_id].update(loser)
    write_json(registry_path, registry)
    return {
        "pair": pair,
        "winner_claim_id": winner_id,
        "superseded_claim_id": loser_id,
        "evidence_ref": ref,
        "basis": basis,
        "state_changes": [
            {
                "claim_id": winner_id,
                "state": "active",
                "evidence_class": "semantic_inference",
                "evidence_ref": ref,
                "basis": basis,
            },
            {
                "claim_id": loser_id,
                "state": "superseded",
                "evidence_class": "semantic_inference",
                "evidence_ref": ref,
                "basis": basis,
            },
        ],
    }


def claim_summary(claim: dict[str, Any]) -> dict[str, Any]:
    migrated = migrate_claim_belief(claim)
    source = migrated.get("source") or {}
    return {
        "claim_id": migrated["claim_id"],
        "doi": migrated.get("doi") or source.get("doi"),
        "title": source.get("title"),
        "journal": source.get("journal"),
        "belief_state": migrated["belief_state"],
        "latest_state_change": latest_state_change(migrated),
    }


def list_contested_pairs(
    queue_path: Path = CONTESTED_PAIRS_PATH,
    *,
    registry_path: Path | None = None,
) -> list[dict[str, Any]]:
    records = [
        record for record in load_queue(queue_path) if record.get("status") == "open"
    ]
    enriched = []
    for record in records:
        path = resolve_registry_path(record, queue_path, registry_path)
        registry = claims_by_id(load_json(path)) if path.exists() else {}
        claim_a = registry.get(record["claim_a_id"])
        claim_b = registry.get(record["claim_b_id"])
        if claim_a is None or claim_b is None:
            # Registry unresolved or a claim id is missing — skip rather than 500.
            continue
        item = dict(record)
        item["claims"] = [claim_summary(claim_a), claim_summary(claim_b)]
        enriched.append(item)
    return sorted(enriched, key=lambda item: item["pair"])


def adjudication_states(verdict: AdjudicationVerdict) -> tuple[str, str]:
    if verdict == "a_supersedes_b":
        return "active", "superseded"
    if verdict == "b_supersedes_a":
        return "superseded", "active"
    if verdict == "mutual":
        return "contested", "contested"
    if verdict == "none":
        return "active", "active"
    raise ValueError(f"Unknown adjudication verdict: {verdict}")


async def adjudicate_pair(
    pair: str,
    verdict: AdjudicationVerdict,
    *,
    basis: str | None = None,
    queue_path: Path = CONTESTED_PAIRS_PATH,
    registry_path: Path | None = None,
    apply_forget: bool = True,
) -> dict[str, Any]:
    queue = load_queue(queue_path)
    record = next((item for item in queue if item["pair"] == pair), None)
    if record is None:
        raise ValueError(f"Unknown contested pair: {pair}")
    path = resolve_registry_path(record, queue_path, registry_path)
    if not path.exists():
        raise ValueError(f"Registry for contested pair not found: {pair}")
    registry = load_json(path)
    indexed = claims_by_id(registry)
    state_a, state_b = adjudication_states(verdict)
    timestamp = now()
    ref = f"adjudication:{pair}"
    adjudication_basis = basis or f"User adjudication resolved {pair} as {verdict}."
    state_changes = []
    forget_results = []

    for claim_id, state in (
        (record["claim_a_id"], state_a),
        (record["claim_b_id"], state_b),
    ):
        claim = migrate_claim_belief(indexed[claim_id])
        transition_once(
            claim,
            state,
            "user_assertion",
            ref,
            adjudication_basis,
            at=timestamp,
        )
        indexed[claim_id].update(claim)
        change = {
            "claim_id": claim_id,
            "state": state,
            "evidence_class": "user_assertion",
            "evidence_ref": ref,
            "basis": adjudication_basis,
        }
        state_changes.append(change)
        if state == "superseded" and apply_forget:
            dataset_entry = claim["datasets"][record["dataset"]]
            cognee = import_cognee()
            forget_results.append(
                await cognee.forget(
                    data_id=UUID(dataset_entry["data_id"]),
                    dataset_id=UUID(dataset_entry["dataset_id"]),
                    memory_only=True,
                )
            )

    record.update(
        {
            "status": "resolved",
            "resolved_at": timestamp,
            "updated_at": timestamp,
            "adjudication": {
                "verdict": verdict,
                "evidence_class": "user_assertion",
                "evidence_ref": ref,
                "basis": adjudication_basis,
            },
            "state_changes": state_changes,
            "forget_results": forget_results,
        }
    )
    write_json(path, registry)
    save_queue(queue, queue_path)
    return {
        "pair": pair,
        "status": "resolved",
        "verdict": verdict,
        "state_changes": state_changes,
        "forget_results": forget_results,
        "record": record,
    }
