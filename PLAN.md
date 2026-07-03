# GroundTruth — Master Build Plan (A → Z)

**Project:** GroundTruth — an agent memory that **unlearns retracted science**. Built on Cognee (open-source, self-hosted). Entry for the WeMakeDevs × Cognee hackathon, **Best Use of Open Source** track, solo.

**One-line pitch:** Every AI memory today is append-only — it never becomes *less wrong*. GroundTruth watches the Retraction Watch feed, detects when a remembered scientific claim is contradicted or retracted, links the contradiction in the knowledge graph, surgically forgets the superseded claim, and proves — with a quantified benchmark — that its answers stop citing retracted science while a naive memory keeps doing it.

**Why this wins (judging criteria are: Potential Impact, Creativity & Innovation, Technical Excellence, Best Use of Cognee, User Experience, Presentation Quality — equal weight):**
- Exercises **every** Cognee lifecycle verb non-trivially: `remember` (per-claim ingestion), `recall` (cited answers), `improve`/`memify` (custom contradiction-detection enrichment + feedback loop), `forget` (surgical, per-claim deletion). Depth of lifecycle use is the single biggest scoring lever.
- The **benchmark** (Phase 4) is the artifact no other submission will have: a hard number ("naive memory cites retracted papers in X/20 answers; GroundTruth in Y/20").
- The **demo** (Phase 5) is one wordless visual moment: same question, before/after, with the superseded claim visibly greyed out in the graph.

---

## 0. Ground rules (apply to every phase)

1. **Verify before calling.** Every cognee API you use must be checked against the installed package source (`<venv>/Lib/site-packages/cognee/...`) before you call it. The signatures in this plan were verified against `topoteretes/cognee` commit `f7e2267` (== PyPI `cognee==1.2.2`), but trust the installed source over this document if they conflict — and note the conflict in the phase's RESULTS file.
2. **Phase gates.** Each phase ends with explicit acceptance checks and a short `RESULTS-P<n>.md` in `docs/`. Do not start phase N+1 if phase N's gate failed — write up the failure honestly and stop. A diagnosed failure is a valid deliverable; a silently-skipped check is not.
3. **No placeholders.** Every function shipped must work. If something can't be finished, delete it and say so.
4. **No secrets in files.** `LLM_API_KEY` comes from the environment (a `.env` loaded via `python-dotenv` is fine — `.env` is gitignored). Never commit keys.
5. **No AI/Claude/Codex attribution** in code, commits, or docs. No Co-Authored-By tags.
6. **Commit per phase** (small, descriptive commits within a phase are fine). Do not push unless told.
7. **Tests:** each phase lists its tests. Run them and record real output. pytest, in `tests/`.
8. **Stack is pinned:** Python 3.10–3.14, `cognee==1.2.2` with its own pins (do NOT override `lancedb` — older lance panics on deletion vectors, which `forget()` creates). Defaults only: **Ladybug** graph store + **LanceDB** vectors + **SQLite** relational. No Neo4j/Postgres/Docker. Python SDK only — never the `cognee-cli -ui` Node frontend.
9. **LLM/embeddings:** cognee defaults are `openai/gpt-5-mini` + `openai/text-embedding-3-large`, both billed to `LLM_API_KEY`. Keep the defaults.
10. If blocked >3 attempts on one error: stop, write the diagnosis, move on or halt at the gate.

## Repository layout (target)

```
groundtruth/
├── PLAN.md, SPIKE.md            # this plan + the P0 spike spec
├── .env.example                 # LLM_API_KEY=, CROSSREF_MAILTO=
├── pyproject.toml               # deps: cognee==1.2.2, fastapi, uvicorn, httpx, python-dotenv, pytest, pytest-asyncio
├── spike/                       # P0 output (run_spike.py, RESULTS.md)
├── groundtruth/                 # the package
│   ├── ontology.py              # P1: Claim/Source DataPoint graph model
│   ├── ingest.py                # P1: RW CSV → curated claims → remember()
│   ├── registry.py              # P1: claim ↔ data_id ledger (claims.json)
│   ├── contradictions.py        # P2: custom memify enrichment task
│   ├── watcher.py               # P2: retraction watcher → contradiction pass → forget
│   ├── answer.py                # P2: recall wrapper (citations, retracted-source check)
│   ├── feedback.py              # P3: session feedback → improve loop
│   └── benchmark.py             # P4: the eval harness
├── data/                        # seed corpus (committed) + RW CSV cache (gitignored)
├── web/                         # P5: FastAPI app + static frontend
├── tests/
└── docs/                        # RESULTS-P*.md, BENCHMARK.md, DEMO.md, AI_USAGE.md
```

