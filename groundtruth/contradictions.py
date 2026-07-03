from __future__ import annotations

from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field
from sqlalchemy import select


class ContradictionDecision(BaseModel):
    contradicts: bool
    superseded_doi: str | None = None
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str


def judge_retraction_contradiction(
    claim: dict[str, Any],
    retraction: dict[str, Any],
) -> ContradictionDecision:
    original_doi = str(retraction.get("original_doi") or "").lower()
    claim_doi = str(claim.get("doi") or "").lower()
    matches_claim = bool(original_doi and original_doi == claim_doi)
    reason = str(retraction.get("reason") or "No reason supplied").strip()
    return ContradictionDecision(
        contradicts=matches_claim,
        superseded_doi=claim.get("doi") if matches_claim else None,
        confidence=1.0 if matches_claim else 0.0,
        rationale=(
            f"Retraction Watch links original DOI {original_doi} to this claim; "
            f"reason: {reason}"
            if matches_claim
            else f"Retraction DOI {original_doi} does not match claim DOI {claim_doi}."
        ),
    )


async def ledger_nodes(dataset_id: UUID, data_id: UUID | None = None) -> list[Any]:
    from cognee.infrastructure.databases.relational import get_relational_engine
    from cognee.modules.graph.models import Node

    stmt = select(Node).where(Node.dataset_id == dataset_id)
    if data_id is not None:
        stmt = stmt.where(Node.data_id == data_id)
    async with get_relational_engine().get_async_session() as session:
        return list((await session.execute(stmt)).scalars().all())


async def ledger_edges(
    dataset_id: UUID,
    data_id: UUID | None = None,
    relationship_name: str | None = None,
) -> list[Any]:
    from cognee.infrastructure.databases.relational import get_relational_engine
    from cognee.modules.graph.models import Edge

    stmt = select(Edge).where(Edge.dataset_id == dataset_id)
    if data_id is not None:
        stmt = stmt.where(Edge.data_id == data_id)
    if relationship_name is not None:
        stmt = stmt.where(Edge.relationship_name == relationship_name)
    async with get_relational_engine().get_async_session() as session:
        return list((await session.execute(stmt)).scalars().all())


async def memory_data_ids(dataset_id: UUID) -> set[str]:
    return {
        str(node.data_id)
        for node in await ledger_nodes(dataset_id)
        if getattr(node, "data_id", None) is not None
    }


def scientific_claim_node(nodes: list[Any]) -> Any:
    for node in nodes:
        if node.type == "ScientificClaim":
            return node
    raise RuntimeError("No ScientificClaim node found for data item")


async def pass_through(data: Any, ctx=None) -> Any:
    return data


async def write_contradiction_edge(data: dict[str, Any], ctx=None) -> dict[str, Any]:
    if isinstance(data, list):
        candidates = [item for item in data if isinstance(item, dict) and "source_node_id" in item]
        if len(candidates) != 1:
            raise TypeError("Expected one contradiction payload in memify input")
        data = candidates[0]

    if not ctx or not ctx.user or not ctx.dataset:
        raise RuntimeError("memify context missing user or dataset")

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

    from cognee.infrastructure.databases.graph import get_graph_engine
    from cognee.modules.graph.methods import upsert_edges
    from cognee.tasks.storage import index_graph_edges

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

    return {"edge": graph_edge, "data_id": str(data["attributed_data_id"])}


async def add_contradiction_edge(
    cognee: Any,
    *,
    dataset_id: UUID,
    superseding_data_id: UUID,
    superseded_data_id: UUID,
    decision: ContradictionDecision,
) -> dict[str, Any]:
    from cognee.modules.pipelines import Task

    superseding_node = scientific_claim_node(await ledger_nodes(dataset_id, superseding_data_id))
    superseded_node = scientific_claim_node(await ledger_nodes(dataset_id, superseded_data_id))
    properties = {
        "relationship_name": "contradicts",
        "edge_text": (
            f"Retraction notice for {decision.superseded_doi} contradicts the original claim"
        ),
        "source_data_id": str(superseding_data_id),
        "target_data_id": str(superseded_data_id),
        "superseded_doi": decision.superseded_doi,
        "confidence": decision.confidence,
        "rationale": decision.rationale,
        "ontology_valid": False,
    }
    payload = {
        "source_node_id": superseding_node.slug,
        "target_node_id": superseded_node.slug,
        "attributed_data_id": superseding_data_id,
        "properties": properties,
    }
    result = await cognee.memify(
        extraction_tasks=[Task(pass_through)],
        enrichment_tasks=[Task(write_contradiction_edge)],
        data=payload,
        dataset=dataset_id,
    )
    return {
        "source_node_id": str(superseding_node.slug),
        "target_node_id": str(superseded_node.slug),
        "memify_result": result,
        "properties": properties,
    }


async def graph_contradiction_edges(dataset_id: UUID) -> list[tuple[str, str, str, dict[str, Any]]]:
    from cognee.context_global_variables import set_database_global_context_variables
    from cognee.infrastructure.databases.graph import get_graph_engine
    from cognee.modules.users.methods import get_default_user

    user = await get_default_user()
    async with set_database_global_context_variables(dataset_id, user.id):
        graph_engine = await get_graph_engine()
        _, edges = await graph_engine.get_graph_data()
    return [edge for edge in edges if edge[2] == "contradicts"]
