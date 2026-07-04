from __future__ import annotations

import argparse
import asyncio
import json
from copy import deepcopy
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from groundtruth.answer import answer_text, score_claim
from groundtruth.beliefs import (
    belief_reference_fields,
    cites_by_state,
    migrate_claim_belief,
    state_history_for_claim,
)
from groundtruth.registry import CLAIMS_PATH, load_claims, write_json
from groundtruth.runtime import DATA_DIR, DOCS_DIR


GROUNDTRUTH_DATASET = "groundtruth_memory"
TIMELINE_CATEGORIES = ("added", "contested", "revised", "purged")
TIMELINE_RUN_PATH = DATA_DIR / "timeline_run.json"
RESULTS_V3_P4_PATH = DOCS_DIR / "RESULTS-V3-P4.md"


def parse_time(value: str | date | datetime) -> datetime:
    if isinstance(value, datetime):
        parsed = value
    elif isinstance(value, date):
        parsed = datetime(value.year, value.month, value.day)
    else:
        text = str(value).strip()
        if not text:
            raise ValueError("date value is required")
        if text.endswith("Z"):
            text = f"{text[:-1]}+00:00"
        parsed = datetime.fromisoformat(text)
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def state_at(
    claim: dict[str, Any],
    as_of: str | date | datetime,
) -> dict[str, str] | None:
    target = parse_time(as_of)
    events = []
    for index, event in enumerate(state_history_for_claim(migrate_claim_belief(claim))):
        event_time = parse_time(event["at"])
        if event_time <= target:
            events.append((event_time, index, event))
    if not events:
        return None
    return dict(sorted(events, key=lambda item: (item[0], item[1]))[-1][2])


def history_until(
    claim: dict[str, Any],
    as_of: str | date | datetime,
) -> list[dict[str, str]]:
    target = parse_time(as_of)
    events = []
    for index, event in enumerate(state_history_for_claim(migrate_claim_belief(claim))):
        event_time = parse_time(event["at"])
        if event_time <= target:
            events.append((event_time, index, dict(event)))
    return [event for _, _, event in sorted(events, key=lambda item: (item[0], item[1]))]


def claim_as_of(
    claim: dict[str, Any],
    as_of: str | date | datetime,
) -> dict[str, Any] | None:
    chain = history_until(claim, as_of)
    if not chain:
        return None
    copy = deepcopy(claim)
    copy["state_history"] = chain
    copy["belief_state"] = chain[-1]["state"]
    return copy


def memory_status_for_state(
    claim: dict[str, Any],
    state: str,
    dataset: str,
) -> str | None:
    if state == "purged":
        return "purged"
    if state in {"active", "contested", "superseded"}:
        return "active"
    dataset_status = ((claim.get("datasets") or {}).get(dataset) or {}).get("status")
    if state == "retracted" and dataset_status:
        return dataset_status
    return state


def reference_for_as_of_claim(
    claim: dict[str, Any],
    dataset: str,
    *,
    score: int,
) -> dict[str, Any] | None:
    state = claim["belief_state"]
    if state == "purged":
        return None

    dataset_entry = (claim.get("datasets") or {}).get(dataset) or {}
    kind = "original_claim"
    data_id = dataset_entry.get("data_id")
    if state == "retracted" and dataset_entry.get("retraction_notice_data_id"):
        kind = "retraction_notice"
        data_id = dataset_entry["retraction_notice_data_id"]
    if not data_id:
        return None

    reference = {
        "claim_id": claim["claim_id"],
        "kind": kind,
        "doi": claim.get("doi") or (claim.get("source") or {}).get("doi"),
        "data_id": data_id,
        "dataset": dataset,
        "dataset_id": dataset_entry.get("dataset_id"),
        "source": (claim.get("source") or {}).get("journal"),
        "status": claim.get("status"),
        "dataset_status": memory_status_for_state(claim, state, dataset),
        "cohort": claim.get("cohort"),
        "retracted": kind == "original_claim" and state == "retracted",
        "score": score,
        **belief_reference_fields(claim),
    }
    return reference


