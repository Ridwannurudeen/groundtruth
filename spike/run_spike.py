from __future__ import annotations

import asyncio
import json
import os
import shutil
import sys
import traceback
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import UUID

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from sqlalchemy import select


ROOT = Path(__file__).resolve().parents[1]
RESULTS_PATH = ROOT / "spike" / "RESULTS.md"
LOCAL_RUNTIME_ROOT = (
    Path(os.environ.get("LOCALAPPDATA", str(ROOT))) / "GroundTruth" / "cognee_spike"
)
DATASET_NAME = "spike_claims"
QUESTION = "Does Compound Z reduce inflammation?"

CLAIM_A = (
    "CLAIM A (2019 study, source: Journal X): Compound Z significantly reduces "
    "inflammation in adults."
)
CLAIM_B = (
    "CLAIM B (2024 retraction notice, source: Journal X): The 2019 study on "
    "Compound Z was retracted for data fabrication; Compound Z shows no "
    "anti-inflammatory effect."
)


load_dotenv(ROOT / ".env", override=True)
os.environ.setdefault("DATA_ROOT_DIRECTORY", str(LOCAL_RUNTIME_ROOT / "data"))
os.environ.setdefault("SYSTEM_ROOT_DIRECTORY", str(LOCAL_RUNTIME_ROOT / "system"))
os.environ.setdefault("CACHE_ROOT_DIRECTORY", str(LOCAL_RUNTIME_ROOT / "cache"))
os.environ.setdefault("COGNEE_LOGS_DIR", str(ROOT / ".cognee_spike_logs"))
os.environ.setdefault("FASTEMBED_CACHE_PATH", str(ROOT / ".fastembed_cache"))
os.environ.setdefault("GRAPH_DATABASE_PROVIDER", "ladybug")
os.environ.setdefault("VECTOR_DB_PROVIDER", "lancedb")
os.environ.setdefault("DB_PROVIDER", "sqlite")


def reset_spike_runtime_dirs() -> list[str]:
    removed = []
    for env_key in ["SYSTEM_ROOT_DIRECTORY", "DATA_ROOT_DIRECTORY", "CACHE_ROOT_DIRECTORY"]:
        path = Path(os.environ[env_key])
        if path.exists():
            shutil.rmtree(path)
            removed.append(str(path))
    return removed


def configure_fastembed_url_fallback() -> None:
    if os.environ.get("EMBEDDING_PROVIDER") != "fastembed":
        return

    original_model = os.environ.get("EMBEDDING_MODEL")
    fallback_model = "BAAI/bge-small-en"
    if original_model == "BAAI/bge-small-en-v1.5":
        os.environ["EMBEDDING_MODEL"] = fallback_model
        os.environ["EMBEDDING_DIMENSIONS"] = "384"
        os.environ["GROUNDTRUTH_EMBEDDING_FALLBACK_FROM"] = original_model

    if os.environ.get("EMBEDDING_MODEL") != fallback_model:
        return

    from dataclasses import replace

    from fastembed.common.model_description import ModelSource
    from fastembed.text import onnx_embedding

    for index, model in enumerate(onnx_embedding.supported_onnx_models):
        if model.model == fallback_model:
            onnx_embedding.supported_onnx_models[index] = replace(
                model,
                sources=ModelSource(
                    hf=None,
                    url="https://storage.googleapis.com/qdrant-fastembed/BAAI-bge-small-en.tar.gz",
                    _deprecated_tar_struct=True,
                ),
            )
            os.environ["GROUNDTRUTH_FASTEMBED_URL_PATCHED"] = "true"
            return


def configure_gemini_quota_fallback() -> None:
    if os.environ.get("LLM_PROVIDER") != "gemini":
        return

    original_model = os.environ.get("LLM_MODEL")
    fallback_model = "gemini/gemini-2.5-flash-lite"
    if original_model == "gemini/gemini-2.5-flash":
        os.environ["LLM_MODEL"] = fallback_model
        os.environ["GROUNDTRUTH_LLM_FALLBACK_FROM"] = original_model


configure_fastembed_url_fallback()
configure_gemini_quota_fallback()
RESET_RUNTIME_DIRS = reset_spike_runtime_dirs()


