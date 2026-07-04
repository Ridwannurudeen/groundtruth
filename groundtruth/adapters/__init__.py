from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol


@dataclass(frozen=True)
class EvidenceItem:
    adapter: str
    match_key: dict[str, str]
    evidence_ref: str
    basis: str
    target_state: str
    relationship_name: str
    at: str | None = None
    evidence_class: str = "authority_feed"
    raw: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.evidence_class != "authority_feed":
            raise ValueError("authority adapters must emit authority_feed evidence")
        if not self.match_key:
            raise ValueError("match_key is required")
        if not self.evidence_ref:
            raise ValueError("evidence_ref is required")
        if not self.basis:
            raise ValueError("basis is required")
        if not self.target_state:
            raise ValueError("target_state is required")
        if not self.relationship_name:
            raise ValueError("relationship_name is required")

    def to_dict(self) -> dict[str, Any]:
        return {
            "adapter": self.adapter,
            "match_key": self.match_key,
            "evidence_class": self.evidence_class,
            "evidence_ref": self.evidence_ref,
            "basis": self.basis,
            "target_state": self.target_state,
            "relationship_name": self.relationship_name,
            "at": self.at,
            "raw": self.raw,
        }


class AuthorityAdapter(Protocol):
    def poll(self, claims: list[dict[str, Any]]) -> list[EvidenceItem]:
        ...
