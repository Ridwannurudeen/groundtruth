from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any
from uuid import UUID

from groundtruth.beliefs import belief_reference_fields, cites_by_state
from groundtruth.contradictions import (
    ledger_edges_for_node,
    ledger_nodes,
    memory_data_ids,
)
from groundtruth.registry import CLAIMS_PATH, load_claims
from groundtruth.runtime import import_cognee


STOPWORDS = {
    "about",
    "active",
    "after",
    "and",
    "does",
    "from",
    "paper",
    "research",
    "say",
    "that",
    "the",
    "what",
    "with",
}


def compact_recall(value: Any) -> Any:
    if hasattr(value, "model_dump"):
        return value.model_dump(mode="json")
    if isinstance(value, list):
        return [compact_recall(item) for item in value]
    if isinstance(value, dict):
        return {str(key): compact_recall(item) for key, item in value.items()}
    return value


def recall_text(results: Any) -> str:
    payload = compact_recall(results)
    if isinstance(payload, list):
        return "\n\n".join(
            str(item.get("text") or item) if isinstance(item, dict) else str(item)
            for item in payload
        )
    return str(payload)


def tokens(text: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9]+", text.lower())
        if len(token) >= 3 and token not in STOPWORDS
    }


def score_claim(question: str, claim: dict[str, Any]) -> int:
    question_tokens = tokens(question)
    source = claim["source"]
    haystack = " ".join(
        [
            claim["claim_text"],
            source["title"],
            source["journal"],
            claim["doi"],
        ]
    )
    return len(question_tokens & tokens(haystack))


async def dataset_id(cognee: Any, dataset_name: str) -> UUID:
    from cognee.low_level import setup

    await setup()
    for dataset in await cognee.datasets.list_datasets():
        if getattr(dataset, "name", None) == dataset_name:
            return dataset.id
    raise RuntimeError(f"Dataset not found: {dataset_name}")


def reference_for_claim(
    claim: dict[str, Any],
    dataset_name: str,
    dataset_entry: dict[str, Any],
    *,
    kind: str,
    data_id: str,
    score: int,
) -> dict[str, Any]:
    is_retracted_original = (
        kind == "original_claim" and claim.get("cohort") == "retracted_original"
    )
    return {
        "claim_id": claim["claim_id"],
        "kind": kind,
        "doi": claim["doi"],
        "data_id": data_id,
        "dataset": dataset_name,
        "dataset_id": dataset_entry["dataset_id"],
        "source": claim["source"]["journal"],
        "status": claim["status"],
        "dataset_status": dataset_entry.get("status", claim["status"]),
        "cohort": claim.get("cohort"),
        "retracted": is_retracted_original,
        "score": score,
        **belief_reference_fields(claim),
    }


def select_references(
    question: str,
    dataset_name: str,
    claims: list[dict[str, Any]],
    memory_ids: set[str],
) -> list[dict[str, Any]]:
    references: list[dict[str, Any]] = []
    for claim in claims:
        dataset_entry = claim.get("datasets", {}).get(dataset_name)
        if not dataset_entry:
            continue
        score = score_claim(question, claim)
        if score == 0:
            continue

        original_data_id = dataset_entry["data_id"]
        if original_data_id in memory_ids:
            references.append(
                reference_for_claim(
                    claim,
                    dataset_name,
                    dataset_entry,
                    kind="original_claim",
                    data_id=original_data_id,
                    score=score,
                )
            )

        notice_data_id = dataset_entry.get("retraction_notice_data_id")
        if notice_data_id and notice_data_id in memory_ids:
            references.append(
                reference_for_claim(
                    claim,
                    dataset_name,
                    dataset_entry,
                    kind="retraction_notice",
                    data_id=notice_data_id,
                    score=score,
                )
            )

    references.sort(key=lambda item: (-item["score"], item["kind"]))
    return references[:5]


