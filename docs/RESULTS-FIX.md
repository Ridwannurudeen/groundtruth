# Fix Pass Results

Generated: 2026-07-04T19:15:26.715926+00:00
Status: `complete`

## Retraction Pass

- GroundTruth forgotten: 25/25 retracted-cohort originals.
- Pending: []

## Memory Integrity

```json
{
  "active_control_total": 15,
  "retracted_original_total": 25,
  "violations": []
}
```

## Regenerated Numbers

- Naive memory retrieves retracted originals in 18/20 answers.
- GroundTruth retrieves retracted originals in 0/20 answers.
- Control retention: 5/5.

## Metric

The headline metric is the fraction of answers whose relevance-ranked Cognee GRAPH_COMPLETION references include a still-present original claim from `cohort == "retracted_original"`. Raw graph references remain in the JSON for audit.

## Sample Recall References

### Q01 - naive_memory

- `cites_retracted`: `True`
- `retracted_dois`: `['10.1056/nejmoa2023386']`

```json
[
  {
    "claim_id": "R001",
    "cohort": "retracted_original",
    "data_id": "033e8c14-5e6e-5dbf-8a50-a7b850015cf2",
    "kind": "original_claim",
    "retracted": true
  },
  {
    "claim_id": "R001",
    "cohort": "retracted_original",
    "data_id": "4b2daf7b-0340-572d-adde-ce491af50f5d",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "R015",
    "cohort": "retracted_original",
    "data_id": "10dd0a00-a6f2-533b-a6af-5d4884e532ac",
    "kind": "retraction_notice",
    "retracted": false
  }
]
```

### Q01 - groundtruth_memory

- `cites_retracted`: `False`
- `retracted_dois`: `[]`

```json
[
  {
    "claim_id": "R001",
    "cohort": "retracted_original",
    "data_id": "4b2daf7b-0340-572d-adde-ce491af50f5d",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "R015",
    "cohort": "retracted_original",
    "data_id": "10dd0a00-a6f2-533b-a6af-5d4884e532ac",
    "kind": "retraction_notice",
    "retracted": false
  }
]
```

### Q13 - naive_memory

- `cites_retracted`: `False`
- `retracted_dois`: `[]`

```json
[
  {
    "claim_id": "C001",
    "cohort": "active_control",
    "data_id": "2c13440c-7ff4-59ef-aa40-290685b98ff4",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C013",
    "cohort": "active_control",
    "data_id": "f8069e33-8232-5c12-838d-ec08a41190f6",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C012",
    "cohort": "active_control",
    "data_id": "eec39b26-e7a8-5064-bd34-eca24c47b414",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C015",
    "cohort": "active_control",
    "data_id": "386a3edb-8fd5-5e04-8d52-c44362b40598",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C004",
    "cohort": "active_control",
    "data_id": "41a51fa9-c5fa-5006-b45f-3d6bab8de1f0",
    "kind": "original_claim",
    "retracted": false
  }
]
```

### Q13 - groundtruth_memory

- `cites_retracted`: `False`
- `retracted_dois`: `[]`

```json
[
  {
    "claim_id": "C001",
    "cohort": "active_control",
    "data_id": "2c13440c-7ff4-59ef-aa40-290685b98ff4",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C013",
    "cohort": "active_control",
    "data_id": "f8069e33-8232-5c12-838d-ec08a41190f6",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C012",
    "cohort": "active_control",
    "data_id": "eec39b26-e7a8-5064-bd34-eca24c47b414",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C015",
    "cohort": "active_control",
    "data_id": "386a3edb-8fd5-5e04-8d52-c44362b40598",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C004",
    "cohort": "active_control",
    "data_id": "41a51fa9-c5fa-5006-b45f-3d6bab8de1f0",
    "kind": "original_claim",
    "retracted": false
  }
]
```

### Q18 - naive_memory

- `cites_retracted`: `True`
- `retracted_dois`: `['10.1056/nejmoa2023386']`

```json
[
  {
    "claim_id": "C003",
    "cohort": "active_control",
    "data_id": "d3d710dc-228a-5960-bfce-a06ad17503ce",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "R001",
    "cohort": "retracted_original",
    "data_id": "033e8c14-5e6e-5dbf-8a50-a7b850015cf2",
    "kind": "original_claim",
    "retracted": true
  },
  {
    "claim_id": "C012",
    "cohort": "active_control",
    "data_id": "eec39b26-e7a8-5064-bd34-eca24c47b414",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "R001",
    "cohort": "retracted_original",
    "data_id": "4b2daf7b-0340-572d-adde-ce491af50f5d",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "R021",
    "cohort": "retracted_original",
    "data_id": "5a1af7d0-fa90-5f24-bebf-fe8d24c80ada",
    "kind": "retraction_notice",
    "retracted": false
  }
]
```

### Q18 - groundtruth_memory

- `cites_retracted`: `False`
- `retracted_dois`: `[]`

```json
[
  {
    "claim_id": "C003",
    "cohort": "active_control",
    "data_id": "d3d710dc-228a-5960-bfce-a06ad17503ce",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C012",
    "cohort": "active_control",
    "data_id": "eec39b26-e7a8-5064-bd34-eca24c47b414",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "R001",
    "cohort": "retracted_original",
    "data_id": "4b2daf7b-0340-572d-adde-ce491af50f5d",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "R003",
    "cohort": "retracted_original",
    "data_id": "99e5a7e4-1f8d-588b-8317-c7a32aa727ce",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "R021",
    "cohort": "retracted_original",
    "data_id": "5a1af7d0-fa90-5f24-bebf-fe8d24c80ada",
    "kind": "retraction_notice",
    "retracted": false
  }
]
```
