# AI Usage

This project was built with substantial AI assistance throughout the hackathon build, from architecture through deployment. Disclosed in full below, per the hackathon rules.

## Assistants Used

- **Claude (Anthropic, Claude Code)**: primary architecture and direction throughout the build. Authored all specification documents driving the work (`PLAN.md`, `SPIKE.md`, `FIX.md`, `REPAIR.md`, `V3.md`, `REDESIGN.md`) and handed them to Codex for execution. Independently audited every phase of Codex's work against raw data and re-ran tests before accepting results (this caught and drove the fix for a real data-integrity bug in the P6 benchmark pass). Directly authored and committed code fixes found during production verification, including the `registry_path` portability fix and `find_existing_claim_data_id` path-resolution fix in `groundtruth/contest.py` and `groundtruth/ingest.py`. Performed the production VPS deployment (systemd service, nginx/TLS config, a Windows-to-Linux memory-transplant path fix applied directly to the Cognee SQLite store). Built and ran the demo-video production pipeline (Playwright screen recording of the live site, edge-tts narration, ffmpeg assembly) that produced `groundtruth-demo.mp4`.
- **OpenAI Codex**: executed the specification documents above — implementing the Cognee ingestion pipeline, the belief-lifecycle engine, the contested-claim workflow, the briefing/timeline features, the multi-page frontend redesign, and writing/running the test suite and benchmark scripts.

## Human-Controlled Decisions

- Project idea, scope, target track, and every phase gate came from the project owner working with Claude; Codex executed against those specs, not its own scope.
- Secrets were kept in `.env` (and the production server's environment) only, never committed.
- The project owner made the final calls to publish the repository, deploy to production, and submit to the hackathon.

## What Was AI-Generated vs. Human-Directed

- **AI-generated**: the majority of the source code (Cognee integration, backend, frontend, tests) via Codex, and the code fixes / deployment scripts / video pipeline via Claude.
- **Human-directed**: the belief-maintenance concept, domain choice (retracted science), track selection, what to build/cut under the deadline, and the final go/no-go on every deploy and the submission itself.

## Verification

- Every phase was independently re-tested; the full suite (`pytest -q`) passes locally and was re-verified after each fix.
- Benchmark results are recorded in `docs/BENCHMARK.md` and `data/benchmark_results.json`; the headline numbers were independently recomputed from raw data, not taken on trust from a single run.
- The deployed site (https://groundtruth.gudman.xyz) was verified live end-to-end (all pages/API endpoints, a real Cognee-backed answer) after every deploy.
