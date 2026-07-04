from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


BELIEF_STATES = ("active", "contested", "superseded", "retracted", "purged")
EVIDENCE_CLASSES = ("authority_feed", "semantic_inference", "user_assertion")


def belief_state_from_status(status: str | None) -> str:
    status_value = str(status or "active")
    if status_value in BELIEF_STATES:
        return status_value
    if status_value in {"retracted_forgotten", "retracted_retained"}:
        return "retracted"
    return "active"


def belief_nodeset_name(state: str) -> str:
    if state not in BELIEF_STATES:
        raise ValueError(f"Unknown belief state: {state}")
    return f"beliefs_{state}"


def parse_evidence_time(value: Any) -> str | None:
    if not value:
        return None
    text = str(value).strip()
    for date_format in ("%m/%d/%Y %H:%M", "%m/%d/%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(text, date_format).replace(
                tzinfo=timezone.utc
            ).isoformat()
        except ValueError:
            continue
    return None


def source_time(claim: dict[str, Any]) -> str:
    year = int((claim.get("source") or {}).get("year") or 1970)
    return datetime(year, 1, 1, tzinfo=timezone.utc).isoformat()


def active_history_entry(claim: dict[str, Any]) -> dict[str, str]:
    return {
        "state": "active",
        "at": source_time(claim),
        "evidence_class": "user_assertion",
        "evidence_ref": str(claim.get("doi") or (claim.get("source") or {}).get("doi")),
        "basis": "Seed corpus imported this claim as an active memory claim.",
    }


def retraction_history_entry(claim: dict[str, Any]) -> dict[str, str]:
    retraction = claim.get("retraction") or {}
    retraction_doi = (
        retraction.get("retraction_doi")
        or claim.get("retraction_doi")
        or (claim.get("datasets", {}).get("groundtruth_memory") or {}).get(
            "retraction_notice_doi"
        )
    )
    reason = str(retraction.get("reason") or "No reason supplied").strip()
    original_doi = retraction.get("original_doi") or claim.get("doi")
    return {
        "state": "retracted",
        "at": parse_evidence_time(retraction.get("retraction_date"))
        or source_time(claim),
        "evidence_class": "authority_feed",
        "evidence_ref": str(retraction_doi),
        "basis": (
            f"Retraction Watch record {retraction_doi} supersedes original DOI "
            f"{original_doi}; reason: {reason}"
        ),
    }


def inferred_history_entry(claim: dict[str, Any], state: str) -> dict[str, str]:
    return {
        "state": state,
        "at": source_time(claim),
        "evidence_class": "user_assertion",
        "evidence_ref": str(claim.get("doi") or (claim.get("source") or {}).get("doi")),
        "basis": f"Registry status `{claim.get('status')}` maps to belief state `{state}`.",
    }


def initial_state_history(claim: dict[str, Any]) -> list[dict[str, str]]:
    state = belief_state_from_status(claim.get("status"))
    if state == "active":
        return [active_history_entry(claim)]
    if state == "retracted":
        return [active_history_entry(claim), retraction_history_entry(claim)]
    return [active_history_entry(claim), inferred_history_entry(claim, state)]


def belief_state_for_claim(claim: dict[str, Any]) -> str:
    state = claim.get("belief_state") or belief_state_from_status(claim.get("status"))
    if state not in BELIEF_STATES:
        raise ValueError(f"Unknown belief state for {claim.get('claim_id')}: {state}")
    return state


def state_history_for_claim(claim: dict[str, Any]) -> list[dict[str, str]]:
    history = claim.get("state_history")
    if history:
        return history
    return initial_state_history(claim)


def latest_state_change(claim: dict[str, Any]) -> dict[str, str]:
    return state_history_for_claim(claim)[-1]


def state_history_event(
    state: str,
    evidence_class: str,
    evidence_ref: str,
    basis: str,
    *,
    at: str | None = None,
) -> dict[str, str]:
    if state not in BELIEF_STATES:
        raise ValueError(f"Unknown belief state: {state}")
    if evidence_class not in EVIDENCE_CLASSES:
        raise ValueError(f"Unknown evidence class: {evidence_class}")
    if not evidence_ref:
        raise ValueError("evidence_ref is required")
    if not basis:
        raise ValueError("basis is required")
    return {
        "state": state,
        "at": at or datetime.now(timezone.utc).isoformat(),
        "evidence_class": evidence_class,
        "evidence_ref": evidence_ref,
        "basis": basis,
    }


def transition_belief(
    claim: dict[str, Any],
    state: str,
    evidence_class: str,
    evidence_ref: str,
    basis: str,
    *,
    at: str | None = None,
) -> dict[str, Any]:
    event = state_history_event(
        state,
        evidence_class,
        evidence_ref,
        basis,
        at=at,
    )
    history = state_history_for_claim(claim)
    if history[-1] != event:
        history.append(event)
    claim["belief_state"] = state
    claim["state_history"] = history
    return claim


def migrate_claim_belief(claim: dict[str, Any]) -> dict[str, Any]:
    migrated = dict(claim)
    migrated["belief_state"] = belief_state_for_claim(migrated)
    migrated["state_history"] = state_history_for_claim(migrated)
    return migrated


def migrate_belief_registry(claims: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [migrate_claim_belief(claim) for claim in claims]


def belief_reference_fields(claim: dict[str, Any]) -> dict[str, Any]:
    latest = latest_state_change(claim)
    return {
        "belief_state": belief_state_for_claim(claim),
        "latest_basis": latest["basis"],
        "latest_state_change": latest,
        "belief_state_changed_at": latest["at"],
        "belief_evidence_class": latest["evidence_class"],
        "belief_evidence_ref": latest["evidence_ref"],
        "belief_state_basis": latest["basis"],
    }


def cites_by_state(references: list[dict[str, Any]]) -> dict[str, int]:
    counts = {state: 0 for state in BELIEF_STATES}
    for reference in references:
        state = reference.get("belief_state")
        if state in counts:
            counts[state] += 1
    return counts
