# Vision

## Belief-Maintenance Thesis

GroundTruth is built on a single claim registry and explicit state machine, not a pile of answers. Every source claim carries a durable state (`active`, `contested`, `revised`, `superseded`, `retired`), and every transition is justified by a recorded evidence class and evidence reference.  

This makes the agent stateful in the right dimension: not just remembering facts, but preserving a memory of what is currently believed and why it changed. A retraction means "replace old belief with newer evidence". A contested pair means "don't erase, route to arbitration". An adjudication means "close the uncertainty with user-backed authority". The implementation goal is simple: every future response can be traced to current belief state, and every belief change can be reconstructed from registry history.

## Adapter Roadmap

Authority adapters already prove this model can cross domains:

- medical guidelines: map guideline updates and alert errata into `evidence_class=authority_feed` and replay them through the same claim state transitions; the same evidence ledger can flip stale recommendations while leaving audit trails intact.
- news corrections: ingest correction notices for rapidly changing factual claims (names, numbers, event facts) and let `timeline`/`briefing` expose what changed and when.
- legal overrulings: ingest court rulings or precedence changes to mark earlier legal claims as revised and surface the chain of basis in a way that preserves query-time attribution.

## Upstream Contribution Candidates

- `beliefs.py` as a reusable, evidence-classed state-history layer for Cognee datasets.  
- contest-to-revision wiring in a first-class truth-subspace that separates unresolved ambiguity (`contested`) from confident supersession.  
- `memoryrot` benchmark scaffold as a reusable retrieval-vs-lifecycle baseline once the corpus and interface are stabilized.