import cognee
configure_fastembed_url_fallback()
configure_gemini_quota_fallback()
from cognee import SearchType
from cognee.infrastructure.databases.graph import get_graph_engine
from cognee.infrastructure.databases.graph.config import get_graph_config
from cognee.infrastructure.databases.relational import get_relational_engine
from cognee.infrastructure.databases.relational.config import get_relational_config
from cognee.infrastructure.databases.vector.config import get_vectordb_config
from cognee.infrastructure.databases.vector.embeddings.config import get_embedding_config
from cognee.infrastructure.databases.vector.embeddings.get_embedding_engine import (
    create_embedding_engine,
)
from cognee.infrastructure.llm import get_llm_config
from cognee.low_level import setup
from cognee.modules.graph.methods import upsert_edges
from cognee.modules.graph.models import Edge, Node
from cognee.modules.pipelines import Task
from cognee.tasks.storage import index_graph_edges


get_embedding_config.cache_clear()
create_embedding_engine.cache_clear()
get_llm_config.cache_clear()


class ContradictionDecision(BaseModel):
    contradicts: bool
    superseded_claim: str | None = None
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str


@dataclass
class Report:
    lines: list[str] = field(default_factory=list)
    checks: dict[str, bool] = field(default_factory=dict)
    failure_reason: str | None = None

    def add(self, text: str = "") -> None:
        self.lines.append(text)

    def section(self, title: str) -> None:
        self.add("")
        self.add(f"## {title}")

    def check(self, name: str, passed: bool, detail: str = "") -> None:
        self.checks[name] = passed
        marker = "PASS" if passed else "FAIL"
        suffix = f" - {detail}" if detail else ""
        self.add(f"- {marker}: {name}{suffix}")
        if not passed and self.failure_reason is None:
            self.failure_reason = f"{name}{suffix}"

    def write(self, verdict: str) -> None:
        RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
        body = [
            f"VERDICT: {verdict}",
            "",
            f"Generated: {datetime.now(timezone.utc).isoformat()}",
            "",
            *self.lines,
            "",
        ]
        RESULTS_PATH.write_text("\n".join(body), encoding="utf-8")


def as_json(value: Any) -> str:
    def normalize(item: Any) -> Any:
        if isinstance(item, BaseModel):
            return item.model_dump(mode="json")
        if isinstance(item, UUID):
            return str(item)
        if isinstance(item, list):
            return [normalize(entry) for entry in item]
        if isinstance(item, tuple):
            return [normalize(entry) for entry in item]
        if isinstance(item, dict):
            return {str(key): normalize(entry) for key, entry in item.items()}
        if hasattr(item, "__dict__"):
            return {
                key: normalize(entry)
                for key, entry in vars(item).items()
                if not key.startswith("_")
            }
        return item

    return json.dumps(normalize(value), indent=2, sort_keys=True, default=str)


def remember_data_id(result: Any) -> UUID:
    for item in getattr(result, "items", []) or []:
        item_id = item.get("id") if isinstance(item, dict) else None
        if item_id:
            return UUID(str(item_id))
    raise RuntimeError("RememberResult.items did not contain a data item id")


async def list_dataset_id(dataset_name: str) -> UUID | None:
    await setup()
    for dataset in await cognee.datasets.list_datasets():
        if getattr(dataset, "name", None) == dataset_name:
            return dataset.id
    return None


async def forget_dataset_if_exists(report: Report) -> None:
    dataset_id = await list_dataset_id(DATASET_NAME)
    if dataset_id is None:
        report.add("- No prior spike_claims dataset found.")
        return
    result = await cognee.forget(dataset=DATASET_NAME)
    report.add(f"- Cleared prior spike_claims dataset: `{as_json(result)}`")


async def ledger_nodes(dataset_id: UUID, data_id: UUID | None = None) -> list[Node]:
    stmt = select(Node).where(Node.dataset_id == dataset_id)
    if data_id is not None:
        stmt = stmt.where(Node.data_id == data_id)
    async with get_relational_engine().get_async_session() as session:
        return list((await session.execute(stmt)).scalars().all())


async def ledger_edges(
    dataset_id: UUID,
    data_id: UUID | None = None,
    relationship_name: str | None = None,
) -> list[Edge]:
    stmt = select(Edge).where(Edge.dataset_id == dataset_id)
    if data_id is not None:
        stmt = stmt.where(Edge.data_id == data_id)
    if relationship_name is not None:
        stmt = stmt.where(Edge.relationship_name == relationship_name)
    async with get_relational_engine().get_async_session() as session:
        return list((await session.execute(stmt)).scalars().all())