def reference_index(
    dataset_name: str,
    claims: list[dict[str, Any]],
    memory_ids: set[str],
) -> dict[str, dict[str, Any]]:
    indexed: dict[str, dict[str, Any]] = {}
    for claim in claims:
        dataset_entry = claim.get("datasets", {}).get(dataset_name)
        if not dataset_entry:
            continue

        original_data_id = dataset_entry["data_id"]
        if original_data_id in memory_ids:
            indexed[original_data_id] = reference_for_claim(
                claim,
                dataset_name,
                dataset_entry,
                kind="original_claim",
                data_id=original_data_id,
                score=0,
            )

        notice_data_id = dataset_entry.get("retraction_notice_data_id")
        if notice_data_id and notice_data_id in memory_ids:
            indexed[notice_data_id] = reference_for_claim(
                claim,
                dataset_name,
                dataset_entry,
                kind="retraction_notice",
                data_id=notice_data_id,
                score=0,
            )
    return indexed


def edge_node_ids(edges: list[Any]) -> list[str]:
    node_ids: list[str] = []
    for edge in edges:
        for node in (getattr(edge, "node1", None), getattr(edge, "node2", None)):
            node_id = getattr(node, "id", None)
            if node_id is not None and str(node_id) not in node_ids:
                node_ids.append(str(node_id))
    return node_ids


async def references_from_graph_edges(
    dataset_id: UUID,
    dataset_name: str,
    claims: list[dict[str, Any]],
    memory_ids: set[str],
    edges: list[Any],
) -> list[dict[str, Any]]:
    node_to_data_id = {
        str(node.slug): str(node.data_id)
        for node in await ledger_nodes(dataset_id)
        if getattr(node, "data_id", None) is not None
    }
    data_id_to_reference = reference_index(dataset_name, claims, memory_ids)
    references: list[dict[str, Any]] = []
    seen_data_ids: set[str] = set()

    for node_id in edge_node_ids(edges):
        data_id = node_to_data_id.get(node_id)
        if (
            not data_id
            or data_id in seen_data_ids
            or data_id not in data_id_to_reference
        ):
            continue
        reference = dict(data_id_to_reference[data_id])
        reference["retrieval_rank"] = len(references) + 1
        references.append(reference)
        seen_data_ids.add(data_id)

    return references


async def relationship_edges_for_references(
    dataset_id: UUID,
    references: list[dict[str, Any]],
) -> dict[str, list[dict[str, Any]]]:
    from cognee.infrastructure.databases.graph import get_graph_engine

    graph_engine = await get_graph_engine()
    relationships = {"contradicts", "supersedes", "superseded_by"}
    by_reference: dict[str, list[dict[str, Any]]] = {}
    for reference in references:
        reference_key = f"{reference['claim_id']}:{reference['kind']}"
        reference_edges: list[dict[str, Any]] = []
        for node in await ledger_nodes(dataset_id, UUID(reference["data_id"])):
            graph_edges = await graph_engine.get_edges(str(node.slug))
            for source_node, relationship_name, target_node in graph_edges:
                if relationship_name in relationships:
                    reference_edges.append(
                        {
                            "source_node": source_node,
                            "relationship_name": relationship_name,
                            "target_node": target_node,
                            "origin": "graph_engine.get_edges",
                        }
                    )
            for ledger_edge in await ledger_edges_for_node(
                dataset_id, node.slug, relationships
            ):
                reference_edges.append(
                    {
                        "source_node_id": str(ledger_edge.source_node_id),
                        "destination_node_id": str(ledger_edge.destination_node_id),
                        "relationship_name": ledger_edge.relationship_name,
                        "attributes": ledger_edge.attributes or {},
                        "origin": "ledger_edges",
                    }
                )
        by_reference[reference_key] = reference_edges
    return by_reference


def superseded_references(
    references: list[dict[str, Any]],
    reference_edges: dict[str, list[dict[str, Any]]],
) -> list[dict[str, Any]]:
    superseded = []
    for reference in references:
        reference_key = f"{reference['claim_id']}:{reference['kind']}"
        edges = reference_edges.get(reference_key, [])
        for edge in edges:
            relationship_name = edge["relationship_name"]
            attributes = edge.get("attributes") or {}
            reference_data_id = reference["data_id"]
            target_data_id = attributes.get("target_data_id")
            if (
                relationship_name == "supersedes"
                and target_data_id == reference_data_id
            ):
                superseded.append(
                    {
                        "reference": reference,
                        "edge": edge,
                        "basis": attributes.get("basis") or attributes.get("rationale"),
                    }
                )
            elif (
                relationship_name in {"contradicts", "superseded_by"}
                and target_data_id == reference_data_id
            ):
                superseded.append(
                    {
                        "reference": reference,
                        "edge": edge,
                        "basis": attributes.get("basis") or attributes.get("rationale"),
                    }
                )
    return superseded


