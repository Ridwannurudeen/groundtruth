from __future__ import annotations

import json

from fastapi.testclient import TestClient

from web.app import app


client = TestClient(app)


def test_state_exposes_demo_inventory() -> None:
    response = client.get("/state")
    assert response.status_code == 200

    payload = response.json()
    assert payload["datasets"] == ["naive_memory", "groundtruth_memory"]
    assert payload["benchmark"]["naive_cites_retracted"] == 19
    assert payload["benchmark"]["groundtruth_cites_retracted"] == 0
    assert payload["active_retractions"] == []
    assert len(payload["processed_retractions"]) == 25
    assert payload["default_question"]


def test_ask_endpoint_uses_answer_layer(monkeypatch) -> None:
    async def fake_answer(question, dataset, **kwargs):
        return {
            "question": question,
            "dataset": dataset,
            "text": "cited answer",
            "references": [],
            "cites_retracted": False,
            "retracted_dois": [],
            "qa_id": "qa-1",
            "session_id": kwargs["session_id"],
        }

    monkeypatch.setattr("web.app.answer_question", fake_answer)
    response = client.post(
        "/ask",
        json={
            "question": "What should the memory cite?",
            "dataset": "groundtruth_memory",
            "session_id": "session-1",
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["text"] == "cited answer"
    assert payload["session_id"] == "session-1"


def test_retract_endpoint_streams_timeline(monkeypatch) -> None:
    active_doi = "10.5555/demo-active"

    def fake_claim_for_doi(doi):
        return {"claim_id": "R999", "doi": doi, "status": "active"}

    async def fake_process_retraction(doi):
        return {
            "claim_id": "R999",
            "doi": doi,
            "decision": {"contradicts": True, "confidence": 1.0},
            "forget_result": {"status": "success"},
            "graph_edges_after_forget": 0,
        }

    monkeypatch.setattr("web.app.claim_for_doi", fake_claim_for_doi)
    monkeypatch.setattr("web.app.process_retraction", fake_process_retraction)
    response = client.post("/retract", json={"doi": active_doi})

    assert response.status_code == 200
    events = [json.loads(line)["event"] for line in response.text.splitlines()]
    assert events == [
        "detected",
        "running",
        "contradiction_found",
        "forgotten",
        "complete",
    ]


def test_feedback_and_improve_endpoints(monkeypatch) -> None:
    async def fake_add_feedback(session_id, qa_id, feedback_score, feedback_text=None):
        return {
            "session_id": session_id,
            "qa_id": qa_id,
            "feedback_score": feedback_score,
            "feedback_text": feedback_text,
            "updated": True,
        }

    async def fake_improve(dataset, session_ids, *, feedback_alpha=1.0):
        return {
            "dataset": dataset,
            "session_ids": session_ids,
            "feedback_alpha": feedback_alpha,
            "session_bridge": "skipped_quota_fallback",
        }

    monkeypatch.setattr("web.app.add_feedback", fake_add_feedback)
    monkeypatch.setattr("web.app.improve_from_feedback", fake_improve)

    feedback = client.post(
        "/feedback",
        json={"session_id": "session-1", "qa_id": "qa-1", "score": 1},
    )
    improve = client.post(
        "/improve",
        json={"dataset": "groundtruth_memory", "session_ids": ["session-1"]},
    )

    assert feedback.status_code == 200
    assert feedback.json()["updated"] is True
    assert improve.status_code == 200
    assert improve.json()["session_bridge"] == "skipped_quota_fallback"


def test_graph_endpoint_serves_html(monkeypatch) -> None:
    async def fake_render_graph_html():
        return "<html><body>graph</body></html>"

    monkeypatch.setattr("web.app.render_graph_html", fake_render_graph_html)
    response = client.get("/graph")

    assert response.status_code == 200
    assert "graph" in response.text
