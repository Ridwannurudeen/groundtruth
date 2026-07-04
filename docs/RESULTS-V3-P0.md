# GroundTruth V3 P0 Results

Generated: 2026-07-04
Status: `partial_quota_stop_with_relevance_fix`

## Baseline

Command:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Result:

```text
28 passed, 12 warnings in 139.42s (0:02:19)
```

Verified runtime:

```text
Python 3.12.10
Cognee 1.2.2
LLM_PROVIDER=gemini
LLM_MODEL=gemini/gemini-2.5-flash-lite
EMBEDDING_PROVIDER=fastembed
EMBEDDING_MODEL=BAAI/bge-small-en
```

## V2 Resume Attempt

Command:

```powershell
$env:PYTHONIOENCODING='utf-8'; .\.venv\Scripts\python.exe -m groundtruth.v2
```

Single-command reproduction window:

```text
Started: 2026-07-04T19:04:06Z
Artifact generated: 2026-07-04T19:08:28.114967+00:00
Approx wall-clock: 4m22s
```

Result from `data/v2_results.json`:

```json
{
  "status": "partial_quota_stop",
  "stop_reason": "quota",
  "evaluation_coverage": {
    "all_pair_total": 28,
    "candidate_pairs": 28,
    "claims": 8,
    "evaluated_pairs": 21,
    "manifest_pairs": 28,
    "manifest_pairs_not_candidates": [],
    "pending_pairs": [
      "V2C001::V2C007",
      "V2C001::V2C008",
      "V2C002::V2C007",
      "V2C004::V2C006",
      "V2C005::V2C007",
      "V2C006::V2C007",
      "V2C006::V2C008"
    ],
    "planned_pairs": 28,
    "protocol": "exhaustive_all_pairs_over_committed_v2_claims",
    "unlabeled_candidate_pairs": []
  },
  "semantic_metrics": {
    "evaluated_pairs": 21,
    "false_negative": 1,
    "false_positive": 0,
    "precision": 1.0,
    "recall": 0.6666666666666666,
    "true_negative": 18,
    "true_positive": 2
  },
  "answer_probes": 0
}
```

Provider stop transcript excerpt:

```text
litellm.RateLimitError: geminiException
code: 429
status: RESOURCE_EXHAUSTED
quotaMetric: generativelanguage.googleapis.com/generate_content_free_tier_requests
quotaValue: 20
```

No pending V2 pair was fabricated. The 21 signed cache entries remain reusable; the 7 pairs above still require live quota.

## Retrieval Relevance Fix

Diagnosis:

- Cognee `GRAPH_COMPLETION` with `only_context=True` skips completion, so relevance can be tested without answer-generation quota.
- Cognee vector retrieval found candidates, but the ID-filtered graph projection returned empty and fell back to full-graph retrieval.
- Before the fix, `answer()` surfaced every graph-mapped reference from that fallback, so the V2 probes included unrelated claims even when the top reference was correct.

Fix:

- Added relevance ranking in `groundtruth.answer.rank_graph_references`.
- Ranking is applied only to references already derived from Cognee graph edges.
- `raw_graph_references` remains in the answer payload for audit.

Probe transcript after the fix:

```json
[
  {
    "question_id": "V2Q01",
    "target_claim_ids": ["V2C001", "V2C002"],
    "raw_graph_references": ["V2C002", "V2C006", "V2C005", "V2C001", "V2C003", "V2C004", "V2C007", "V2C008"],
    "ranked_references": ["V2C002", "V2C001", "V2C005", "V2C006", "V2C003"],
    "top_reference": "V2C002",
    "top_is_target": true
  },
  {
    "question_id": "V2Q02",
    "target_claim_ids": ["V2C003", "V2C004"],
    "raw_graph_references": ["V2C004", "V2C003", "V2C002", "V2C007", "V2C008", "V2C001", "V2C006", "V2C005"],
    "ranked_references": ["V2C004", "V2C003", "V2C002", "V2C008", "V2C001"],
    "top_reference": "V2C004",
    "top_is_target": true
  },
  {
    "question_id": "V2Q03",
    "target_claim_ids": ["V2C005", "V2C006"],
    "raw_graph_references": ["V2C006", "V2C005", "V2C002", "V2C004", "V2C001", "V2C003", "V2C008", "V2C007"],
    "ranked_references": ["V2C006", "V2C005", "V2C002", "V2C001"],
    "top_reference": "V2C006",
    "top_is_target": true
  }
]
```

Gate result: all 3 named-entity probes return an on-topic target as the top ranked reference. The raw full-graph fallback remains visible rather than hidden.

## Benchmark Regeneration

Command:

```powershell
$env:PYTHONIOENCODING='utf-8'; .\.venv\Scripts\python.exe -m groundtruth.benchmark --skip-prepare
```

Result from `data/benchmark_results.json`:

```json
{
  "control_claim_retention": 5,
  "control_claim_total": 5,
  "correctness_judge": "skipped_quota_disclosed",
  "groundtruth_cites_retracted": 0,
  "naive_cites_retracted": 18,
  "rows": 40,
  "total_questions": 20
}
```

The previous headline changed from 20 of 20 to 18/20 for naive memory because the metric now scores relevance-ranked graph references, not every raw full-graph fallback reference. GroundTruth remains 0/20, and controls remain 5/5.

## Files Updated

- `groundtruth/answer.py`
- `groundtruth/benchmark.py`
- `groundtruth/v2.py`
- `tests/test_answer.py`
- `tests/test_web.py`
- `README.md`
- `docs/BENCHMARK.md`
- `docs/RESULTS-FIX.md`
- `docs/RESULTS-V2.md`
- `docs/DEMO.md`
- `data/benchmark_results.json`
- `data/v2_results.json`
- `data/v2_semantic_judgments.json`
- `web/static/index.html`

## Final Verification

```text
ruff format groundtruth tests web -> 21 files left unchanged
ruff check groundtruth tests web -> All checks passed
git diff --check -> clean
rg stale headline scan -> no stale 20/20 or old metric wording
.\.venv\Scripts\python.exe -m pytest -q -> 29 passed, 12 warnings in 91.81s
.\.venv\Scripts\python.exe -m compileall -q groundtruth web tests -> clean
.\.venv\Scripts\python.exe -m pip check -> No broken requirements found
```
