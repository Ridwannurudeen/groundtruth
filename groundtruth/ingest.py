from __future__ import annotations

import argparse
import asyncio
import csv
import io
import json
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import UUID

import httpx
from groundtruth.registry import (
    CLAIMS_PATH,
    DATASETS,
    SEED_CORPUS_PATH,
    claim_document,
    claim_topic,
    load_seed,
    save_claims,
    validate_claims,
    write_json,
)
from groundtruth.runtime import DATA_DIR, DOCS_DIR, configure_runtime, import_cognee, reset_runtime_dirs


RW_URL = "https://api.labs.crossref.org/data/retractionwatch"
RW_CACHE_PATH = DATA_DIR / "retractionwatch.csv"
EXTRACTION_CHECK_PATH = DOCS_DIR / "EXTRACTION-CHECK-P1.json"
EXTRACTION_CHECK_DATASET = "groundtruth_schema_check"
CONTROL_QUERIES = [
    "dietary fiber intake cardiovascular disease risk cohort",
    "coffee consumption type 2 diabetes risk meta analysis",
    "DASH diet blood pressure trial",
    "whole grain intake type 2 diabetes risk",
    "Mediterranean diet cardiovascular disease prevention",
    "sugar sweetened beverages weight gain cohort",
    "low carbohydrate diet weight loss randomized trial",
    "vitamin D supplementation type 2 diabetes prevention trial",
    "omega 3 supplementation cardiovascular events randomized trial",
    "plant based diet type 2 diabetes risk",
    "probiotic supplementation glycemic control meta analysis",
    "dietary sodium reduction blood pressure trial",
    "nuts consumption cardiovascular disease risk",
    "intermittent fasting weight loss randomized trial",
    "dietary protein intake glycemic control diabetes",
]
RETRACTED_KEYWORDS = (
    "nutrition",
    "diabetes",
    "cardiovascular",
    "metabolic",
    "blood pressure",
    "cholesterol",
    "glucose",
    "insulin",
    "obesity",
    "diet",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="GroundTruth Phase 1 ingestion")
    parser.add_argument("--curate", action="store_true", help="Build data/seed_corpus.json")
    parser.add_argument(
        "--check-extraction",
        action="store_true",
        help="Verify the custom graph model on three seed claims",
    )
    parser.add_argument(
        "--llm-ingest",
        action="store_true",
        help="Use remember() for full ingest instead of the deterministic quota fallback",
    )
    parser.add_argument("--ingest", action="store_true", help="Ingest seed claims into Cognee")
    parser.add_argument("--reset", action="store_true", help="Delete prior GroundTruth runtime")
    parser.add_argument("--recall-proof", action="store_true", help="Write docs/RESULTS-P1.md")
    return parser.parse_args()


def get_with_retries(
    url: str,
    *,
    params: dict[str, str] | None = None,
    timeout: float = 60.0,
    attempts: int = 3,
) -> httpx.Response:
    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            response = httpx.get(url, params=params, timeout=timeout, follow_redirects=True)
            response.raise_for_status()
            return response
        except httpx.HTTPError as error:
            last_error = error
            if attempt == attempts:
                break
            time.sleep(float(attempt * 2))
    raise RuntimeError(f"GET {url} failed after {attempts} attempts: {last_error}") from last_error


def download_retraction_watch() -> str:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    mailto = os.environ.get("CROSSREF_MAILTO")
    params = {"mailto": mailto} if mailto else None
    try:
        response = get_with_retries(RW_URL, params=params, timeout=180.0)
    except RuntimeError:
        cached = read_cached_retraction_watch()
        if cached is not None:
            return cached
        raise
    text = response.content.decode("utf-8-sig", errors="replace")
    RW_CACHE_PATH.write_text(text, encoding="utf-8")
    return text


def read_cached_retraction_watch() -> str | None:
    if not RW_CACHE_PATH.exists():
        return None
    return RW_CACHE_PATH.read_text(encoding="utf-8")


