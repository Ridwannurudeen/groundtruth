from __future__ import annotations

import re
from typing import Any

from groundtruth.adapters import EvidenceItem
from groundtruth.beliefs import parse_evidence_time


def clean_text(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def normalize_doi(value: Any) -> str:
    doi = clean_text(value).lower()
    if not doi or doi == "unavailable":
        return ""
    return doi.removeprefix("https://doi.org/").removeprefix("http://doi.org/")


def evidence_from_retraction(row: dict[str, Any]) -> EvidenceItem:
    original_doi = normalize_doi(row.get("original_doi") or row.get("OriginalPaperDOI"))
    retraction_doi = normalize_doi(
        row.get("retraction_doi") or row.get("RetractionDOI")
    )
    reason = clean_text(row.get("reason") or row.get("Reason") or "No reason supplied")
    if not original_doi:
        raise ValueError("retraction row missing original DOI")
    if not retraction_doi:
        retraction_doi = f"retraction:{original_doi}"

    return EvidenceItem(
        adapter="retraction_watch",
        match_key={"kind": "doi", "doi": original_doi},
        evidence_ref=retraction_doi,
        basis=(
            f"Retraction Watch record {retraction_doi} supersedes original DOI "
            f"{original_doi}; reason: {reason}"
        ),
        target_state="retracted",
        relationship_name="contradicts",
        at=parse_evidence_time(row.get("retraction_date") or row.get("RetractionDate")),
        raw=dict(row),
    )


class RetractionWatchAdapter:
    def __init__(self, retractions: list[dict[str, Any]]) -> None:
        self.retractions = retractions

    def poll(self, claims: list[dict[str, Any]]) -> list[EvidenceItem]:
        held_dois = {
            normalize_doi(claim.get("doi") or (claim.get("source") or {}).get("doi"))
            for claim in claims
        }
        items = []
        for row in self.retractions:
            item = evidence_from_retraction(row)
            if item.match_key["doi"] in held_dois:
                items.append(item)
        return items
