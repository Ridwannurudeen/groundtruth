from __future__ import annotations

import argparse
import json
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from groundtruth.adapters import EvidenceItem
from groundtruth.adapters.osv import OSVAdapter, package_from_claim
from groundtruth.adapters.retraction_watch import evidence_from_retraction, normalize_doi
from groundtruth.beliefs import latest_state_change, migrate_claim_belief, transition_belief
from groundtruth.registry import write_json
from groundtruth.runtime import DATA_DIR, DOCS_DIR


OSV_SEED_CORPUS_PATH = DATA_DIR / "osv_seed_corpus.json"
OSV_CVE_RUN_PATH = DATA_DIR / "osv_cve_run.json"
RESULTS_V3_P5_PATH = DOCS_DIR / "RESULTS-V3-P5.md"
DEFAULT_QUESTION = "Should our coding agent recommend jinja2 2.4.1?"
OSV_DOCS = {
    "api": "https://google.github.io/osv.dev/api/",
    "query": "https://google.github.io/osv.dev/post-v1-query/",
}


SEED_PACKAGES = [
    {
        "ecosystem": "PyPI",
        "name": "jinja2",
        "version": "2.4.1",
        "year": 2010,
    },
    {
        "ecosystem": "PyPI",
        "name": "PyYAML",
        "version": "5.3.1",
        "year": 2020,
    },
    {
        "ecosystem": "PyPI",
        "name": "urllib3",
        "version": "1.26.5",
        "year": 2021,
    },
    {
        "ecosystem": "npm",
        "name": "lodash",
        "version": "4.17.20",
        "year": 2020,
    },
    {
        "ecosystem": "npm",
        "name": "minimist",
        "version": "0.0.8",
        "year": 2013,
    },
    {
        "ecosystem": "PyPI",
        "name": "packaging",
        "version": "24.2",
        "year": 2024,
    },
    {
        "ecosystem": "PyPI",
        "name": "click",
        "version": "8.1.8",
        "year": 2024,
    },
    {
        "ecosystem": "PyPI",
        "name": "six",
        "version": "1.17.0",
        "year": 2024,
    },
    {
        "ecosystem": "PyPI",
        "name": "h11",
        "version": "0.16.0",
        "year": 2025,
    },
    {
        "ecosystem": "npm",
        "name": "is-number",
        "version": "7.0.0",
        "year": 2018,
    },
]


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def purl(package: dict[str, Any]) -> str:
    ecosystem = str(package["ecosystem"])
    purl_ecosystem = "pypi" if ecosystem == "PyPI" else ecosystem.lower()
    return f"pkg:{purl_ecosystem}/{package['name']}@{package['version']}"


def package_claim(package: dict[str, Any], index: int) -> dict[str, Any]:
    package_ref = purl(package)
    registry_name = (
        "PyPI package index"
        if package["ecosystem"] == "PyPI"
        else f"{package['ecosystem']} package registry"
    )
    return migrate_claim_belief(
        {
            "claim_id": f"OSV{index:03d}",
            "doi": package_ref,
            "claim_text": (
                f"Package {package['name']} {package['version']} is safe to "
                "recommend for new software projects."
            ),
            "source": {
                "title": (
                    f"{package['name']} {package['version']} dependency "
                    "recommendation"
                ),
                "journal": registry_name,
                "year": package["year"],
                "doi": package_ref,
                "package": {
                    "ecosystem": package["ecosystem"],
                    "name": package["name"],
                    "version": package["version"],
                },
            },
            "status": "active",
            "cohort": "osv_package_claim",
        }
    )


def build_osv_seed_corpus() -> list[dict[str, Any]]:
    return [package_claim(package, index) for index, package in enumerate(SEED_PACKAGES, 1)]


def load_or_create_osv_claims(path: Path = OSV_SEED_CORPUS_PATH) -> list[dict[str, Any]]:
    claims = build_osv_seed_corpus()
    write_json(path, claims)
    return claims


def claim_matches(claim: dict[str, Any], match_key: dict[str, str]) -> bool:
    if match_key.get("kind") == "doi":
        claim_doi = claim.get("doi") or (claim.get("source") or {}).get("doi")
        return normalize_doi(claim_doi) == normalize_doi(match_key.get("doi"))

    if match_key.get("kind") != "package_version":
        return False
    package = package_from_claim(claim)
    if package is None:
        return False
    return (
        package["ecosystem"] == match_key.get("ecosystem")
        and package["name"].lower() == str(match_key.get("name") or "").lower()
        and package["version"] == match_key.get("version")
    )