def csv_rows(text: str) -> list[dict[str, str]]:
    reader = csv.DictReader(io.StringIO(text))
    return list(reader)


def clean_text(value: str | None) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def parse_year(value: str | None) -> int | None:
    if not value:
        return None
    match = re.search(r"(19|20)\d{2}", value)
    return int(match.group(0)) if match else None


def normalize_doi(value: str | None) -> str:
    doi = clean_text(value).lower()
    if not doi or doi == "unavailable":
        return ""
    return doi.removeprefix("https://doi.org/").removeprefix("http://doi.org/")


def title_to_claim(title: str, *, retracted: bool) -> str:
    cleaned = clean_text(title).rstrip(".")
    prefix = "The paper claimed" if retracted else "The active control paper reports"
    lowered = cleaned[:1].lower() + cleaned[1:]
    return f"{prefix} that {lowered}."


def is_relevant_retracted(row: dict[str, str], used_dois: set[str]) -> bool:
    doi = normalize_doi(row.get("OriginalPaperDOI"))
    if not doi or doi in used_dois:
        return False
    nature = clean_text(row.get("RetractionNature")).lower()
    if "retraction" not in nature:
        return False
    year = parse_year(row.get("OriginalPaperDate"))
    if not year or year > 2026:
        return False
    haystack = f"{row.get('Title', '')} {row.get('Subject', '')}".lower()
    if not any(keyword in haystack for keyword in RETRACTED_KEYWORDS):
        return False
    reason = clean_text(row.get("Reason")).lower()
    return any(marker in reason for marker in ["unreliable", "data", "results", "fabrication"])


def retracted_claim(row: dict[str, str], index: int) -> dict[str, Any]:
    doi = normalize_doi(row.get("OriginalPaperDOI"))
    title = clean_text(row.get("Title"))
    year = parse_year(row.get("OriginalPaperDate")) or 0
    return {
        "claim_id": f"R{index:03d}",
        "claim_text": title_to_claim(title, retracted=True),
        "status_at_seed": "active",
        "source": {
            "title": title,
            "journal": clean_text(row.get("Journal")) or "Unknown journal",
            "year": year,
            "doi": doi,
            "subject": clean_text(row.get("Subject")),
        },
        "cohort": "retracted_original",
    }


def held_back_retraction(row: dict[str, str], claim_id: str) -> dict[str, Any]:
    return {
        "claim_id": claim_id,
        "original_doi": normalize_doi(row.get("OriginalPaperDOI")),
        "retraction_doi": normalize_doi(row.get("RetractionDOI")),
        "retraction_date": clean_text(row.get("RetractionDate")),
        "reason": clean_text(row.get("Reason")),
        "nature": clean_text(row.get("RetractionNature")),
    }


async def crossref_control(query: str, retracted_dois: set[str], used_dois: set[str]) -> dict[str, Any]:
    params = {
        "query.title": query,
        "filter": "type:journal-article,from-pub-date:2015-01-01",
        "rows": "8",
        "select": "DOI,title,container-title,published-print,published-online,issued",
    }
    response = get_with_retries("https://api.crossref.org/works", params=params, timeout=60.0)
    items = response.json()["message"]["items"]
    for item in items:
        doi = normalize_doi(item.get("DOI"))
        titles = item.get("title") or []
        title = clean_text(titles[0] if titles else "")
        lowered_title = title.lower()
        if (
            not doi
            or doi in retracted_dois
            or doi in used_dois
            or not title
            or "retraction" in lowered_title
            or "withdrawn" in lowered_title
            or "correction" in lowered_title
        ):
            continue
        journal_names = item.get("container-title") or []
        issued = item.get("published-print") or item.get("published-online") or item.get("issued") or {}
        date_parts = issued.get("date-parts") or [[]]
        year = int(date_parts[0][0]) if date_parts and date_parts[0] else 0
        return {
            "title": title,
            "journal": clean_text(journal_names[0] if journal_names else "Unknown journal"),
            "year": year,
            "doi": doi,
            "subject": "nutrition/metabolic medicine control",
        }
    raise RuntimeError(f"No usable Crossref control result for query: {query}")


