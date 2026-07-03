# GroundTruth — Day-1 Spike (GO/NO-GO gate)

**Project:** GroundTruth — a Cognee-powered agent memory that *unlearns* retracted/superseded knowledge (WeMakeDevs × Cognee hackathon, Best Use of Open Source track).

**This spike:** prove the one end-to-end path that no Cognee example covers, before any product code is written:

> remember two contradicting claims → custom memify task writes a `contradicts` edge → surgically `forget()` the superseded claim → the edge is cleaned up AND `recall()`'s answer changes.

If this works, the whole project is buildable. If the edge-stamping seam (Step 3) fails, we need the fallback (documented below) before proceeding. **Report the honest result either way — a failed spike with a clear diagnosis is a successful spike.**

Every API fact below was verified by reading `topoteretes/cognee` source at commit `f7e2267` (version 1.2.2, the current PyPI release). File references are into the installed package / that commit.

---

## 0. Environment

- Python **3.10–3.13** (fastembed needs `python_version < '3.14'`).
- Fresh venv, then: `pip install "cognee[fastembed]==1.2.2"`
- **Do NOT override the lancedb version** — cognee pins `lancedb>=0.24.3,<1.0.0` because older lance panics on tables with deletion vectors, which `forget()` creates. Let pip resolve it.
- Defaults need no external services: **Ladybug** graph store (NOT Kuzu — Kuzu was archived upstream) + LanceDB vectors + SQLite relational. Do not configure Neo4j/Postgres for the spike.
- **Providers come from `.env` (already written): FREE stack = Gemini `gemini-2.5-flash` (LLM) + local Fastembed (embeddings).** Requires a free Gemini key in `LLM_API_KEY`+`GEMINI_API_KEY` (https://aistudio.google.com/apikey). Load `.env` via `python-dotenv` before importing cognee. **Step 0 of the spike:** `remember()` one claim and confirm Fastembed indexes (no dimension error) AND `cognify` returns a non-empty graph (Gemini honored structured output). If that fails, switch to the OpenAI fallback block in `.env` (needs ~$5 credit) and record it. Never hardcode a key in a file.
- Gemini free tier = 15 req/min; `.env` sets `LLM_RATE_LIMIT_ENABLED=true`/`LLM_RATE_LIMIT_REQUESTS=14`. If you still hit 429s, lower it.
- Windows note: cognee depends on `python-magic-bin` on Windows (auto-installed). Everything is driven from the Python SDK — do NOT touch `cognee-cli -ui` / the Node frontend.
- Put the spike in `spike/` in this repo: `spike/run_spike.py` (single script, asyncio) plus at most one helper module. No product scaffolding yet.

## 1. Step 1 — remember two contradicting claims (one per call)

**Critical constraint (verified):** `forget(data_id=...)` deletes per ingested **data item**, not per graph node. Deletion is keyed on `Node.data_id AND Node.dataset_id` (`cognee/modules/graph/methods/delete_data_related_nodes.py:10-13`, same for edges). Therefore **each claim must be its own `remember()` call** so it gets its own `data_id`.

```python
import cognee

r1 = await cognee.remember(
    "CLAIM A (2019 study, source: Journal X): Compound Z significantly reduces inflammation in adults.",
    dataset_name="spike_claims",
)
r2 = await cognee.remember(
    "CLAIM B (2024 retraction notice, source: Journal X): The 2019 study on Compound Z was retracted for data fabrication; Compound Z shows no anti-inflammatory effect.",
    dataset_name="spike_claims",
)
```

- `remember()` = `add()` + `cognify()` (`cognee/api/v1/remember/remember.py:623`). Returns `RememberResult` with `.dataset_id`, `.content_hash`, `.items` — but **not** a `data_id` UUID.
- **To get each claim's `data_id`:** enumerate the dataset via `cognee.datasets.list_data(dataset_id: UUID)` (`cognee/api/v1/datasets/datasets.py:59`) and match items to claims (by name/content_hash from `RememberResult.items`). Record both `data_id`s.

## 2. Step 2 — baseline recall

```python
results = await cognee.recall(
    "Does Compound Z reduce inflammation?",
    datasets=["spike_claims"],
    include_references=True,
)
```

- `include_references: bool = False` is a real param (`cognee/api/v1/recall/recall.py:384`) — use it; answer-level citations are a product feature later.
- Log the full response. Expected: the answer mentions both/either claim (memory currently holds a contradiction).

## 3. Step 3 — custom memify enrichment task: the `contradicts` edge (THE RISK SEAM)

There is **no built-in contradiction detection** in cognee. Build a custom enrichment task and run it via `memify(enrichment_tasks=[...])` (`cognee/modules/memify/memify.py:25`).

**Adapt the reference implementation** — `add_rule_associations` in `cognee/tasks/codingagents/coding_rule_associations.py` (used by `examples/custom_pipelines/memify_coding_agent_rule_extraction_example.py`). It demonstrates the full pattern (lines ~100–140):
1. Call the LLM for structured output: `LLMGateway.acreate_structured_output(text_input=..., system_prompt=..., response_model=YourPydanticModel)`
2. Create nodes if needed: `add_data_points(data_points=[...])`
3. Add edges between existing nodes: tuples `(source_node_id, target_node_id, "contradicts", {props})` via `graph_engine.add_edges(edges_to_save)` (get engine via `get_graph_engine()`)
4. **Stamp the edges into the relational ledger** so `forget()` can clean them:
   ```python
   if ctx and ctx.user and ctx.data_item and hasattr(ctx.data_item, "id"):
       await upsert_edges(edges_to_save, tenant_id=ctx.user.tenant_id,
                          user_id=ctx.user.id, dataset_id=ctx.dataset.id,
                          data_id=ctx.data_item.id)
   await index_graph_edges(edges_to_save)
   ```

**The known gotcha (this is what the spike exists to resolve):** `ctx` is injected only into tasks that declare a `ctx` parameter (`cognee/modules/pipelines/operations/run_tasks_base.py:173-176` — "Pass ctx only to tasks that declare it"). In a `memify` run, `ctx.data_item` **may not be populated** (there may be no single data item in scope). So:

- Your task MUST declare `ctx`, then **log whether `ctx`, `ctx.user`, `ctx.dataset`, `ctx.data_item` are populated** in the memify path you use.
- The `contradicts` edge should be attributed to the **superseding claim's** data item (CLAIM B's `data_id`) — when the retraction is later itself forgotten, its edge should go with it. If `ctx.data_item` is unpopulated, **fallback:** call `upsert_edges` directly with explicit values (you already have `dataset_id` and CLAIM B's `data_id` from Step 1) instead of relying on `ctx`. Verify `upsert_edges`'s signature in the installed package before calling.
- For the spike, the contradiction "detection" can be minimal: fetch the claim nodes (the reference example uses `get_nodeset_subgraph` / vector `search` to find endpoints), ask the LLM "do these contradict; which supersedes which," emit the edge. Precision-engineering the prompt is Day-3 work, not spike work.

**Verify after this step:** the `contradicts` edge exists in the graph AND has a row in the relational `edges` ledger with the expected `data_id`. (Nodes/edges ledger models: `cognee/modules/graph/models/`; SQLite db lives under cognee's data dir — inspect directly if needed.)

## 4. Step 4 — surgical forget + proof

```python
# forget CLAIM A (the superseded 2019 study) only
await cognee.forget(data_id=claim_a_data_id, dataset_id=dataset_id, memory_only=True)
```

- Signature verified: `forget(*, data_id, dataset, dataset_id, everything, memory_only, user)` (`cognee/api/v1/forget/forget.py:16`). `memory_only=True` deletes graph nodes/edges + vector entries but keeps raw data records.

**Acceptance checks (ALL must be logged with actual output):**
1. CLAIM A's nodes are gone from the graph; CLAIM B's nodes survive.
2. No dangling `contradicts` edge: if the edge was attributed to CLAIM B it survives pointing at nothing… → check what actually happens: does the graph edge dangle after its endpoint node was deleted? Log the graph state honestly. (If dangling edges are a real artifact, note it — Day-3 design must handle re-resolution after forget.)
3. Re-run the Step-2 recall verbatim. The answer must now reflect only CLAIM B (no anti-inflammatory effect / study retracted). **This before/after answer pair is the core demo artifact — save both outputs to `spike/RESULTS.md`.**
4. Then also `forget(data_id=claim_b_data_id, ...)` and confirm the `contradicts` edge's ledger row is cleaned (this proves the Step-3 stamping worked).

## 5. Deliverables

- `spike/run_spike.py` — runs Steps 1–4 top to bottom, idempotent (start by `forget(dataset="spike_claims")` if it exists).
- `spike/RESULTS.md` — honest writeup: what worked, what didn't, whether `ctx.data_item` was populated in memify, whether the explicit-`upsert_edges` fallback was needed, whether forget left dangling graph edges, and the verbatim before/after recall answers.
- **VERDICT line at the top of RESULTS.md: `GO` / `GO-WITH-FALLBACK` / `NO-GO (reason)`.**

## Rules

- Do not build anything beyond the spike (no UI, no ingestion pipeline, no benchmark). Those are Days 2–6.
- Verify any API you use beyond the ones cited here against the installed package source (`site-packages/cognee/...`) before calling it — do not guess signatures.
- No secrets in files. No Claude/AI attribution in commits.
- If blocked >3 attempts on the same error, stop and write up the diagnosis in RESULTS.md instead of thrashing.
