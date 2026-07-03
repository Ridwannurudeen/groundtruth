from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Literal
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, Response, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from groundtruth.answer import answer as answer_question
from groundtruth.feedback import add_feedback, improve_from_feedback
from groundtruth.ingest import normalize_doi
from groundtruth.registry import DATASETS, load_claims, load_json, load_seed
from groundtruth.runtime import DATA_DIR, LOCAL_RUNTIME_ROOT, import_cognee
from groundtruth.watcher import process_retraction, retraction_index


WEB_DIR = Path(__file__).resolve().parent
STATIC_DIR = WEB_DIR / "static"
BENCHMARK_RESULTS_PATH = DATA_DIR / "benchmark_results.json"
BENCHMARK_QUESTIONS_PATH = DATA_DIR / "benchmark_questions.json"
GRAPH_HTML_PATH = LOCAL_RUNTIME_ROOT / "memory_provenance.html"
DEMO_RETRACTION_ORDER = {
    "R014": 0,
    "R015": 1,
    "R016": 2,
    "R017": 3,
    "R018": 4,
    "R019": 5,
    "R020": 6,
    "R021": 7,
    "R022": 8,
    "R023": 9,
    "R024": 10,
    "R025": 11,
    "R013": 12,
}


class AskRequest(BaseModel):
    question: str = Field(min_length=1)
    dataset: Literal["naive_memory", "groundtruth_memory"]
    session_id: str | None = None
    record_session: bool = True
    feedback_influence: float = 0.0


class RetractionRequest(BaseModel):
    doi: str = Field(min_length=1)


class FeedbackRequest(BaseModel):
    session_id: str = Field(min_length=1)
    qa_id: str = Field(min_length=1)
    score: int = Field(ge=1, le=5)
    text: str | None = None


class ImproveRequest(BaseModel):
    dataset: Literal["groundtruth_memory"] = "groundtruth_memory"
    session_ids: list[str] = Field(min_length=1)
    feedback_alpha: float = 1.0


app = FastAPI(title="GroundTruth Demo", version="0.1.0")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


def compact_json(value: Any) -> Any:
    if hasattr(value, "model_dump"):
        return value.model_dump(mode="json")
    if isinstance(value, list):
        return [compact_json(item) for item in value]
    if isinstance(value, tuple):
        return [compact_json(item) for item in value]
    if isinstance(value, dict):
        return {str(key): compact_json(item) for key, item in value.items()}
    if isinstance(value, UUID):
        return str(value)
    return value


def demo_question(claim: dict[str, Any]) -> str:
    title = claim["source"]["title"]
    return f"What does the memory say about {title}?"


def retraction_options() -> list[dict[str, Any]]:
    seed = load_seed()
    indexed_retractions = retraction_index(seed)
    options = []
    for claim in load_claims():
        retraction = indexed_retractions.get(normalize_doi(claim["doi"]))
        if not retraction:
            continue
        options.append(
            {
                "claim_id": claim["claim_id"],
                "doi": claim["doi"],
                "status": claim["status"],
                "title": claim["source"]["title"],
                "journal": claim["source"]["journal"],
                "year": claim["source"]["year"],
                "retraction_doi": retraction.get("retraction_doi"),
                "reason": retraction.get("reason"),
                "question": demo_question(claim),
            }
        )
    return sorted(
        options,
        key=lambda option: (
            option["status"] != "active",
            DEMO_RETRACTION_ORDER.get(option["claim_id"], 99),
            option["claim_id"],
        ),
    )


def claim_for_doi(doi: str) -> dict[str, Any] | None:
    normalized = normalize_doi(doi)
    for option in retraction_options():
        if normalize_doi(option["doi"]) == normalized:
            return option
    return None


def benchmark_summary() -> dict[str, Any] | None:
    if not BENCHMARK_RESULTS_PATH.exists():
        return None
    return load_json(BENCHMARK_RESULTS_PATH)["summary"]


