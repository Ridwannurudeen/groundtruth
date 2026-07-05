from __future__ import annotations

import json

from fastapi.testclient import TestClient

from web.app import MUTATION_CONFIRMATION, app


client = TestClient(app)


def test_state_exposes_demo_inventory() -> None:
    response = client.get("/api/state")
    assert response.status_code == 200

    payload = response.json()
    assert payload["datasets"] == ["naive_memory", "groundtruth_memory"]
    assert payload["benchmark"]["naive_cites_retracted"] == 18
    assert payload["benchmark"]["groundtruth_cites_retracted"] == 0
    assert payload["active_retractions"] == []
    assert len(payload["processed_retractions"]) == 25
    assert payload["default_question"]
    assert payload["mutations_require_confirmation"] is True
    assert payload["mutation_confirmation"] == MUTATION_CONFIRMATION


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
        "/api/ask",
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


def test_retract_endpoint_requires_mutation_confirmation(monkeypatch) -> None:
    def fake_claim_for_doi(doi):
        return {"claim_id": "R999", "doi": doi, "status": "active"}

    monkeypatch.setattr("web.app.claim_for_doi", fake_claim_for_doi)
    response = client.post("/api/retract", json={"doi": "10.5555/demo-active"})

    assert response.status_code == 409
    assert "Mutation confirmation required" in response.text


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
    response = client.post(
        "/api/retract",
        json={
            "doi": active_doi,
            "confirm_mutation": MUTATION_CONFIRMATION,
        },
    )

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
        "/api/feedback",
        json={
            "session_id": "session-1",
            "qa_id": "qa-1",
            "score": 1,
            "confirm_mutation": MUTATION_CONFIRMATION,
        },
    )
    improve = client.post(
        "/api/improve",
        json={
            "dataset": "groundtruth_memory",
            "session_ids": ["session-1"],
            "confirm_mutation": MUTATION_CONFIRMATION,
        },
    )

    assert feedback.status_code == 200
    assert feedback.json()["updated"] is True
    assert improve.status_code == 200
    assert improve.json()["session_bridge"] == "skipped_quota_fallback"


def test_contested_endpoint_lists_open_pairs(monkeypatch) -> None:
    monkeypatch.setattr(
        "web.app.list_contested_pairs",
        lambda: [
            {
                "pair": "V2C003::V2C004",
                "status": "open",
                "decision": {
                    "conflicts": True,
                    "direction": "mutual",
                    "basis": "Claims disagree.",
                    "confidence": 1.0,
                },
                "claims": [
                    {
                        "claim_id": "V2C003",
                        "doi": "10.5555/a",
                        "belief_state": "contested",
                        "latest_state_change": {"evidence_class": "semantic_inference"},
                    },
                    {
                        "claim_id": "V2C004",
                        "doi": "10.5555/b",
                        "belief_state": "contested",
                        "latest_state_change": {"evidence_class": "semantic_inference"},
                    },
                ],
            }
        ],
    )

    response = client.get("/api/contested")

    assert response.status_code == 200
    payload = response.json()
    assert payload["count"] == 1
    assert payload["items"][0]["pair"] == "V2C003::V2C004"
    assert (
        payload["items"][0]["claims"][0]["latest_state_change"]["evidence_class"]
        == "semantic_inference"
    )


def test_briefing_endpoint_uses_briefing_layer(monkeypatch) -> None:
    def fake_build_briefing():
        return {
            "generated_at": "2026-07-04T08:00:00+00:00",
            "learned_last_night": [],
            "now_contested": [
                {
                    "pair": "V2C003::V2C004",
                    "evidence_class": "semantic_inference",
                    "evidence_ref": "pair:V2C003::V2C004",
                    "basis": "Claims disagree.",
                }
            ],
            "revised": [
                {
                    "claim_id": "V2C001",
                    "belief_state": "superseded",
                    "evidence_class": "semantic_inference",
                    "evidence_ref": "pair:V2C001::V2C002",
                    "basis": "Newer evidence supersedes it.",
                }
            ],
            "purged": [],
        }

    monkeypatch.setattr("web.app.build_briefing", fake_build_briefing)

    response = client.get("/api/briefing")

    assert response.status_code == 200
    payload = response.json()
    assert payload["generated_at"] == "2026-07-04T08:00:00+00:00"
    assert payload["now_contested"][0]["pair"] == "V2C003::V2C004"
    assert payload["revised"][0]["evidence_class"] == "semantic_inference"


def test_briefing_markdown_endpoint_serves_markdown(monkeypatch) -> None:
    monkeypatch.setattr(
        "web.app.build_briefing",
        lambda: {"generated_at": "2026-07-04T08:00:00+00:00"},
    )
    monkeypatch.setattr(
        "web.app.render_briefing_markdown",
        lambda briefing: "# Morning Briefing\n\nGenerated.",
    )

    response = client.get("/api/briefing.md")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/markdown")
    assert "# Morning Briefing" in response.text


