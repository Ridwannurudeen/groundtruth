from __future__ import annotations

from uuid import uuid4

import pytest

from groundtruth.answer import answer
from groundtruth.feedback import add_feedback, get_session_entries


@pytest.mark.asyncio
async def test_session_feedback_is_recorded(retraction_lifecycle):
    context = retraction_lifecycle
    _, groundtruth_dataset = context["dataset_names"]
    session_id = f"test-feedback-{uuid4().hex[:8]}"

    result = await answer(
        context["question"],
        groundtruth_dataset,
        registry_path=context["registry_path"],
        session_id=session_id,
    )

    assert result["qa_id"]
    assert result["session_status"] == "session_stored"
    assert result["used_graph_element_ids"]["node_ids"]

    feedback = await add_feedback(
        session_id,
        result["qa_id"],
        feedback_score=1,
        feedback_text="Downvote test feedback",
    )
    assert feedback["updated"] is True

    entries = await get_session_entries(session_id)
    entry = next(item for item in entries if item["qa_id"] == result["qa_id"])
    assert entry["feedback_score"] == 1
    assert entry["feedback_text"] == "Downvote test feedback"