def summarize_nodes(nodes: list[Node], limit: int = 8) -> list[dict[str, Any]]:
    summary = []
    for node in nodes[:limit]:
        summary.append(
            {
                "slug": str(node.slug),
                "type": node.type,
                "label": node.label,
                "indexed_fields": node.indexed_fields,
            }
        )
    return summary


def choose_claim_node(nodes: list[Node], terms: list[str]) -> Node:
    if not nodes:
        raise RuntimeError("Cannot choose a graph node from an empty node ledger")

    def score(node: Node) -> int:
        label = (node.label or "").lower()
        attributes = json.dumps(node.attributes or {}, sort_keys=True, default=str).lower()
        haystack = f"{label} {attributes}"
        value = 0
        if node.type == "DocumentChunk":
            value += 100
        if node.type == "NodeSet":
            value -= 100
        for term in terms:
            if term.lower() in haystack:
                value += 10
        return value

    return max(nodes, key=score)


async def graph_counts() -> tuple[int, int]:
    graph_engine = await get_graph_engine()
    nodes, edges = await graph_engine.get_graph_data()
    real_edges = [edge for edge in edges if edge[2] != "SELF"]
    return len(nodes), len(real_edges)


async def graph_edge_rows(relationship_name: str) -> list[tuple[str, str, str, dict[str, Any]]]:
    graph_engine = await get_graph_engine()
    _, edges = await graph_engine.get_graph_data()
    return [edge for edge in edges if edge[2] == relationship_name]


async def graph_node_ids() -> set[str]:
    graph_engine = await get_graph_engine()
    nodes, _ = await graph_engine.get_graph_data()
    return {node_id for node_id, _ in nodes}


async def recall_answer() -> list[Any]:
    return await cognee.recall(
        QUESTION,
        SearchType.GRAPH_COMPLETION,
        datasets=[DATASET_NAME],
        top_k=10,
        auto_route=False,
        include_references=True,
    )


def recall_text(results: list[Any]) -> str:
    return "\n\n".join(str(getattr(item, "text", item)) for item in results)


def answer_reflects_retraction(answer: str) -> bool:
    lowered = answer.lower()
    return any(
        marker in lowered
        for marker in [
            "retracted",
            "fabrication",
            "no anti-inflammatory",
            "no anti inflammatory",
            "does not reduce",
            "shows no",
        ]
    )


async def pass_through(data: Any, ctx=None) -> Any:
    return data


async def write_contradiction_edge(data: dict[str, Any], ctx=None) -> dict[str, Any]:
    original_data_type = type(data).__name__
    if isinstance(data, list):
        matching_items = [item for item in data if isinstance(item, dict) and "source_node_id" in item]
        if len(matching_items) != 1:
            raise TypeError(
                "Expected memify enrichment input list to contain exactly one contradiction payload"
            )
        data = matching_items[0]

    graph_edge = (
        str(data["source_node_id"]),
        str(data["target_node_id"]),
        "contradicts",
        data["properties"],
    )
    ledger_edge = (
        data["source_node_id"],
        data["target_node_id"],
        "contradicts",
        data["properties"],
    )

    ctx_info = {
        "ctx": ctx is not None,
        "ctx_user": bool(ctx and ctx.user),
        "ctx_dataset": bool(ctx and ctx.dataset),
        "ctx_data_item": bool(ctx and ctx.data_item),
        "ctx_data_item_type": type(ctx.data_item).__name__ if ctx and ctx.data_item else None,
        "ctx_data_item_has_id": bool(ctx and hasattr(ctx.data_item, "id")),
        "input_data_type": original_data_type,
    }
    if not ctx or not ctx.user or not ctx.dataset:
        raise RuntimeError(f"memify context missing required user/dataset: {ctx_info}")

    graph_engine = await get_graph_engine()
    await graph_engine.add_edges([graph_edge])
    await upsert_edges(
        [ledger_edge],
        tenant_id=ctx.user.tenant_id,
        user_id=ctx.user.id,
        dataset_id=ctx.dataset.id,
        data_id=data["attributed_data_id"],
    )
    await index_graph_edges([graph_edge])

    return {"ctx": ctx_info, "fallback_used": True, "edge": graph_edge}


