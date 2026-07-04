from __future__ import annotations

from typing import Any

import httpx

from groundtruth.adapters import EvidenceItem


OSV_QUERY_URL = "https://api.osv.dev/v1/query"
OSV_VULNERABILITY_URL = "https://osv.dev/vulnerability"


def package_from_claim(claim: dict[str, Any]) -> dict[str, str] | None:
    package = (claim.get("source") or {}).get("package") or claim.get("package")
    if not package:
        return None
    required = ("ecosystem", "name", "version")
    if not all(package.get(field) for field in required):
        return None
    return {field: str(package[field]) for field in required}


def package_match_key(package: dict[str, str]) -> dict[str, str]:
    return {
        "kind": "package_version",
        "ecosystem": package["ecosystem"],
        "name": package["name"],
        "version": package["version"],
    }


def query_payload(package: dict[str, str]) -> dict[str, Any]:
    return {
        "package": {
            "name": package["name"],
            "ecosystem": package["ecosystem"],
        },
        "version": package["version"],
    }


def vuln_alias_text(vuln: dict[str, Any]) -> str:
    aliases = [str(alias) for alias in vuln.get("aliases", []) if alias]
    cves = [alias for alias in aliases if alias.startswith("CVE-")]
    if cves:
        return " / ".join(cves)
    return " / ".join(aliases)


def evidence_from_vuln(
    package: dict[str, str],
    vuln: dict[str, Any],
    *,
    raw_result: dict[str, Any],
) -> EvidenceItem:
    osv_id = str(vuln["id"])
    alias_text = vuln_alias_text(vuln)
    label = f"{osv_id} / {alias_text}" if alias_text else osv_id
    summary = str(vuln.get("summary") or "OSV advisory affects this package")
    return EvidenceItem(
        adapter="osv",
        match_key=package_match_key(package),
        evidence_ref=osv_id,
        basis=(
            f"OSV advisory {label} affects {package['ecosystem']} "
            f"{package['name']} {package['version']}: {summary}"
        ),
        target_state="superseded",
        relationship_name="supersedes",
        at=vuln.get("modified") or vuln.get("published"),
        raw={
            "osv_url": f"{OSV_VULNERABILITY_URL}/{osv_id}",
            "package": package,
            "vulnerability": vuln,
            "result_vuln_count": len(raw_result.get("vulns") or []),
        },
    )


class OSVAdapter:
    def __init__(
        self,
        *,
        client: httpx.Client | None = None,
        api_url: str = OSV_QUERY_URL,
    ) -> None:
        self.client = client or httpx.Client(timeout=30.0)
        self.api_url = api_url

    def query(self, package: dict[str, str]) -> dict[str, Any]:
        response = self.client.post(self.api_url, json=query_payload(package))
        response.raise_for_status()
        return response.json()

    def poll(self, claims: list[dict[str, Any]]) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        for claim in claims:
            package = package_from_claim(claim)
            if package is None:
                continue
            result = self.query(package)
            vulns = sorted(
                result.get("vulns") or [],
                key=lambda vuln: str(vuln.get("id") or ""),
            )
            if vulns:
                items.append(
                    evidence_from_vuln(
                        package,
                        vulns[0],
                        raw_result=result,
                    )
                )
        return items
