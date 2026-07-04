# GroundTruth V3 P3 Results

Generated: 2026-07-04T22:59:03.864793+00:00
Status: `complete_session_executed_fixture`

## Gate

- Evening evidence is represented as a session-only Cognee `remember` call with `self_improvement=False`.
- The public Cognee `improve(dataset, session_ids=[...])` bridge is recorded but not executed in the scripted artifact because installed Cognee 1.2.2 can enter LLM-backed session distillation/cognify stages.
- The before/after answer transcript is a deterministic fixture over an isolated registry transition, preserving committed P0-P2 data.
- The briefing artifact is written to `MORNING_BRIEFING.md`; `GET /briefing` exposes a current projection seeded by the artifact transcript.

## Command

```powershell
.\.venv\Scripts\python.exe -m groundtruth.briefing --results-v3-p3
```

## Session And Bridge

```json
{
  "bridge": {
    "call_shape": "cognee.improve(dataset=dataset_name, session_ids=[session_id])",
    "dataset": "groundtruth_memory",
    "reason": "Cognee 1.2.2 public improve(session_ids=...) was source-verified to run session persistence, distillation, and default enrichment stages that can consume LLM quota. The scripted P3 artifact records the bridge boundary and performs deterministic registry reconciliation.",
    "session_ids": [
      "analyst-2026-07-04"
    ],
    "status": "recorded_not_executed"
  },
  "session_remember": {
    "dataset": "groundtruth_memory",
    "results": [
      {
        "dataset_id": null,
        "dataset_name": "groundtruth_memory",
        "elapsed_seconds": 0.0,
        "items_processed": 0,
        "pipeline_run_id": null,
        "session_ids": [
          "analyst-2026-07-04"
        ],
        "status": "session_stored"
      }
    ],
    "self_improvement": false,
    "session_id": "analyst-2026-07-04",
    "source_claim_id": "R001",
    "source_registry_path": "C:\\Users\\gudma\\OneDrive\\Desktop\\GITHUB-FILES\\groundtruth\\data\\claims.json",
    "status": "executed",
    "texts": [
      "Retraction Watch notice 10.1056/nejme2608684 says original DOI 10.1056/nejmoa2023386 was retracted. Reason: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);"
    ]
  }
}
```

## Deterministic Before/After Transcript

Question: `What does the memory say about Avacopan for the Treatment of ANCA-Associated Vasculitis?`

Before:

```text
groundtruth_memory still cites the active claim 10.1056/nejmoa2023386 from NEJM: The New England Journal of Medicine: The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.
```

After:

```text
groundtruth_memory no longer cites original DOI 10.1056/nejmoa2023386. The belief is retracted by authority_feed evidence 10.1056/nejme2608684: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);
```

## Briefing JSON

