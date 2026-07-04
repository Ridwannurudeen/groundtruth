from __future__ import annotations

from typing import Any, Literal
from uuid import UUID

from pydantic import BaseModel, Field
from sqlalchemy import select


class ContradictionDecision(BaseModel):
    contradicts: bool
    superseded_doi: str | None = None
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str


class SemanticConflictDecision(BaseModel):
    conflicts: bool
    direction: Literal["a_supersedes_b", "b_supersedes_a", "mutual", "none"]
    basis: str
    confidence: float = Field(ge=0.0, le=1.0)


def judge_retraction_supersession(
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


def judge_retraction_contradiction(
    claim: dict[str, Any],
    retraction: dict[str, Any],
) -> ContradictionDecision:
    return judge_retraction_supersession(claim, retraction)


async def judge_semantic_conflict(
    claim_a: dict[str, Any],
    claim_b: dict[str, Any],
) -> SemanticConflictDecision:
    from cognee.infrastructure.llm import LLMGateway

    system_prompt = """
You judge whether two scientific memory claims genuinely conflict.
Return conflicts=true only when the claims make incompatible assertions about
the same intervention, exposure, population, outcome, or mechanism. Do not mark
mere topic overlap, different populations, or complementary findings as a
conflict. Direction means which claim should supersede the other if one is newer
or stronger; use mutual when the conflict is real but direction is not justified.
"""
    text_input = "\n".join(
        [
            "Claim A:",
            f"ID: {claim_a['claim_id']}",
            f"Text: {claim_a['claim_text']}",
            f"Source: {claim_a['source']['title']} ({claim_a['source']['year']})",
            f"DOI: {claim_a['source']['doi']}",
            "",
            "Claim B:",
            f"ID: {claim_b['claim_id']}",
            f"Text: {claim_b['claim_text']}",
            f"Source: {claim_b['source']['title']} ({claim_b['source']['year']})",
            f"DOI: {claim_b['source']['doi']}",
        ]
    )
    return await LLMGateway.acreate_structured_output(
        text_input=text_input,
        system_prompt=system_prompt,
        response_model=SemanticConflictDecision,
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


async def ledger_edges_for_node(
    dataset_id: UUID,
    node_id: UUID,
    relationship_names: set[str] | None = None,
) -> list[Any]:
    from cognee.infrastructure.databases.relational import get_relational_engine
    from cognee.modules.graph.models import Edge

    stmt = select(Edge).where(
        Edge.dataset_id == dataset_id,
        (Edge.source_node_id == node_id) | (Edge.destination_node_id == node_id),
    )
    if relationship_names is not None:
        stmt = stmt.where(Edge.relationship_name.in_(relationship_names))
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


async def write_relationship_edge(data: dict[str, Any], ctx=None) -> dict[str, Any]:
    if isinstance(data, list):
        candidates = [
            item for item in data if isinstance(item, dict) and "source_node_id" in item
        ]
        if len(candidates) != 1:
            raise TypeError("Expected one relationship payload in memify input")
        data = candidates[0]

    if not ctx or not ctx.user or not ctx.dataset:
        raise RuntimeError("memify context missing user or dataset")

    relationship_name = data.get("relationship_name") or "contradicts"
    graph_edge = (
        str(data["source_node_id"]),
        str(data["target_node_id"]),
        relationship_name,
        data["properties"],
    )
    ledger_edge = (
        data["source_node_id"],
        data["target_node_id"],
        relationship_name,
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


async def write_contradiction_edge(data: dict[str, Any], ctx=None) -> dict[str, Any]:
    return await write_relationship_edge(data, ctx=ctx)


async def add_relationship_edge(
    cognee: Any,
    *,
    dataset_id: UUID,
    source_data_id: UUID,
    target_data_id: UUID,
    relationship_name: str,
    attributed_data_id: UUID,
    properties: dict[str, Any],
) -> dict[str, Any]:
    from cognee.modules.pipelines import Task

    source_node = scientific_claim_node(await ledger_nodes(dataset_id, source_data_id))
    target_node = scientific_claim_node(await ledger_nodes(dataset_id, target_data_id))
    payload = {
        "source_node_id": source_node.slug,
        "target_node_id": target_node.slug,
        "relationship_name": relationship_name,
        "attributed_data_id": attributed_data_id,
        "properties": {
            "relationship_name": relationship_name,
            "source_data_id": str(source_data_id),
            "target_data_id": str(target_data_id),
            **properties,
        },
    }
    result = await cognee.memify(
        extraction_tasks=[Task(pass_through)],
        enrichment_tasks=[Task(write_relationship_edge)],
        data=payload,
        dataset=dataset_id,
    )
    return {
        "source_node_id": str(source_node.slug),
        "target_node_id": str(target_node.slug),
        "relationship_name": relationship_name,
        "memify_result": result,
        "properties": payload["properties"],
    }


async def add_contradiction_edge(
    cognee: Any,
    *,
    dataset_id: UUID,
    superseding_data_id: UUID,
    superseded_data_id: UUID,
    decision: ContradictionDecision,
) -> dict[str, Any]:
    properties = {
        "edge_text": (
            f"Retraction notice for {decision.superseded_doi} contradicts the original claim"
        ),
        "superseded_doi": decision.superseded_doi,
        "confidence": decision.confidence,
        "rationale": decision.rationale,
        "ontology_valid": False,
    }
    return await add_relationship_edge(
        cognee,
        dataset_id=dataset_id,
        source_data_id=superseding_data_id,
        target_data_id=superseded_data_id,
        relationship_name="contradicts",
        attributed_data_id=superseding_data_id,
        properties=properties,
    )


async def add_semantic_conflict_edges(
    cognee: Any,
    *,
    dataset_id: UUID,
    claim_a_data_id: UUID,
    claim_b_data_id: UUID,
    claim_a_id: str,
    claim_b_id: str,
    decision: SemanticConflictDecision,
) -> list[dict[str, Any]]:
    if not decision.conflicts or decision.confidence < 0.7:
        return []

    shared_properties = {
        "edge_text": f"{claim_a_id} semantically conflicts with {claim_b_id}",
        "claim_a_id": claim_a_id,
        "claim_b_id": claim_b_id,
        "direction": decision.direction,
        "confidence": decision.confidence,
        "basis": decision.basis,
        "ontology_valid": False,
    }
    results = [
        await add_relationship_edge(
            cognee,
            dataset_id=dataset_id,
            source_data_id=claim_a_data_id,
            target_data_id=claim_b_data_id,
            relationship_name="contradicts",
            attributed_data_id=claim_a_data_id,
            properties=shared_properties,
        )
    ]
    if decision.direction == "a_supersedes_b" and decision.confidence >= 0.9:
        results.append(
            await add_relationship_edge(
                cognee,
                dataset_id=dataset_id,
                source_data_id=claim_a_data_id,
                target_data_id=claim_b_data_id,
                relationship_name="supersedes",
                attributed_data_id=claim_a_data_id,
                properties=shared_properties,
            )
        )
    elif decision.direction == "b_supersedes_a" and decision.confidence >= 0.9:
        results.append(
            await add_relationship_edge(
                cognee,
                dataset_id=dataset_id,
                source_data_id=claim_b_data_id,
                target_data_id=claim_a_data_id,
                relationship_name="supersedes",
                attributed_data_id=claim_b_data_id,
                properties=shared_properties,
            )
        )
    elif decision.direction == "mutual":
        results.append(
            await add_relationship_edge(
                cognee,
                dataset_id=dataset_id,
                source_data_id=claim_b_data_id,
                target_data_id=claim_a_data_id,
                relationship_name="contradicts",
                attributed_data_id=claim_b_data_id,
                properties=shared_properties,
            )
        )
    return results


async def graph_contradiction_edges(
    dataset_id: UUID,
) -> list[tuple[str, str, str, dict[str, Any]]]:
    from cognee.context_global_variables import set_database_global_context_variables
    from cognee.infrastructure.databases.graph import get_graph_engine
    from cognee.modules.users.methods import get_default_user

    user = await get_default_user()
    async with set_database_global_context_variables(dataset_id, user.id):
        graph_engine = await get_graph_engine()
        _, edges = await graph_engine.get_graph_data()
    return [edge for edge in edges if edge[2] == "contradicts"]