---

## Phase 0 — The spike (GO/NO-GO gate) — ~half a day

**Execute `SPIKE.md` exactly as written.** It proves the one path no cognee example covers: remember two contradicting claims (one per `remember()` call) → custom memify task writes a `contradicts` edge (stamped into the relational edges ledger so `forget` can clean it) → `forget(data_id=…, memory_only=True)` the superseded claim → the recall answer changes.

**Gate:** `spike/RESULTS.md` verdict is `GO` or `GO-WITH-FALLBACK`. On `NO-GO`, stop everything.

The spike also settles two design unknowns the later phases depend on:
- whether `ctx.data_item` is populated in the memify path (else: explicit `upsert_edges` with known ids — the fallback becomes the standard pattern in `contradictions.py`);
- whether `forget` leaves dangling graph edges when it deletes one endpoint (if yes, `watcher.py` must re-run a cleanup/re-resolution pass after every forget).

---

## Phase 1 — Data layer: ontology + ingestion — ~1 day

### 1a. Seed corpus from Retraction Watch (real data, free, no key)

The Retraction Watch database is public via Crossref:
- Full CSV: `https://api.labs.crossref.org/data/retractionwatch?mailto=<CROSSREF_MAILTO>` (updated every working day), or `git clone https://gitlab.com/crossref/retraction-watch-data`.
- **Inspect the CSV header on first download** — do not assume column names. Expected fields include original-paper title/DOI, retraction DOI/date, subject, and retraction reason, but verify.

Build `data/seed_corpus.json`, curated **at build time** (a script `groundtruth/ingest.py --curate` that you run once and commit its output — the demo must not depend on live curation):
- Pick **one legible subject area** (prefer nutrition/medicine — judges feel it instantly).
- Select **~25 retracted papers** with clear, statable claims + **~15 non-retracted control papers** in the same area.
- For each paper produce: `claim_text` (1–3 sentences stating what the paper claimed, written from title + retraction reason via one LLM call at curation time), `source` (journal, year, DOI), `status_at_seed` (`active` for all originals), and for retracted ones the `retraction` record (retraction DOI, date, reason) held back in a separate list — the watcher "discovers" these in Phase 2.
- Keep the claims **concrete and contradiction-prone** ("Compound X reduces Y by Z%"), not vague.

### 1b. Ontology

`groundtruth/ontology.py`: custom graph model as `DataPoint` subclasses, following the working example `examples/guides/custom_graph_model.py` in the cognee repo (typed relationship fields on Pydantic models):
- `ScientificClaim` (text, doi, journal, year, status) — relationships: `made_by: Source`, optionally `supersedes: ScientificClaim`.
- `Source` (name, type: journal|retraction_notice).
Pass it via `remember(..., graph_model=ScientificClaim)` (the param forwards to `cognify`; verified at `cognee/api/v1/cognify/cognify.py:43`). Pair with `custom_prompt=` to steer extraction. **Check extraction quality on 3 claims before ingesting all 40** — if the LLM ignores the schema, tune the prompt first.

### 1c. Ingestion with per-claim data items (THE architectural invariant)

`forget(data_id=…)` deletes per ingested **data item** — deletion is keyed on `Node.data_id AND Node.dataset_id` (`cognee/modules/graph/methods/delete_data_related_nodes.py:10-13`). Therefore:

- **One claim = one `remember()` call.** Never batch claims into one document.
- `RememberResult` does **not** return a `data_id`. After each `remember()`, resolve it: `cognee.datasets.list_data(dataset_id)` (`cognee/api/v1/datasets/datasets.py:59`) and match the new item (by content hash from `RememberResult.items` / by diffing against the previous listing).
- `groundtruth/registry.py` maintains `data/claims.json`: `{claim_id, doi, data_id, dataset_id, status, retraction_doi?}` — the ledger every later phase uses to target `forget` and to score the benchmark. Keep it in sync religiously; it is the system's spine.

Ingest into **two datasets** (needed by the benchmark): `naive_memory` and `groundtruth_memory`, same 40 claims each. (Two datasets, not copies of the DB — cognee datasets are isolated by `dataset_id`.)

### Gate P1
- 40 claims ingested into both datasets, one data item each; `claims.json` complete with resolved `data_id`s for both.
- `recall("what does the research say about <topic of claim #3>?", datasets=["groundtruth_memory"], include_references=True)` returns a sensible cited answer (param verified at `cognee/api/v1/recall/recall.py:384`).
- Test: `tests/test_registry.py` — every claims.json entry has a unique data_id; spot-check 3 via `list_data`.
- `docs/RESULTS-P1.md` with real recall output.

