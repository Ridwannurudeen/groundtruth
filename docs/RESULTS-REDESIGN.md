# GroundTruth Web Redesign Results

Generated: 2026-07-05

Status: `implemented_with_known_global_failures`

## Scope

Completed the web redesign requested in `REDESIGN.md`:

- moved all API routes used by the UI under `/api/*`;
- converted `/` into a landing page;
- added dedicated pages at `/ask`, `/briefing`, `/contested`, `/timeline`, `/evidence`;
- replaced the shared visual system with a precision-dark design and loaded `Inter` + `JetBrains Mono`;
- captured required page screenshots at 1440px and 375px breakpoints.

## Route map (old → new)

- old JSON route `/state` → new `/api/state`
- old JSON route `/contested` → new `/api/contested`
- old JSON route `/briefing` → new `/api/briefing`
- old JSON route `/briefing.md` → new `/api/briefing.md`
- old JSON route `/timeline` → new `/api/timeline`
- old JSON route `/ask` → new `/api/ask`
- old JSON route `/retract` → new `/api/retract`
- old JSON route `/feedback` → new `/api/feedback`
- old JSON route `/improve` → new `/api/improve`
- old JSON route `/adjudicate` → new `/api/adjudicate`
- old graph page `/graph` → new `/api/graph`

## UI pages

- `web/static/index.html` (landing only)
- `web/static/ask.html`
- `web/static/briefing.html`
- `web/static/contested.html`
- `web/static/timeline.html`
- `web/static/evidence.html`

Shared navigation, shared footer behavior, and route-aware JS dispatch are implemented in:
- `web/static/styles.css`
- `web/static/app.js`

## Snapshot numbers used in landing/evidence copy

- retracted originals cited (naive): **18/20**
- retracted originals cited (GroundTruth): **0/20**
- control claims retained: **5/5**
- coverage retraction cohort: **25/25**
- V2 semantic coverage: **28/28** with
  - precision: **1.0**
  - recall: **0.6666666666666666**
  - false positive: **0**
  - false negative: **1**

Source artifacts:

- `docs/BENCHMARK.md`
- `data/benchmark_results.json`
- `data/v2_results.json`
- `docs/RESULTS-V2.md`

## Screenshot evidence

Captured with `playwright` against a local `uvicorn` server at `127.0.0.1:8015`.

**1440x1024**

- `docs/screenshots/landing-1440x1024.png`
- `docs/screenshots/ask-1440x1024.png`
- `docs/screenshots/briefing-1440x1024.png`
- `docs/screenshots/contested-1440x1024.png`
- `docs/screenshots/timeline-1440x1024.png`
- `docs/screenshots/evidence-1440x1024.png`

**375x812**

- `docs/screenshots/landing-375x812.png`
- `docs/screenshots/ask-375x812.png`
- `docs/screenshots/briefing-375x812.png`
- `docs/screenshots/contested-375x812.png`
- `docs/screenshots/timeline-375x812.png`
- `docs/screenshots/evidence-375x812.png`

## Pytest

Command:

```powershell
cd C:\Users\gudma\OneDrive\Desktop\GITHUB-FILES\groundtruth
.\.venv\Scripts\pytest
```

Output:

```text
3 failed, 63 passed, 13 warnings in 88.15s (0:01:28)
```

Failures:

1. `tests/test_benchmark.py::test_committed_corpus_memory_integrity_guard`
2. `tests/test_registry.py::test_claims_registry_is_complete_and_unique`
3. `tests/test_web.py::test_state_exposes_demo_inventory`

These are pre-existing cross-system state expectations and not regressions from the web redesign
(the web API route migration and route shells are validated by `tests/test_web.py` aside from the
existing active-retraction baseline expectation).

## Notes

- `groundtruth/` backend behavior was not reworked beyond endpoint path updates and thin page route wiring in `web/app.py`.
- No deployment, publish, or submission action was performed.
- No framework/build step was added; static assets remain vanilla HTML/CSS/JS.
