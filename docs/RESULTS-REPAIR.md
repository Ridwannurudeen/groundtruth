# GroundTruth Repair Report

Generated: 2026-07-05

## Incident summary

The P6 baseline restore rebuilt the live Cognee datasets in place (`naive_memory` and `groundtruth_memory`) with fresh 40-item data IDs, so the committed registry could no longer be used as-is. The committed registry had already been restored from the last good commit, so the remaining fix was to re-anchor it to the rebuilt memory and re-run lifecycle state transitions.

## R1 — Registry re-anchoring

- Reconciled every registry entry back to live memory IDs from the rebuilt datasets.
- Restored `status=active` and `belief_state=active` expectations where appropriate and preserved history with a re-anchor event.
- Re-ran dataset integrity checks for all 40 claims.

### Result

- `data/claims.json` now contains 40 entries.
- Active cohort totals: 25 retracted-original, 15 active-control.
- No missing dataset IDs and all entries resolve in live memory.
- Retraction cohort states are operationally correct for the repaired runtime.

## R2 — Retraction lifecycle replay

- Re-ran the retraction runner path across the full committed retracted cohort using existing resumable, idempotent controls.
- Re-inserted retraction notice items where needed.
- Re-added contradiction edges and applied memory-only forget in GroundTruth for all 25 retracted originals.

### Result

- `retracted_forgotten` in GroundTruth: 25/25.
- `retracted_retained` in naive memory: 25/25.
- Active controls remain retained: 15/15.
- No pending retraction lifecycle items.

## R3 — Benchmark and evidence regeneration

- Re-ran benchmark to regenerate:
  - `data/benchmark_results.json`
  - `docs/BENCHMARK.md`
  - `docs/RESULTS-FIX.md`
- Re-ran briefing and timeline snapshots after repair.

### Result

- Naive cites retracted: **18/20**
- GroundTruth cites retracted: **0/20**
- Control retention: **5/5**
- Retraction coverage: **25/25**
- Memory integrity violations: **0**.

## R4 — Recurrence guard

- Added a documented isolated-runtime override path in `groundtruth/runtime.py` (set `GROUNDTRUTH_RUNTIME_ROOT` for destructive runs).
- Added `.tmp_*` to `.gitignore` to keep temporary runtime roots out of git.

## Test gate

```powershell
cd C:\Users\gudma\OneDrive\Desktop\GITHUB-FILES\groundtruth
.venv\Scripts\python.exe -m pytest -q
```

Result: `66 passed`.