---

## Phase 2 — The engine: watcher → contradiction → forget — ~1.5 days

### 2a. Contradiction task (productionize the spike)

`groundtruth/contradictions.py`: the spike's memify enrichment task, hardened:
- Input: a **new** claim's node(s) + candidate related claims (find candidates via vector search on the claim text — the reference pattern in `cognee/tasks/codingagents/coding_rule_associations.py` shows endpoint lookup, `graph_engine.add_edges`, guarded `upsert_edges(..., data_id=…)`, `index_graph_edges`).
- LLM structured-output judgment (`LLMGateway.acreate_structured_output`): `{contradicts: bool, superseded_doi: str|null, confidence: 0-1, rationale: str}`. Only act on `confidence >= 0.7`; log skipped low-confidence pairs.
- Output: `contradicts` edge (+ `supersedes` direction), attributed (data_id-stamped) to the **superseding** claim's data item, using whichever stamping pattern the spike validated.
- Run via `memify(enrichment_tasks=[...], dataset="groundtruth_memory")` (`cognee/modules/memify/memify.py:25`).

### 2b. Retraction watcher

`groundtruth/watcher.py` — the heart of the demo, runnable step-by-step (the demo needs to trigger retractions one at a time):
1. `check(doi)` / `check_all()`: consult the held-back retraction list (and optionally the live RW CSV) for newly-retracted DOIs among `active` claims.
2. On hit: `remember()` the **retraction notice as a new claim** (its own data item, into `groundtruth_memory` only) → run the contradiction pass → on confirmed contradiction, **`forget(data_id=<superseded claim's data_id>, dataset_id=…, memory_only=True)`** → update `claims.json` (`status: retracted_forgotten`) → if the spike found dangling edges, run the cleanup pass.
3. `naive_memory` gets the retraction notice ingested too **but no contradiction pass and no forget** — that's the honest baseline (it has the same information, it just never resolves it).
4. Every action appends to `data/audit_log.jsonl` (timestamp, doi, action, edge ids, forget summary dict — `forget()` returns one). The audit log becomes demo material.

### 2c. Answer layer

`groundtruth/answer.py`: `answer(question, dataset) -> {text, references, cites_retracted: bool, retracted_dois: [...]}` — wraps `recall(..., include_references=True)`, cross-checks every reference against `claims.json` for retracted status. This function is used by the benchmark, the API, and the UI. One code path, no divergence.

### Gate P2
- Scripted end-to-end run: trigger 3 retractions via the watcher; for each, the graph shows the contradiction edge, then the claim is forgotten; `answer()` on those topics flips from citing the retracted claim to citing the retraction/controls. Naive dataset keeps citing them.
- Tests: `tests/test_watcher.py` (one full retraction lifecycle against a throwaway dataset), `tests/test_answer.py` (retracted-citation detection).
- `docs/RESULTS-P2.md` with before/after answers for the 3 claims (verbatim).

---

## Phase 3 — Feedback loop (`improve`) — ~0.5 day

All verified against source; the loop is real but multi-step and **off by default**:

1. Answer questions in a session: `recall(question, session_id=<sid>, datasets=["groundtruth_memory"], ...)` — session-scoped recall records QA entries with the graph elements used.
2. User feedback: `cognee.session.add_feedback(session_id, qa_id, feedback_text=None, feedback_score=<int>)` (`cognee/api/v1/session/session.py:77`). Determine how to obtain `qa_id` from the session/recall response by reading `session.py` (`get_session` at line 40) — verify, don't guess.
3. Bake it in: `improve(dataset="groundtruth_memory", session_ids=[<sid>], build_truth_subspace=True)` (`cognee/api/v1/improve/improve.py:36`) — stage 1 applies feedback weights to the graph elements behind each answer.
4. Reward it: `recall(..., feedback_influence=<float > 0>)` (param at `recall.py:379`; **default 0.0 — nothing happens unless set**).

Wire thumbs-up/down into the API/UI (Phase 5) and expose `POST /improve`. In the demo: downvote an answer that hedges toward a retracted claim → `improve` → show the re-asked answer ranks the good sources higher.

### Gate P3
- One scripted session: ask → downvote → improve → re-ask with `feedback_influence=1.0`; log both answers and whether ranking/content visibly changed. **If the effect is too subtle to demo, say so in RESULTS-P3.md** — we then present feedback as implemented-but-secondary and the demo leans on Phase 2. Do not fake it.

---

## Phase 4 — The benchmark (the centerpiece artifact) — ~1 day

