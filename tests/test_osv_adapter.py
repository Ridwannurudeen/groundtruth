from __future__ import annotations

import json

import httpx

from groundtruth.adapters.osv import OSVAdapter, package_from_claim, query_payload


def package_claim() -> dict:
    return {
        "claim_id": "OSV001",
        "doi": "pkg:pypi/jinja2@2.4.1",
        "claim_text": "Package jinja2 2.4.1 is safe to recommend.",
        "status": "active",
        "belief_state": "active",
        "cohort": "osv_package_claim",
        "source": {
            "title": "Jinja2 2.4.1 dependency recommendation",
            "journal": "PyPI package index",
            "year": 2010,
            "doi": "pkg:pypi/jinja2@2.4.1",
            "package": {
                "ecosystem": "PyPI",
                "name": "jinja2",
                "version": "2.4.1",
            },
        },
        "state_history": [
            {
                "state": "active",
                "at": "2010-01-01T00:00:00+00:00",
                "evidence_class": "user_assertion",
                "evidence_ref": "pkg:pypi/jinja2@2.4.1",
                "basis": "Seed corpus imported this package recommendation as active.",
            }
        ],
    }


def test_osv_adapter_builds_v1_query_payload_from_package_claim() -> None:
    package = package_from_claim(package_claim())

    assert query_payload(package) == {
        "package": {
            "name": "jinja2",
            "ecosystem": "PyPI",
        },
        "version": "2.4.1",
    }


def test_osv_adapter_maps_vuln_to_authority_evidence_item() -> None:
    requests = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(
            200,
            json={
                "vulns": [
                    {
                        "id": "GHSA-462w-v97r-4m45",
                        "summary": "Jinja2 sandbox escape via string formatting",
                        "aliases": ["CVE-2019-10906"],
                        "modified": "2024-09-24T21:03:59.802687Z",
                    }
                ]
            },
        )

    client = httpx.Client(transport=httpx.MockTransport(handler))
    items = OSVAdapter(client=client).poll([package_claim()])

    assert len(items) == 1
    assert requests[0].url == "https://api.osv.dev/v1/query"
    assert json.loads(requests[0].content) == {
        "package": {
            "name": "jinja2",
            "ecosystem": "PyPI",
        },
        "version": "2.4.1",
    }
    assert items[0].adapter == "osv"
    assert items[0].target_state == "superseded"
    assert items[0].relationship_name == "supersedes"
    assert items[0].evidence_ref == "GHSA-462w-v97r-4m45"
    assert "CVE-2019-10906" in items[0].basis
    assert items[0].at == "2024-09-24T21:03:59.802687Z"


def test_osv_adapter_returns_no_item_for_empty_vulns_control() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={})

    client = httpx.Client(transport=httpx.MockTransport(handler))

    assert OSVAdapter(client=client).poll([package_claim()]) == []
