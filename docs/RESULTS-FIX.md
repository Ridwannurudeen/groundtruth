# Fix Pass Results

Generated: 2026-07-05T14:31:48.233814+00:00
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
    "data_id": "99950f89-006f-5490-947a-1245ca4f5da4",
    "kind": "original_claim",
    "retracted": true
  },
  {
    "claim_id": "R001",
    "cohort": "retracted_original",
    "data_id": "c17c7120-afd7-5ed8-b970-7df0452ad41f",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "R015",
    "cohort": "retracted_original",
    "data_id": "7036b031-b33a-53c1-89f6-abfabcdaf6c5",
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
    "data_id": "c17c7120-afd7-5ed8-b970-7df0452ad41f",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "R015",
    "cohort": "retracted_original",
    "data_id": "7036b031-b33a-53c1-89f6-abfabcdaf6c5",
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
    "data_id": "6cae129e-8367-5c6c-a82b-a36655612134",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C013",
    "cohort": "active_control",
    "data_id": "00de2ff6-3c1a-553e-aaa6-0fad67411f31",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C012",
    "cohort": "active_control",
    "data_id": "a4276ec7-ba67-5bbd-a971-b2216ccce08b",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C015",
    "cohort": "active_control",
    "data_id": "88a1beed-4b16-5e49-9c7b-a7d011ad04c6",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "R006",
    "cohort": "retracted_original",
    "data_id": "fa4b8ca8-6aea-50aa-8a28-f6c5b459a163",
    "kind": "retraction_notice",
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
    "data_id": "6cae129e-8367-5c6c-a82b-a36655612134",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C013",
    "cohort": "active_control",
    "data_id": "00de2ff6-3c1a-553e-aaa6-0fad67411f31",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C012",
    "cohort": "active_control",
    "data_id": "a4276ec7-ba67-5bbd-a971-b2216ccce08b",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C015",
    "cohort": "active_control",
    "data_id": "88a1beed-4b16-5e49-9c7b-a7d011ad04c6",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "R006",
    "cohort": "retracted_original",
    "data_id": "fa4b8ca8-6aea-50aa-8a28-f6c5b459a163",
    "kind": "retraction_notice",
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
    "data_id": "67e303a1-2bc3-548f-b542-1c226f3881b4",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "R001",
    "cohort": "retracted_original",
    "data_id": "99950f89-006f-5490-947a-1245ca4f5da4",
    "kind": "original_claim",
    "retracted": true
  },
  {
    "claim_id": "C012",
    "cohort": "active_control",
    "data_id": "a4276ec7-ba67-5bbd-a971-b2216ccce08b",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "R006",
    "cohort": "retracted_original",
    "data_id": "fa4b8ca8-6aea-50aa-8a28-f6c5b459a163",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "R021",
    "cohort": "retracted_original",
    "data_id": "a30802d4-be71-5fc8-afe2-0fa541b7f0eb",
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
    "data_id": "67e303a1-2bc3-548f-b542-1c226f3881b4",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C012",
    "cohort": "active_control",
    "data_id": "a4276ec7-ba67-5bbd-a971-b2216ccce08b",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "R001",
    "cohort": "retracted_original",
    "data_id": "c17c7120-afd7-5ed8-b970-7df0452ad41f",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "R006",
    "cohort": "retracted_original",
    "data_id": "fa4b8ca8-6aea-50aa-8a28-f6c5b459a163",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "R021",
    "cohort": "retracted_original",
    "data_id": "a30802d4-be71-5fc8-afe2-0fa541b7f0eb",
    "kind": "retraction_notice",
    "retracted": false
  }
]
```
