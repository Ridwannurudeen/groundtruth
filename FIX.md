# GroundTruth — Fix Spec (integrity + honesty pass before submission)

The P0–P6 build works and all 12 tests pass. A verification audit found the headline benchmark overstates, in a way a Cognee-engineer judge would catch by reading `data/claims.json`. This spec closes the gap. **Do not touch anything not listed here.** Re-run the affected gates and update the RESULTS/BENCHMARK/README numbers to whatever the honest re-run produces — do not hand-edit numbers.

Context that is FINE and must stay:
- The spike (`spike/RESULTS.md`) is the real proof: Gemini structured output + Fastembed + the contradict→forget→answer-flip path all verified. Leave it.
- Deterministic Retraction-Watch DOI matching for retractions is CORRECT and honest (a retraction is a fact). Keep it — just reframe wording (FIX-4). Do not replace it with an LLM judge.

---

## FIX-1 (CRITICAL) — the corpus/metric integrity gap

**The bug:** the seed corpus has **25 papers with `cohort: "retracted_original"`** (ground truth: all 25 are retracted), but the watcher only forgot **13**. The other 12 (R013, R015–R025) stay in `groundtruth_memory` with `status: "active"`. The benchmark's retracted check (`answer.py:reference_for_claim` → `is_retracted_original`) keys on **`status`**, not the ground-truth **`cohort`**. Result: GroundTruth cites 12 genuinely-retracted papers but scores them "clean," producing a false **0/20**.

**Fix — key the metric on ground truth AND actually forget every retracted original:**

1. **Ground-truth field.** In `data/claims.json` (and wherever `reference_for_claim`/`select_references` read), treat a claim as retracted iff its seed **`cohort == "retracted_original"`** — independent of pipeline `status`. `answer.py` currently computes `is_retracted_original = kind == "original_claim" and str(claim["status"]).startswith("retracted")`. Change the ground-truth signal to cohort. Keep `status`/`dataset_status` only to express *pipeline state* (forgotten or not), never as the definition of "is retracted."

2. **Forget every retracted original from `groundtruth_memory`.** Extend the watcher/benchmark-prep so ALL 25 retracted-cohort claims are neutralized in `groundtruth_memory` (contradiction edge where a RW retraction DOI exists; forget the original in every case). For the ones RW confirms, keep the RW-linked rationale. For any retracted-cohort claim RW does **not** return, still forget it in groundtruth but label the rationale honestly (e.g. `"seed-designated retraction; no live RW notice matched"`) — do not fabricate a RW link. `naive_memory` forgets nothing (baseline).

3. **Re-key the benchmark.** `groundtruth_memory` must now be clean against the FULL retracted set; `naive_memory` cites retracted originals wherever a question hits one. Expected honest shape: naive cites retracted in most retracted/mixed questions; GroundTruth in **0**, with **control retention intact** (controls must never be forgotten — assert this).

4. **Guard test.** Add a test asserting: every `cohort == "retracted_original"` claim is absent from `groundtruth_memory` (its `data_id` not in memory) and present in `naive_memory`; and no `cohort == "active_control"` claim is forgotten from either. This is the test that would have caught the bug.

### Gate FIX-1
Re-run `python -m groundtruth.benchmark`; regenerate `docs/BENCHMARK.md` + `data/benchmark_results.json`. New guard test + existing suite green. Report the real numbers.

---

## FIX-2 (HIGH) — make the citation metric mean what it says

Currently `cites_retracted` is computed by `select_references()` token-matching `claims.json` and checking memory membership — it does **not** read what the answer/recall actually cited, and `answer_text()` returns a **template**, not the model's answer.

1. **Use the real recall references.** `recall(..., include_references=True)` returns references for the answer; map those to claims and set `cites_retracted` from *the actually-retrieved/cited* retracted-cohort originals. Keep the claims.json membership check as a secondary integrity cross-check, but the headline metric must derive from real recall output. If the two disagree, log it.
2. **Name it truthfully.** Whatever the metric ends up measuring, describe it in one precise sentence in `BENCHMARK.md` (e.g. "fraction of answers whose retrieved context includes a still-present retracted-cohort original"). No "cites" if it's "retrieves."
3. **Answer text.** Prefer the synthesized recall answer over the template in `answer_text()` where a real answer is available (see FIX-3). The template may remain only as a fallback when recall returns nothing.

### Gate FIX-2
For 3 sample questions, show (in `docs/RESULTS-FIX.md`) the recall references, the derived `cites_retracted`, and that it matches ground-truth cohort.

---

## FIX-3 (HIGH) — recall relevance / real answers at 40-claim scale

The P3 log shows a query about *Avacopan/ANCA vasculitis* returning unrelated papers (cancer EMT, food insecurity, cardiac segmentation…), and `recall(only_context=True)` returns a **raw node dump**, not a synthesized answer. At demo scale this looks incoherent next to the clean 2-claim spike.

1. Return a **synthesized natural-language answer** for the demo/answer layer (e.g. drop `only_context=True` so GRAPH_COMPLETION synthesizes, or add a synthesis step), so the UI shows a real answer, not a node dump.
2. Improve topical relevance: verify a topical query returns topical results — tune `top_k`/`wide_search_top_k`, or the embedding model, until at least the top references for a named-drug question are about that drug. Document the before/after for one query.
3. Keep it within Gemini free-tier quota (synthesis adds one LLM call per answer). If quota is tight, cache demo answers.

### Gate FIX-3
One named-entity question returns a coherent, on-topic synthesized answer in both datasets, differing correctly (naive cites the retracted original; GroundTruth cites the notice / omits it). Capture it for the demo.

---

## FIX-4 (MEDIUM) — honest framing in README/docs

- Reframe "contradiction detection" as **"retraction-linked supersession (deterministic Retraction-Watch DOI match)."** It's a strength; don't imply LLM inference of contradictions. The `contradicts` edge is real — keep it — but describe how it's decided accurately.
- Every number in `README.md` (badge line 12, line 52, line 168) must be regenerated from the FIX-1 benchmark — no stale `17/20 vs 0/20` if the honest number differs. The badge and prose must match `docs/BENCHMARK.md` exactly.
- Keep the existing honest limitations section; add the corpus-completeness note (all retracted-cohort forgotten in groundtruth).

## FIX-5 (MEDIUM) — feedback loop claim

P3 marks "visible change = True," but the evidence is a context dump; the real effect of `feedback_influence` is unclear. Either (a) demonstrate a concrete, measurable reordering (a named source moves up after an upvote, shown before/after), or (b) downgrade the README/AI-disclosure wording to "feedback is stored and `improve()` runs; ranking effect is subtle on this corpus." Do not claim it changes answers unless you can show it.

## FIX-6 (LOW) — correctness judge

Keep it skipped-with-disclosure (fine) OR run it once if Gemini/OpenAI quota allows, and record the result. Ensure the README's stated methodology matches what actually ran.

---

## Order & rules
1. FIX-1 first (it changes the corpus/benchmark everything else reports on), then FIX-2/3, then the doc passes FIX-4/5/6.
2. Re-run the full test suite + the affected gates after each fix; record real output in `docs/RESULTS-FIX.md`.
3. Honesty rule: if a fix makes the numbers less impressive, that is the correct outcome — report them. A defensible 0/25-with-full-coverage (or an honest naive-vs-gt split) beats a 0/20 that a judge can break in one file open.
4. No new scope, no secrets in files, no AI attribution in commits. Do not publish/deploy/submit — stop at "fixed, tests green, numbers regenerated."
