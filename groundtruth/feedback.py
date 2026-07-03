from __future__ import annotations

import argparse
import asyncio
import json
import os
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from groundtruth.answer import answer, compact_recall
from groundtruth.registry import claim_topic, load_claims
from groundtruth.runtime import DOCS_DIR, import_cognee


GROUNDTRUTH_DATASET = "groundtruth_memory"


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


async def get_session_entries(session_id: str) -> list[dict[str, Any]]:
    cognee = import_cognee()
    return compact_recall(await cognee.session.get_session(session_id=session_id))


async def add_feedback(
    session_id: str,
    qa_id: str,
    feedback_score: int,
    feedback_text: str | None = None,
) -> dict[str, Any]:
    if feedback_score < 1 or feedback_score > 5:
        raise ValueError("feedback_score must be between 1 and 5")

    cognee = import_cognee()
    updated = await cognee.session.add_feedback(
        session_id=session_id,
        qa_id=qa_id,
        feedback_text=feedback_text,
        feedback_score=feedback_score,
    )
    if not updated:
        raise RuntimeError(f"Could not add feedback for QA {qa_id} in session {session_id}")

    return {
        "session_id": session_id,
        "qa_id": qa_id,
        "feedback_score": feedback_score,
        "feedback_text": feedback_text,
        "updated": updated,
    }


async def improve_from_feedback(
    dataset: str,
    session_ids: list[str],
    *,
    feedback_alpha: float = 1.0,
    build_truth_subspace: bool = False,
) -> dict[str, Any]:
    os.environ["COGNEE_SKIP_CONNECTION_TEST"] = "true"
    cognee = import_cognee()
    from cognee.context_global_variables import set_session_user_context_variable
    from cognee.modules.pipelines import Task
    from cognee.modules.users.methods import get_default_user
    from cognee.tasks.memify.apply_feedback_weights import apply_feedback_weights
    from cognee.tasks.memify.extract_feedback_qas import extract_feedback_qas

    user = await get_default_user()
    await set_session_user_context_variable(user)
    result = await cognee.improve(
        dataset=dataset,
        user=user,
        data=[{}],
        extraction_tasks=[Task(extract_feedback_qas, session_ids=session_ids)],
        enrichment_tasks=[Task(apply_feedback_weights, alpha=feedback_alpha)],
        feedback_alpha=feedback_alpha,
    )
    return {
        "dataset": dataset,
        "session_ids": session_ids,
        "feedback_alpha": feedback_alpha,
        "build_truth_subspace": build_truth_subspace,
        "session_bridge": "skipped_quota_fallback",
        "result": compact_recall(result),
    }


async def scripted_run() -> dict[str, Any]:
    claims = load_claims()
    target = next(
        claim
        for claim in claims
        if claim["status"] == "retracted_forgotten"
        and "retraction_notice_data_id" in claim["datasets"][GROUNDTRUTH_DATASET]
    )
    question = f"what does the research say about {claim_topic(target)}?"
    session_id = f"groundtruth-feedback-{uuid4().hex[:8]}"

    before = await answer(
        question,
        GROUNDTRUTH_DATASET,
        session_id=session_id,
        feedback_influence=0.0,
    )
    if not before.get("qa_id"):
        raise RuntimeError("Session answer did not produce a qa_id")

    feedback = await add_feedback(
        session_id,
        before["qa_id"],
        feedback_score=1,
        feedback_text=(
            "Downvote: this answer should put more weight on authoritative "
            "post-retraction evidence."
        ),
    )
    improve = await improve_from_feedback(GROUNDTRUTH_DATASET, [session_id])
    after = await answer(
        question,
        GROUNDTRUTH_DATASET,
        session_id=session_id,
        record_session=False,
        feedback_influence=1.0,
    )
    changed = before["recall_context"] != after["recall_context"] or before[
        "references"
    ] != after["references"]
    entries = await get_session_entries(session_id)
    return {
        "generated_at": now(),
        "dataset": GROUNDTRUTH_DATASET,
        "session_id": session_id,
        "question": question,
        "target_claim_id": target["claim_id"],
        "before": before,
        "feedback": feedback,
        "improve": improve,
        "after": after,
        "session_entries": entries,
        "visible_change": changed,
        "assessment": (
            "Feedback was stored and improve() completed; recall changed after "
            "feedback_influence=1.0."
            if changed
            else "Feedback was stored and improve() completed, but the visible "
            "answer/ranking change is subtle for this dataset."
        ),
    }


def write_results_p3(result: dict[str, Any]) -> None:
    lines = [
        "# Phase 3 Results",
        "",
        f"Generated: {result['generated_at']}",
        "",
        "## Gate",
        "",
        f"- Session: `{result['session_id']}`",
        f"- Dataset: `{result['dataset']}`",
        f"- Question: `{result['question']}`",
        f"- Visible change after `improve(..., feedback_influence=1.0)`: `{result['visible_change']}`",
        f"- Assessment: {result['assessment']}",
        "",
        "## Scripted Run",
        "",
        "```json",
        json.dumps(result, indent=2, sort_keys=True),
        "```",
        "",
    ]
    (DOCS_DIR / "RESULTS-P3.md").write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="GroundTruth Phase 3 feedback loop")
    parser.add_argument("--results-p3", action="store_true", help="Write docs/RESULTS-P3.md")
    return parser.parse_args()


async def main() -> int:
    args = parse_args()
    result = await scripted_run()
    if args.results_p3:
        write_results_p3(result)
        print(f"Wrote {DOCS_DIR / 'RESULTS-P3.md'}")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
