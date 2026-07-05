# REPAIR — restore memory/registry integrity broken by the P6 experiments (DO THIS BEFORE REDESIGN.md)

**What happened (audit finding, verified):** the P6 MemoryRot baseline runs rebuilt the LIVE Cognee datasets in place. Current live state: `naive_memory` and `groundtruth_memory` each contain a fresh 40-item ingest with NEW data_ids; **zero** of the committed registry's data_ids exist in live memory; no retraction notices are ingested; no forgets are applied. The P6 drop commit (`a1d859a`) also overwrote `data/claims.json` with experimental scratch state — that file has been restored from `a1d859a~1` and committed (25 `retracted_forgotten` + 15 `active`, with `belief_state`/`state_history`). The restored registry is the **reference for what must be true again**, but its data_ids point at memory that no longer exists.

**Failing test (must be green at the end):** `tests/test_benchmark.py::test_committed_corpus_memory_integrity_guard` — 55 violations, e.g. `retracted_original_missing_from_naive`. (`test_registry.py` and `test_web.py` failures were fixed by the registry restore.)

**Strategy — ADOPT the live ingest, re-run the lifecycle (do NOT full-reset):** the live 40+40 ingest is already cognified — re-using it saves ~80 LLM ingestion passes. What's missing is everything that makes the product true: notices, edges, forgets, belief states.

## R1 — Rebuild registry mapping to live memory (deterministic, no LLM)
1. For each dataset, `cognee.datasets.list_data(dataset_id)` and map each live data item to its claim (match by content hash or item name against the seed corpus text — `RememberResult.items`-style names embed a content hash; verify the actual attribute shape before coding).
2. Update each claim's `datasets.<name>.data_id` (+ `dataset_id`) in `data/claims.json` to the LIVE ids. Set every claim back to `status=active`, `belief_state=active`, and reset per-dataset status — but **preserve `state_history`** by appending a new event: `{state: active, evidence_class: system, basis: "registry re-anchored to rebuilt memory after P6 incident"}`. The retraction history stays visible in history; current state restarts honestly.
3. Gate: every registry data_id exists in live memory (40/40 per dataset); `test_claims_registry` may need its expectation adjusted ONLY if it hardcodes `{"active","retracted"}` — the correct expectation right after R1 is all-active; after R2 it returns to mixed. Do not weaken the 80-unique-data-items assertions.

## R2 — Re-run the retraction lifecycle (LLM, resumable — the existing watcher)
1. Run the watcher pass for **all 25** retracted-cohort claims against the re-anchored registry: ingest notice (own data item, both datasets per the established design) → contradicts/supersedes edge (data_id-stamped) → `forget(memory_only=True)` of the original in `groundtruth_memory` only → registry transitions (`belief_state=retracted`, evidence_class=`authority_feed`).
2. Rules unchanged: resumable + idempotent, persist after each claim, never fabricate on 429/quota — stop honestly and resume. Provider lock: Gemini + existing fallback only.
3. Gate: integrity guard passes — 25/25 retracted in groundtruth (originals gone), 25/25 originals still present in naive, controls 15/15 untouched, no violations.

## R3 — Regenerate every number that depends on memory state
1. Re-run the benchmark (`groundtruth.benchmark`) → regenerate `docs/BENCHMARK.md` + `data/benchmark_results.json` with the REAL new numbers, whatever they are.
2. Re-run the briefing + one timeline diff so their RESULTS transcripts reference live data_ids.
3. Update README's stat lines to match regenerated artifacts exactly (the P8 README cites numbers from the destroyed state — every number must trace to a post-repair artifact). Note the incident honestly in `docs/RESULTS-REPAIR.md`: what broke, what was rebuilt, one-line timeline.
4. Gate: **full pytest suite green**; `git grep` finds no doc number that disagrees with its generating artifact.

## R4 — Guard against recurrence
1. Any experiment that ingests/resets datasets MUST run in an isolated runtime (`.tmp_*` roots, gitignored) — never against `C:\Users\gudma\AppData\Local\GroundTruth\cognee`. Add this as a comment where the runtime root is configured, and gitignore `.tmp_*`.
2. Commit sequence: R1 (registry re-anchor), R2 (may be several resumable checkpoints), R3 (regenerated docs), each with clear messages.

**Then proceed directly to `REDESIGN.md`** (the web rebuild) — it is unaffected by this repair but its landing-page stat tiles must use the POST-repair numbers.

**Honesty rule, unchanged:** if quota stops R2 partway, commit the honest partial (e.g. "17/25 re-processed, resume pending"), update the docs to say exactly that, and continue when quota allows. Do not ship a number the data doesn't back.
