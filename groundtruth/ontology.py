from __future__ import annotations

from typing import Literal

from groundtruth.runtime import configure_runtime, restore_runtime_env, snapshot_runtime_env


configure_runtime()
_env_snapshot = snapshot_runtime_env()

from cognee.low_level import DataPoint  # noqa: E402

restore_runtime_env(_env_snapshot)


class Source(DataPoint):
    name: str
    source_type: Literal["journal", "retraction_notice"]
    metadata: dict = {
        "index_fields": ["name"],
        "identity_fields": ["name", "source_type"],
    }


class ScientificClaim(DataPoint):
    text: str
    doi: str
    journal: str
    year: int
    status: str
    made_by: Source
    supersedes_doi: str | None = None
    metadata: dict = {
        "index_fields": ["text", "doi"],
        "identity_fields": ["doi"],
    }


CLAIM_EXTRACTION_PROMPT = """
Extract one ScientificClaim from the text. Use the source DOI as doi, the source
journal as journal, the source year as year, and status as written in the text.
The made_by source must use the journal name. Use source_type="journal" for
paper sources and source_type="retraction_notice" for retraction notices.
Keep the claim text concrete and faithful to the provided claim.
"""