def default_question(options: list[dict[str, Any]]) -> str:
    if BENCHMARK_QUESTIONS_PATH.exists():
        questions = load_json(BENCHMARK_QUESTIONS_PATH)
        for question in questions:
            if question["kind"] == "retracted":
                return question["question"]
    return options[0]["question"]


def ndjson(event: str, payload: dict[str, Any]) -> str:
    return json.dumps({"event": event, **compact_json(payload)}, sort_keys=True) + "\n"


async def render_graph_html() -> str:
    os.environ["COGNEE_SKIP_CONNECTION_TEST"] = "true"
    import_cognee()
    from cognee.api.v1.visualize.memory_provenance import visualize_memory_provenance
    from cognee.low_level import setup
    from cognee.modules.users.methods import get_default_user

    await setup()
    user = await get_default_user()
    GRAPH_HTML_PATH.parent.mkdir(parents=True, exist_ok=True)
    return await visualize_memory_provenance(
        destination_file_path=str(GRAPH_HTML_PATH),
        include_memory=True,
        scope_user_ids=[user.id],
    )


@app.get("/", response_class=HTMLResponse)
async def index() -> HTMLResponse:
    return HTMLResponse((STATIC_DIR / "index.html").read_text(encoding="utf-8"))


@app.get("/favicon.ico", include_in_schema=False)
async def favicon() -> Response:
    return Response(status_code=204)


@app.get("/state")
async def state() -> dict[str, Any]:
    options = retraction_options()
    active = [option for option in options if option["status"] == "active"]
    processed = [option for option in options if option["status"] != "active"]
    return {
        "datasets": DATASETS,
        "session_id": f"groundtruth-ui-{uuid4().hex[:10]}",
        "benchmark": benchmark_summary(),
        "active_retractions": active,
        "processed_retractions": processed,
        "default_question": default_question(options),
        "default_doi": active[0]["doi"] if active else options[0]["doi"],
    }


@app.post("/ask")
async def ask(request: AskRequest) -> dict[str, Any]:
    return await answer_question(
        request.question,
        request.dataset,
        session_id=request.session_id,
        record_session=request.record_session,
        feedback_influence=request.feedback_influence,
    )


@app.post("/retract")
async def retract(request: RetractionRequest) -> StreamingResponse:
    async def stream():
        claim = claim_for_doi(request.doi)
        if claim is None:
            yield ndjson("error", {"message": f"No held-back retraction for DOI {request.doi}"})
            return
        if claim["status"] != "active":
            yield ndjson("already_prepared", claim)
            return

        yield ndjson("detected", claim)
        yield ndjson(
            "running",
            {
                "claim_id": claim["claim_id"],
                "doi": claim["doi"],
                "message": "Contradiction pass and memory-only forget are running.",
            },
        )
        result = await process_retraction(request.doi)
        decision = result.get("decision", {})
        yield ndjson(
            "contradiction_found",
            {
                "claim_id": result.get("claim_id"),
                "doi": result.get("doi"),
                "contradicts": decision.get("contradicts"),
                "confidence": decision.get("confidence"),
            },
        )
        yield ndjson(
            "forgotten",
            {
                "claim_id": result.get("claim_id"),
                "doi": result.get("doi"),
                "forget_result": result.get("forget_result"),
                "graph_edges_after_forget": result.get("graph_edges_after_forget"),
            },
        )
        yield ndjson("complete", {"result": result})

    return StreamingResponse(stream(), media_type="application/x-ndjson")


@app.post("/feedback")
async def feedback(request: FeedbackRequest) -> dict[str, Any]:
    return await add_feedback(
        request.session_id,
        request.qa_id,
        request.score,
        feedback_text=request.text,
    )


@app.post("/improve")
async def improve(request: ImproveRequest) -> dict[str, Any]:
    return await improve_from_feedback(
        request.dataset,
        request.session_ids,
        feedback_alpha=request.feedback_alpha,
    )


@app.get("/graph", response_class=HTMLResponse)
async def graph() -> HTMLResponse:
    try:
        html = await render_graph_html()
    except Exception as error:
        raise HTTPException(status_code=503, detail=str(error)) from error
    return HTMLResponse(html)