`groundtruth/benchmark.py`:
- **20 questions**, written against the seed corpus: 12 target retracted claims ("Does compound X reduce inflammation?"), 5 target control claims (must NOT be forgotten — catches over-forgetting), 3 mixed/multi-hop. Committed as `data/benchmark_questions.json` with expected classification per question.
- Run every question against **both** datasets via `answer()`. Primary metric is **deterministic, not LLM-judged**: `cites_retracted` — does the answer's reference set include a claim whose status is retracted? Secondary metric (LLM-as-judge, clearly labeled as such): factual correctness of the answer text vs the post-retraction ground truth, 0–2 scale, judge prompt committed.
- Output: `docs/BENCHMARK.md` — a results table (per-question: dataset, cites_retracted, correctness), the headline numbers ("naive cites retracted sources in N/20; GroundTruth in M/20; control-claim retention 5/5"), and the exact reproduction command. Plus `data/benchmark_results.json` (raw).
- **Report the real numbers, whatever they are.** If GroundTruth over-forgets a control claim, that goes in the table. A 19/20-vs-11/20 honest result beats a suspicious 20/20.

### Gate P4
- Benchmark runs end-to-end with one command (`python -m groundtruth.benchmark`), reproducible from a fresh ingest. Numbers in BENCHMARK.md match `benchmark_results.json`.

---

## Phase 5 — Demo UI + provenance visualization — ~1 day

`web/` — FastAPI + a single static page (vanilla JS/CSS, no build step, no framework):
- `POST /ask {question, dataset}` → `answer()` result, with references and a red **"cites retracted source"** badge when `cites_retracted` (that badge on the naive side IS the demo).
- **Side-by-side mode:** same question against `naive_memory` and `groundtruth_memory` — the core visual.
- `POST /retract {doi}` → runs the watcher for one DOI live on stage; response streams the steps (detected → contradiction found → edge added → forgotten) into a visible timeline from the audit log.
- `POST /feedback {session_id, qa_id, score}` and `POST /improve`.
- `GET /graph` → serves the HTML from `visualize_memory_provenance(destination_file_path=..., include_memory=True, scope_user_ids=[...])` (`cognee/api/v1/visualize/memory_provenance.py:495`; returns a self-contained HTML file). **Honest caveat baked into the plan:** this shows the global file→entity provenance graph, NOT "sources behind this answer" — answer-level citations come from `include_references`. Use the graph as the big-picture visual (claim disappears after forget = the money shot); do not label it as answer provenance.
- Style: clean, dark, minimal; the side-by-side answers and the retraction timeline are the entire page. No settings screens, no auth.

### Gate P5
- Scripted demo path works locally end-to-end: load page → ask question (both sides answer, naive shows red badge) → trigger retraction → watch timeline → re-ask (GroundTruth side flips, naive stays wrong) → open graph before/after. Screen-recordable in under 90 seconds.
- `docs/DEMO.md`: the exact click-by-click demo script.

---

## Phase 6 — Submission package — ~0.5 day

- **README.md** (the judges' 60-second read): problem (memory that can't unlearn) → the 15-second gif of the side-by-side flip → benchmark headline numbers → lifecycle table (verb → where it's used in code, file links: remember=ingest.py, recall=answer.py, improve/memify=contradictions.py+feedback.py, forget=watcher.py) → architecture sketch → quickstart (env vars, `pip install -e .`, ingest, benchmark, `uvicorn web.app:app`).
- `docs/AI_USAGE.md`: AI-assistant disclosure (**required by hackathon rules** — list the assistants used and how). Honest and specific.
- Confirm repo is clean: no keys, no scratch files, `.env.example` present, tests green — record final `pytest` output in `docs/RESULTS-P6.md`.
- **Do NOT submit, publish the repo, or post anything.** Final deploy to the VPS, the demo video, and the Google Form submission are handled by the owner. Stop at "everything ready".

---

## What the owner must provide (Codex: ask for these up front, then start)

| # | Item | Used for | Cost |
|---|------|----------|------|
| 1 | **`LLM_API_KEY`** — an OpenAI API key in env / `.env` | All cognee LLM calls (`gpt-5-mini`) + embeddings (`text-embedding-3-large`) + curation & judge calls | ~$5–15 total at this corpus size; set a hard spend limit on the key |
| 2 | **`CROSSREF_MAILTO`** — any contact email | Polite-pool param for the Retraction Watch CSV download | Free, no signup |
| 3 | Python 3.10–3.14 on PATH | everything | — |
| — | *Nothing else.* No other API keys, no databases, no Docker, no paid services. | | |

Owner-side items outside Codex's scope (later): GitHub repo publish, VPS deploy + subdomain, demo video recording, Google Form submission (all approval-gated to the owner).
