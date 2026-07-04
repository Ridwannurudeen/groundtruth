# GroundTruth V3 P5 Results

Generated: 2026-07-04T23:44:34.028111+00:00
Status: `complete_live_osv_authority_adapter`

## Gate

- Retraction Watch and OSV both emit normalized `EvidenceItem` records.
- The same authority engine applies adapter evidence into claim `state_history`.
- The CVE vertical uses OSV.dev package/version authority evidence; no LLM/provider calls are used.

## Command

```powershell
.\.venv\Scripts\python.exe -m groundtruth.p5 --results-v3-p5
```

## OSV Source

- API docs: https://google.github.io/osv.dev/api/
- Package/version query docs: https://google.github.io/osv.dev/post-v1-query/

## CVE Transcript

### Before

```text
GroundTruth still treats PyPI jinja2 2.4.1 as an active safe recommendation.
```

### After

```text
GroundTruth no longer recommends PyPI jinja2 2.4.1. Authority evidence `GHSA-462w-v97r-4m45` superseded the safe recommendation. Basis: OSV advisory GHSA-462w-v97r-4m45 / CVE-2019-10906 affects PyPI jinja2 2.4.1: Jinja2 sandbox escape via string formatting
```

## Adapter Evidence

- `osv` `GHSA-462w-v97r-4m45` -> `superseded` for `PyPI:jinja2@2.4.1`
  - Basis: OSV advisory GHSA-462w-v97r-4m45 / CVE-2019-10906 affects PyPI jinja2 2.4.1: Jinja2 sandbox escape via string formatting
- `osv` `GHSA-8q59-q68h-6hv4` -> `superseded` for `PyPI:PyYAML@5.3.1`
  - Basis: OSV advisory GHSA-8q59-q68h-6hv4 / CVE-2020-14343 affects PyPI PyYAML 5.3.1: Improper Input Validation in PyYAML
- `osv` `GHSA-2xpw-w6gg-jr37` -> `superseded` for `PyPI:urllib3@1.26.5`
  - Basis: OSV advisory GHSA-2xpw-w6gg-jr37 / CVE-2025-66471 affects PyPI urllib3 1.26.5: urllib3 streaming API improperly handles highly compressed data
- `osv` `GHSA-29mw-wpgm-hmr9` -> `superseded` for `npm:lodash@4.17.20`
  - Basis: OSV advisory GHSA-29mw-wpgm-hmr9 / CVE-2020-28500 affects npm lodash 4.17.20: Regular Expression Denial of Service (ReDoS) in lodash
- `osv` `GHSA-vh95-rmgr-6w4m` -> `superseded` for `npm:minimist@0.0.8`
  - Basis: OSV advisory GHSA-vh95-rmgr-6w4m / CVE-2020-7598 affects npm minimist 0.0.8: Prototype Pollution in minimist

## Shared Engine Adapter Check

- Adapters processed through `process_authority_evidence`: `retraction_watch`, `osv`.

## Summary

- Claims: 10
- Evidence items: 5
- Superseded claims: 5
- Active claims: 5

## Raw Run

