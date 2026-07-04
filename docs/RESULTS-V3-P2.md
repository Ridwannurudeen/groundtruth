# GroundTruth V3 P2 Results

Generated: 2026-07-04
Status: `complete`

## Gate

- Confidence bands are implemented in `groundtruth.contest.semantic_action`: `<0.7` log-only, `0.7-0.9` contested, directional `>=0.9` auto-act, and high-confidence `mutual` remains contested.
- Cached V2 evidence was materialized without a provider call:
  - `V2C001` is `superseded` by `V2C002` from semantic inference `pair:V2C001::V2C002`.
  - `V2C003::V2C004` is an open contested pair in `data/contested_pairs.json`.
  - V2 registry state counts: `active=5`, `contested=2`, `superseded=1`, `retracted=0`, `purged=0`.
- `GET /contested` returns the open queue; `POST /adjudicate` is mutation-confirmed and records `user_assertion` state changes.
- Answer references now warn when `belief_state == contested` and include `cites_contested` / `contested_dois`.
- Feedback wiring is verified with Cognee's installed `extract_feedback_qas`, `apply_feedback_weights`, and graph ranking blend, without LLM calls.

## Lifecycle Transcript

Source row: cached V2 semantic judgment from `data/v2_results.json`, pair `V2C003::V2C004`.

Detect:

```json
{
  "pair": "V2C003::V2C004",
  "action": "contested",
  "confidence": 1.0,
  "direction": "mutual",
  "evidence_ref": "pair:V2C003::V2C004"
}
```

Contested answer before adjudication:

```text
groundtruth_v2_semantic_memory retrieved 10.1161/JAHA.119.013543, but the registry marks that source as contested. Basis: Semantic inference for V2C003::V2C004 landed in the contested band (confidence 1.00, direction mutual); basis: Both claims evaluate the effect of marine omega-3 (n-3) fatty acid supplementation on cardiovascular events...
```

Adjudicate in a temporary registry copy:

```json
{
  "verdict": "none",
  "evidence_class": "user_assertion",
  "evidence_ref": "adjudication:V2C003::V2C004",
  "state_changes": [
    {"claim_id": "V2C004", "state": "active"},
    {"claim_id": "V2C003", "state": "active"}
  ],
  "forget_results": []
}
```

Resolved answer after adjudication:

```text
groundtruth_v2_semantic_memory cites an active remembered source for 10.1161/JAHA.119.013543 from Journal of the American Heart Association.
```

The committed queue intentionally remains open so the UI can demonstrate adjudication; the full resolution path above was run against temporary files.

## Feedback Effect

No LLM was used. `tests/test_p2_feedback_wiring_no_llm.py` stores a session QA with graph IDs, extracts it through Cognee's feedback task, applies `feedback_score=5` with `alpha=1.0`, and verifies:

```text
node feedback weight n1: 0.5 -> 1.0
edge feedback weight e1: 0.5 -> 1.0
top edge with feedback_influence=0.0: close-low-feedback
top edge with feedback_influence=1.0: far-high-feedback
```

## Verification So Far

Focused P2 command:

```powershell
.\.venv\Scripts\pytest.exe -q tests\test_contest.py tests\test_answer.py::test_contested_warning_uses_reference_belief_state tests\test_web.py::test_contested_endpoint_lists_open_pairs tests\test_web.py::test_adjudicate_endpoint_requires_mutation_confirmation tests\test_web.py::test_adjudicate_endpoint_resolves_pair tests\test_web.py::test_index_serves_contested_mount_points tests\test_p2_feedback_wiring_no_llm.py
```

Result:

```text
9 passed, 12 warnings in 6.58s
```

Static checks:

```powershell
.\.venv\Scripts\python.exe -m compileall -q groundtruth tests web
git diff --check
```

Result:

```text
passed
```

Full suite:

```powershell
.\.venv\Scripts\pytest.exe -q --durations=10
```

Result:

```text
40 passed, 13 warnings in 95.80s (0:01:35)
```