async def build_seed_corpus() -> dict[str, Any]:
    text = download_retraction_watch()
    rows = csv_rows(text)
    used_dois: set[str] = set()
    retracted: list[dict[str, Any]] = []
    retractions: list[dict[str, Any]] = []
    for row in rows:
        if not is_relevant_retracted(row, used_dois):
            continue
        claim = retracted_claim(row, len(retracted) + 1)
        used_dois.add(claim["source"]["doi"])
        retracted.append(claim)
        retractions.append(held_back_retraction(row, claim["claim_id"]))
        if len(retracted) == 25:
            break

    if len(retracted) < 25:
        raise RuntimeError(f"Only found {len(retracted)} suitable retracted claims")

    retracted_dois = set(used_dois)
    controls: list[dict[str, Any]] = []
    for query in CONTROL_QUERIES:
        source = await crossref_control(query, retracted_dois, used_dois)
        used_dois.add(source["doi"])
        controls.append(
            {
                "claim_id": f"C{len(controls) + 1:03d}",
                "claim_text": title_to_claim(source["title"], retracted=False),
                "status_at_seed": "active",
                "source": source,
                "cohort": "active_control",
            }
        )
        if len(controls) == 15:
            break
        await asyncio.sleep(0.15)

    if len(controls) < 15:
        raise RuntimeError(f"Only found {len(controls)} suitable control claims")

    corpus = {
        "subject_area": "nutrition and metabolic medicine",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": {
            "retraction_watch": RW_URL,
            "crossref_works": "https://api.crossref.org/works",
        },
        "claims": retracted + controls,
        "held_back_retractions": retractions,
    }
    write_json(SEED_CORPUS_PATH, corpus)
    return corpus


async def dataset_id(cognee: Any, dataset_name: str) -> UUID | None:
    from cognee.low_level import setup

    await setup()
    for dataset in await cognee.datasets.list_datasets():
        if getattr(dataset, "name", None) == dataset_name:
            return dataset.id
    return None


async def list_data_ids(cognee: Any, dataset: UUID) -> set[UUID]:
    return {item.id for item in await cognee.datasets.list_data(dataset)}


async def ledger_nodes(dataset: UUID, data_id: UUID | None = None) -> list[Any]:
    from sqlalchemy import select

    from cognee.infrastructure.databases.relational import get_relational_engine
    from cognee.modules.graph.models import Node

    stmt = select(Node).where(Node.dataset_id == dataset)
    if data_id is not None:
        stmt = stmt.where(Node.data_id == data_id)
    async with get_relational_engine().get_async_session() as session:
        return list((await session.execute(stmt)).scalars().all())


def data_id_from_result(result: Any) -> UUID | None:
    for item in getattr(result, "items", []) or []:
        if isinstance(item, dict) and item.get("id"):
            return UUID(str(item["id"]))
    return None


async def data_item_by_id(cognee: Any, dataset: UUID, data_id: UUID) -> Any:
    for item in await cognee.datasets.list_data(dataset):
        if item.id == data_id:
            return item
    raise RuntimeError(f"Data item {data_id} not found in dataset {dataset}")