```json
{
  "after": {
    "question": "Should our coding agent recommend jinja2 2.4.1?",
    "references": [
      {
        "belief_state": "superseded",
        "claim_id": "OSV001",
        "latest_state_change": {
          "at": "2024-09-24T21:03:59.802687Z",
          "basis": "OSV advisory GHSA-462w-v97r-4m45 / CVE-2019-10906 affects PyPI jinja2 2.4.1: Jinja2 sandbox escape via string formatting",
          "evidence_class": "authority_feed",
          "evidence_ref": "GHSA-462w-v97r-4m45",
          "state": "superseded"
        },
        "package": {
          "ecosystem": "PyPI",
          "name": "jinja2",
          "version": "2.4.1"
        }
      }
    ],
    "text": "GroundTruth no longer recommends PyPI jinja2 2.4.1. Authority evidence `GHSA-462w-v97r-4m45` superseded the safe recommendation. Basis: OSV advisory GHSA-462w-v97r-4m45 / CVE-2019-10906 affects PyPI jinja2 2.4.1: Jinja2 sandbox escape via string formatting"
  },
  "before": {
    "question": "Should our coding agent recommend jinja2 2.4.1?",
    "references": [
      {
        "belief_state": "active",
        "claim_id": "OSV001",
        "latest_state_change": {
          "at": "2010-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "pkg:pypi/jinja2@2.4.1",
          "state": "active"
        },
        "package": {
          "ecosystem": "PyPI",
          "name": "jinja2",
          "version": "2.4.1"
        }
      }
    ],
    "text": "GroundTruth still treats PyPI jinja2 2.4.1 as an active safe recommendation."
  },
  "claims": [
    {
      "belief_state": "superseded",
      "claim_id": "OSV001",
      "claim_text": "Package jinja2 2.4.1 is safe to recommend for new software projects.",
      "cohort": "osv_package_claim",
      "doi": "pkg:pypi/jinja2@2.4.1",
      "source": {
        "doi": "pkg:pypi/jinja2@2.4.1",
        "journal": "PyPI package index",
        "package": {
          "ecosystem": "PyPI",
          "name": "jinja2",
          "version": "2.4.1"
        },
        "title": "jinja2 2.4.1 dependency recommendation",
        "year": 2010
      },
      "state_history": [
        {
          "at": "2010-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "pkg:pypi/jinja2@2.4.1",
          "state": "active"
        },
        {
          "at": "2024-09-24T21:03:59.802687Z",
          "basis": "OSV advisory GHSA-462w-v97r-4m45 / CVE-2019-10906 affects PyPI jinja2 2.4.1: Jinja2 sandbox escape via string formatting",
          "evidence_class": "authority_feed",
          "evidence_ref": "GHSA-462w-v97r-4m45",
          "state": "superseded"
        }
      ],
      "status": "superseded"
    },
    {
      "belief_state": "superseded",
      "claim_id": "OSV002",
      "claim_text": "Package PyYAML 5.3.1 is safe to recommend for new software projects.",
      "cohort": "osv_package_claim",
      "doi": "pkg:pypi/PyYAML@5.3.1",
      "source": {
        "doi": "pkg:pypi/PyYAML@5.3.1",
        "journal": "PyPI package index",
        "package": {
          "ecosystem": "PyPI",
          "name": "PyYAML",
          "version": "5.3.1"
        },
        "title": "PyYAML 5.3.1 dependency recommendation",
        "year": 2020
      },
      "state_history": [
        {
          "at": "2020-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "pkg:pypi/PyYAML@5.3.1",
          "state": "active"
        },
        {
          "at": "2026-02-04T03:33:10.792778Z",
          "basis": "OSV advisory GHSA-8q59-q68h-6hv4 / CVE-2020-14343 affects PyPI PyYAML 5.3.1: Improper Input Validation in PyYAML",
          "evidence_class": "authority_feed",
          "evidence_ref": "GHSA-8q59-q68h-6hv4",
          "state": "superseded"
        }
      ],
      "status": "superseded"
    },
    {
      "belief_state": "superseded",
      "claim_id": "OSV003",
      "claim_text": "Package urllib3 1.26.5 is safe to recommend for new software projects.",
      "cohort": "osv_package_claim",
      "doi": "pkg:pypi/urllib3@1.26.5",
      "source": {
        "doi": "pkg:pypi/urllib3@1.26.5",
        "journal": "PyPI package index",
        "package": {
          "ecosystem": "PyPI",
          "name": "urllib3",
          "version": "1.26.5"
        },
        "title": "urllib3 1.26.5 dependency recommendation",
        "year": 2021
      },
      "state_history": [
        {
          "at": "2021-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "pkg:pypi/urllib3@1.26.5",
          "state": "active"
        },
        {
          "at": "2026-02-04T02:36:12.983430Z",
          "basis": "OSV advisory GHSA-2xpw-w6gg-jr37 / CVE-2025-66471 affects PyPI urllib3 1.26.5: urllib3 streaming API improperly handles highly compressed data",
          "evidence_class": "authority_feed",
          "evidence_ref": "GHSA-2xpw-w6gg-jr37",
          "state": "superseded"
        }
      ],
      "status": "superseded"
    },
    {
      "belief_state": "superseded",
      "claim_id": "OSV004",
      "claim_text": "Package lodash 4.17.20 is safe to recommend for new software projects.",
      "cohort": "osv_package_claim",
      "doi": "pkg:npm/lodash@4.17.20",
      "source": {
        "doi": "pkg:npm/lodash@4.17.20",
        "journal": "npm package registry",
        "package": {
          "ecosystem": "npm",
          "name": "lodash",
          "version": "4.17.20"
        },
        "title": "lodash 4.17.20 dependency recommendation",
        "year": 2020
      },
      "state_history": [
        {
          "at": "2020-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "pkg:npm/lodash@4.17.20",
          "state": "active"
        },
        {
          "at": "2025-09-29T21:12:31.102523Z",
          "basis": "OSV advisory GHSA-29mw-wpgm-hmr9 / CVE-2020-28500 affects npm lodash 4.17.20: Regular Expression Denial of Service (ReDoS) in lodash",
          "evidence_class": "authority_feed",
          "evidence_ref": "GHSA-29mw-wpgm-hmr9",
          "state": "superseded"
        }
      ],
      "status": "superseded"
    },
    {
      "belief_state": "superseded",
      "claim_id": "OSV005",
      "claim_text": "Package minimist 0.0.8 is safe to recommend for new software projects.",
      "cohort": "osv_package_claim",
      "doi": "pkg:npm/minimist@0.0.8",
      "source": {
        "doi": "pkg:npm/minimist@0.0.8",
        "journal": "npm package registry",
        "package": {
          "ecosystem": "npm",
          "name": "minimist",
          "version": "0.0.8"
        },
        "title": "minimist 0.0.8 dependency recommendation",
        "year": 2013
      },
      "state_history": [
        {
          "at": "2013-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "pkg:npm/minimist@0.0.8",
          "state": "active"
        },
        {
          "at": "2026-03-13T22:11:31.390433Z",
          "basis": "OSV advisory GHSA-vh95-rmgr-6w4m / CVE-2020-7598 affects npm minimist 0.0.8: Prototype Pollution in minimist",
          "evidence_class": "authority_feed",
          "evidence_ref": "GHSA-vh95-rmgr-6w4m",
          "state": "superseded"
        }
      ],
      "status": "superseded"
    },
    {
      "belief_state": "active",
      "claim_id": "OSV006",
      "claim_text": "Package packaging 24.2 is safe to recommend for new software projects.",
      "cohort": "osv_package_claim",
      "doi": "pkg:pypi/packaging@24.2",
      "source": {
        "doi": "pkg:pypi/packaging@24.2",
        "journal": "PyPI package index",
        "package": {
          "ecosystem": "PyPI",
          "name": "packaging",
          "version": "24.2"
        },
        "title": "packaging 24.2 dependency recommendation",
        "year": 2024
      },
      "state_history": [
        {
          "at": "2024-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "pkg:pypi/packaging@24.2",
          "state": "active"
        }
      ],
      "status": "active"
    },
    {
      "belief_state": "active",
      "claim_id": "OSV007",
      "claim_text": "Package click 8.1.8 is safe to recommend for new software projects.",
      "cohort": "osv_package_claim",
      "doi": "pkg:pypi/click@8.1.8",
      "source": {
        "doi": "pkg:pypi/click@8.1.8",
        "journal": "PyPI package index",
        "package": {
          "ecosystem": "PyPI",
          "name": "click",
          "version": "8.1.8"
        },
        "title": "click 8.1.8 dependency recommendation",
        "year": 2024
      },
      "state_history": [
        {
          "at": "2024-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "pkg:pypi/click@8.1.8",
          "state": "active"
        }
      ],
      "status": "active"
    },
    {
      "belief_state": "active",
      "claim_id": "OSV008",
      "claim_text": "Package six 1.17.0 is safe to recommend for new software projects.",
      "cohort": "osv_package_claim",
      "doi": "pkg:pypi/six@1.17.0",
      "source": {
        "doi": "pkg:pypi/six@1.17.0",
        "journal": "PyPI package index",
        "package": {
          "ecosystem": "PyPI",
          "name": "six",
          "version": "1.17.0"
        },
        "title": "six 1.17.0 dependency recommendation",
        "year": 2024
      },
      "state_history": [
        {
          "at": "2024-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "pkg:pypi/six@1.17.0",
          "state": "active"
        }
      ],
      "status": "active"
    },
    {
      "belief_state": "active",
      "claim_id": "OSV009",
      "claim_text": "Package h11 0.16.0 is safe to recommend for new software projects.",
      "cohort": "osv_package_claim",
      "doi": "pkg:pypi/h11@0.16.0",
      "source": {
        "doi": "pkg:pypi/h11@0.16.0",
        "journal": "PyPI package index",
        "package": {
          "ecosystem": "PyPI",
          "name": "h11",
          "version": "0.16.0"
        },
        "title": "h11 0.16.0 dependency recommendation",
        "year": 2025
      },
      "state_history": [
        {
          "at": "2025-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "pkg:pypi/h11@0.16.0",
          "state": "active"
        }
      ],
      "status": "active"
    },
    {
      "belief_state": "active",
      "claim_id": "OSV010",
      "claim_text": "Package is-number 7.0.0 is safe to recommend for new software projects.",
      "cohort": "osv_package_claim",
      "doi": "pkg:npm/is-number@7.0.0",
      "source": {
        "doi": "pkg:npm/is-number@7.0.0",
        "journal": "npm package registry",
        "package": {
          "ecosystem": "npm",
          "name": "is-number",
          "version": "7.0.0"
        },
        "title": "is-number 7.0.0 dependency recommendation",
        "year": 2018
      },
      "state_history": [
        {
          "at": "2018-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "pkg:npm/is-number@7.0.0",
          "state": "active"
        }
      ],
      "status": "active"
    }
  ],
  "evidence_items": [
    {
      "adapter": "osv",
      "at": "2024-09-24T21:03:59.802687Z",
      "basis": "OSV advisory GHSA-462w-v97r-4m45 / CVE-2019-10906 affects PyPI jinja2 2.4.1: Jinja2 sandbox escape via string formatting",
      "evidence_class": "authority_feed",
      "evidence_ref": "GHSA-462w-v97r-4m45",
      "match_key": {
        "ecosystem": "PyPI",
        "kind": "package_version",
        "name": "jinja2",
        "version": "2.4.1"
      },
      "raw": {
        "osv_url": "https://osv.dev/vulnerability/GHSA-462w-v97r-4m45",
        "package": {
          "ecosystem": "PyPI",
          "name": "jinja2",
          "version": "2.4.1"
        },
        "result_vuln_count": 14,
        "vulnerability": {
          "affected": [
            {
              "database_specific": {
                "source": "https://github.com/github/advisory-database/blob/main/advisories/github-reviewed/2019/04/GHSA-462w-v97r-4m45/GHSA-462w-v97r-4m45.json"
              },
              "package": {
                "ecosystem": "PyPI",
                "name": "jinja2",
                "purl": "pkg:pypi/jinja2"
              },
              "ranges": [
                {
                  "events": [
                    {
                      "introduced": "0"
                    },
                    {
                      "fixed": "2.10.1"
                    }
                  ],
                  "type": "ECOSYSTEM"
                }
              ],
              "versions": [
                "2.0",
                "2.0rc1",
                "2.1",
                "2.1.1",
                "2.10",
                "2.2",
                "2.2.1",
                "2.3",
                "2.3.1",
                "2.4",
                "2.4.1",
                "2.5",
                "2.5.1",
                "2.5.2",
                "2.5.3",
                "2.5.4",
                "2.5.5",
                "2.6",
                "2.7",
                "2.7.1",
                "2.7.2",
                "2.7.3",
                "2.8",
                "2.8.1",
                "2.9",
                "2.9.1",
                "2.9.2",
                "2.9.3",
                "2.9.4",
                "2.9.5",
                "2.9.6"
              ]
            }
          ],
          "aliases": [
            "CVE-2019-10906",
            "PYSEC-2019-217"
          ],
          "database_specific": {
            "cwe_ids": [
              "CWE-693"
            ],
            "github_reviewed": true,
            "github_reviewed_at": "2020-06-16T20:57:35Z",
            "nvd_published_at": "2019-04-07T00:29:00Z",
            "severity": "HIGH"
          },
          "details": "In Pallets Jinja before 2.10.1, `str.format_map` allows a sandbox escape.\n\nThe sandbox is used to restrict what code can be evaluated when rendering untrusted, user-provided templates. Due to the way string formatting works in Python, the `str.format_map` method could be used to escape the sandbox.\n\nThis issue was previously addressed for the `str.format` method in Jinja 2.8.1, which discusses the issue in detail. However, the less-common `str.format_map` method was overlooked. This release applies the same sandboxing to both methods.\n\nIf you cannot upgrade Jinja, you can override the `is_safe_attribute` method on the sandbox and explicitly disallow the `format_map` method on string objects.",
          "id": "GHSA-462w-v97r-4m45",
          "modified": "2024-09-24T21:03:59.802687Z",
          "published": "2019-04-10T14:30:24Z",
          "references": [
            {
              "type": "ADVISORY",
              "url": "https://nvd.nist.gov/vuln/detail/CVE-2019-10906"
            },
            {
              "type": "WEB",
              "url": "https://usn.ubuntu.com/4011-2"
            },
            {
              "type": "WEB",
              "url": "https://usn.ubuntu.com/4011-1"
            },
            {
              "type": "WEB",
              "url": "https://palletsprojects.com/blog/jinja-2-10-1-released"
            },
            {
              "type": "WEB",
              "url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/TS7IVZAJBWOHNRDMFJDIZVFCMRP6YIUQ"
            },
            {
              "type": "WEB",
              "url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/QCDYIS254EJMBNWOG4S5QY6AOTOR4TZU"
            },
            {
              "type": "WEB",
              "url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/DSW3QZMFVVR7YE3UT4YRQA272TYAL5AF"
            },
            {
              "type": "WEB",
              "url": "https://lists.apache.org/thread.html/f0c4a03418bcfe70c539c5dbaf99c04c98da13bfa1d3266f08564316@%3Ccommits.airflow.apache.org%3E"
            },
            {
              "type": "WEB",
              "url": "https://lists.apache.org/thread.html/b2380d147b508bbcb90d2cad443c159e63e12555966ab4f320ee22da@%3Ccommits.airflow.apache.org%3E"
            },
            {
              "type": "WEB",
              "url": "https://lists.apache.org/thread.html/7f39f01392d320dfb48e4901db68daeece62fd60ef20955966739993@%3Ccommits.airflow.apache.org%3E"
            },
            {
              "type": "WEB",
              "url": "https://lists.apache.org/thread.html/57673a78c4d5c870d3f21465c7e2946b9f8285c7c57e54c2ae552f02@%3Ccommits.airflow.apache.org%3E"
            },
            {
              "type": "WEB",
              "url": "https://lists.apache.org/thread.html/46c055e173b52d599c648a98199972dbd6a89d2b4c4647b0500f2284@%3Cdevnull.infra.apache.org%3E"
            },
            {
              "type": "WEB",
              "url": "https://lists.apache.org/thread.html/320441dccbd9a545320f5f07306d711d4bbd31ba43dc9eebcfc602df@%3Cdevnull.infra.apache.org%3E"
            },
            {
              "type": "WEB",
              "url": "https://lists.apache.org/thread.html/2b52b9c8b9d6366a4f1b407a8bde6af28d9fc73fdb3b37695fd0d9ac@%3Cdevnull.infra.apache.org%3E"
            },
            {
              "type": "WEB",
              "url": "https://lists.apache.org/thread.html/09fc842ff444cd43d9d4c510756fec625ef8eb1175f14fd21de2605f@%3Cdevnull.infra.apache.org%3E"
            },
            {
              "type": "WEB",
              "url": "https://github.com/pypa/advisory-database/tree/main/vulns/jinja2/PYSEC-2019-217.yaml"
            },
            {
              "type": "PACKAGE",
              "url": "https://github.com/pallets/jinja"
            },
            {
              "type": "ADVISORY",
              "url": "https://github.com/advisories/GHSA-462w-v97r-4m45"
            },
            {
              "type": "WEB",
              "url": "https://access.redhat.com/errata/RHSA-2019:1329"
            },
            {
              "type": "WEB",
              "url": "https://access.redhat.com/errata/RHSA-2019:1237"
            },
            {
              "type": "WEB",
              "url": "https://access.redhat.com/errata/RHSA-2019:1152"
            },
            {
              "type": "WEB",
              "url": "http://lists.opensuse.org/opensuse-security-announce/2019-05/msg00030.html"
            },
            {
              "type": "WEB",
              "url": "http://lists.opensuse.org/opensuse-security-announce/2019-06/msg00064.html"
            }
          ],
          "schema_version": "1.7.3",
          "severity": [
            {
              "score": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:N/A:N",
              "type": "CVSS_V3"
            },
            {
              "score": "CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:N/VA:N/SC:H/SI:N/SA:N",
              "type": "CVSS_V4"
            }
          ],
          "summary": "Jinja2 sandbox escape via string formatting"
        }
      },
      "relationship_name": "supersedes",
      "target_state": "superseded"
    },
    {
      "adapter": "osv",
      "at": "2026-02-04T03:33:10.792778Z",
      "basis": "OSV advisory GHSA-8q59-q68h-6hv4 / CVE-2020-14343 affects PyPI PyYAML 5.3.1: Improper Input Validation in PyYAML",
      "evidence_class": "authority_feed",
      "evidence_ref": "GHSA-8q59-q68h-6hv4",
      "match_key": {
        "ecosystem": "PyPI",
        "kind": "package_version",
        "name": "PyYAML",
        "version": "5.3.1"
      },
      "raw": {
        "osv_url": "https://osv.dev/vulnerability/GHSA-8q59-q68h-6hv4",
        "package": {
          "ecosystem": "PyPI",
          "name": "PyYAML",
          "version": "5.3.1"
        },
        "result_vuln_count": 2,
        "vulnerability": {
          "affected": [
            {
              "database_specific": {
                "source": "https://github.com/github/advisory-database/blob/main/advisories/github-reviewed/2021/03/GHSA-8q59-q68h-6hv4/GHSA-8q59-q68h-6hv4.json"
              },
              "package": {
                "ecosystem": "PyPI",
                "name": "pyyaml",
                "purl": "pkg:pypi/pyyaml"
              },
              "ranges": [
                {
                  "events": [
                    {
                      "introduced": "0"
                    },
                    {
                      "fixed": "5.4"
                    }
                  ],
                  "type": "ECOSYSTEM"
                }
              ],
              "versions": [
                "3.01",
                "3.02",
                "3.03",
                "3.04",
                "3.05",
                "3.06",
                "3.07",
                "3.08",
                "3.09",
                "3.10",
                "3.11",
                "3.12",
                "3.13",
                "3.13b1",
                "3.13rc1",
                "4.2b1",
                "4.2b2",
                "4.2b4",
                "5.1",
                "5.1.1",
                "5.1.2",
                "5.1b1",
                "5.1b3",
                "5.1b5",
                "5.1b7",
                "5.2",
                "5.2b1",
                "5.3",
                "5.3.1",
                "5.3b1",
                "5.4b1",
                "5.4b2"
              ]
            }
          ],
          "aliases": [
            "CVE-2020-14343",
            "PYSEC-2021-142"
          ],
          "database_specific": {
            "cwe_ids": [
              "CWE-20"
            ],
            "github_reviewed": true,
            "github_reviewed_at": "2021-03-25T21:15:23Z",
            "nvd_published_at": "2021-02-09T21:15:00Z",
            "severity": "CRITICAL"
          },
          "details": "A vulnerability was discovered in the PyYAML library in versions before 5.4, where it is susceptible to arbitrary code execution when it processes untrusted YAML files through the full_load method or with the FullLoader loader. Applications that use the library to process untrusted input may be vulnerable to this flaw. This flaw allows an attacker to execute arbitrary code on the system by abusing the python/object/new constructor. This flaw is due to an incomplete fix for CVE-2020-1747.",
          "id": "GHSA-8q59-q68h-6hv4",
          "modified": "2026-02-04T03:33:10.792778Z",
          "published": "2021-03-25T21:26:26Z",
          "references": [
            {
              "type": "ADVISORY",
              "url": "https://nvd.nist.gov/vuln/detail/CVE-2020-14343"
            },
            {
              "type": "WEB",
              "url": "https://github.com/SeldonIO/seldon-core/issues/2252"
            },
            {
              "type": "WEB",
              "url": "https://github.com/yaml/pyyaml/issues/420"
            },
            {
              "type": "WEB",
              "url": "https://github.com/yaml/pyyaml/issues/420#issuecomment-663673966"
            },
            {
              "type": "WEB",
              "url": "https://github.com/yaml/pyyaml/commit/a001f2782501ad2d24986959f0239a354675f9dc"
            },
            {
              "type": "WEB",
              "url": "https://bugzilla.redhat.com/show_bug.cgi?id=1860466"
            },
            {
              "type": "ADVISORY",
              "url": "https://github.com/advisories/GHSA-8q59-q68h-6hv4"
            },
            {
              "type": "WEB",
              "url": "https://github.com/pypa/advisory-database/tree/main/vulns/pyyaml/PYSEC-2021-142.yaml"
            },
            {
              "type": "PACKAGE",
              "url": "https://github.com/yaml/pyyaml"
            },
            {
              "type": "WEB",
              "url": "https://pypi.org/project/PyYAML"
            },
            {
              "type": "WEB",
              "url": "https://www.oracle.com/security-alerts/cpuapr2022.html"
            },
            {
              "type": "WEB",
              "url": "https://www.oracle.com/security-alerts/cpujul2022.html"
            }
          ],
          "related": [
            "CVE-2026-24009"
          ],
          "schema_version": "1.7.3",
          "severity": [
            {
              "score": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
              "type": "CVSS_V3"
            },
            {
              "score": "CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N",
              "type": "CVSS_V4"
            }
          ],
          "summary": "Improper Input Validation in PyYAML"
        }
      },
      "relationship_name": "supersedes",
      "target_state": "superseded"
    },
    {
      "adapter": "osv",
      "at": "2026-02-04T02:36:12.983430Z",
      "basis": "OSV advisory GHSA-2xpw-w6gg-jr37 / CVE-2025-66471 affects PyPI urllib3 1.26.5: urllib3 streaming API improperly handles highly compressed data",
      "evidence_class": "authority_feed",
      "evidence_ref": "GHSA-2xpw-w6gg-jr37",
      "match_key": {
        "ecosystem": "PyPI",
        "kind": "package_version",
        "name": "urllib3",
        "version": "1.26.5"
      },
      "raw": {
        "osv_url": "https://osv.dev/vulnerability/GHSA-2xpw-w6gg-jr37",
        "package": {
          "ecosystem": "PyPI",
          "name": "urllib3",
          "version": "1.26.5"
        },
        "result_vuln_count": 11,
        "vulnerability": {
          "affected": [
            {
              "database_specific": {
                "source": "https://github.com/github/advisory-database/blob/main/advisories/github-reviewed/2025/12/GHSA-2xpw-w6gg-jr37/GHSA-2xpw-w6gg-jr37.json"
              },
              "package": {
                "ecosystem": "PyPI",
                "name": "urllib3",
                "purl": "pkg:pypi/urllib3"
              },
              "ranges": [
                {
                  "events": [
                    {
                      "introduced": "1.0"
                    },
                    {
                      "fixed": "2.6.0"
                    }
                  ],
                  "type": "ECOSYSTEM"
                }
              ],
              "versions": [
                "1.0",
                "1.0.1",
                "1.0.2",
                "1.1",
                "1.10",
                "1.10.1",
                "1.10.2",
                "1.10.3",
                "1.10.4",
                "1.11",
                "1.12",
                "1.13",
                "1.13.1",
                "1.14",
                "1.15",
                "1.15.1",
                "1.16",
                "1.17",
                "1.18",
                "1.18.1",
                "1.19",
                "1.19.1",
                "1.2",
                "1.2.1",
                "1.2.2",
                "1.20",
                "1.21",
                "1.21.1",
                "1.22",
                "1.23",
                "1.24",
                "1.24.1",
                "1.24.2",
                "1.24.3",
                "1.25",
                "1.25.1",
                "1.25.10",
                "1.25.11",
                "1.25.2",
                "1.25.3",
                "1.25.4",
                "1.25.5",
                "1.25.6",
                "1.25.7",
                "1.25.8",
                "1.25.9",
                "1.26.0",
                "1.26.1",
                "1.26.10",
                "1.26.11",
                "1.26.12",
                "1.26.13",
                "1.26.14",
                "1.26.15",
                "1.26.16",
                "1.26.17",
                "1.26.18",
                "1.26.19",
                "1.26.2",
                "1.26.20",
                "1.26.3",
                "1.26.4",
                "1.26.5",
                "1.26.6",
                "1.26.7",
                "1.26.8",
                "1.26.9",
                "1.3",
                "1.4",
                "1.5",
                "1.6",
                "1.7",
                "1.7.1",
                "1.8",
                "1.8.2",
                "1.8.3",
                "1.9",
                "1.9.1",
                "2.0.0",
                "2.0.0a1",
                "2.0.0a2",
                "2.0.0a3",
                "2.0.0a4",
                "2.0.1",
                "2.0.2",
                "2.0.3",
                "2.0.4",
                "2.0.5",
                "2.0.6",
                "2.0.7",
                "2.1.0",
                "2.2.0",
                "2.2.1",
                "2.2.2",
                "2.2.3",
                "2.3.0",
                "2.4.0",
                "2.5.0"
              ]
            }
          ],
          "aliases": [
            "CVE-2025-66471"
          ],
          "database_specific": {
            "cwe_ids": [
              "CWE-409"
            ],
            "github_reviewed": true,
            "github_reviewed_at": "2025-12-05T18:15:54Z",
            "nvd_published_at": "2025-12-05T17:16:04Z",
            "severity": "HIGH"
          },
          "details": "### Impact\n\nurllib3's [streaming API](https://urllib3.readthedocs.io/en/2.5.0/advanced-usage.html#streaming-and-i-o) is designed for the efficient handling of large HTTP responses by reading the content in chunks, rather than loading the entire response body into memory at once.\n\nWhen streaming a compressed response, urllib3 can perform decoding or decompression based on the HTTP `Content-Encoding` header (e.g., `gzip`, `deflate`, `br`, or `zstd`). The library must read compressed data from the network and decompress it until the requested chunk size is met. Any resulting decompressed data that exceeds the requested amount is held in an internal buffer for the next read operation.\n\nThe decompression logic could cause urllib3 to fully decode a small amount of highly compressed data in a single operation. This can result in excessive resource consumption (high CPU usage and massive memory allocation for the decompressed data; CWE-409) on the client side, even if the application only requested a small chunk of data.\n\n\n### Affected usages\n\nApplications and libraries using urllib3 version 2.5.0 and earlier to stream large compressed responses or content from untrusted sources.\n\n`stream()`, `read(amt=256)`, `read1(amt=256)`, `read_chunked(amt=256)`, `readinto(b)` are examples of `urllib3.HTTPResponse` method calls using the affected logic unless decoding is disabled explicitly.\n\n\n### Remediation\n\nUpgrade to at least urllib3 v2.6.0 in which the library avoids decompressing data that exceeds the requested amount.\n\nIf your environment contains a package facilitating the Brotli encoding, upgrade to at least Brotli 1.2.0 or brotlicffi 1.2.0.0 too. These versions are enforced by the `urllib3[brotli]` extra in the patched versions of urllib3.\n\n\n### Credits\n\nThe issue was reported by @Cycloctane.\nSupplemental information was provided by @stamparm during a security audit performed by [7ASecurity](https://7asecurity.com/) and facilitated by [OSTIF](https://ostif.org/).",
          "id": "GHSA-2xpw-w6gg-jr37",
          "modified": "2026-02-04T02:36:12.983430Z",
          "published": "2025-12-05T18:15:54Z",
          "references": [
            {
              "type": "WEB",
              "url": "https://github.com/urllib3/urllib3/security/advisories/GHSA-2xpw-w6gg-jr37"
            },
            {
              "type": "ADVISORY",
              "url": "https://nvd.nist.gov/vuln/detail/CVE-2025-66471"
            },
            {
              "type": "WEB",
              "url": "https://github.com/urllib3/urllib3/commit/c19571de34c47de3a766541b041637ba5f716ed7"
            },
            {
              "type": "PACKAGE",
              "url": "https://github.com/urllib3/urllib3"
            }
          ],
          "related": [
            "CGA-3vv3-3897-wc6m"
          ],
          "schema_version": "1.7.3",
          "severity": [
            {
              "score": "CVSS:4.0/AV:N/AC:L/AT:P/PR:N/UI:N/VC:N/VI:N/VA:H/SC:N/SI:N/SA:H",
              "type": "CVSS_V4"
            }
          ],
          "summary": "urllib3 streaming API improperly handles highly compressed data"
        }
      },
      "relationship_name": "supersedes",
      "target_state": "superseded"
    },
    {
      "adapter": "osv",
      "at": "2025-09-29T21:12:31.102523Z",
      "basis": "OSV advisory GHSA-29mw-wpgm-hmr9 / CVE-2020-28500 affects npm lodash 4.17.20: Regular Expression Denial of Service (ReDoS) in lodash",
      "evidence_class": "authority_feed",
      "evidence_ref": "GHSA-29mw-wpgm-hmr9",
      "match_key": {
        "ecosystem": "npm",
        "kind": "package_version",
        "name": "lodash",
        "version": "4.17.20"
      },
      "raw": {
        "osv_url": "https://osv.dev/vulnerability/GHSA-29mw-wpgm-hmr9",
        "package": {
          "ecosystem": "npm",
          "name": "lodash",
          "version": "4.17.20"
        },
        "result_vuln_count": 5,
        "vulnerability": {
          "affected": [
            {
              "database_specific": {
                "source": "https://github.com/github/advisory-database/blob/main/advisories/github-reviewed/2022/01/GHSA-29mw-wpgm-hmr9/GHSA-29mw-wpgm-hmr9.json"
              },
              "package": {
                "ecosystem": "npm",
                "name": "lodash",
                "purl": "pkg:npm/lodash"
              },
              "ranges": [
                {
                  "events": [
                    {
                      "introduced": "4.0.0"
                    },
                    {
                      "fixed": "4.17.21"
                    }
                  ],
                  "type": "SEMVER"
                }
              ]
            },
            {
              "database_specific": {
                "source": "https://github.com/github/advisory-database/blob/main/advisories/github-reviewed/2022/01/GHSA-29mw-wpgm-hmr9/GHSA-29mw-wpgm-hmr9.json"
              },
              "package": {
                "ecosystem": "npm",
                "name": "lodash-es",
                "purl": "pkg:npm/lodash-es"
              },
              "ranges": [
                {
                  "events": [
                    {
                      "introduced": "4.0.0"
                    },
                    {
                      "fixed": "4.17.21"
                    }
                  ],
                  "type": "SEMVER"
                }
              ]
            },
            {
              "database_specific": {
                "source": "https://github.com/github/advisory-database/blob/main/advisories/github-reviewed/2022/01/GHSA-29mw-wpgm-hmr9/GHSA-29mw-wpgm-hmr9.json"
              },
              "package": {
                "ecosystem": "npm",
                "name": "lodash.trimend",
                "purl": "pkg:npm/lodash.trimend"
              },
              "ranges": [
                {
                  "events": [
                    {
                      "introduced": "4.0.0"
                    },
                    {
                      "last_affected": "4.5.1"
                    }
                  ],
                  "type": "SEMVER"
                }
              ]
            },
            {
              "database_specific": {
                "source": "https://github.com/github/advisory-database/blob/main/advisories/github-reviewed/2022/01/GHSA-29mw-wpgm-hmr9/GHSA-29mw-wpgm-hmr9.json"
              },
              "package": {
                "ecosystem": "npm",
                "name": "lodash.trim",
                "purl": "pkg:npm/lodash.trim"
              },
              "ranges": [
                {
                  "events": [
                    {
                      "introduced": "4.0.0"
                    },
                    {
                      "last_affected": "4.5.1"
                    }
                  ],
                  "type": "SEMVER"
                }
              ]
            },
            {
              "database_specific": {
                "source": "https://github.com/github/advisory-database/blob/main/advisories/github-reviewed/2022/01/GHSA-29mw-wpgm-hmr9/GHSA-29mw-wpgm-hmr9.json"
              },
              "package": {
                "ecosystem": "RubyGems",
                "name": "lodash-rails",
                "purl": "pkg:gem/lodash-rails"
              },
              "ranges": [
                {
                  "events": [
                    {
                      "introduced": "4.0.0"
                    },
                    {
                      "fixed": "4.17.21"
                    }
                  ],
                  "type": "ECOSYSTEM"
                }
              ],
              "versions": [
                "4.0.0",
                "4.11.2",
                "4.12.0",
                "4.13.1",
                "4.14.1",
                "4.15.0",
                "4.16.1",
                "4.16.3",
                "4.16.4",
                "4.16.6",
                "4.17.10",
                "4.17.11",
                "4.17.14",
                "4.17.15",
                "4.17.2",
                "4.17.4",
                "4.17.5",
                "4.3.0",
                "4.5.1",
                "4.6.1"
              ]
            }
          ],
          "aliases": [
            "CVE-2020-28500"
          ],
          "database_specific": {
            "cwe_ids": [
              "CWE-1333",
              "CWE-400"
            ],
            "github_reviewed": true,
            "github_reviewed_at": "2021-03-19T22:45:28Z",
            "nvd_published_at": "2021-02-15T11:15:00Z",
            "severity": "MODERATE"
          },
          "details": "All versions of package lodash prior to 4.17.21 are vulnerable to Regular Expression Denial of Service (ReDoS) via the `toNumber`, `trim` and `trimEnd` functions. \n\nSteps to reproduce (provided by reporter Liyuan Chen):\n```js\nvar lo = require('lodash');\n\nfunction build_blank(n) {\n    var ret = \"1\"\n    for (var i = 0; i < n; i++) {\n        ret += \" \"\n    }\n    return ret + \"1\";\n}\nvar s = build_blank(50000) var time0 = Date.now();\nlo.trim(s) \nvar time_cost0 = Date.now() - time0;\nconsole.log(\"time_cost0: \" + time_cost0);\nvar time1 = Date.now();\nlo.toNumber(s) var time_cost1 = Date.now() - time1;\nconsole.log(\"time_cost1: \" + time_cost1);\nvar time2 = Date.now();\nlo.trimEnd(s);\nvar time_cost2 = Date.now() - time2;\nconsole.log(\"time_cost2: \" + time_cost2);\n```",
          "id": "GHSA-29mw-wpgm-hmr9",
          "modified": "2025-09-29T21:12:31.102523Z",
          "published": "2022-01-06T20:30:46Z",
          "references": [
            {
              "type": "ADVISORY",
              "url": "https://nvd.nist.gov/vuln/detail/CVE-2020-28500"
            },
            {
              "type": "WEB",
              "url": "https://github.com/github/advisory-database/pull/6139"
            },
            {
              "type": "WEB",
              "url": "https://github.com/lodash/lodash/pull/5065"
            },
            {
              "type": "WEB",
              "url": "https://github.com/lodash/lodash/pull/5065/commits/02906b8191d3c100c193fe6f7b27d1c40f200bb7"
            },
            {
              "type": "WEB",
              "url": "https://github.com/lodash/lodash/commit/c4847ebe7d14540bb28a8b932a9ce1b9ecbfee1a"
            },
            {
              "type": "WEB",
              "url": "https://www.oracle.com/security-alerts/cpuoct2021.html"
            },
            {
              "type": "WEB",
              "url": "https://www.oracle.com/security-alerts/cpujul2022.html"
            },
            {
              "type": "WEB",
              "url": "https://www.oracle.com/security-alerts/cpujan2022.html"
            },
            {
              "type": "WEB",
              "url": "https://www.oracle.com//security-alerts/cpujul2021.html"
            },
            {
              "type": "WEB",
              "url": "https://snyk.io/vuln/SNYK-JS-LODASH-1018905"
            },
            {
              "type": "WEB",
              "url": "https://snyk.io/vuln/SNYK-JAVA-ORGWEBJARSNPM-1074893"
            },
            {
              "type": "WEB",
              "url": "https://snyk.io/vuln/SNYK-JAVA-ORGWEBJARSBOWERGITHUBLODASH-1074895"
            },
            {
              "type": "WEB",
              "url": "https://snyk.io/vuln/SNYK-JAVA-ORGWEBJARSBOWER-1074892"
            },
            {
              "type": "WEB",
              "url": "https://snyk.io/vuln/SNYK-JAVA-ORGWEBJARS-1074894"
            },
            {
              "type": "WEB",
              "url": "https://snyk.io/vuln/SNYK-JAVA-ORGFUJIONWEBJARS-1074896"
            },
            {
              "type": "WEB",
              "url": "https://security.netapp.com/advisory/ntap-20210312-0006"
            },
            {
              "type": "WEB",
              "url": "https://github.com/rubysec/ruby-advisory-db/blob/master/gems/lodash-rails/CVE-2020-28500.yml"
            },
            {
              "type": "WEB",
              "url": "https://github.com/lodash/lodash/blob/npm/trimEnd.js%23L8"
            },
            {
              "type": "PACKAGE",
              "url": "https://github.com/lodash/lodash"
            },
            {
              "type": "WEB",
              "url": "https://cert-portal.siemens.com/productcert/pdf/ssa-637483.pdf"
            }
          ],
          "schema_version": "1.7.3",
          "severity": [
            {
              "score": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L",
              "type": "CVSS_V3"
            }
          ],
          "summary": "Regular Expression Denial of Service (ReDoS) in lodash"
        }
      },
      "relationship_name": "supersedes",
      "target_state": "superseded"
    },
    {
      "adapter": "osv",
      "at": "2026-03-13T22:11:31.390433Z",
      "basis": "OSV advisory GHSA-vh95-rmgr-6w4m / CVE-2020-7598 affects npm minimist 0.0.8: Prototype Pollution in minimist",
      "evidence_class": "authority_feed",
      "evidence_ref": "GHSA-vh95-rmgr-6w4m",
      "match_key": {
        "ecosystem": "npm",
        "kind": "package_version",
        "name": "minimist",
        "version": "0.0.8"
      },
      "raw": {
        "osv_url": "https://osv.dev/vulnerability/GHSA-vh95-rmgr-6w4m",
        "package": {
          "ecosystem": "npm",
          "name": "minimist",
          "version": "0.0.8"
        },
        "result_vuln_count": 2,
        "vulnerability": {
          "affected": [
            {
              "database_specific": {
                "source": "https://github.com/github/advisory-database/blob/main/advisories/github-reviewed/2020/04/GHSA-vh95-rmgr-6w4m/GHSA-vh95-rmgr-6w4m.json"
              },
              "package": {
                "ecosystem": "npm",
                "name": "minimist",
                "purl": "pkg:npm/minimist"
              },
              "ranges": [
                {
                  "events": [
                    {
                      "introduced": "0"
                    },
                    {
                      "fixed": "0.2.1"
                    }
                  ],
                  "type": "SEMVER"
                }
              ]
            },
            {
              "database_specific": {
                "source": "https://github.com/github/advisory-database/blob/main/advisories/github-reviewed/2020/04/GHSA-vh95-rmgr-6w4m/GHSA-vh95-rmgr-6w4m.json"
              },
              "package": {
                "ecosystem": "npm",
                "name": "minimist",
                "purl": "pkg:npm/minimist"
              },
              "ranges": [
                {
                  "events": [
                    {
                      "introduced": "1.0.0"
                    },
                    {
                      "fixed": "1.2.3"
                    }
                  ],
                  "type": "SEMVER"
                }
              ]
            }
          ],
          "aliases": [
            "CVE-2020-7598"
          ],
          "database_specific": {
            "cwe_ids": [
              "CWE-1321"
            ],
            "github_reviewed": true,
            "github_reviewed_at": "2020-04-03T21:42:08Z",
            "nvd_published_at": "2020-03-11T23:15:00Z",
            "severity": "MODERATE"
          },
          "details": "Affected versions of `minimist` are vulnerable to prototype pollution. Arguments are not properly sanitized, allowing an attacker to modify the prototype of `Object`, causing the addition or modification of an existing property that will exist on all objects.  \nParsing the argument `--__proto__.y=Polluted` adds a `y` property with value `Polluted` to all objects. The argument `--__proto__=Polluted` raises and uncaught error and crashes the application.  \nThis is exploitable if attackers have control over the arguments being passed to `minimist`.\n\n\n## Recommendation\n\nUpgrade to versions 0.2.1, 1.2.3 or later.",
          "id": "GHSA-vh95-rmgr-6w4m",
          "modified": "2026-03-13T22:11:31.390433Z",
          "published": "2020-04-03T21:48:32Z",
          "references": [
            {
              "type": "ADVISORY",
              "url": "https://nvd.nist.gov/vuln/detail/CVE-2020-7598"
            },
            {
              "type": "WEB",
              "url": "https://github.com/minimistjs/minimist/commit/10bd4cdf49d9686d48214be9d579a9cdfda37c68"
            },
            {
              "type": "WEB",
              "url": "https://github.com/minimistjs/minimist/commit/38a4d1caead72ef99e824bb420a2528eec03d9ab"
            },
            {
              "type": "WEB",
              "url": "https://github.com/minimistjs/minimist/commit/4cf1354839cb972e38496d35e12f806eea92c11f#diff-a1e0ee62c91705696ddb71aa30ad4f95"
            },
            {
              "type": "WEB",
              "url": "https://github.com/minimistjs/minimist/commit/63e7ed05aa4b1889ec2f3b196426db4500cbda94"
            },
            {
              "type": "PACKAGE",
              "url": "https://github.com/substack/minimist"
            },
            {
              "type": "WEB",
              "url": "https://snyk.io/vuln/SNYK-JS-MINIMIST-559764"
            },
            {
              "type": "WEB",
              "url": "https://www.npmjs.com/advisories/1179"
            },
            {
              "type": "WEB",
              "url": "http://lists.opensuse.org/opensuse-security-announce/2020-06/msg00024.html"
            }
          ],
          "schema_version": "1.7.5",
          "severity": [
            {
              "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:L",
              "type": "CVSS_V3"
            }
          ],
          "summary": "Prototype Pollution in minimist"
        }
      },
      "relationship_name": "supersedes",
      "target_state": "superseded"
    }
  ],
  "generated_at": "2026-07-04T23:44:34.028111+00:00",
  "osv_docs": {
    "api": "https://google.github.io/osv.dev/api/",
    "query": "https://google.github.io/osv.dev/post-v1-query/"
  },
  "provider_policy": "OSV adapter uses keyless OSV.dev HTTP API only; no LLM provider, Cognee provider, Azure, or Groq calls are used.",
  "question": "Should our coding agent recommend jinja2 2.4.1?",
  "seed_claims": [
    {
      "belief_state": "active",
      "claim_id": "OSV001",
      "claim_text": "Package jinja2 2.4.1 is safe to recommend for new software projects.",
      "cohort": "osv_package_claim",
      "doi": "pkg:pypi/jinja2@2.4.1",
      "source": {
        "doi": "pkg:pypi/jinja2@2.4.1",
        "journal": "PyPI package index",
        "package": {
          "ecosystem": "PyPI",
          "name": "jinja2",
          "version": "2.4.1"
        },
        "title": "jinja2 2.4.1 dependency recommendation",
        "year": 2010
      },
      "state_history": [
        {
          "at": "2010-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "pkg:pypi/jinja2@2.4.1",
          "state": "active"
        }
      ],
      "status": "active"
    },
    {
      "belief_state": "active",
      "claim_id": "OSV002",
      "claim_text": "Package PyYAML 5.3.1 is safe to recommend for new software projects.",
      "cohort": "osv_package_claim",
      "doi": "pkg:pypi/PyYAML@5.3.1",
      "source": {
        "doi": "pkg:pypi/PyYAML@5.3.1",
        "journal": "PyPI package index",
        "package": {
          "ecosystem": "PyPI",
          "name": "PyYAML",
          "version": "5.3.1"
        },
        "title": "PyYAML 5.3.1 dependency recommendation",
        "year": 2020
      },
      "state_history": [
        {
          "at": "2020-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "pkg:pypi/PyYAML@5.3.1",
          "state": "active"
        }
      ],
      "status": "active"
    },
    {
      "belief_state": "active",
      "claim_id": "OSV003",
      "claim_text": "Package urllib3 1.26.5 is safe to recommend for new software projects.",
      "cohort": "osv_package_claim",
      "doi": "pkg:pypi/urllib3@1.26.5",
      "source": {
        "doi": "pkg:pypi/urllib3@1.26.5",
        "journal": "PyPI package index",
        "package": {
          "ecosystem": "PyPI",
          "name": "urllib3",
          "version": "1.26.5"
        },
        "title": "urllib3 1.26.5 dependency recommendation",
        "year": 2021
      },
      "state_history": [
        {
          "at": "2021-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "pkg:pypi/urllib3@1.26.5",
          "state": "active"
        }
      ],
      "status": "active"
    },
    {
      "belief_state": "active",
      "claim_id": "OSV004",
      "claim_text": "Package lodash 4.17.20 is safe to recommend for new software projects.",
      "cohort": "osv_package_claim",
      "doi": "pkg:npm/lodash@4.17.20",
      "source": {
        "doi": "pkg:npm/lodash@4.17.20",
        "journal": "npm package registry",
        "package": {
          "ecosystem": "npm",
          "name": "lodash",
          "version": "4.17.20"
        },
        "title": "lodash 4.17.20 dependency recommendation",
        "year": 2020
      },
      "state_history": [
        {
          "at": "2020-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "pkg:npm/lodash@4.17.20",
          "state": "active"
        }
      ],
      "status": "active"
    },
    {
      "belief_state": "active",
      "claim_id": "OSV005",
      "claim_text": "Package minimist 0.0.8 is safe to recommend for new software projects.",
      "cohort": "osv_package_claim",
      "doi": "pkg:npm/minimist@0.0.8",
      "source": {
        "doi": "pkg:npm/minimist@0.0.8",
        "journal": "npm package registry",
        "package": {
          "ecosystem": "npm",
          "name": "minimist",
          "version": "0.0.8"
        },
        "title": "minimist 0.0.8 dependency recommendation",
        "year": 2013
      },
      "state_history": [
        {
          "at": "2013-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "pkg:npm/minimist@0.0.8",
          "state": "active"
        }
      ],
      "status": "active"
    },
    {
      "belief_state": "active",
      "claim_id": "OSV006",
      "claim_text": "Package packaging 24.2 is safe to recommend for new software projects.",
      "cohort": "osv_package_claim",
      "doi": "pkg:pypi/packaging@24.2",
      "source": {
        "doi": "pkg:pypi/packaging@24.2",
        "journal": "PyPI package index",
        "package": {
          "ecosystem": "PyPI",
          "name": "packaging",
          "version": "24.2"
        },
        "title": "packaging 24.2 dependency recommendation",
        "year": 2024
      },
      "state_history": [
        {
          "at": "2024-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "pkg:pypi/packaging@24.2",
          "state": "active"
        }
      ],
      "status": "active"
    },
    {
      "belief_state": "active",
      "claim_id": "OSV007",
      "claim_text": "Package click 8.1.8 is safe to recommend for new software projects.",
      "cohort": "osv_package_claim",
      "doi": "pkg:pypi/click@8.1.8",
      "source": {
        "doi": "pkg:pypi/click@8.1.8",
        "journal": "PyPI package index",
        "package": {
          "ecosystem": "PyPI",
          "name": "click",
          "version": "8.1.8"
        },
        "title": "click 8.1.8 dependency recommendation",
        "year": 2024
      },
      "state_history": [
        {
          "at": "2024-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "pkg:pypi/click@8.1.8",
          "state": "active"
        }
      ],
      "status": "active"
    },
    {
      "belief_state": "active",
      "claim_id": "OSV008",
      "claim_text": "Package six 1.17.0 is safe to recommend for new software projects.",
      "cohort": "osv_package_claim",
      "doi": "pkg:pypi/six@1.17.0",
      "source": {
        "doi": "pkg:pypi/six@1.17.0",
        "journal": "PyPI package index",
        "package": {
          "ecosystem": "PyPI",
          "name": "six",
          "version": "1.17.0"
        },
        "title": "six 1.17.0 dependency recommendation",
        "year": 2024
      },
      "state_history": [
        {
          "at": "2024-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "pkg:pypi/six@1.17.0",
          "state": "active"
        }
      ],
      "status": "active"
    },
    {
      "belief_state": "active",
      "claim_id": "OSV009",
      "claim_text": "Package h11 0.16.0 is safe to recommend for new software projects.",
      "cohort": "osv_package_claim",
      "doi": "pkg:pypi/h11@0.16.0",
      "source": {
        "doi": "pkg:pypi/h11@0.16.0",
        "journal": "PyPI package index",
        "package": {
          "ecosystem": "PyPI",
          "name": "h11",
          "version": "0.16.0"
        },
        "title": "h11 0.16.0 dependency recommendation",
        "year": 2025
      },
      "state_history": [
        {
          "at": "2025-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "pkg:pypi/h11@0.16.0",
          "state": "active"
        }
      ],
      "status": "active"
    },
    {
      "belief_state": "active",
      "claim_id": "OSV010",
      "claim_text": "Package is-number 7.0.0 is safe to recommend for new software projects.",
      "cohort": "osv_package_claim",
      "doi": "pkg:npm/is-number@7.0.0",
      "source": {
        "doi": "pkg:npm/is-number@7.0.0",
        "journal": "npm package registry",
        "package": {
          "ecosystem": "npm",
          "name": "is-number",
          "version": "7.0.0"
        },
        "title": "is-number 7.0.0 dependency recommendation",
        "year": 2018
      },
      "state_history": [
        {
          "at": "2018-01-01T00:00:00+00:00",
          "basis": "Seed corpus imported this claim as an active memory claim.",
          "evidence_class": "user_assertion",
          "evidence_ref": "pkg:npm/is-number@7.0.0",
          "state": "active"
        }
      ],
      "status": "active"
    }
  ],
  "shared_engine_demo": {
    "adapters": [
      "retraction_watch",
      "osv"
    ],
    "registry": [
      {
        "belief_state": "retracted",
        "claim_id": "RW-DEMO",
        "claim_text": "The paper claimed that a demo intervention works.",
        "cohort": "adapter_protocol_demo",
        "doi": "10.5555/demo-original",
        "source": {
          "doi": "10.5555/demo-original",
          "journal": "Journal of Demo Medicine",
          "title": "A demo intervention works",
          "year": 2020
        },
        "state_history": [
          {
            "at": "2020-01-01T00:00:00+00:00",
            "basis": "Seed corpus imported this claim as an active memory claim.",
            "evidence_class": "user_assertion",
            "evidence_ref": "10.5555/demo-original",
            "state": "active"
          },
          {
            "at": "2026-07-04T00:00:00+00:00",
            "basis": "Retraction Watch record 10.5555/demo-retraction supersedes original DOI 10.5555/demo-original; reason: Adapter protocol demonstration.",
            "evidence_class": "authority_feed",
            "evidence_ref": "10.5555/demo-retraction",
            "state": "retracted"
          }
        ],
        "status": "retracted"
      },
      {
        "belief_state": "superseded",
        "claim_id": "OSV001",
        "claim_text": "Package jinja2 2.4.1 is safe to recommend for new software projects.",
        "cohort": "osv_package_claim",
        "doi": "pkg:pypi/jinja2@2.4.1",
        "source": {
          "doi": "pkg:pypi/jinja2@2.4.1",
          "journal": "PyPI package index",
          "package": {
            "ecosystem": "PyPI",
            "name": "jinja2",
            "version": "2.4.1"
          },
          "title": "jinja2 2.4.1 dependency recommendation",
          "year": 2010
        },
        "state_history": [
          {
            "at": "2010-01-01T00:00:00+00:00",
            "basis": "Seed corpus imported this claim as an active memory claim.",
            "evidence_class": "user_assertion",
            "evidence_ref": "pkg:pypi/jinja2@2.4.1",
            "state": "active"
          },
          {
            "at": "2024-09-24T21:03:59.802687Z",
            "basis": "OSV advisory GHSA-462w-v97r-4m45 / CVE-2019-10906 affects PyPI jinja2 2.4.1: Jinja2 sandbox escape via string formatting",
            "evidence_class": "authority_feed",
            "evidence_ref": "GHSA-462w-v97r-4m45",
            "state": "superseded"
          }
        ],
        "status": "superseded"
      }
    ],
    "results": [
      {
        "evidence": {
          "adapter": "retraction_watch",
          "at": "2026-07-04T00:00:00+00:00",
          "basis": "Retraction Watch record 10.5555/demo-retraction supersedes original DOI 10.5555/demo-original; reason: Adapter protocol demonstration.",
          "evidence_class": "authority_feed",
          "evidence_ref": "10.5555/demo-retraction",
          "match_key": {
            "doi": "10.5555/demo-original",
            "kind": "doi"
          },
          "raw": {
            "original_doi": "10.5555/demo-original",
            "reason": "Adapter protocol demonstration.",
            "retraction_date": "2026-07-04",
            "retraction_doi": "10.5555/demo-retraction"
          },
          "relationship_name": "contradicts",
          "target_state": "retracted"
        },
        "matched_claim_ids": [
          "RW-DEMO"
        ],
        "matched_claims": [
          {
            "after": {
              "at": "2026-07-04T00:00:00+00:00",
              "basis": "Retraction Watch record 10.5555/demo-retraction supersedes original DOI 10.5555/demo-original; reason: Adapter protocol demonstration.",
              "evidence_class": "authority_feed",
              "evidence_ref": "10.5555/demo-retraction",
              "state": "retracted"
            },
            "before": {
              "at": "2020-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "10.5555/demo-original",
              "state": "active"
            },
            "belief_state": "retracted",
            "claim_id": "RW-DEMO"
          }
        ],
        "status": "applied"
      },
      {
        "evidence": {
          "adapter": "osv",
          "at": "2024-09-24T21:03:59.802687Z",
          "basis": "OSV advisory GHSA-462w-v97r-4m45 / CVE-2019-10906 affects PyPI jinja2 2.4.1: Jinja2 sandbox escape via string formatting",
          "evidence_class": "authority_feed",
          "evidence_ref": "GHSA-462w-v97r-4m45",
          "match_key": {
            "ecosystem": "PyPI",
            "kind": "package_version",
            "name": "jinja2",
            "version": "2.4.1"
          },
          "raw": {
            "osv_url": "https://osv.dev/vulnerability/GHSA-462w-v97r-4m45",
            "package": {
              "ecosystem": "PyPI",
              "name": "jinja2",
              "version": "2.4.1"
            },
            "result_vuln_count": 14,
            "vulnerability": {
              "affected": [
                {
                  "database_specific": {
                    "source": "https://github.com/github/advisory-database/blob/main/advisories/github-reviewed/2019/04/GHSA-462w-v97r-4m45/GHSA-462w-v97r-4m45.json"
                  },
                  "package": {
                    "ecosystem": "PyPI",
                    "name": "jinja2",
                    "purl": "pkg:pypi/jinja2"
                  },
                  "ranges": [
                    {
                      "events": [
                        {
                          "introduced": "0"
                        },
                        {
                          "fixed": "2.10.1"
                        }
                      ],
                      "type": "ECOSYSTEM"
                    }
                  ],
                  "versions": [
                    "2.0",
                    "2.0rc1",
                    "2.1",
                    "2.1.1",
                    "2.10",
                    "2.2",
                    "2.2.1",
                    "2.3",
                    "2.3.1",
                    "2.4",
                    "2.4.1",
                    "2.5",
                    "2.5.1",
                    "2.5.2",
                    "2.5.3",
                    "2.5.4",
                    "2.5.5",
                    "2.6",
                    "2.7",
                    "2.7.1",
                    "2.7.2",
                    "2.7.3",
                    "2.8",
                    "2.8.1",
                    "2.9",
                    "2.9.1",
                    "2.9.2",
                    "2.9.3",
                    "2.9.4",
                    "2.9.5",
                    "2.9.6"
                  ]
                }
              ],
              "aliases": [
                "CVE-2019-10906",
                "PYSEC-2019-217"
              ],
              "database_specific": {
                "cwe_ids": [
                  "CWE-693"
                ],
                "github_reviewed": true,
                "github_reviewed_at": "2020-06-16T20:57:35Z",
                "nvd_published_at": "2019-04-07T00:29:00Z",
                "severity": "HIGH"
              },
              "details": "In Pallets Jinja before 2.10.1, `str.format_map` allows a sandbox escape.\n\nThe sandbox is used to restrict what code can be evaluated when rendering untrusted, user-provided templates. Due to the way string formatting works in Python, the `str.format_map` method could be used to escape the sandbox.\n\nThis issue was previously addressed for the `str.format` method in Jinja 2.8.1, which discusses the issue in detail. However, the less-common `str.format_map` method was overlooked. This release applies the same sandboxing to both methods.\n\nIf you cannot upgrade Jinja, you can override the `is_safe_attribute` method on the sandbox and explicitly disallow the `format_map` method on string objects.",
              "id": "GHSA-462w-v97r-4m45",
              "modified": "2024-09-24T21:03:59.802687Z",
              "published": "2019-04-10T14:30:24Z",
              "references": [
                {
                  "type": "ADVISORY",
                  "url": "https://nvd.nist.gov/vuln/detail/CVE-2019-10906"
                },
                {
                  "type": "WEB",
                  "url": "https://usn.ubuntu.com/4011-2"
                },
                {
                  "type": "WEB",
                  "url": "https://usn.ubuntu.com/4011-1"
                },
                {
                  "type": "WEB",
                  "url": "https://palletsprojects.com/blog/jinja-2-10-1-released"
                },
                {
                  "type": "WEB",
                  "url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/TS7IVZAJBWOHNRDMFJDIZVFCMRP6YIUQ"
                },
                {
                  "type": "WEB",
                  "url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/QCDYIS254EJMBNWOG4S5QY6AOTOR4TZU"
                },
                {
                  "type": "WEB",
                  "url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/DSW3QZMFVVR7YE3UT4YRQA272TYAL5AF"
                },
                {
                  "type": "WEB",
                  "url": "https://lists.apache.org/thread.html/f0c4a03418bcfe70c539c5dbaf99c04c98da13bfa1d3266f08564316@%3Ccommits.airflow.apache.org%3E"
                },
                {
                  "type": "WEB",
                  "url": "https://lists.apache.org/thread.html/b2380d147b508bbcb90d2cad443c159e63e12555966ab4f320ee22da@%3Ccommits.airflow.apache.org%3E"
                },
                {
                  "type": "WEB",
                  "url": "https://lists.apache.org/thread.html/7f39f01392d320dfb48e4901db68daeece62fd60ef20955966739993@%3Ccommits.airflow.apache.org%3E"
                },
                {
                  "type": "WEB",
                  "url": "https://lists.apache.org/thread.html/57673a78c4d5c870d3f21465c7e2946b9f8285c7c57e54c2ae552f02@%3Ccommits.airflow.apache.org%3E"
                },
                {
                  "type": "WEB",
                  "url": "https://lists.apache.org/thread.html/46c055e173b52d599c648a98199972dbd6a89d2b4c4647b0500f2284@%3Cdevnull.infra.apache.org%3E"
                },
                {
                  "type": "WEB",
                  "url": "https://lists.apache.org/thread.html/320441dccbd9a545320f5f07306d711d4bbd31ba43dc9eebcfc602df@%3Cdevnull.infra.apache.org%3E"
                },
                {
                  "type": "WEB",
                  "url": "https://lists.apache.org/thread.html/2b52b9c8b9d6366a4f1b407a8bde6af28d9fc73fdb3b37695fd0d9ac@%3Cdevnull.infra.apache.org%3E"
                },
                {
                  "type": "WEB",
                  "url": "https://lists.apache.org/thread.html/09fc842ff444cd43d9d4c510756fec625ef8eb1175f14fd21de2605f@%3Cdevnull.infra.apache.org%3E"
                },
                {
                  "type": "WEB",
                  "url": "https://github.com/pypa/advisory-database/tree/main/vulns/jinja2/PYSEC-2019-217.yaml"
                },
                {
                  "type": "PACKAGE",
                  "url": "https://github.com/pallets/jinja"
                },
                {
                  "type": "ADVISORY",
                  "url": "https://github.com/advisories/GHSA-462w-v97r-4m45"
                },
                {
                  "type": "WEB",
                  "url": "https://access.redhat.com/errata/RHSA-2019:1329"
                },
                {
                  "type": "WEB",
                  "url": "https://access.redhat.com/errata/RHSA-2019:1237"
                },
                {
                  "type": "WEB",
                  "url": "https://access.redhat.com/errata/RHSA-2019:1152"
                },
                {
                  "type": "WEB",
                  "url": "http://lists.opensuse.org/opensuse-security-announce/2019-05/msg00030.html"
                },
                {
                  "type": "WEB",
                  "url": "http://lists.opensuse.org/opensuse-security-announce/2019-06/msg00064.html"
                }
              ],
              "schema_version": "1.7.3",
              "severity": [
                {
                  "score": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:N/A:N",
                  "type": "CVSS_V3"
                },
                {
                  "score": "CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:N/VA:N/SC:H/SI:N/SA:N",
                  "type": "CVSS_V4"
                }
              ],
              "summary": "Jinja2 sandbox escape via string formatting"
            }
          },
          "relationship_name": "supersedes",
          "target_state": "superseded"
        },
        "matched_claim_ids": [
          "OSV001"
        ],
        "matched_claims": [
          {
            "after": {
              "at": "2024-09-24T21:03:59.802687Z",
              "basis": "OSV advisory GHSA-462w-v97r-4m45 / CVE-2019-10906 affects PyPI jinja2 2.4.1: Jinja2 sandbox escape via string formatting",
              "evidence_class": "authority_feed",
              "evidence_ref": "GHSA-462w-v97r-4m45",
              "state": "superseded"
            },
            "before": {
              "at": "2010-01-01T00:00:00+00:00",
              "basis": "Seed corpus imported this claim as an active memory claim.",
              "evidence_class": "user_assertion",
              "evidence_ref": "pkg:pypi/jinja2@2.4.1",
              "state": "active"
            },
            "belief_state": "superseded",
            "claim_id": "OSV001"
          }
        ],
        "status": "applied"
      }
    ]
  },
  "state_changes": [
    {
      "evidence": {
        "adapter": "osv",
        "at": "2024-09-24T21:03:59.802687Z",
        "basis": "OSV advisory GHSA-462w-v97r-4m45 / CVE-2019-10906 affects PyPI jinja2 2.4.1: Jinja2 sandbox escape via string formatting",
        "evidence_class": "authority_feed",
        "evidence_ref": "GHSA-462w-v97r-4m45",
        "match_key": {
          "ecosystem": "PyPI",
          "kind": "package_version",
          "name": "jinja2",
          "version": "2.4.1"
        },
        "raw": {
          "osv_url": "https://osv.dev/vulnerability/GHSA-462w-v97r-4m45",
          "package": {
            "ecosystem": "PyPI",
            "name": "jinja2",
            "version": "2.4.1"
          },
          "result_vuln_count": 14,
          "vulnerability": {
            "affected": [
              {
                "database_specific": {
                  "source": "https://github.com/github/advisory-database/blob/main/advisories/github-reviewed/2019/04/GHSA-462w-v97r-4m45/GHSA-462w-v97r-4m45.json"
                },
                "package": {
                  "ecosystem": "PyPI",
                  "name": "jinja2",
                  "purl": "pkg:pypi/jinja2"
                },
                "ranges": [
                  {
                    "events": [
                      {
                        "introduced": "0"
                      },
                      {
                        "fixed": "2.10.1"
                      }
                    ],
                    "type": "ECOSYSTEM"
                  }
                ],
                "versions": [
                  "2.0",
                  "2.0rc1",
                  "2.1",
                  "2.1.1",
                  "2.10",
                  "2.2",
                  "2.2.1",
                  "2.3",
                  "2.3.1",
                  "2.4",
                  "2.4.1",
                  "2.5",
                  "2.5.1",
                  "2.5.2",
                  "2.5.3",
                  "2.5.4",
                  "2.5.5",
                  "2.6",
                  "2.7",
                  "2.7.1",
                  "2.7.2",
                  "2.7.3",
                  "2.8",
                  "2.8.1",
                  "2.9",
                  "2.9.1",
                  "2.9.2",
                  "2.9.3",
                  "2.9.4",
                  "2.9.5",
                  "2.9.6"
                ]
              }
            ],
            "aliases": [
              "CVE-2019-10906",
              "PYSEC-2019-217"
            ],
            "database_specific": {
              "cwe_ids": [
                "CWE-693"
              ],
              "github_reviewed": true,
              "github_reviewed_at": "2020-06-16T20:57:35Z",
              "nvd_published_at": "2019-04-07T00:29:00Z",
              "severity": "HIGH"
            },
            "details": "In Pallets Jinja before 2.10.1, `str.format_map` allows a sandbox escape.\n\nThe sandbox is used to restrict what code can be evaluated when rendering untrusted, user-provided templates. Due to the way string formatting works in Python, the `str.format_map` method could be used to escape the sandbox.\n\nThis issue was previously addressed for the `str.format` method in Jinja 2.8.1, which discusses the issue in detail. However, the less-common `str.format_map` method was overlooked. This release applies the same sandboxing to both methods.\n\nIf you cannot upgrade Jinja, you can override the `is_safe_attribute` method on the sandbox and explicitly disallow the `format_map` method on string objects.",
            "id": "GHSA-462w-v97r-4m45",
            "modified": "2024-09-24T21:03:59.802687Z",
            "published": "2019-04-10T14:30:24Z",
            "references": [
              {
                "type": "ADVISORY",
                "url": "https://nvd.nist.gov/vuln/detail/CVE-2019-10906"
              },
              {
                "type": "WEB",
                "url": "https://usn.ubuntu.com/4011-2"
              },
              {
                "type": "WEB",
                "url": "https://usn.ubuntu.com/4011-1"
              },
              {
                "type": "WEB",
                "url": "https://palletsprojects.com/blog/jinja-2-10-1-released"
              },
              {
                "type": "WEB",
                "url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/TS7IVZAJBWOHNRDMFJDIZVFCMRP6YIUQ"
              },
              {
                "type": "WEB",
                "url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/QCDYIS254EJMBNWOG4S5QY6AOTOR4TZU"
              },
              {
                "type": "WEB",
                "url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/DSW3QZMFVVR7YE3UT4YRQA272TYAL5AF"
              },
              {
                "type": "WEB",
                "url": "https://lists.apache.org/thread.html/f0c4a03418bcfe70c539c5dbaf99c04c98da13bfa1d3266f08564316@%3Ccommits.airflow.apache.org%3E"
              },
              {
                "type": "WEB",
                "url": "https://lists.apache.org/thread.html/b2380d147b508bbcb90d2cad443c159e63e12555966ab4f320ee22da@%3Ccommits.airflow.apache.org%3E"
              },
              {
                "type": "WEB",
                "url": "https://lists.apache.org/thread.html/7f39f01392d320dfb48e4901db68daeece62fd60ef20955966739993@%3Ccommits.airflow.apache.org%3E"
              },
              {
                "type": "WEB",
                "url": "https://lists.apache.org/thread.html/57673a78c4d5c870d3f21465c7e2946b9f8285c7c57e54c2ae552f02@%3Ccommits.airflow.apache.org%3E"
              },
              {
                "type": "WEB",
                "url": "https://lists.apache.org/thread.html/46c055e173b52d599c648a98199972dbd6a89d2b4c4647b0500f2284@%3Cdevnull.infra.apache.org%3E"
              },
              {
                "type": "WEB",
                "url": "https://lists.apache.org/thread.html/320441dccbd9a545320f5f07306d711d4bbd31ba43dc9eebcfc602df@%3Cdevnull.infra.apache.org%3E"
              },
              {
                "type": "WEB",
                "url": "https://lists.apache.org/thread.html/2b52b9c8b9d6366a4f1b407a8bde6af28d9fc73fdb3b37695fd0d9ac@%3Cdevnull.infra.apache.org%3E"
              },
              {
                "type": "WEB",
                "url": "https://lists.apache.org/thread.html/09fc842ff444cd43d9d4c510756fec625ef8eb1175f14fd21de2605f@%3Cdevnull.infra.apache.org%3E"
              },
              {
                "type": "WEB",
                "url": "https://github.com/pypa/advisory-database/tree/main/vulns/jinja2/PYSEC-2019-217.yaml"
              },
              {
                "type": "PACKAGE",
                "url": "https://github.com/pallets/jinja"
              },
              {
                "type": "ADVISORY",
                "url": "https://github.com/advisories/GHSA-462w-v97r-4m45"
              },
              {
                "type": "WEB",
                "url": "https://access.redhat.com/errata/RHSA-2019:1329"
              },
              {
                "type": "WEB",
                "url": "https://access.redhat.com/errata/RHSA-2019:1237"
              },
              {
                "type": "WEB",
                "url": "https://access.redhat.com/errata/RHSA-2019:1152"
              },
              {
                "type": "WEB",
                "url": "http://lists.opensuse.org/opensuse-security-announce/2019-05/msg00030.html"
              },
              {
                "type": "WEB",
                "url": "http://lists.opensuse.org/opensuse-security-announce/2019-06/msg00064.html"
              }
            ],
            "schema_version": "1.7.3",
            "severity": [
              {
                "score": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:N/A:N",
                "type": "CVSS_V3"
              },
              {
                "score": "CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:N/VA:N/SC:H/SI:N/SA:N",
                "type": "CVSS_V4"
              }
            ],
            "summary": "Jinja2 sandbox escape via string formatting"
          }
        },
        "relationship_name": "supersedes",
        "target_state": "superseded"
      },
      "matched_claim_ids": [
        "OSV001"
      ],
      "matched_claims": [
        {
          "after": {
            "at": "2024-09-24T21:03:59.802687Z",
            "basis": "OSV advisory GHSA-462w-v97r-4m45 / CVE-2019-10906 affects PyPI jinja2 2.4.1: Jinja2 sandbox escape via string formatting",
            "evidence_class": "authority_feed",
            "evidence_ref": "GHSA-462w-v97r-4m45",
            "state": "superseded"
          },
          "before": {
            "at": "2010-01-01T00:00:00+00:00",
            "basis": "Seed corpus imported this claim as an active memory claim.",
            "evidence_class": "user_assertion",
            "evidence_ref": "pkg:pypi/jinja2@2.4.1",
            "state": "active"
          },
          "belief_state": "superseded",
          "claim_id": "OSV001"
        }
      ],
      "status": "applied"
    },
    {
      "evidence": {
        "adapter": "osv",
        "at": "2026-02-04T03:33:10.792778Z",
        "basis": "OSV advisory GHSA-8q59-q68h-6hv4 / CVE-2020-14343 affects PyPI PyYAML 5.3.1: Improper Input Validation in PyYAML",
        "evidence_class": "authority_feed",
        "evidence_ref": "GHSA-8q59-q68h-6hv4",
        "match_key": {
          "ecosystem": "PyPI",
          "kind": "package_version",
          "name": "PyYAML",
          "version": "5.3.1"
        },
        "raw": {
          "osv_url": "https://osv.dev/vulnerability/GHSA-8q59-q68h-6hv4",
          "package": {
            "ecosystem": "PyPI",
            "name": "PyYAML",
            "version": "5.3.1"
          },
          "result_vuln_count": 2,
          "vulnerability": {
            "affected": [
              {
                "database_specific": {
                  "source": "https://github.com/github/advisory-database/blob/main/advisories/github-reviewed/2021/03/GHSA-8q59-q68h-6hv4/GHSA-8q59-q68h-6hv4.json"
                },
                "package": {
                  "ecosystem": "PyPI",
                  "name": "pyyaml",
                  "purl": "pkg:pypi/pyyaml"
                },
                "ranges": [
                  {
                    "events": [
                      {
                        "introduced": "0"
                      },
                      {
                        "fixed": "5.4"
                      }
                    ],
                    "type": "ECOSYSTEM"
                  }
                ],
                "versions": [
                  "3.01",
                  "3.02",
                  "3.03",
                  "3.04",
                  "3.05",
                  "3.06",
                  "3.07",
                  "3.08",
                  "3.09",
                  "3.10",
                  "3.11",
                  "3.12",
                  "3.13",
                  "3.13b1",
                  "3.13rc1",
                  "4.2b1",
                  "4.2b2",
                  "4.2b4",
                  "5.1",
                  "5.1.1",
                  "5.1.2",
                  "5.1b1",
                  "5.1b3",
                  "5.1b5",
                  "5.1b7",
                  "5.2",
                  "5.2b1",
                  "5.3",
                  "5.3.1",
                  "5.3b1",
                  "5.4b1",
                  "5.4b2"
                ]
              }
            ],
            "aliases": [
              "CVE-2020-14343",
              "PYSEC-2021-142"
            ],
            "database_specific": {
              "cwe_ids": [
                "CWE-20"
              ],
              "github_reviewed": true,
              "github_reviewed_at": "2021-03-25T21:15:23Z",
              "nvd_published_at": "2021-02-09T21:15:00Z",
              "severity": "CRITICAL"
            },
            "details": "A vulnerability was discovered in the PyYAML library in versions before 5.4, where it is susceptible to arbitrary code execution when it processes untrusted YAML files through the full_load method or with the FullLoader loader. Applications that use the library to process untrusted input may be vulnerable to this flaw. This flaw allows an attacker to execute arbitrary code on the system by abusing the python/object/new constructor. This flaw is due to an incomplete fix for CVE-2020-1747.",
            "id": "GHSA-8q59-q68h-6hv4",
            "modified": "2026-02-04T03:33:10.792778Z",
            "published": "2021-03-25T21:26:26Z",
            "references": [
              {
                "type": "ADVISORY",
                "url": "https://nvd.nist.gov/vuln/detail/CVE-2020-14343"
              },
              {
                "type": "WEB",
                "url": "https://github.com/SeldonIO/seldon-core/issues/2252"
              },
              {
                "type": "WEB",
                "url": "https://github.com/yaml/pyyaml/issues/420"
              },
              {
                "type": "WEB",
                "url": "https://github.com/yaml/pyyaml/issues/420#issuecomment-663673966"
              },
              {
                "type": "WEB",
                "url": "https://github.com/yaml/pyyaml/commit/a001f2782501ad2d24986959f0239a354675f9dc"
              },
              {
                "type": "WEB",
                "url": "https://bugzilla.redhat.com/show_bug.cgi?id=1860466"
              },
              {
                "type": "ADVISORY",
                "url": "https://github.com/advisories/GHSA-8q59-q68h-6hv4"
              },
              {
                "type": "WEB",
                "url": "https://github.com/pypa/advisory-database/tree/main/vulns/pyyaml/PYSEC-2021-142.yaml"
              },
              {
                "type": "PACKAGE",
                "url": "https://github.com/yaml/pyyaml"
              },
              {
                "type": "WEB",
                "url": "https://pypi.org/project/PyYAML"
              },
              {
                "type": "WEB",
                "url": "https://www.oracle.com/security-alerts/cpuapr2022.html"
              },
              {
                "type": "WEB",
                "url": "https://www.oracle.com/security-alerts/cpujul2022.html"
              }
            ],
            "related": [
              "CVE-2026-24009"
            ],
            "schema_version": "1.7.3",
            "severity": [
              {
                "score": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
                "type": "CVSS_V3"
              },
              {
                "score": "CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N",
                "type": "CVSS_V4"
              }
            ],
            "summary": "Improper Input Validation in PyYAML"
          }
        },
        "relationship_name": "supersedes",
        "target_state": "superseded"
      },
      "matched_claim_ids": [
        "OSV002"
      ],
      "matched_claims": [
        {
          "after": {
            "at": "2026-02-04T03:33:10.792778Z",
            "basis": "OSV advisory GHSA-8q59-q68h-6hv4 / CVE-2020-14343 affects PyPI PyYAML 5.3.1: Improper Input Validation in PyYAML",
            "evidence_class": "authority_feed",
            "evidence_ref": "GHSA-8q59-q68h-6hv4",
            "state": "superseded"
          },
          "before": {
            "at": "2020-01-01T00:00:00+00:00",
            "basis": "Seed corpus imported this claim as an active memory claim.",
            "evidence_class": "user_assertion",
            "evidence_ref": "pkg:pypi/PyYAML@5.3.1",
            "state": "active"
          },
          "belief_state": "superseded",
          "claim_id": "OSV002"
        }
      ],
      "status": "applied"
    },
    {
      "evidence": {
        "adapter": "osv",
        "at": "2026-02-04T02:36:12.983430Z",
        "basis": "OSV advisory GHSA-2xpw-w6gg-jr37 / CVE-2025-66471 affects PyPI urllib3 1.26.5: urllib3 streaming API improperly handles highly compressed data",
        "evidence_class": "authority_feed",
        "evidence_ref": "GHSA-2xpw-w6gg-jr37",
        "match_key": {
          "ecosystem": "PyPI",
          "kind": "package_version",
          "name": "urllib3",
          "version": "1.26.5"
        },
        "raw": {
          "osv_url": "https://osv.dev/vulnerability/GHSA-2xpw-w6gg-jr37",
          "package": {
            "ecosystem": "PyPI",
            "name": "urllib3",
            "version": "1.26.5"
          },
          "result_vuln_count": 11,
          "vulnerability": {
            "affected": [
              {
                "database_specific": {
                  "source": "https://github.com/github/advisory-database/blob/main/advisories/github-reviewed/2025/12/GHSA-2xpw-w6gg-jr37/GHSA-2xpw-w6gg-jr37.json"
                },
                "package": {
                  "ecosystem": "PyPI",
                  "name": "urllib3",
                  "purl": "pkg:pypi/urllib3"
                },
                "ranges": [
                  {
                    "events": [
                      {
                        "introduced": "1.0"
                      },
                      {
                        "fixed": "2.6.0"
                      }
                    ],
                    "type": "ECOSYSTEM"
                  }
                ],
                "versions": [
                  "1.0",
                  "1.0.1",
                  "1.0.2",
                  "1.1",
                  "1.10",
                  "1.10.1",
                  "1.10.2",
                  "1.10.3",
                  "1.10.4",
                  "1.11",
                  "1.12",
                  "1.13",
                  "1.13.1",
                  "1.14",
                  "1.15",
                  "1.15.1",
                  "1.16",
                  "1.17",
                  "1.18",
                  "1.18.1",
                  "1.19",
                  "1.19.1",
                  "1.2",
                  "1.2.1",
                  "1.2.2",
                  "1.20",
                  "1.21",
                  "1.21.1",
                  "1.22",
                  "1.23",
                  "1.24",
                  "1.24.1",
                  "1.24.2",
                  "1.24.3",
                  "1.25",
                  "1.25.1",
                  "1.25.10",
                  "1.25.11",
                  "1.25.2",
                  "1.25.3",
                  "1.25.4",
                  "1.25.5",
                  "1.25.6",
                  "1.25.7",
                  "1.25.8",
                  "1.25.9",
                  "1.26.0",
                  "1.26.1",
                  "1.26.10",
                  "1.26.11",
                  "1.26.12",
                  "1.26.13",
                  "1.26.14",
                  "1.26.15",
                  "1.26.16",
                  "1.26.17",
                  "1.26.18",
                  "1.26.19",
                  "1.26.2",
                  "1.26.20",
                  "1.26.3",
                  "1.26.4",
                  "1.26.5",
                  "1.26.6",
                  "1.26.7",
                  "1.26.8",
                  "1.26.9",
                  "1.3",
                  "1.4",
                  "1.5",
                  "1.6",
                  "1.7",
                  "1.7.1",
                  "1.8",
                  "1.8.2",
                  "1.8.3",
                  "1.9",
                  "1.9.1",
                  "2.0.0",
                  "2.0.0a1",
                  "2.0.0a2",
                  "2.0.0a3",
                  "2.0.0a4",
                  "2.0.1",
                  "2.0.2",
                  "2.0.3",
                  "2.0.4",
                  "2.0.5",
                  "2.0.6",
                  "2.0.7",
                  "2.1.0",
                  "2.2.0",
                  "2.2.1",
                  "2.2.2",
                  "2.2.3",
                  "2.3.0",
                  "2.4.0",
                  "2.5.0"
                ]
              }
            ],
            "aliases": [
              "CVE-2025-66471"
            ],
            "database_specific": {
              "cwe_ids": [
                "CWE-409"
              ],
              "github_reviewed": true,
              "github_reviewed_at": "2025-12-05T18:15:54Z",
              "nvd_published_at": "2025-12-05T17:16:04Z",
              "severity": "HIGH"
            },
            "details": "### Impact\n\nurllib3's [streaming API](https://urllib3.readthedocs.io/en/2.5.0/advanced-usage.html#streaming-and-i-o) is designed for the efficient handling of large HTTP responses by reading the content in chunks, rather than loading the entire response body into memory at once.\n\nWhen streaming a compressed response, urllib3 can perform decoding or decompression based on the HTTP `Content-Encoding` header (e.g., `gzip`, `deflate`, `br`, or `zstd`). The library must read compressed data from the network and decompress it until the requested chunk size is met. Any resulting decompressed data that exceeds the requested amount is held in an internal buffer for the next read operation.\n\nThe decompression logic could cause urllib3 to fully decode a small amount of highly compressed data in a single operation. This can result in excessive resource consumption (high CPU usage and massive memory allocation for the decompressed data; CWE-409) on the client side, even if the application only requested a small chunk of data.\n\n\n### Affected usages\n\nApplications and libraries using urllib3 version 2.5.0 and earlier to stream large compressed responses or content from untrusted sources.\n\n`stream()`, `read(amt=256)`, `read1(amt=256)`, `read_chunked(amt=256)`, `readinto(b)` are examples of `urllib3.HTTPResponse` method calls using the affected logic unless decoding is disabled explicitly.\n\n\n### Remediation\n\nUpgrade to at least urllib3 v2.6.0 in which the library avoids decompressing data that exceeds the requested amount.\n\nIf your environment contains a package facilitating the Brotli encoding, upgrade to at least Brotli 1.2.0 or brotlicffi 1.2.0.0 too. These versions are enforced by the `urllib3[brotli]` extra in the patched versions of urllib3.\n\n\n### Credits\n\nThe issue was reported by @Cycloctane.\nSupplemental information was provided by @stamparm during a security audit performed by [7ASecurity](https://7asecurity.com/) and facilitated by [OSTIF](https://ostif.org/).",
            "id": "GHSA-2xpw-w6gg-jr37",
            "modified": "2026-02-04T02:36:12.983430Z",
            "published": "2025-12-05T18:15:54Z",
            "references": [
              {
                "type": "WEB",
                "url": "https://github.com/urllib3/urllib3/security/advisories/GHSA-2xpw-w6gg-jr37"
              },
              {
                "type": "ADVISORY",
                "url": "https://nvd.nist.gov/vuln/detail/CVE-2025-66471"
              },
              {
                "type": "WEB",
                "url": "https://github.com/urllib3/urllib3/commit/c19571de34c47de3a766541b041637ba5f716ed7"
              },
              {
                "type": "PACKAGE",
                "url": "https://github.com/urllib3/urllib3"
              }
            ],
            "related": [
              "CGA-3vv3-3897-wc6m"
            ],
            "schema_version": "1.7.3",
            "severity": [
              {
                "score": "CVSS:4.0/AV:N/AC:L/AT:P/PR:N/UI:N/VC:N/VI:N/VA:H/SC:N/SI:N/SA:H",
                "type": "CVSS_V4"
              }
            ],
            "summary": "urllib3 streaming API improperly handles highly compressed data"
          }
        },
        "relationship_name": "supersedes",
        "target_state": "superseded"
      },
      "matched_claim_ids": [
        "OSV003"
      ],
      "matched_claims": [
        {
          "after": {
            "at": "2026-02-04T02:36:12.983430Z",
            "basis": "OSV advisory GHSA-2xpw-w6gg-jr37 / CVE-2025-66471 affects PyPI urllib3 1.26.5: urllib3 streaming API improperly handles highly compressed data",
            "evidence_class": "authority_feed",
            "evidence_ref": "GHSA-2xpw-w6gg-jr37",
            "state": "superseded"
          },
          "before": {
            "at": "2021-01-01T00:00:00+00:00",
            "basis": "Seed corpus imported this claim as an active memory claim.",
            "evidence_class": "user_assertion",
            "evidence_ref": "pkg:pypi/urllib3@1.26.5",
            "state": "active"
          },
          "belief_state": "superseded",
          "claim_id": "OSV003"
        }
      ],
      "status": "applied"
    },
    {
      "evidence": {
        "adapter": "osv",
        "at": "2025-09-29T21:12:31.102523Z",
        "basis": "OSV advisory GHSA-29mw-wpgm-hmr9 / CVE-2020-28500 affects npm lodash 4.17.20: Regular Expression Denial of Service (ReDoS) in lodash",
        "evidence_class": "authority_feed",
        "evidence_ref": "GHSA-29mw-wpgm-hmr9",
        "match_key": {
          "ecosystem": "npm",
          "kind": "package_version",
          "name": "lodash",
          "version": "4.17.20"
        },
        "raw": {
          "osv_url": "https://osv.dev/vulnerability/GHSA-29mw-wpgm-hmr9",
          "package": {
            "ecosystem": "npm",
            "name": "lodash",
            "version": "4.17.20"
          },
          "result_vuln_count": 5,
          "vulnerability": {
            "affected": [
              {
                "database_specific": {
                  "source": "https://github.com/github/advisory-database/blob/main/advisories/github-reviewed/2022/01/GHSA-29mw-wpgm-hmr9/GHSA-29mw-wpgm-hmr9.json"
                },
                "package": {
                  "ecosystem": "npm",
                  "name": "lodash",
                  "purl": "pkg:npm/lodash"
                },
                "ranges": [
                  {
                    "events": [
                      {
                        "introduced": "4.0.0"
                      },
                      {
                        "fixed": "4.17.21"
                      }
                    ],
                    "type": "SEMVER"
                  }
                ]
              },
              {
                "database_specific": {
                  "source": "https://github.com/github/advisory-database/blob/main/advisories/github-reviewed/2022/01/GHSA-29mw-wpgm-hmr9/GHSA-29mw-wpgm-hmr9.json"
                },
                "package": {
                  "ecosystem": "npm",
                  "name": "lodash-es",
                  "purl": "pkg:npm/lodash-es"
                },
                "ranges": [
                  {
                    "events": [
                      {
                        "introduced": "4.0.0"
                      },
                      {
                        "fixed": "4.17.21"
                      }
                    ],
                    "type": "SEMVER"
                  }
                ]
              },
              {
                "database_specific": {
                  "source": "https://github.com/github/advisory-database/blob/main/advisories/github-reviewed/2022/01/GHSA-29mw-wpgm-hmr9/GHSA-29mw-wpgm-hmr9.json"
                },
                "package": {
                  "ecosystem": "npm",
                  "name": "lodash.trimend",
                  "purl": "pkg:npm/lodash.trimend"
                },
                "ranges": [
                  {
                    "events": [
                      {
                        "introduced": "4.0.0"
                      },
                      {
                        "last_affected": "4.5.1"
                      }
                    ],
                    "type": "SEMVER"
                  }
                ]
              },
              {
                "database_specific": {
                  "source": "https://github.com/github/advisory-database/blob/main/advisories/github-reviewed/2022/01/GHSA-29mw-wpgm-hmr9/GHSA-29mw-wpgm-hmr9.json"
                },
                "package": {
                  "ecosystem": "npm",
                  "name": "lodash.trim",
                  "purl": "pkg:npm/lodash.trim"
                },
                "ranges": [
                  {
                    "events": [
                      {
                        "introduced": "4.0.0"
                      },
                      {
                        "last_affected": "4.5.1"
                      }
                    ],
                    "type": "SEMVER"
                  }
                ]
              },
              {
                "database_specific": {
                  "source": "https://github.com/github/advisory-database/blob/main/advisories/github-reviewed/2022/01/GHSA-29mw-wpgm-hmr9/GHSA-29mw-wpgm-hmr9.json"
                },
                "package": {
                  "ecosystem": "RubyGems",
                  "name": "lodash-rails",
                  "purl": "pkg:gem/lodash-rails"
                },
                "ranges": [
                  {
                    "events": [
                      {
                        "introduced": "4.0.0"
                      },
                      {
                        "fixed": "4.17.21"
                      }
                    ],
                    "type": "ECOSYSTEM"
                  }
                ],
                "versions": [
                  "4.0.0",
                  "4.11.2",
                  "4.12.0",
                  "4.13.1",
                  "4.14.1",
                  "4.15.0",
                  "4.16.1",
                  "4.16.3",
                  "4.16.4",
                  "4.16.6",
                  "4.17.10",
                  "4.17.11",
                  "4.17.14",
                  "4.17.15",
                  "4.17.2",
                  "4.17.4",
                  "4.17.5",
                  "4.3.0",
                  "4.5.1",
                  "4.6.1"
                ]
              }
            ],
            "aliases": [
              "CVE-2020-28500"
            ],
            "database_specific": {
              "cwe_ids": [
                "CWE-1333",
                "CWE-400"
              ],
              "github_reviewed": true,
              "github_reviewed_at": "2021-03-19T22:45:28Z",
              "nvd_published_at": "2021-02-15T11:15:00Z",
              "severity": "MODERATE"
            },
            "details": "All versions of package lodash prior to 4.17.21 are vulnerable to Regular Expression Denial of Service (ReDoS) via the `toNumber`, `trim` and `trimEnd` functions. \n\nSteps to reproduce (provided by reporter Liyuan Chen):\n```js\nvar lo = require('lodash');\n\nfunction build_blank(n) {\n    var ret = \"1\"\n    for (var i = 0; i < n; i++) {\n        ret += \" \"\n    }\n    return ret + \"1\";\n}\nvar s = build_blank(50000) var time0 = Date.now();\nlo.trim(s) \nvar time_cost0 = Date.now() - time0;\nconsole.log(\"time_cost0: \" + time_cost0);\nvar time1 = Date.now();\nlo.toNumber(s) var time_cost1 = Date.now() - time1;\nconsole.log(\"time_cost1: \" + time_cost1);\nvar time2 = Date.now();\nlo.trimEnd(s);\nvar time_cost2 = Date.now() - time2;\nconsole.log(\"time_cost2: \" + time_cost2);\n```",
            "id": "GHSA-29mw-wpgm-hmr9",
            "modified": "2025-09-29T21:12:31.102523Z",
            "published": "2022-01-06T20:30:46Z",
            "references": [
              {
                "type": "ADVISORY",
                "url": "https://nvd.nist.gov/vuln/detail/CVE-2020-28500"
              },
              {
                "type": "WEB",
                "url": "https://github.com/github/advisory-database/pull/6139"
              },
              {
                "type": "WEB",
                "url": "https://github.com/lodash/lodash/pull/5065"
              },
              {
                "type": "WEB",
                "url": "https://github.com/lodash/lodash/pull/5065/commits/02906b8191d3c100c193fe6f7b27d1c40f200bb7"
              },
              {
                "type": "WEB",
                "url": "https://github.com/lodash/lodash/commit/c4847ebe7d14540bb28a8b932a9ce1b9ecbfee1a"
              },
              {
                "type": "WEB",
                "url": "https://www.oracle.com/security-alerts/cpuoct2021.html"
              },
              {
                "type": "WEB",
                "url": "https://www.oracle.com/security-alerts/cpujul2022.html"
              },
              {
                "type": "WEB",
                "url": "https://www.oracle.com/security-alerts/cpujan2022.html"
              },
              {
                "type": "WEB",
                "url": "https://www.oracle.com//security-alerts/cpujul2021.html"
              },
              {
                "type": "WEB",
                "url": "https://snyk.io/vuln/SNYK-JS-LODASH-1018905"
              },
              {
                "type": "WEB",
                "url": "https://snyk.io/vuln/SNYK-JAVA-ORGWEBJARSNPM-1074893"
              },
              {
                "type": "WEB",
                "url": "https://snyk.io/vuln/SNYK-JAVA-ORGWEBJARSBOWERGITHUBLODASH-1074895"
              },
              {
                "type": "WEB",
                "url": "https://snyk.io/vuln/SNYK-JAVA-ORGWEBJARSBOWER-1074892"
              },
              {
                "type": "WEB",
                "url": "https://snyk.io/vuln/SNYK-JAVA-ORGWEBJARS-1074894"
              },
              {
                "type": "WEB",
                "url": "https://snyk.io/vuln/SNYK-JAVA-ORGFUJIONWEBJARS-1074896"
              },
              {
                "type": "WEB",
                "url": "https://security.netapp.com/advisory/ntap-20210312-0006"
              },
              {
                "type": "WEB",
                "url": "https://github.com/rubysec/ruby-advisory-db/blob/master/gems/lodash-rails/CVE-2020-28500.yml"
              },
              {
                "type": "WEB",
                "url": "https://github.com/lodash/lodash/blob/npm/trimEnd.js%23L8"
              },
              {
                "type": "PACKAGE",
                "url": "https://github.com/lodash/lodash"
              },
              {
                "type": "WEB",
                "url": "https://cert-portal.siemens.com/productcert/pdf/ssa-637483.pdf"
              }
            ],
            "schema_version": "1.7.3",
            "severity": [
              {
                "score": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L",
                "type": "CVSS_V3"
              }
            ],
            "summary": "Regular Expression Denial of Service (ReDoS) in lodash"
          }
        },
        "relationship_name": "supersedes",
        "target_state": "superseded"
      },
      "matched_claim_ids": [
        "OSV004"
      ],
      "matched_claims": [
        {
          "after": {
            "at": "2025-09-29T21:12:31.102523Z",
            "basis": "OSV advisory GHSA-29mw-wpgm-hmr9 / CVE-2020-28500 affects npm lodash 4.17.20: Regular Expression Denial of Service (ReDoS) in lodash",
            "evidence_class": "authority_feed",
            "evidence_ref": "GHSA-29mw-wpgm-hmr9",
            "state": "superseded"
          },
          "before": {
            "at": "2020-01-01T00:00:00+00:00",
            "basis": "Seed corpus imported this claim as an active memory claim.",
            "evidence_class": "user_assertion",
            "evidence_ref": "pkg:npm/lodash@4.17.20",
            "state": "active"
          },
          "belief_state": "superseded",
          "claim_id": "OSV004"
        }
      ],
      "status": "applied"
    },
    {
      "evidence": {
        "adapter": "osv",
        "at": "2026-03-13T22:11:31.390433Z",
        "basis": "OSV advisory GHSA-vh95-rmgr-6w4m / CVE-2020-7598 affects npm minimist 0.0.8: Prototype Pollution in minimist",
        "evidence_class": "authority_feed",
        "evidence_ref": "GHSA-vh95-rmgr-6w4m",
        "match_key": {
          "ecosystem": "npm",
          "kind": "package_version",
          "name": "minimist",
          "version": "0.0.8"
        },
        "raw": {
          "osv_url": "https://osv.dev/vulnerability/GHSA-vh95-rmgr-6w4m",
          "package": {
            "ecosystem": "npm",
            "name": "minimist",
            "version": "0.0.8"
          },
          "result_vuln_count": 2,
          "vulnerability": {
            "affected": [
              {
                "database_specific": {
                  "source": "https://github.com/github/advisory-database/blob/main/advisories/github-reviewed/2020/04/GHSA-vh95-rmgr-6w4m/GHSA-vh95-rmgr-6w4m.json"
                },
                "package": {
                  "ecosystem": "npm",
                  "name": "minimist",
                  "purl": "pkg:npm/minimist"
                },
                "ranges": [
                  {
                    "events": [
                      {
                        "introduced": "0"
                      },
                      {
                        "fixed": "0.2.1"
                      }
                    ],
                    "type": "SEMVER"
                  }
                ]
              },
              {
                "database_specific": {
                  "source": "https://github.com/github/advisory-database/blob/main/advisories/github-reviewed/2020/04/GHSA-vh95-rmgr-6w4m/GHSA-vh95-rmgr-6w4m.json"
                },
                "package": {
                  "ecosystem": "npm",
                  "name": "minimist",
                  "purl": "pkg:npm/minimist"
                },
                "ranges": [
                  {
                    "events": [
                      {
                        "introduced": "1.0.0"
                      },
                      {
                        "fixed": "1.2.3"
                      }
                    ],
                    "type": "SEMVER"
                  }
                ]
              }
            ],
            "aliases": [
              "CVE-2020-7598"
            ],
            "database_specific": {
              "cwe_ids": [
                "CWE-1321"
              ],
              "github_reviewed": true,
              "github_reviewed_at": "2020-04-03T21:42:08Z",
              "nvd_published_at": "2020-03-11T23:15:00Z",
              "severity": "MODERATE"
            },
            "details": "Affected versions of `minimist` are vulnerable to prototype pollution. Arguments are not properly sanitized, allowing an attacker to modify the prototype of `Object`, causing the addition or modification of an existing property that will exist on all objects.  \nParsing the argument `--__proto__.y=Polluted` adds a `y` property with value `Polluted` to all objects. The argument `--__proto__=Polluted` raises and uncaught error and crashes the application.  \nThis is exploitable if attackers have control over the arguments being passed to `minimist`.\n\n\n## Recommendation\n\nUpgrade to versions 0.2.1, 1.2.3 or later.",
            "id": "GHSA-vh95-rmgr-6w4m",
            "modified": "2026-03-13T22:11:31.390433Z",
            "published": "2020-04-03T21:48:32Z",
            "references": [
              {
                "type": "ADVISORY",
                "url": "https://nvd.nist.gov/vuln/detail/CVE-2020-7598"
              },
              {
                "type": "WEB",
                "url": "https://github.com/minimistjs/minimist/commit/10bd4cdf49d9686d48214be9d579a9cdfda37c68"
              },
              {
                "type": "WEB",
                "url": "https://github.com/minimistjs/minimist/commit/38a4d1caead72ef99e824bb420a2528eec03d9ab"
              },
              {
                "type": "WEB",
                "url": "https://github.com/minimistjs/minimist/commit/4cf1354839cb972e38496d35e12f806eea92c11f#diff-a1e0ee62c91705696ddb71aa30ad4f95"
              },
              {
                "type": "WEB",
                "url": "https://github.com/minimistjs/minimist/commit/63e7ed05aa4b1889ec2f3b196426db4500cbda94"
              },
              {
                "type": "PACKAGE",
                "url": "https://github.com/substack/minimist"
              },
              {
                "type": "WEB",
                "url": "https://snyk.io/vuln/SNYK-JS-MINIMIST-559764"
              },
              {
                "type": "WEB",
                "url": "https://www.npmjs.com/advisories/1179"
              },
              {
                "type": "WEB",
                "url": "http://lists.opensuse.org/opensuse-security-announce/2020-06/msg00024.html"
              }
            ],
            "schema_version": "1.7.5",
            "severity": [
              {
                "score": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:L",
                "type": "CVSS_V3"
              }
            ],
            "summary": "Prototype Pollution in minimist"
          }
        },
        "relationship_name": "supersedes",
        "target_state": "superseded"
      },
      "matched_claim_ids": [
        "OSV005"
      ],
      "matched_claims": [
        {
          "after": {
            "at": "2026-03-13T22:11:31.390433Z",
            "basis": "OSV advisory GHSA-vh95-rmgr-6w4m / CVE-2020-7598 affects npm minimist 0.0.8: Prototype Pollution in minimist",
            "evidence_class": "authority_feed",
            "evidence_ref": "GHSA-vh95-rmgr-6w4m",
            "state": "superseded"
          },
          "before": {
            "at": "2013-01-01T00:00:00+00:00",
            "basis": "Seed corpus imported this claim as an active memory claim.",
            "evidence_class": "user_assertion",
            "evidence_ref": "pkg:npm/minimist@0.0.8",
            "state": "active"
          },
          "belief_state": "superseded",
          "claim_id": "OSV005"
        }
      ],
      "status": "applied"
    }
  ],
  "status": "complete_live_osv_authority_adapter",
  "summary": {
    "active_claims": 5,
    "claims": 10,
    "evidence_items": 5,
    "superseded_claims": 5
  }
}
```

## Verification So Far

- `.\.venv\Scripts\python.exe -m groundtruth.p5 --results-v3-p5` completed and regenerated `data/osv_seed_corpus.json`, `data/osv_cve_run.json`, and this document from live keyless OSV.dev package/version queries.
- `.\.venv\Scripts\pytest.exe -q tests\test_authority_adapters.py tests\test_osv_adapter.py tests\test_authority_engine.py tests\test_p5_artifacts.py` -> 9 passed in 0.11s.
- `ruff check groundtruth\adapters groundtruth\p5.py tests\test_authority_adapters.py tests\test_osv_adapter.py tests\test_authority_engine.py tests\test_p5_artifacts.py` -> all checks passed.
- `.\.venv\Scripts\python.exe -m compileall -q groundtruth\adapters groundtruth\p5.py tests\test_authority_adapters.py tests\test_osv_adapter.py tests\test_authority_engine.py tests\test_p5_artifacts.py` -> passed.
- `ruff check groundtruth tests web` -> all checks passed.
- `.\.venv\Scripts\python.exe -m compileall -q groundtruth tests web` -> passed.
- `git diff --check` -> passed.
- `.\.venv\Scripts\pytest.exe -q --durations=10` -> 65 passed, 13 warnings in 128.28s (0:02:08).
- Artifact smoke: `data/osv_seed_corpus.json` has 10 active seed claims; `data/osv_cve_run.json` summary is `claims=10`, `evidence_items=5`, `superseded_claims=5`, `active_claims=5`; transcript changes jinja2 2.4.1 from `active` to `superseded`; shared engine demo adapters are `retraction_watch` and `osv`.
