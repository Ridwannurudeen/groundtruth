# GroundTruth V3 P8 Results

Generated: 2026-07-05
Status: `complete_with_failing_smoke_suite` (doc phase finished; suite shows three existing regressions)

## Commands Run

```powershell
cd C:\Users\gudma\OneDrive\Desktop\GITHUB-FILES\groundtruth
.\.venv\Scripts\pytest.exe -q
```

Result:

```text
3 failed, 62 passed, 13 warnings in 80.43s
FAILED tests/test_benchmark.py::test_committed_corpus_memory_integrity_guard
FAILED tests/test_registry.py::test_claims_registry_is_complete_and_unique
FAILED tests/test_web.py::test_state_exposes_demo_inventory
```

## Metrics Recomputed From Raw JSON

Recomputed values used in README and DEMO were not hand-edited:

```text
benchmark_summary = {
  naive_cites_retracted: 18,
  groundtruth_cites_retracted: 0,
  control_claim_retention: 5,
  control_claim_total: 5,
  correctness_judge: skipped_quota_disclosed
}
memory_integrity = {
  active_control_total: 15,
  retracted_original_total: 25,
  violations: []
}
v2_semantic_metrics = {
  precision: 1.0,
  recall: 0.6666666666666666,
  false_positive: 0,
  false_negative: 1,
  evaluated_pairs: 28
}
```

Sources:

- `data/benchmark_results.json`
- `data/v2_results.json`
- `docs/RESULTS-V2.md` (for formatted rendering of V2 probe rows)

## Traceability Map (README / VISION / DEMO)

- README headline benchmark numbers come from `data/benchmark_results.json`.
- README "remember/recall/improve/forget" map points to exact modules in `groundtruth/`.
- README evidence ladder and limitations correspond to implemented pathways in `groundtruth/beliefs.py`, `groundtruth/answer.py`, `groundtruth/contest.py`, `groundtruth/feedback.py`, `groundtruth/watcher.py`, and `groundtruth/briefing.py`.
- VISION claims are architectural claims, not numeric; no recomputed metric required beyond the same artifact-backed README figures.
- DEMO flow references:
  - `/state` baseline badges from app state,
  - `/briefing` and `/briefing.md`,
  - `/contested`,
  - `/timeline`,
  - `/ask`.
  These are present in `web/app.py` and rendered in `web/static/index.html` / `web/static/app.js`.

## P8 Failures Logged in This Run

1. `tests/test_benchmark.py::test_committed_corpus_memory_integrity_guard` still expects dataset-level `violations` to be empty after retraction pipeline execution, but `retracted_original_present` remains for active datasets in current committed state.
2. `tests/test_registry.py::test_claims_registry_is_complete_and_unique` still expects at least one `retracted` claim in registry state; current registry is fully `active`.
3. `tests/test_web.py::test_state_exposes_demo_inventory` expects zero `active_retractions`; API currently returns committed pending retractions in `/state`, which matches the demo workflow used in this phase.

## P6 Decision

P6 remains dropped; there is no `groundtruth/memoryrot.py` on this branch, and no `.tmp_*` residue. The single required pass was attempted via `python -m groundtruth.memoryrot` and failed with module-missing.

## Commit Pointers

- P6 drop: `7e8bcd6`
- P8-1 (README rewrite): `8b7e636`
- P8-2 (VISION): `cb3d962`
- P8-3 (DEMO): `7a5497b`