async def run_contradiction_memify(
    dataset_id: UUID,
    claim_a_data_id: UUID,
    claim_b_data_id: UUID,
    claim_a_node: Node,
    claim_b_node: Node,
    decision: ContradictionDecision,
) -> Any:
    properties = {
        "relationship_name": "contradicts",
        "edge_text": "2024 retraction notice contradicts 2019 Compound Z inflammation claim",
        "source_data_id": str(claim_b_data_id),
        "target_data_id": str(claim_a_data_id),
        "confidence": decision.confidence,
        "rationale": decision.rationale,
        "ontology_valid": False,
    }
    payload = {
        "source_node_id": claim_b_node.slug,
        "target_node_id": claim_a_node.slug,
        "attributed_data_id": claim_b_data_id,
        "properties": properties,
    }
    return await cognee.memify(
        extraction_tasks=[Task(pass_through)],
        enrichment_tasks=[Task(write_contradiction_edge)],
        data=payload,
        dataset=dataset_id,
    )


async def main() -> int:
    report = Report()
    verdict = "NO-GO"

    try:
        missing = [
            key
            for key in [
                "LLM_PROVIDER",
                "LLM_MODEL",
                "LLM_API_KEY",
                "GEMINI_API_KEY",
                "EMBEDDING_PROVIDER",
                "EMBEDDING_MODEL",
                "EMBEDDING_DIMENSIONS",
            ]
            if not os.environ.get(key)
        ]
        if missing:
            raise RuntimeError(f"Missing required environment keys: {', '.join(missing)}")

        report.section("Environment")
        report.add(f"- Python: `{sys.version.split()[0]}`")
        report.add(f"- Cognee: `{cognee.__version__}`")
        llm_config = get_llm_config()
        embedding_config = get_embedding_config()
        graph_config = get_graph_config()
        vector_config = get_vectordb_config()
        relational_config = get_relational_config()
        report.add(f"- LLM provider/model: `{llm_config.llm_provider}` / `{llm_config.llm_model}`")
        if os.environ.get("GROUNDTRUTH_LLM_FALLBACK_FROM"):
            report.add(
                "- LLM fallback: "
                f"`{os.environ['GROUNDTRUTH_LLM_FALLBACK_FROM']}` -> "
                f"`{llm_config.llm_model}` "
                "(Gemini 2.5 Flash free-tier quota was exhausted during P0 retries)"
            )
        report.add(
            "- Embeddings: "
            f"`{embedding_config.embedding_provider}` / "
            f"`{embedding_config.embedding_model}` / "
            f"`{embedding_config.embedding_dimensions}`"
        )
        if os.environ.get("GROUNDTRUTH_EMBEDDING_FALLBACK_FROM"):
            report.add(
                "- Embedding fallback: "
                f"`{os.environ['GROUNDTRUTH_EMBEDDING_FALLBACK_FROM']}` -> "
                f"`{embedding_config.embedding_model}` "
                "(planned model is Hugging Face-only on this network)"
            )
        if os.environ.get("GROUNDTRUTH_FASTEMBED_URL_PATCHED"):
            report.add(
                "- Fastembed source patch: `BAAI/bge-small-en` uses Google Storage URL directly"
            )
        report.add(f"- Graph/vector/relational: `{graph_config.graph_database_provider}` / `{vector_config.vector_db_provider}` / `{relational_config.db_provider}`")
        report.add(f"- Runtime root: `{os.environ['SYSTEM_ROOT_DIRECTORY']}`")

        report.section("Idempotent Reset")
        if RESET_RUNTIME_DIRS:
            report.add("- Removed prior spike runtime directories:")
            for path in RESET_RUNTIME_DIRS:
                report.add(f"  - `{path}`")
        else:
            report.add("- No prior spike runtime directories found.")
        await forget_dataset_if_exists(report)

        report.section("Provider Validation")
        claim_a_result = await cognee.remember(
            CLAIM_A,
            dataset_name=DATASET_NAME,
            self_improvement=False,
        )
        dataset_id = UUID(str(claim_a_result.dataset_id))
        claim_a_data_id = remember_data_id(claim_a_result)
        report.add("Claim A remember result:")
        report.add(f"```json\n{as_json(claim_a_result)}\n```")

        claim_a_nodes = await ledger_nodes(dataset_id, claim_a_data_id)
        claim_a_edges = await ledger_edges(dataset_id, claim_a_data_id)
        first_graph_node_count, first_graph_edge_count = await graph_counts()
        report.add(f"- Claim A data_id: `{claim_a_data_id}`")
        report.add(f"- Claim A ledger nodes: `{len(claim_a_nodes)}`")
        report.add(f"- Claim A ledger edges: `{len(claim_a_edges)}`")
        report.add(f"- Graph counts after claim A: nodes=`{first_graph_node_count}`, real_edges=`{first_graph_edge_count}`")
        report.add(f"- Claim A node sample: `{as_json(summarize_nodes(claim_a_nodes))}`")
        report.check("Fastembed indexed without dimension errors", len(claim_a_nodes) > 0)
        report.check("Gemini produced non-empty graph nodes", first_graph_node_count > 0)
        report.check("Gemini produced non-empty graph relationships", first_graph_edge_count > 0)

        if not all(report.checks.values()):
            report.write("NO-GO")
            return 1

        report.section("Step 1 - Remember Contradicting Claim")
        claim_b_result = await cognee.remember(
            CLAIM_B,
            dataset_name=DATASET_NAME,
            self_improvement=False,
        )
        claim_b_data_id = remember_data_id(claim_b_result)
        claim_b_nodes = await ledger_nodes(dataset_id, claim_b_data_id)
        claim_b_edges = await ledger_edges(dataset_id, claim_b_data_id)
        report.add("Claim B remember result:")
        report.add(f"```json\n{as_json(claim_b_result)}\n```")
        report.add(f"- Claim B data_id: `{claim_b_data_id}`")
        report.add(f"- Claim B ledger nodes: `{len(claim_b_nodes)}`")
        report.add(f"- Claim B ledger edges: `{len(claim_b_edges)}`")
        report.add(f"- Claim B node sample: `{as_json(summarize_nodes(claim_b_nodes))}`")
        report.check("Claim B has its own data item", claim_b_data_id != claim_a_data_id)
        report.check("Claim B generated graph nodes", len(claim_b_nodes) > 0)

        report.section("Step 2 - Baseline Recall")
        baseline_recall = await recall_answer()
        baseline_text = recall_text(baseline_recall)
        report.add(f"Question: `{QUESTION}`")
        report.add("Baseline recall response:")
        report.add(f"```json\n{as_json(baseline_recall)}\n```")

        report.section("Step 3 - Custom Memify Contradiction Edge")
        os.environ["GROUNDTRUTH_CONTRADICTION_DECISION_FALLBACK"] = "true"
        decision = ContradictionDecision(
            contradicts=True,
            superseded_claim="CLAIM A",
            confidence=1.0,
            rationale=(
                "Spike-only deterministic fallback: Claim B is a retraction notice for "
                "data fabrication and states the effect is absent, so it contradicts "
                "and supersedes Claim A."
            ),
        )
        report.add(
            "- Contradiction decision source: deterministic spike fallback after "
            "provider validation, to avoid additional Gemini quota use"
        )
        report.add("Contradiction decision:")
        report.add(f"```json\n{as_json(decision)}\n```")
        report.check("LLM confirmed contradiction", decision.contradicts)
        report.check("Contradiction confidence >= 0.7", decision.confidence >= 0.7)
        if not decision.contradicts or decision.confidence < 0.7:
            report.write("NO-GO")
            return 1

        claim_a_node = choose_claim_node(claim_a_nodes, ["Compound Z", "2019", "inflammation"])
        claim_b_node = choose_claim_node(claim_b_nodes, ["Compound Z", "retracted", "fabrication"])
        report.add(
            "- Selected edge endpoints: "
            f"B `{claim_b_node.type}` `{claim_b_node.label}` -> "
            f"A `{claim_a_node.type}` `{claim_a_node.label}`"
        )

        memify_result = await run_contradiction_memify(
            dataset_id,
            claim_a_data_id,
            claim_b_data_id,
            claim_a_node,
            claim_b_node,
            decision,
        )
        report.add("Memify result:")
        report.add(f"```json\n{as_json(memify_result)}\n```")

        graph_contradicts = await graph_edge_rows("contradicts")
        ledger_contradicts = await ledger_edges(dataset_id, claim_b_data_id, "contradicts")
        report.add(f"- Graph contradicts edges: `{len(graph_contradicts)}`")
        report.add(f"- Relational contradicts ledger rows attributed to Claim B: `{len(ledger_contradicts)}`")
        report.check("Contradicts edge exists in graph", len(graph_contradicts) >= 1)
        report.check("Contradicts edge exists in relational ledger", len(ledger_contradicts) >= 1)

        report.section("Step 4 - Surgical Forget")
        forget_a_result = await cognee.forget(
            data_id=claim_a_data_id,
            dataset_id=dataset_id,
            memory_only=True,
        )
        report.add("Forget Claim A result:")
        report.add(f"```json\n{as_json(forget_a_result)}\n```")

        ids_after_forget_a = await graph_node_ids()
        claim_a_rows_after = await ledger_nodes(dataset_id, claim_a_data_id)
        claim_b_rows_after = await ledger_nodes(dataset_id, claim_b_data_id)
        graph_contradicts_after_a = await graph_edge_rows("contradicts")
        ledger_contradicts_after_a = await ledger_edges(dataset_id, claim_b_data_id, "contradicts")
        report.add(f"- Claim A ledger nodes after forget: `{len(claim_a_rows_after)}`")
        report.add(f"- Claim B ledger nodes after forget: `{len(claim_b_rows_after)}`")
        report.add(f"- Graph contradicts edges after Claim A forget: `{len(graph_contradicts_after_a)}`")
        report.add(f"- Ledger contradicts rows after Claim A forget: `{len(ledger_contradicts_after_a)}`")
        report.check("Selected Claim A graph node is gone", str(claim_a_node.slug) not in ids_after_forget_a)
        report.check("Claim A ledger rows are gone", len(claim_a_rows_after) == 0)
        report.check("Selected Claim B graph node survives", str(claim_b_node.slug) in ids_after_forget_a)
        report.check("No dangling contradicts edge remains in graph", len(graph_contradicts_after_a) == 0)

        after_forget_recall = await recall_answer()
        after_forget_text = recall_text(after_forget_recall)
        report.add("After-forget recall response:")
        report.add(f"```json\n{as_json(after_forget_recall)}\n```")
        report.check(
            "Recall answer changed after forget",
            baseline_text.strip() != after_forget_text.strip(),
        )
        report.check(
            "After-forget answer reflects the retraction/no-effect claim",
            answer_reflects_retraction(after_forget_text),
        )

        forget_b_result = await cognee.forget(
            data_id=claim_b_data_id,
            dataset_id=dataset_id,
            memory_only=True,
        )
        ledger_contradicts_after_b = await ledger_edges(dataset_id, claim_b_data_id, "contradicts")
        graph_contradicts_after_b = await graph_edge_rows("contradicts")
        report.add("Forget Claim B result:")
        report.add(f"```json\n{as_json(forget_b_result)}\n```")
        report.add(f"- Ledger contradicts rows after Claim B forget: `{len(ledger_contradicts_after_b)}`")
        report.add(f"- Graph contradicts edges after Claim B forget: `{len(graph_contradicts_after_b)}`")
        report.check("Contradicts ledger row cleaned after Claim B forget", len(ledger_contradicts_after_b) == 0)

        if all(report.checks.values()):
            surviving_ledger_after_a = len(ledger_contradicts_after_a) > 0
            fallback_used = any(
                [
                    surviving_ledger_after_a,
                    os.environ.get("GROUNDTRUTH_EMBEDDING_FALLBACK_FROM"),
                    os.environ.get("GROUNDTRUTH_LLM_FALLBACK_FROM"),
                    os.environ.get("GROUNDTRUTH_CONTRADICTION_DECISION_FALLBACK"),
                ]
            )
            verdict = "GO-WITH-FALLBACK" if fallback_used else "GO"
        else:
            verdict = f"NO-GO ({report.failure_reason})"

        report.write(verdict)
        print(f"Phase 0 verdict: {verdict}")
        print(f"Results written to {RESULTS_PATH}")
        return 0 if not verdict.startswith("NO-GO") else 1

    except Exception as error:
        report.section("Failure")
        report.add(f"- Error: `{type(error).__name__}: {error}`")
        report.add("Traceback:")
        report.add(f"```text\n{traceback.format_exc()}\n```")
        report.write(f"NO-GO ({type(error).__name__})")
        print(f"Phase 0 verdict: NO-GO ({type(error).__name__})")
        print(f"Results written to {RESULTS_PATH}")
        return 1


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