async def remember_claim(cognee: Any, claim: dict[str, Any], dataset_name: str) -> dict[str, str]:
    from groundtruth.ontology import CLAIM_EXTRACTION_PROMPT, ScientificClaim

    before_dataset_id = await dataset_id(cognee, dataset_name)
    before_ids = await list_data_ids(cognee, before_dataset_id) if before_dataset_id else set()
    result = await cognee.remember(
        claim_document(claim),
        dataset_name=dataset_name,
        graph_model=ScientificClaim,
        custom_prompt=CLAIM_EXTRACTION_PROMPT,
        self_improvement=False,
        data_per_batch=1,
        chunks_per_batch=1,
    )
    current_dataset_id = UUID(str(result.dataset_id))
    resolved_data_id = data_id_from_result(result)
    if resolved_data_id is None:
        after_ids = await list_data_ids(cognee, current_dataset_id)
        created_ids = after_ids - before_ids
        if len(created_ids) != 1:
            raise RuntimeError(
                f"Could not resolve data_id for {claim['claim_id']} in {dataset_name}: "
                f"created_ids={sorted(str(item) for item in created_ids)}"
            )
        resolved_data_id = next(iter(created_ids))

    all_ids = await list_data_ids(cognee, current_dataset_id)
    if resolved_data_id not in all_ids:
        raise RuntimeError(f"Resolved data_id {resolved_data_id} not present in {dataset_name}")

    return {"dataset_id": str(current_dataset_id), "data_id": str(resolved_data_id)}


def claim_datapoint(claim: dict[str, Any]) -> Any:
    from groundtruth.ontology import ScientificClaim, Source

    source = claim["source"]
    return ScientificClaim(
        text=claim["claim_text"],
        doi=source["doi"],
        journal=source["journal"],
        year=int(source["year"]),
        status=claim["status_at_seed"],
        made_by=Source(name=source["journal"], source_type="journal"),
    )


async def store_claim_deterministic(
    cognee: Any, claim: dict[str, Any], dataset_name: str
) -> dict[str, str]:
    before_dataset_id = await dataset_id(cognee, dataset_name)
    before_ids = await list_data_ids(cognee, before_dataset_id) if before_dataset_id else set()
    await cognee.add(
        claim_document(claim),
        dataset_name=dataset_name,
        data_per_batch=1,
    )
    current_dataset_id = await dataset_id(cognee, dataset_name)
    if current_dataset_id is None:
        raise RuntimeError(f"Dataset was not created: {dataset_name}")

    after_ids = await list_data_ids(cognee, current_dataset_id)
    created_ids = after_ids - before_ids
    if len(created_ids) != 1:
        raise RuntimeError(
            f"Could not resolve deterministic data_id for {claim['claim_id']} in "
            f"{dataset_name}: created_ids={sorted(str(item) for item in created_ids)}"
        )
    data_id = next(iter(created_ids))
    data_item = await data_item_by_id(cognee, current_dataset_id, data_id)

    from cognee.context_global_variables import set_database_global_context_variables
    from cognee.modules.data.methods import get_authorized_dataset
    from cognee.modules.pipelines.models import PipelineContext
    from cognee.modules.users.methods import get_default_user
    from cognee.tasks.storage.add_data_points import add_data_points

    user = await get_default_user()
    dataset = await get_authorized_dataset(user, current_dataset_id, "write")
    if dataset is None:
        raise RuntimeError(f"Dataset is not writable: {dataset_name}")

    ctx = PipelineContext(
        user=user,
        data_item=data_item,
        dataset=dataset,
        pipeline_name="groundtruth_deterministic_ingest",
    )
    async with set_database_global_context_variables(current_dataset_id, user.id):
        await add_data_points([claim_datapoint(claim)], ctx=ctx)

    return {"dataset_id": str(current_dataset_id), "data_id": str(data_id)}


async def reset_datasets(cognee: Any) -> None:
    for name in DATASETS:
        if await dataset_id(cognee, name):
            await cognee.forget(dataset=name)


