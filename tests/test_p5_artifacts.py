from __future__ import annotations

import json

from groundtruth.p5 import OSV_DOCS, render_results_markdown, write_artifacts


def sample_run() -> dict:
    return {
        "generated_at": "2026-07-04T00:00:00+00:00",
        "status": "complete_live_osv_authority_adapter",
        "osv_docs": OSV_DOCS,
        "question": "Should our coding agent recommend jinja2 2.4.1?",
        "before": {
            "text": "GroundTruth still treats PyPI jinja2 2.4.1 as active.",
            "references": [],
        },
        "after": {
            "text": "GroundTruth no longer recommends PyPI jinja2 2.4.1.",
            "references": [],
        },
        "evidence_items": [
            {
                "adapter": "osv",
                "match_key": {
                    "kind": "package_version",
                    "ecosystem": "PyPI",
                    "name": "jinja2",
                    "version": "2.4.1",
                },
                "evidence_class": "authority_feed",
                "evidence_ref": "GHSA-462w-v97r-4m45",
                "basis": "OSV advisory affects PyPI jinja2 2.4.1.",
                "target_state": "superseded",
                "relationship_name": "supersedes",
                "at": "2024-09-24T21:03:59.802687Z",
                "raw": {},
            }
        ],
        "state_changes": [],
        "claims": [],
        "summary": {
            "claims": 10,
            "evidence_items": 1,
            "superseded_claims": 1,
            "active_claims": 9,
        },
    }


def test_results_v3_p5_artifacts_render_raw_run(tmp_path) -> None:
    run = sample_run()
    cve_run_path = tmp_path / "osv_cve_run.json"
    results_path = tmp_path / "RESULTS-V3-P5.md"

    write_artifacts(run, cve_run_path=cve_run_path, results_path=results_path)

    assert json.loads(cve_run_path.read_text())["summary"]["claims"] == 10
    markdown = results_path.read_text()
    assert "GroundTruth V3 P5 Results" in markdown
    assert "python.exe -m groundtruth.p5 --results-v3-p5" in markdown
    assert "CVE Transcript" in markdown
    assert "Raw Run" in markdown
    assert render_results_markdown(run) == markdown