```json
{
  "after_answer": "groundtruth_memory no longer cites original DOI 10.1056/nejmoa2023386. The belief is retracted by authority_feed evidence 10.1056/nejme2608684: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);",
  "before_answer": "groundtruth_memory still cites the active claim 10.1056/nejmoa2023386 from NEJM: The New England Journal of Medicine: The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.",
  "bridge": {
    "call_shape": "cognee.improve(dataset=dataset_name, session_ids=[session_id])",
    "dataset": "groundtruth_memory",
    "reason": "Cognee 1.2.2 public improve(session_ids=...) was source-verified to run session persistence, distillation, and default enrichment stages that can consume LLM quota. The scripted P3 artifact records the bridge boundary and performs deterministic registry reconciliation.",
    "session_ids": [
      "analyst-2026-07-04"
    ],
    "status": "recorded_not_executed"
  },
  "dataset": "groundtruth_memory",
  "generated_at": "2026-07-04T22:59:03.864793+00:00",
  "learned_last_night": [
    {
      "basis": "Retraction Watch notice 10.1056/nejme2608684 says original DOI 10.1056/nejmoa2023386 was retracted. Reason: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);",
      "belief_state": "active",
      "changed_at": "2026-06-29T00:00:00+00:00",
      "claim_id": "R001",
      "doi": "10.1056/nejme2608684",
      "evidence_class": "authority_feed",
      "evidence_ref": "10.1056/nejme2608684",
      "session_id": "analyst-2026-07-04",
      "title": "Retraction notice for Avacopan for the Treatment of ANCA-Associated Vasculitis"
    }
  ],
  "now_contested": [
    {
      "basis": "Semantic inference for V2C003::V2C004 landed in the contested band (confidence 1.00, direction mutual); basis: Both claims evaluate the effect of marine omega-3 (n-3) fatty acid supplementation on cardiovascular events. Claim A asserts that supplementation lowers the risk for several cardiovascular outcomes (myocardial infarction, coronary heart disease death, cardiovascular disease death, and total cardiovascular disease). Claim B, conversely, states that marine n-3 fatty acid supplementation does not lower the incidence of major cardiovascular events compared with placebo. These are directly contradictory findings regarding the efficacy of marine omega-3 supplementation for cardiovascular disease prevention.",
      "belief_state": "contested",
      "changed_at": "2026-07-04T21:03:35.457405+00:00",
      "claim_id": "V2C003::V2C004",
      "claims": [
        {
          "belief_state": "contested",
          "claim_id": "V2C004",
          "doi": "10.1161/JAHA.119.013543",
          "journal": "Journal of the American Heart Association",
          "latest_state_change": {
            "at": "2026-07-04T21:03:35.457405+00:00",
            "basis": "Semantic inference for V2C003::V2C004 landed in the contested band (confidence 1.00, direction mutual); basis: Both claims evaluate the effect of marine omega-3 (n-3) fatty acid supplementation on cardiovascular events. Claim A asserts that supplementation lowers the risk for several cardiovascular outcomes (myocardial infarction, coronary heart disease death, cardiovascular disease death, and total cardiovascular disease). Claim B, conversely, states that marine n-3 fatty acid supplementation does not lower the incidence of major cardiovascular events compared with placebo. These are directly contradictory findings regarding the efficacy of marine omega-3 supplementation for cardiovascular disease prevention.",
            "evidence_class": "semantic_inference",
            "evidence_ref": "pair:V2C003::V2C004",
            "state": "contested"
          },
          "title": "Marine Omega-3 Supplementation and Cardiovascular Disease"
        },
        {
          "belief_state": "contested",
          "claim_id": "V2C003",
          "doi": "10.1056/NEJMoa1811403",
          "journal": "New England Journal of Medicine",
          "latest_state_change": {
            "at": "2026-07-04T21:03:35.457405+00:00",
            "basis": "Semantic inference for V2C003::V2C004 landed in the contested band (confidence 1.00, direction mutual); basis: Both claims evaluate the effect of marine omega-3 (n-3) fatty acid supplementation on cardiovascular events. Claim A asserts that supplementation lowers the risk for several cardiovascular outcomes (myocardial infarction, coronary heart disease death, cardiovascular disease death, and total cardiovascular disease). Claim B, conversely, states that marine n-3 fatty acid supplementation does not lower the incidence of major cardiovascular events compared with placebo. These are directly contradictory findings regarding the efficacy of marine omega-3 supplementation for cardiovascular disease prevention.",
            "evidence_class": "semantic_inference",
            "evidence_ref": "pair:V2C003::V2C004",
            "state": "contested"
          },
          "title": "Marine n-3 Fatty Acids and Prevention of Cardiovascular Disease and Cancer"
        }
      ],
      "doi": null,
      "evidence_class": "semantic_inference",
      "evidence_ref": "pair:V2C003::V2C004",
      "pair": "V2C003::V2C004",
      "title": "Marine Omega-3 Supplementation and Cardiovascular Disease vs Marine n-3 Fatty Acids and Prevention of Cardiovascular Disease and Cancer"
    }
  ],
  "purged": [
    {
      "basis": "Retraction Watch record 10.1056/nejme2608684 supersedes original DOI 10.1056/nejmoa2023386; reason: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);",
      "belief_state": "retracted",
      "changed_at": "2026-06-29T00:00:00+00:00",
      "claim_id": "R001",
      "doi": "10.1056/nejmoa2023386",
      "evidence_class": "authority_feed",
      "evidence_ref": "10.1056/nejme2608684",
      "journal": "NEJM: The New England Journal of Medicine",
      "memory_status": "retracted_forgotten",
      "status": "retracted_forgotten",
      "title": "Avacopan for the Treatment of ANCA-Associated Vasculitis"
    }
  ],
  "question": "What does the memory say about Avacopan for the Treatment of ANCA-Associated Vasculitis?",
  "revised": [
    {
      "basis": "Retraction Watch record 10.1056/nejme2608684 supersedes original DOI 10.1056/nejmoa2023386; reason: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);",
      "belief_state": "retracted",
      "changed_at": "2026-06-29T00:00:00+00:00",
      "claim_id": "R001",
      "doi": "10.1056/nejmoa2023386",
      "evidence_class": "authority_feed",
      "evidence_ref": "10.1056/nejme2608684",
      "journal": "NEJM: The New England Journal of Medicine",
      "memory_status": "retracted_forgotten",
      "status": "retracted_forgotten",
      "title": "Avacopan for the Treatment of ANCA-Associated Vasculitis"
    },
    {
      "basis": "Semantic inference for V2C001::V2C002 auto-superseded V2C001 with confidence 0.90; basis: Claim A, a systematic review and meta-analysis published in 2020, synthesizes evidence that Vitamin D supplementation appears to reduce progression to type 2 diabetes in people with prediabetes. Claim B, from a 2019 randomized controlled trial (the D2d study), specifically states that Vitamin D3 supplementation at 4000 IU per day does not significantly lower diabetes risk in adults at high risk. Given that Claim A is a more recent meta-analysis, it likely incorporated the findings of the D2d study (Claim B's source) along with other relevant studies to provide a more comprehensive and statistically robust overall estimate of effect. Therefore, its conclusion, representing a broader synthesis of evidence, supersedes the finding of a single trial, even a large one.",
      "belief_state": "superseded",
      "changed_at": "2026-07-04T21:03:35.457405+00:00",
      "claim_id": "V2C001",
      "doi": "10.1056/NEJMoa1900906",
      "evidence_class": "semantic_inference",
      "evidence_ref": "pair:V2C001::V2C002",
      "journal": "New England Journal of Medicine",
      "memory_status": null,
      "status": "active",
      "title": "Vitamin D Supplementation and Prevention of Type 2 Diabetes"
    }
  ],
  "session_id": "analyst-2026-07-04",
  "status": "complete_session_executed_fixture"
}
```

## Verification So Far

- Focused P3/web command:

```powershell
.\.venv\Scripts\pytest.exe -q tests\test_briefing.py tests\test_web.py
```

Result:

```text
16 passed, 1 warning in 0.32s
```

- Static checks:

```powershell
ruff check groundtruth tests web
.\.venv\Scripts\python.exe -m compileall -q groundtruth tests web
git diff --check
```

Result:

```text
passed
```

- Full suite:

```powershell
.\.venv\Scripts\pytest.exe -q --durations=10
```

Result:

```text
46 passed, 13 warnings in 120.23s (0:02:00)
```

- `/briefing` app-layer smoke:

```text
status 200
briefing status complete_session_executed_fixture_with_current_projection
now_contested=1 revised=2 purged=1
```