def graph_elements_from_edges(edges: list[Any]) -> dict[str, list[str]] | None:
    node_ids = edge_node_ids(edges)
    edge_ids = sorted(
        {
            str(edge.attributes["edge_object_id"])
            for edge in edges
            if getattr(edge, "attributes", None)
            and edge.attributes.get("edge_object_id") is not None
        }
    )
    graph_elements: dict[str, list[str]] = {}
    if node_ids:
        graph_elements["node_ids"] = sorted(node_ids)
    if edge_ids:
        graph_elements["edge_ids"] = edge_ids
    return graph_elements or None


def compact_graph_search(results: list[dict[str, Any]]) -> list[dict[str, Any]]:
    compacted = []
    for result in results:
        edges = result.get("objects_result") or []
        compacted.append(
            {
                "dataset_id": str(result.get("dataset_id")),
                "dataset_name": result.get("dataset_name"),
                "context_result": result.get("context_result"),
                "edge_count": len(edges),
                "node_ids": edge_node_ids(edges),
            }
        )
    return compacted


def reference_ids(references: list[dict[str, Any]]) -> list[str]:
    return [f"{reference['claim_id']}:{reference['kind']}" for reference in references]


def rank_graph_references(
    question: str,
    references: list[dict[str, Any]],
    claims: list[dict[str, Any]],
    *,
    limit: int = 5,
) -> list[dict[str, Any]]:
    claims_by_id = {claim["claim_id"]: claim for claim in claims}
    ranked = []
    scored = []
    for index, reference in enumerate(references):
        claim = claims_by_id.get(reference["claim_id"])
        relevance_score = score_claim(question, claim) if claim else 0
        item = {
            **reference,
            "graph_retrieval_rank": reference.get("retrieval_rank"),
            "graph_relevance_score": relevance_score,
            "score": relevance_score,
        }
        scored.append(item)
        if relevance_score > 0:
            ranked.append((relevance_score, index, item))

    if not ranked:
        return scored[:limit]

    ranked.sort(key=lambda item: (-item[0], item[1]))
    return [item for _, _, item in ranked[:limit]]


async def synthesized_recall(
    cognee: Any,
    question: str,
    dataset: str,
    *,
    session_id: str | None,
    feedback_influence: float,
) -> str:
    results = await cognee.recall(
        question,
        datasets=[dataset],
        include_references=True,
        only_context=False,
        auto_route=False,
        scope="graph",
        session_id=session_id,
        top_k=5,
        wide_search_top_k=10,
        feedback_influence=feedback_influence,
    )
    return recall_text(results).strip()


def answer_text(
    dataset_name: str,
    references: list[dict[str, Any]],
    synthesized_text: str | None = None,
    superseded: list[dict[str, Any]] | None = None,
) -> str:
    if not references:
        return "No matching remembered source was found for this question."

    if superseded:
        first = superseded[0]
        reference = first["reference"]
        relationship = first["edge"]["relationship_name"]
        state = "superseded" if relationship == "supersedes" else "conflicted"
        basis = first.get("basis") or "a graph supersession edge"
        warning = (
            f"{dataset_name} retrieved {reference['doi']}, but the graph marks that "
            f"source as {state} via `{relationship}`. Basis: {basis}"
        )
        if synthesized_text:
            return f"{synthesized_text}\n\n{warning}"
        return warning

    if synthesized_text:
        return synthesized_text

    cited_retracted = [reference for reference in references if reference["retracted"]]
    notices = [
        reference
        for reference in references
        if reference["kind"] == "retraction_notice"
    ]
    primary = references[0]

    if cited_retracted:
        cited = cited_retracted[0]
        return (
            f"{dataset_name} still cites the retracted original source "
            f"{cited['doi']} from {cited['source']}. Treat the answer as unsafe until "
            "that source is forgotten."
        )

    if notices:
        notice = notices[0]
        return (
            f"{dataset_name} no longer cites the original retracted claim for "
            f"{notice['doi']}. The active memory cites the retraction notice instead."
        )

    return (
        f"{dataset_name} cites an active remembered source for {primary['doi']} "
        f"from {primary['source']}."
    )


