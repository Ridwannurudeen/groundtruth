from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any
from uuid import UUID

from groundtruth.contradictions import ledger_nodes, memory_data_ids
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
    is_retracted_original = kind == "original_claim" and str(claim["status"]).startswith(
        "retracted"
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
        "retracted": is_retracted_original,
        "score": score,
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


async def used_graph_element_ids(
    dataset_id: UUID,
    references: list[dict[str, Any]],
) -> dict[str, list[str]] | None:
    node_ids: set[str] = set()
    for reference in references:
        for node in await ledger_nodes(dataset_id, UUID(reference["data_id"])):
            node_ids.add(str(node.slug))

    if not node_ids:
        return None
    return {"node_ids": sorted(node_ids)}


def answer_text(dataset_name: str, references: list[dict[str, Any]]) -> str:
    if not references:
        return "No matching remembered source was found for this question."

    cited_retracted = [reference for reference in references if reference["retracted"]]
    notices = [reference for reference in references if reference["kind"] == "retraction_notice"]
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
) -> dict[str, Any]:
    cognee = import_cognee()
    resolved_dataset_id = await dataset_id(cognee, dataset)
    recall_results = await cognee.recall(
        question,
        datasets=[dataset],
        include_references=True,
        only_context=True,
        auto_route=False,
        scope="graph",
        session_id=session_id,
        top_k=10,
        wide_search_top_k=20,
        feedback_influence=feedback_influence,
    )
    claims = load_claims(registry_path)
    references = select_references(
        question,
        dataset,
        claims,
        await memory_data_ids(resolved_dataset_id),
    )
    retracted_dois = sorted(
        {reference["doi"] for reference in references if reference["retracted"]}
    )
    graph_elements = await used_graph_element_ids(resolved_dataset_id, references)
    payload = {
        "question": question,
        "dataset": dataset,
        "dataset_id": str(resolved_dataset_id),
        "text": answer_text(dataset, references),
        "references": references,
        "cites_retracted": bool(retracted_dois),
        "retracted_dois": retracted_dois,
        "recall_mode": "GRAPH_COMPLETION only_context=True",
        "feedback_influence": feedback_influence,
        "session_id": session_id,
        "qa_id": None,
        "used_graph_element_ids": graph_elements,
        "recall_output": compact_recall(recall_results),
        "recall_context": recall_text(recall_results),
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