def transition_once(
    claim: dict[str, Any],
    evidence: EvidenceItem,
) -> dict[str, Any]:
    migrated = migrate_claim_belief(claim)
    latest = latest_state_change(migrated)
    if (
        latest["state"] == evidence.target_state
        and latest["evidence_class"] == evidence.evidence_class
        and latest["evidence_ref"] == evidence.evidence_ref
        and latest["basis"] == evidence.basis
    ):
        claim.update(migrated)
        return claim

    transition_belief(
        migrated,
        evidence.target_state,
        evidence.evidence_class,
        evidence.evidence_ref,
        evidence.basis,
        at=evidence.at,
    )
    migrated["status"] = evidence.target_state
    claim.update(migrated)
    return claim


def process_authority_evidence(
    registry: list[dict[str, Any]],
    evidence: EvidenceItem,
) -> dict[str, Any]:
    matched_claims = []
    for claim in registry:
        if not claim_matches(claim, evidence.match_key):
            continue
        before = deepcopy(migrate_claim_belief(claim))
        transition_once(claim, evidence)
        after = migrate_claim_belief(claim)
        matched_claims.append(
            {
                "claim_id": claim["claim_id"],
                "before": latest_state_change(before),
                "after": latest_state_change(after),
                "belief_state": after["belief_state"],
            }
        )

    return {
        "evidence": evidence.to_dict(),
        "matched_claim_ids": [item["claim_id"] for item in matched_claims],
        "matched_claims": matched_claims,
        "status": "applied" if matched_claims else "no_match",
    }


def apply_evidence_items(
    registry: list[dict[str, Any]],
    evidence_items: list[EvidenceItem],
) -> list[dict[str, Any]]:
    return [process_authority_evidence(registry, item) for item in evidence_items]


def package_question_matches(question: str, claim: dict[str, Any]) -> bool:
    package = package_from_claim(claim)
    if package is None:
        return False
    lowered = question.lower()
    return package["name"].lower() in lowered and package["version"].lower() in lowered


def answer_package_question(
    question: str,
    claims: list[dict[str, Any]],
) -> dict[str, Any]:
    references = [
        migrate_claim_belief(claim)
        for claim in claims
        if package_question_matches(question, claim)
    ]
    if not references:
        return {
            "question": question,
            "text": "No matching package recommendation was found.",
            "references": [],
        }

    primary = references[0]
    package = package_from_claim(primary)
    latest = latest_state_change(primary)
    package_label = f"{package['ecosystem']} {package['name']} {package['version']}"
    if primary["belief_state"] == "superseded":
        text = (
            f"GroundTruth no longer recommends {package_label}. "
            f"Authority evidence `{latest['evidence_ref']}` superseded the safe "
            f"recommendation. Basis: {latest['basis']}"
        )
    else:
        text = (
            f"GroundTruth still treats {package_label} as an active safe "
            "recommendation."
        )
    return {
        "question": question,
        "text": text,
        "references": [
            {
                "claim_id": primary["claim_id"],
                "package": package,
                "belief_state": primary["belief_state"],
                "latest_state_change": latest,
            }
        ],
    }


def run_osv_adapter(claims: list[dict[str, Any]]) -> list[EvidenceItem]:
    return OSVAdapter().poll(claims)


def demo_retraction_claim() -> dict[str, Any]:
    return migrate_claim_belief(
        {
            "claim_id": "RW-DEMO",
            "doi": "10.5555/demo-original",
            "claim_text": "The paper claimed that a demo intervention works.",
            "source": {
                "doi": "10.5555/demo-original",
                "journal": "Journal of Demo Medicine",
                "title": "A demo intervention works",
                "year": 2020,
            },
            "status": "active",
            "cohort": "adapter_protocol_demo",
        }
    )


def shared_engine_demo(osv_item: EvidenceItem | None) -> dict[str, Any]:
    registry = [demo_retraction_claim(), package_claim(SEED_PACKAGES[0], 1)]
    retraction_item = evidence_from_retraction(
        {
            "original_doi": "10.5555/demo-original",
            "retraction_doi": "10.5555/demo-retraction",
            "retraction_date": "2026-07-04",
            "reason": "Adapter protocol demonstration.",
        }
    )
    results = [process_authority_evidence(registry, retraction_item)]
    if osv_item is not None:
        results.append(process_authority_evidence(registry, osv_item))
    return {
        "registry": registry,
        "results": results,
        "adapters": [result["evidence"]["adapter"] for result in results],
    }