def test_timeline_endpoint_uses_timeline_layer(monkeypatch) -> None:
    def fake_timeline_diff(from_date, to_date):
        return {
            "from": f"{from_date}T00:00:00+00:00",
            "to": f"{to_date}T00:00:00+00:00",
            "dataset": "groundtruth_memory",
            "changes": {
                "added": [],
                "contested": [],
                "revised": [
                    {
                        "claim_id": "R001",
                        "from_state": "active",
                        "to_state": "retracted",
                        "evidence_class": "authority_feed",
                        "basis": "Retraction Watch record.",
                    }
                ],
                "purged": [],
            },
        }

    monkeypatch.setattr("web.app.timeline_diff", fake_timeline_diff)

    response = client.get("/api/timeline?from=2023-01-01&to=2026-07-04")

    assert response.status_code == 200
    payload = response.json()
    assert payload["changes"]["revised"][0]["claim_id"] == "R001"
    assert payload["changes"]["revised"][0]["from_state"] == "active"
    assert payload["changes"]["revised"][0]["to_state"] == "retracted"
    assert payload["changes"]["revised"][0]["evidence_class"] == "authority_feed"
    assert payload["changes"]["revised"][0]["basis"] == "Retraction Watch record."


def test_timeline_endpoint_can_include_as_of_answers(monkeypatch) -> None:
    monkeypatch.setattr(
        "web.app.timeline_diff",
        lambda from_date, to_date: {
            "from": f"{from_date}T00:00:00+00:00",
            "to": f"{to_date}T00:00:00+00:00",
            "dataset": "groundtruth_memory",
            "changes": {
                "added": [],
                "contested": [],
                "revised": [],
                "purged": [],
            },
        },
    )

    def fake_answer_as_of(question, as_of):
        return {
            "question": question,
            "as_of": as_of,
            "text": f"As of {as_of}, answer for {question}",
            "references": [],
        }

    monkeypatch.setattr("web.app.answer_as_of", fake_answer_as_of)

    response = client.get(
        "/api/timeline?from=2023-01-01&to=2026-07-04&question=What%20changed%3F"
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["before"]["text"] == "As of 2023-01-01, answer for What changed?"
    assert payload["after"]["text"] == "As of 2026-07-04, answer for What changed?"


def test_adjudicate_endpoint_requires_mutation_confirmation(monkeypatch) -> None:
    async def fake_adjudicate(*args, **kwargs):
        return {"status": "resolved"}

    monkeypatch.setattr("web.app.adjudicate_pair", fake_adjudicate)
    response = client.post(
        "/api/adjudicate",
        json={"pair": "V2C003::V2C004", "verdict": "none"},
    )

    assert response.status_code == 409
    assert "Mutation confirmation required" in response.text


def test_adjudicate_endpoint_resolves_pair(monkeypatch) -> None:
    calls = []

    async def fake_adjudicate(pair, verdict, *, basis=None):
        calls.append((pair, verdict, basis))
        return {
            "pair": pair,
            "status": "resolved",
            "verdict": verdict,
            "state_changes": [
                {
                    "claim_id": "V2C003",
                    "state": "active",
                    "evidence_class": "user_assertion",
                    "evidence_ref": f"adjudication:{pair}",
                }
            ],
        }

    monkeypatch.setattr("web.app.adjudicate_pair", fake_adjudicate)
    response = client.post(
        "/api/adjudicate",
        json={
            "pair": "V2C003::V2C004",
            "verdict": "none",
            "basis": "Endpoint mismatch.",
            "confirm_mutation": MUTATION_CONFIRMATION,
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert calls == [("V2C003::V2C004", "none", "Endpoint mismatch.")]
    assert payload["state_changes"][0]["evidence_class"] == "user_assertion"
    assert payload["state_changes"][0]["evidence_ref"] == "adjudication:V2C003::V2C004"


def test_index_serves_contested_mount_points() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert 'data-page="landing"' in response.text
    assert 'href="/ask"' in response.text
    assert 'href="/briefing"' in response.text
    assert 'href="/contested"' in response.text
    assert 'href="/timeline"' in response.text
    assert 'href="/evidence"' in response.text


def test_graph_endpoint_serves_html(monkeypatch) -> None:
    async def fake_render_graph_html():
        return "<html><body>graph</body></html>"

    monkeypatch.setattr("web.app.render_graph_html", fake_render_graph_html)
    response = client.get("/api/graph")

    assert response.status_code == 200
    assert "graph" in response.text


def test_multi_page_routes_return_html_shells() -> None:
    for path in ("/ask", "/briefing", "/contested", "/timeline", "/evidence"):
        response = client.get(path)
        assert response.status_code == 200
        assert '<body data-page="' in response.text