def answer_as_of(
    question: str,
    as_of: str | date | datetime,
    *,
    dataset: str = GROUNDTRUTH_DATASET,
    registry_path: Path = CLAIMS_PATH,
    limit: int = 5,
) -> dict[str, Any]:
    timestamp = parse_time(as_of).isoformat()
    claims = load_claims(registry_path)
    scored_references: list[tuple[int, int, dict[str, Any]]] = []
    chains: list[dict[str, Any]] = []
    eligible_claims = 0
    for index, claim in enumerate(claims):
        as_of_claim = claim_as_of(claim, timestamp)
        if as_of_claim is None:
            continue
        eligible_claims += 1
        score = score_claim(question, as_of_claim)
        if score == 0:
            continue
        reference = reference_for_as_of_claim(as_of_claim, dataset, score=score)
        if reference is None:
            continue
        scored_references.append((score, index, reference))
        chains.append(
            {
                "claim_id": as_of_claim["claim_id"],
                "state_history": as_of_claim["state_history"],
            }
        )

    references = [
        reference
        for _, _, reference in sorted(
            scored_references, key=lambda item: (-item[0], item[1])
        )[:limit]
    ]
    selected_claim_ids = {reference["claim_id"] for reference in references}
    selected_chains = [
        chain for chain in chains if chain["claim_id"] in selected_claim_ids
    ]
    retracted_dois = sorted(
        {reference["doi"] for reference in references if reference["retracted"]}
    )
    return {
        "question": question,
        "dataset": dataset,
        "as_of": timestamp,
        "text": f"As of {timestamp}, {answer_text(dataset, references)}",
        "references": references,
        "chains": selected_chains,
        "cites_retracted": bool(retracted_dois),
        "retracted_dois": retracted_dois,
        "cites_by_state": cites_by_state(references),
        "eligible_claims": eligible_claims,
        "recall_mode": "deterministic_registry_time_travel",
    }


def event_changed(
    before: dict[str, str] | None,
    after: dict[str, str],
) -> bool:
    if before is None:
        return True
    return (
        before.get("state") != after.get("state")
        or before.get("evidence_class") != after.get("evidence_class")
        or before.get("evidence_ref") != after.get("evidence_ref")
        or before.get("basis") != after.get("basis")
    )


def timeline_item(
    claim: dict[str, Any],
    before: dict[str, str] | None,
    after: dict[str, str],
    *,
    to_date: str,
    dataset: str,
) -> dict[str, Any]:
    source = claim.get("source") or {}
    after_state = after["state"]
    return {
        "claim_id": claim["claim_id"],
        "doi": claim.get("doi") or source.get("doi"),
        "title": source.get("title"),
        "from_state": before.get("state") if before else None,
        "to_state": after_state,
        "changed_at": after["at"],
        "evidence_class": after["evidence_class"],
        "evidence_ref": after["evidence_ref"],
        "basis": after["basis"],
        "memory_status": memory_status_for_state(claim, after_state, dataset),
        "chain": history_until(claim, to_date),
    }


def is_purged_transition(item: dict[str, Any], before_memory_status: str | None) -> bool:
    return item["to_state"] == "purged" or (
        item["memory_status"] in {"retracted_forgotten", "purged"}
        and before_memory_status not in {"retracted_forgotten", "purged"}
    )


def timeline_diff(
    from_date: str | date | datetime,
    to_date: str | date | datetime,
    *,
    dataset: str = GROUNDTRUTH_DATASET,
    registry_path: Path = CLAIMS_PATH,
) -> dict[str, Any]:
    from_timestamp = parse_time(from_date)
    to_timestamp = parse_time(to_date)
    if from_timestamp > to_timestamp:
        raise ValueError("from date must be before or equal to to date")

    changes = {category: [] for category in TIMELINE_CATEGORIES}
    for claim in load_claims(registry_path):
        before = state_at(claim, from_timestamp)
        after = state_at(claim, to_timestamp)
        if after is None or not event_changed(before, after):
            continue

        item = timeline_item(
            claim,
            before,
            after,
            to_date=to_timestamp.isoformat(),
            dataset=dataset,
        )
        before_memory_status = (
            memory_status_for_state(claim, before["state"], dataset)
            if before
            else None
        )

        if before is None:
            changes["added"].append(item)
        elif item["to_state"] == "contested" and before.get("state") != "contested":
            changes["contested"].append(item)
        elif item["to_state"] in {"superseded", "retracted"} or (
            before.get("state") == "contested" and item["to_state"] != "contested"
        ):
            changes["revised"].append(item)

        if is_purged_transition(item, before_memory_status):
            changes["purged"].append(item)

    for category in changes:
        changes[category] = sorted(changes[category], key=lambda item: item["claim_id"])

    return {
        "from": from_timestamp.isoformat(),
        "to": to_timestamp.isoformat(),
        "dataset": dataset,
        "changes": changes,
    }


