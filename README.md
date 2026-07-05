# GroundTruth

Most agents wake up with amnesia. Ours wakes up knowing what it learned last night, and what it must unlearn.

## Links

- **Demo video:** https://www.youtube.com/watch?v=I7YnU_0Y-ps
- **Live demo:** https://groundtruth.gudman.xyz
- **AI usage disclosure:** [AI_USAGE.md](AI_USAGE.md)

## Benchmark Headlines

These values are from committed artifacts in this branch:

- **Benchmark (20 questions):** `data/benchmark_results.json`
  - Naive memory cites retracted originals in `18/20`.
  - GroundTruth memory cites retracted originals in `0/20`.
  - Active control retention is `5/5`.
  - Retraction coverage is `25/25` with `0` violations in `memory_integrity`.
- **V2 semantic eval (complete):** `docs/RESULTS-V2.md`
  - `precision: 1.00`
  - `recall: 0.6666666666666666`
  - `false_positive: 0`, `false_negative: 1`
  - Evaluated semantic pairs: `28/28` (complete, no pending pairs)

## Cognee Verb Lifecycle

| Verb | Exact Implementation |
|---|---|
| remember | `groundtruth/ingest.py:remember_claim`; session-only evidence capture is in `groundtruth/briefing.py:remember_evening_evidence` |
| recall | `groundtruth/answer.py:answer` |
| improve | `groundtruth/feedback.py:improve_from_feedback` |
| forget | `groundtruth/watcher.py:process_retraction` (authority supersession) and `groundtruth/contest.py:adjudicate_pair` (resolved contested supersession) |

## Evidence Ladder

- `authority_feed`: deterministic evidence from retrievers (for example, retraction or OSV notices).
- `semantic_inference`: LLM-derived direction/confidence judgments for conflicting claims.
- `user_assertion`: explicit human-backed actions, including adjudication and session feedback.

These classes are written to every state change via `state_history` in the registry, then surfaced on both `/ask` and `/timeline`.

## Quickstart

```powershell
# from repo root
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
Copy-Item .env.example .env
```

```powershell
# full tests
.\.venv\Scripts\pytest.exe -q

# baseline benchmark
$env:PYTHONIOENCODING='utf-8'
.\.venv\Scripts\python.exe -m groundtruth.benchmark

# v2 artifacts
.\.venv\Scripts\python.exe -m groundtruth.v2 --results
```

```powershell
# local demo
.\.venv\Scripts\uvicorn.exe web.app:app --host 127.0.0.1 --port 8000
```

## P6 Status

P6 MemoryRot-Bench is intentionally not shipped in this phase; a single required pass was attempted and dropped because `groundtruth.memoryrot` is not present on this branch.

## Limitations

- Correctness judge in benchmark is `skipped_quota_disclosed` due current Gemini free-tier constraints.
- Benchmark uses relevance-ranked `GRAPH_COMPLETION` retrieval and discloses raw summaries in `data/benchmark_results.json`.
- Session improvement is bounded by local mutation-guard confirmation and `feedback_influence` behavior.
- V2 semantic eval is complete and reproducible from `data/v2_results.json`, but it is a narrow eight-claim corpus.
- P7 (MCP server) is skipped by instruction and is not present in this phase.

## Roadmap

The two changes that would move this from a strong proof-of-concept to a robust system — both deferred here by honest constraints (LLM budget and a Cognee-internals graph-indexing issue on the transplanted store), not by design:

1. **Make semantic contradiction-detection load-bearing at scale.** Today it is evaluated on a narrow curated corpus (precision `1.00` / recall `0.67`). Plan: expand to hundreds of Retraction Watch / Crossref claims with a hand-labeled ground-truth conflict set, run the LLM judge over vector-neighbor pairs to completion (needs a funded LLM key so runs don't truncate on free-tier quota), and report honest precision/recall at scale.
2. **Restore the live streaming `forget` flow on the deployed memory.** The interactive retract path currently fails deep in Cognee (`index_graph_edges` → `Graph edge indexing error`) on the Windows→Linux transplanted store, so the deployed demo relies on the static before/after. Plan: rebuild the memory natively on the host (re-ingest rather than transplant) or patch the graph-indexing seam so `remember → detect → forget` runs end-to-end in the browser.

Further out: an MCP server (P7), MemoryRot-Bench (P6), and additional evidence-ladder adapters (e.g. OSV.dev CVE supersession) — see `VISION.md`.

## Primary Artifacts

- `docs/RESULTS-V3-P3.md`
- `docs/RESULTS-V3-P4.md`
- `docs/RESULTS-V3-P5.md`
- `docs/RESULTS-V2.md`
- `docs/BENCHMARK.md`
- `docs/RESULTS-V3-P8.md`
- `docs/DEMO.md`
- `VISION.md`
