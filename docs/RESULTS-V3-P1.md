# GroundTruth V3 P1 Results

Generated: 2026-07-04
Status: `complete`

## Gate

- Registry source of truth now carries `belief_state` and append-only `state_history` for all 40 committed claims.
- State counts from `data/claims.json`: `active=15`, `retracted=25`, `contested=0`, `superseded=0`, `purged=0`.
- Every state-history event records `state`, `at`, `evidence_class`, `evidence_ref`, and `basis`.
- Answer references now include per-reference belief annotations and the answer payload includes `cites_by_state`.
- Existing compatibility fields remain: `status`, `cites_retracted`, `retracted_dois`, `cites_superseded`, `superseded_dois`, `superseded_references`.

## Evidence Ladder

- `authority_feed`: retraction events from Retraction Watch / Crossref records.
- `semantic_inference`: reserved for V3 contested semantic workflow.
- `user_assertion`: seed/import assertions and future adjudication/feedback.

## Graph Mirror Verification

Verified installed Cognee `1.2.2` source before implementation:

- `DataPoint.belongs_to_set` exists in `.venv/Lib/site-packages/cognee/infrastructure/engine/models/DataPoint.py`.
- `NodeSet` is a `DataPoint` subclass with `name`.
- Cognee uses `NodeSet(id=generate_node_id(f"NodeSet:{name}"), name=name)` for first-class NodeSet tags.
- The graph interface exposes `add_node` and `add_nodes`, but no generic `update_node`.
- Ladybug `add_node` only sets properties on create; Ladybug `add_nodes` can update existing properties on match.

Implementation consequence: the registry remains authoritative for lifecycle state. Future claim ingest tags `ScientificClaim` with NodeSets such as `beliefs_active` and `beliefs_retracted`, but P1 does not depend on in-place mutation of existing graph nodes.

## Verification

Focused P1 command:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_beliefs.py tests/test_registry.py tests/test_answer.py tests/test_watcher.py -q
```

Result:

```text
8 passed, 10 warnings in 77.41s (0:01:17)
```

Full suite:

```powershell
.\.venv\Scripts\python.exe -m pytest -q --durations=10
```

Result:

```text
31 passed, 12 warnings in 94.87s (0:01:34)
```