def scripted_run(
    *,
    question: str,
    from_date: str,
    to_date: str,
    dataset: str = GROUNDTRUTH_DATASET,
    registry_path: Path = CLAIMS_PATH,
) -> dict[str, Any]:
    before = answer_as_of(
        question,
        from_date,
        dataset=dataset,
        registry_path=registry_path,
    )
    after = answer_as_of(
        question,
        to_date,
        dataset=dataset,
        registry_path=registry_path,
    )
    diff = timeline_diff(
        from_date,
        to_date,
        dataset=dataset,
        registry_path=registry_path,
    )
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "question": question,
        "from": before["as_of"],
        "to": after["as_of"],
        "before": before,
        "after": after,
        "timeline": diff,
    }


def render_item(item: dict[str, Any]) -> str:
    return (
        f"- `{item['claim_id']}` `{item['from_state']}` -> `{item['to_state']}` / "
        f"DOI `{item['doi']}`\n"
        f"  - Evidence: `{item['evidence_class']}` `{item['evidence_ref']}`\n"
        f"  - Basis: {item['basis']}"
    )


def render_category(title: str, items: list[dict[str, Any]]) -> list[str]:
    lines = [f"## {title}", ""]
    if not items:
        lines.extend(["- None.", ""])
        return lines
    for item in items:
        lines.extend([render_item(item), ""])
    return lines


def render_results_markdown(run: dict[str, Any]) -> str:
    lines = [
        "# GroundTruth V3 P4 Results",
        "",
        f"Generated: {run['generated_at']}",
        "Status: `complete_deterministic_registry`",
        "",
        "## Gate",
        "",
        "- Time travel is deterministic over registry `state_history`; no Cognee/provider calls are used.",
        "- `answer_as_of` filters references by state at the requested date and includes each cited claim's state chain.",
        "- `/timeline?from=X&to=Y` exposes added / contested / revised / purged belief changes.",
        "",
        "## Command",
        "",
        "```powershell",
        ".\\.venv\\Scripts\\python.exe -m groundtruth.timeline --results-v3-p4",
        "```",
        "",
        "## Answer Then",
        "",
        "```text",
        run["before"]["text"],
        "```",
        "",
        "## Answer Now",
        "",
        "```text",
        run["after"]["text"],
        "```",
        "",
    ]
    changes = run["timeline"]["changes"]
    lines.extend(render_category("Added", changes["added"]))
    lines.extend(render_category("Contested", changes["contested"]))
    lines.extend(render_category("Revised", changes["revised"]))
    lines.extend(render_category("Purged", changes["purged"]))
    lines.extend(
        [
            "## Raw Run",
            "",
            "```json",
            json.dumps(run, indent=2, sort_keys=True),
            "```",
            "",
            "## Verification So Far",
            "",
            "- Run focused tests, static checks, and the full suite after generation; committed results record the final outputs.",
            "",
        ]
    )
    return "\n".join(lines)


def write_artifacts(
    run: dict[str, Any],
    *,
    timeline_run_path: Path = TIMELINE_RUN_PATH,
    results_path: Path = RESULTS_V3_P4_PATH,
) -> None:
    write_json(timeline_run_path, run)
    results_path.write_text(render_results_markdown(run), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="GroundTruth V3 belief timeline")
    parser.add_argument(
        "--question",
        default=(
            "What did we believe about Avacopan for the Treatment of "
            "ANCA-Associated Vasculitis?"
        ),
    )
    parser.add_argument("--from-date", default="2023-01-01")
    parser.add_argument("--to-date", default="2026-07-04")
    parser.add_argument("--dataset", default=GROUNDTRUTH_DATASET)
    parser.add_argument(
        "--results-v3-p4",
        action="store_true",
        help="Write data/timeline_run.json and docs/RESULTS-V3-P4.md.",
    )
    return parser.parse_args()


async def main() -> int:
    args = parse_args()
    run = scripted_run(
        question=args.question,
        from_date=args.from_date,
        to_date=args.to_date,
        dataset=args.dataset,
    )
    if args.results_v3_p4:
        write_artifacts(run)
        print(f"Wrote {TIMELINE_RUN_PATH}")
        print(f"Wrote {RESULTS_V3_P4_PATH}")
    print(json.dumps(run, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