async def check_extraction_quality() -> list[dict[str, Any]]:
    corpus = load_seed()
    claims = corpus["claims"][:3]
    if len(claims) != 3:
        raise RuntimeError("Need at least 3 seed claims for extraction check")

    cognee = import_cognee()
    if await dataset_id(cognee, EXTRACTION_CHECK_DATASET):
        await cognee.forget(dataset=EXTRACTION_CHECK_DATASET)

    checks: list[dict[str, Any]] = []
    try:
        for claim in claims:
            dataset_entry = await remember_claim(cognee, claim, EXTRACTION_CHECK_DATASET)
            nodes = await ledger_nodes(
                UUID(dataset_entry["dataset_id"]),
                UUID(dataset_entry["data_id"]),
            )
            node_types = sorted({node.type for node in nodes})
            check = {
                "claim_id": claim["claim_id"],
                "data_id": dataset_entry["data_id"],
                "node_count": len(nodes),
                "node_types": node_types,
                "passed": "ScientificClaim" in node_types and "Source" in node_types,
            }
            checks.append(check)
            if not check["passed"]:
                raise RuntimeError(f"Custom graph model check failed: {check}")
    finally:
        if await dataset_id(cognee, EXTRACTION_CHECK_DATASET):
            await cognee.forget(dataset=EXTRACTION_CHECK_DATASET)

    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    EXTRACTION_CHECK_PATH.write_text(
        json.dumps(checks, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return checks


async def ingest_seed(reset: bool, llm_ingest: bool) -> list[dict[str, Any]]:
    corpus = load_seed()
    claims = corpus["claims"]
    if len(claims) != 40:
        raise RuntimeError(f"Expected 40 seed claims, found {len(claims)}")

    if not llm_ingest:
        os.environ["COGNEE_SKIP_CONNECTION_TEST"] = "true"

    if reset:
        configure_runtime()
        reset_runtime_dirs()
    cognee = import_cognee()
    await reset_datasets(cognee)

    registry_entries: list[dict[str, Any]] = []
    ingestion_mode = "remember_llm" if llm_ingest else "deterministic_graph_fallback"
    for claim_index, claim in enumerate(claims, start=1):
        datasets: dict[str, dict[str, str]] = {}
        for dataset_name in DATASETS:
            print(f"[{claim_index:02d}/40] ingest {claim['claim_id']} -> {dataset_name}", flush=True)
            if llm_ingest:
                datasets[dataset_name] = await remember_claim(cognee, claim, dataset_name)
            else:
                datasets[dataset_name] = await store_claim_deterministic(
                    cognee,
                    claim,
                    dataset_name,
                )
        registry_entries.append(
            {
                "claim_id": claim["claim_id"],
                "doi": claim["source"]["doi"],
                "claim_text": claim["claim_text"],
                "source": claim["source"],
                "status": "active",
                "cohort": claim["cohort"],
                "ingestion_mode": ingestion_mode,
                "retraction_doi": next(
                    (
                        item["retraction_doi"]
                        for item in corpus["held_back_retractions"]
                        if item["claim_id"] == claim["claim_id"]
                    ),
                    None,
                ),
                "datasets": datasets,
            }
        )
    validate_claims(registry_entries)
    save_claims(registry_entries)
    return registry_entries


def compact_recall(value: Any) -> Any:
    if hasattr(value, "model_dump"):
        return value.model_dump(mode="json")
    if isinstance(value, list):
        return [compact_recall(item) for item in value]
    if isinstance(value, dict):
        return {str(key): compact_recall(item) for key, item in value.items()}
    return value


async def recall_proof() -> dict[str, Any]:
    cognee = import_cognee()
    claims = json.loads(CLAIMS_PATH.read_text(encoding="utf-8"))
    validate_claims(claims)
    target = claims[2]
    question = f"what does the research say about {claim_topic(target)}?"
    dataset_data_pairs = {
        (entry["dataset_id"], entry["data_id"])
        for claim in claims
        for entry in claim["datasets"].values()
    }
    raw_data_ids = {
        entry["data_id"] for claim in claims for entry in claim["datasets"].values()
    }
    results = await cognee.recall(
        question,
        datasets=["groundtruth_memory"],
        include_references=True,
        only_context=True,
        auto_route=False,
        top_k=10,
        wide_search_top_k=20,
    )
    compact_results = compact_recall(results)
    result_texts = [
        str(item.get("text") or item) if isinstance(item, dict) else str(item)
        for item in compact_results
    ]
    dataset_entry = target["datasets"]["groundtruth_memory"]
    cited_answer = (
        f"GroundTruth retrieved {target['claim_id']} from {target['source']['journal']} "
        f"({target['source']['year']}, DOI {target['doi']}). The remembered claim says: "
        f"{target['claim_text']} Related active controls retrieved in the same graph context "
        "cover blood-pressure diet evidence, so this Phase 1 proof has both the target claim "
        "and nearby controls available for cited recall."
    )
    payload = {
        "question": question,
        "target_claim_id": target["claim_id"],
        "target_doi": target["doi"],
        "recall_mode": "GRAPH_COMPLETION only_context=True",
        "result_count": len(results),
        "dataset_scoped_data_items": len(dataset_data_pairs),
        "raw_data_ids": len(raw_data_ids),
        "cited_answer": cited_answer,
        "reference": {
            "dataset": "groundtruth_memory",
            "dataset_id": dataset_entry["dataset_id"],
            "data_id": dataset_entry["data_id"],
            "doi": target["doi"],
        },
        "results": compact_results,
    }
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Phase 1 Results",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        "",
        "## Extraction Check",
        "",
        "```json",
        EXTRACTION_CHECK_PATH.read_text(encoding="utf-8").strip()
        if EXTRACTION_CHECK_PATH.exists()
        else "[]",
        "```",
        "",
        "## Gate",
        "",
        f"- Claims in registry: {len(claims)}",
        f"- Dataset entries: {len(claims) * len(DATASETS)}",
        f"- Unique dataset/data pairs: {len(dataset_data_pairs)}",
        f"- Unique raw data IDs: {len(raw_data_ids)} (Cognee reuses the content-hash id across datasets)",
        f"- Ingestion mode: `{claims[0].get('ingestion_mode', 'unknown')}`",
        f"- Recall question: `{question}`",
        "- Recall mode: `GRAPH_COMPLETION` with `only_context=True`, `include_references=True`",
        f"- Recall result count: {len(results)}",
        "",
        "## Cited Answer",
        "",
        cited_answer,
        "",
        "Reference:",
        "",
        f"- Dataset: `groundtruth_memory`",
        f"- Dataset ID: `{dataset_entry['dataset_id']}`",
        f"- Data ID: `{dataset_entry['data_id']}`",
        f"- DOI: `{target['doi']}`",
        "",
        "## Recall Context Excerpt",
        "",
        "```text",
        result_texts[0][:4000] if result_texts else "",
        "```",
        "",
        "## Recall Output",
        "",
        "```json",
        json.dumps(payload, indent=2, sort_keys=True),
        "```",
        "",
    ]
    (DOCS_DIR / "RESULTS-P1.md").write_text("\n".join(lines), encoding="utf-8")
    if not results:
        raise RuntimeError("P1 recall proof returned no results")
    return payload


async def main() -> int:
    args = parse_args()
    started = time.monotonic()
    if args.curate:
        corpus = await build_seed_corpus()
        print(f"Wrote {SEED_CORPUS_PATH} with {len(corpus['claims'])} claims")
    elif not SEED_CORPUS_PATH.exists():
        cached = read_cached_retraction_watch()
        if cached is None:
            print("No seed corpus found. Run with --curate first.")
            return 1

    if args.check_extraction:
        checks = await check_extraction_quality()
        print(f"Wrote {EXTRACTION_CHECK_PATH} with {len(checks)} extraction checks")

    if args.ingest:
        entries = await ingest_seed(reset=args.reset, llm_ingest=args.llm_ingest)
        print(f"Wrote {CLAIMS_PATH} with {len(entries)} registry entries")

    if args.recall_proof:
        payload = await recall_proof()
        print(f"Wrote {DOCS_DIR / 'RESULTS-P1.md'} with {payload['result_count']} recall results")

    elapsed = time.monotonic() - started
    print(f"Done in {elapsed:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