async def answer(
    question: str,
    dataset: str,
    *,
    registry_path: Path = CLAIMS_PATH,
    session_id: str | None = None,
    record_session: bool = True,
    feedback_influence: float = 0.0,
    synthesize: bool = False,
) -> dict[str, Any]:
    cognee = import_cognee()
    from cognee.modules.search.types import SearchType

    search_results = await cognee.search(
        question,
        query_type=SearchType.GRAPH_COMPLETION,
        datasets=[dataset],
        only_context=True,
        verbose=True,
        top_k=10,
        wide_search_top_k=20,
        feedback_influence=feedback_influence,
    )
    resolved_dataset_id = UUID(str(search_results[0]["dataset_id"]))
    edges = search_results[0].get("objects_result") or []
    claims = load_claims(registry_path)
    memory_ids = await memory_data_ids(resolved_dataset_id)
    deterministic_references = select_references(
        question,
        dataset,
        claims,
        memory_ids,
    )
    raw_graph_references = await references_from_graph_edges(
        resolved_dataset_id,
        dataset,
        claims,
        memory_ids,
        edges,
    )
    references = rank_graph_references(question, raw_graph_references, claims)
    synthesized_text = (
        await synthesized_recall(
            cognee,
            question,
            dataset,
            session_id=session_id,
            feedback_influence=feedback_influence,
        )
        if synthesize
        else None
    )
    retracted_dois = sorted(
        {reference["doi"] for reference in references if reference["retracted"]}
    )
    graph_elements = graph_elements_from_edges(edges)
    recall_context = str(search_results[0].get("context_result") or "")
    reference_cross_check = {
        "retrieved_graph_references": reference_ids(raw_graph_references),
        "ranked_graph_references": reference_ids(references),
        "deterministic_membership_references": reference_ids(deterministic_references),
        "disagreement": reference_ids(raw_graph_references)
        != reference_ids(deterministic_references),
    }
    reference_edges = await relationship_edges_for_references(
        resolved_dataset_id, references
    )
    superseded = superseded_references(references, reference_edges)
    superseded_dois = sorted(
        {
            item["reference"]["doi"]
            for item in superseded
            if item["reference"].get("doi")
        }
    )
    payload = {
        "question": question,
        "dataset": dataset,
        "dataset_id": str(resolved_dataset_id),
        "text": answer_text(dataset, references, synthesized_text, superseded),
        "references": references,
        "raw_graph_references": raw_graph_references,
        "reference_edges": reference_edges,
        "deterministic_references": deterministic_references,
        "reference_cross_check": reference_cross_check,
        "cites_retracted": bool(retracted_dois),
        "cites_by_state": cites_by_state(references),
        "cites_superseded": bool(superseded_dois),
        "superseded_dois": superseded_dois,
        "superseded_references": superseded,
        "retracted_dois": retracted_dois,
        "recall_mode": "GRAPH_COMPLETION only_context=True verbose graph references",
        "synthesis_mode": (
            "GRAPH_COMPLETION only_context=False include_references=True"
            if synthesize
            else "disabled_deterministic_benchmark"
        ),
        "feedback_influence": feedback_influence,
        "session_id": session_id,
        "qa_id": None,
        "used_graph_element_ids": graph_elements,
        "recall_output": compact_graph_search(search_results),
        "recall_context": recall_context,
    }
    if session_id and record_session:
        session_result = await cognee.remember(
            cognee.QAEntry(
                question=question,
                context=payload["recall_context"],
                answer=payload["text"],
                used_graph_element_ids=graph_elements,
            ),
            dataset_name=dataset,
            session_id=session_id,
        )
        payload["qa_id"] = session_result.entry_id
        payload["session_status"] = session_result.status

    json.dumps(payload, default=str)
    return payload