def scripted_run(question: str = DEFAULT_QUESTION) -> dict[str, Any]:
    seed_claims = load_or_create_osv_claims()
    claims = deepcopy(seed_claims)
    before = answer_package_question(question, claims)
    evidence_items = run_osv_adapter(claims)
    state_changes = apply_evidence_items(claims, evidence_items)
    after = answer_package_question(question, claims)
    protocol_demo = shared_engine_demo(evidence_items[0] if evidence_items else None)
    return {
        "generated_at": now(),
        "status": "complete_live_osv_authority_adapter",
        "provider_policy": (
            "OSV adapter uses keyless OSV.dev HTTP API only; no LLM provider, "
            "Cognee provider, Azure, or Groq calls are used."
        ),
        "osv_docs": OSV_DOCS,
        "question": question,
        "before": before,
        "after": after,
        "evidence_items": [item.to_dict() for item in evidence_items],
        "state_changes": state_changes,
        "shared_engine_demo": protocol_demo,
        "seed_claims": seed_claims,
        "claims": claims,
        "summary": {
            "claims": len(claims),
            "evidence_items": len(evidence_items),
            "superseded_claims": sum(
                1 for claim in claims if claim.get("belief_state") == "superseded"
            ),
            "active_claims": sum(
                1 for claim in claims if claim.get("belief_state") == "active"
            ),
        },
    }


def render_results_markdown(run: dict[str, Any]) -> str:
    lines = [
        "# GroundTruth V3 P5 Results",
        "",
        f"Generated: {run['generated_at']}",
        f"Status: `{run['status']}`",
        "",
        "## Gate",
        "",
        "- Retraction Watch and OSV both emit normalized `EvidenceItem` records.",
        "- The same authority engine applies adapter evidence into claim `state_history`.",
        "- The CVE vertical uses OSV.dev package/version authority evidence; no LLM/provider calls are used.",
        "",
        "## Command",
        "",
        "```powershell",
        ".\\.venv\\Scripts\\python.exe -m groundtruth.p5 --results-v3-p5",
        "```",
        "",
        "## OSV Source",
        "",
        f"- API docs: {run['osv_docs']['api']}",
        f"- Package/version query docs: {run['osv_docs']['query']}",
        "",
        "## CVE Transcript",
        "",
        "### Before",
        "",
        "```text",
        run["before"]["text"],
        "```",
        "",
        "### After",
        "",
        "```text",
        run["after"]["text"],
        "```",
        "",
        "## Adapter Evidence",
        "",
    ]
    for item in run["evidence_items"]:
        package = item["match_key"]
        lines.extend(
            [
                (
                    f"- `{item['adapter']}` `{item['evidence_ref']}` -> "
                    f"`{item['target_state']}` for "
                    f"`{package.get('ecosystem')}:{package.get('name')}@{package.get('version')}`"
                ),
                f"  - Basis: {item['basis']}",
            ]
        )
    if not run["evidence_items"]:
        lines.append("- None.")
    protocol_demo = run.get("shared_engine_demo") or {}
    demo_adapters = protocol_demo.get("adapters") or []
    lines.extend(
        [
            "",
            "## Shared Engine Adapter Check",
            "",
            (
                "- Adapters processed through `process_authority_evidence`: "
                f"{', '.join(f'`{adapter}`' for adapter in demo_adapters) or 'none'}."
            ),
        ]
    )
    lines.extend(
        [
            "",
            "## Summary",
            "",
            f"- Claims: {run['summary']['claims']}",
            f"- Evidence items: {run['summary']['evidence_items']}",
            f"- Superseded claims: {run['summary']['superseded_claims']}",
            f"- Active claims: {run['summary']['active_claims']}",
            "",
            "## Raw Run",
            "",
            "```json",
            json.dumps(run, indent=2, sort_keys=True),
            "```",
            "",
            "## Verification So Far",
            "",
            "- Run focused tests, static checks, and the full suite after generation; committed results record the final outputs.",
            "",
        ]
    )
    return "\n".join(lines)


def write_artifacts(
    run: dict[str, Any],
    *,
    cve_run_path: Path = OSV_CVE_RUN_PATH,
    results_path: Path = RESULTS_V3_P5_PATH,
) -> None:
    write_json(cve_run_path, run)
    results_path.write_text(render_results_markdown(run), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="GroundTruth V3 P5 authority adapters")
    parser.add_argument("--question", default=DEFAULT_QUESTION)
    parser.add_argument(
        "--results-v3-p5",
        action="store_true",
        help="Write data/osv_cve_run.json, data/osv_seed_corpus.json, and docs/RESULTS-V3-P5.md.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    run = scripted_run(args.question)
    if args.results_v3_p5:
        write_artifacts(run)
        print(f"Wrote {OSV_SEED_CORPUS_PATH}")
        print(f"Wrote {OSV_CVE_RUN_PATH}")
        print(f"Wrote {RESULTS_V3_P5_PATH}")
    print(json.dumps(run, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
