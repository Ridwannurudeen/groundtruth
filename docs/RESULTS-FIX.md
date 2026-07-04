# Fix Pass Results

Generated: 2026-07-04T13:35:27.294840+00:00
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

- Naive memory retrieves retracted originals in 19/20 answers.
- GroundTruth retrieves retracted originals in 0/20 answers.
- Control retention: 5/5.

## Metric

The headline metric is the fraction of answers whose Cognee GRAPH_COMPLETION retrieved graph context includes a still-present original claim from `cohort == "retracted_original"`.

## Sample Recall References

### Q01 - naive_memory

- `cites_retracted`: `True`
- `retracted_dois`: `['10.1016/j.jacadv.2025.101686', '10.1056/nejmoa2023386']`

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
    "claim_id": "R009",
    "cohort": "retracted_original",
    "data_id": "fd06d41a-718c-5980-aa6d-1c99ee176224",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "R008",
    "cohort": "retracted_original",
    "data_id": "7f4d9085-c721-5aa6-b59d-f07faec035f1",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "R014",
    "cohort": "retracted_original",
    "data_id": "a5064084-be81-5ee2-9a52-9a955f1c5683",
    "kind": "original_claim",
    "retracted": true
  },
  {
    "claim_id": "R005",
    "cohort": "retracted_original",
    "data_id": "26a06040-1641-5fb4-b618-aac0a99829ec",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "R007",
    "cohort": "retracted_original",
    "data_id": "e0b8a838-2d0b-5eb6-b05b-22bbacb7b6a6",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "R012",
    "cohort": "retracted_original",
    "data_id": "7de422b8-8606-50c3-951a-17a00330ff96",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "C003",
    "cohort": "active_control",
    "data_id": "d3d710dc-228a-5960-bfce-a06ad17503ce",
    "kind": "original_claim",
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
    "claim_id": "R009",
    "cohort": "retracted_original",
    "data_id": "fd06d41a-718c-5980-aa6d-1c99ee176224",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "R008",
    "cohort": "retracted_original",
    "data_id": "7f4d9085-c721-5aa6-b59d-f07faec035f1",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "R014",
    "cohort": "retracted_original",
    "data_id": "07fce8c0-7a17-5e40-867b-acfcc87d2110",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "R015",
    "cohort": "retracted_original",
    "data_id": "10dd0a00-a6f2-533b-a6af-5d4884e532ac",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "R021",
    "cohort": "retracted_original",
    "data_id": "5a1af7d0-fa90-5f24-bebf-fe8d24c80ada",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "R025",
    "cohort": "retracted_original",
    "data_id": "818fd588-396d-50cf-8cb7-7f38c268eb42",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "R019",
    "cohort": "retracted_original",
    "data_id": "56cb288a-2ea0-558d-8fb8-0b4faab233b3",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "C001",
    "cohort": "active_control",
    "data_id": "2c13440c-7ff4-59ef-aa40-290685b98ff4",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "R007",
    "cohort": "retracted_original",
    "data_id": "e0b8a838-2d0b-5eb6-b05b-22bbacb7b6a6",
    "kind": "retraction_notice",
    "retracted": false
  }
]
```

### Q13 - naive_memory

- `cites_retracted`: `True`
- `retracted_dois`: `['10.1534/genetics.120.303481']`

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
    "claim_id": "C002",
    "cohort": "active_control",
    "data_id": "7a2b1e21-7196-5b43-95d1-74d837680599",
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
    "claim_id": "C001",
    "cohort": "active_control",
    "data_id": "2c13440c-7ff4-59ef-aa40-290685b98ff4",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "R021",
    "cohort": "retracted_original",
    "data_id": "0b3c61b5-688d-5161-8739-a8795964101f",
    "kind": "original_claim",
    "retracted": true
  },
  {
    "claim_id": "C004",
    "cohort": "active_control",
    "data_id": "41a51fa9-c5fa-5006-b45f-3d6bab8de1f0",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C010",
    "cohort": "active_control",
    "data_id": "8f1833d6-f1a6-5a17-bab0-53c083976398",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C005",
    "cohort": "active_control",
    "data_id": "a43d1581-e8c2-52d3-9317-f339967252c0",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C009",
    "cohort": "active_control",
    "data_id": "4d721de0-b238-5daa-afff-6a492dc589bc",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C006",
    "cohort": "active_control",
    "data_id": "5f0c21e3-3306-511a-889a-3219e07a831e",
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
    "claim_id": "C003",
    "cohort": "active_control",
    "data_id": "d3d710dc-228a-5960-bfce-a06ad17503ce",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C002",
    "cohort": "active_control",
    "data_id": "7a2b1e21-7196-5b43-95d1-74d837680599",
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
    "claim_id": "C001",
    "cohort": "active_control",
    "data_id": "2c13440c-7ff4-59ef-aa40-290685b98ff4",
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
    "claim_id": "C011",
    "cohort": "active_control",
    "data_id": "e0feccd5-0f24-515d-9900-32c96ad0be08",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "R021",
    "cohort": "retracted_original",
    "data_id": "5a1af7d0-fa90-5f24-bebf-fe8d24c80ada",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "R009",
    "cohort": "retracted_original",
    "data_id": "fd06d41a-718c-5980-aa6d-1c99ee176224",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "C004",
    "cohort": "active_control",
    "data_id": "41a51fa9-c5fa-5006-b45f-3d6bab8de1f0",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C010",
    "cohort": "active_control",
    "data_id": "8f1833d6-f1a6-5a17-bab0-53c083976398",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C005",
    "cohort": "active_control",
    "data_id": "a43d1581-e8c2-52d3-9317-f339967252c0",
    "kind": "original_claim",
    "retracted": false
  }
]
```

### Q18 - naive_memory

- `cites_retracted`: `True`
- `retracted_dois`: `['10.1056/nejmoa2023386', '10.1534/genetics.120.303481']`

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
    "claim_id": "C003",
    "cohort": "active_control",
    "data_id": "d3d710dc-228a-5960-bfce-a06ad17503ce",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C002",
    "cohort": "active_control",
    "data_id": "7a2b1e21-7196-5b43-95d1-74d837680599",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C001",
    "cohort": "active_control",
    "data_id": "2c13440c-7ff4-59ef-aa40-290685b98ff4",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C010",
    "cohort": "active_control",
    "data_id": "8f1833d6-f1a6-5a17-bab0-53c083976398",
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
    "claim_id": "R009",
    "cohort": "retracted_original",
    "data_id": "fd06d41a-718c-5980-aa6d-1c99ee176224",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "R021",
    "cohort": "retracted_original",
    "data_id": "5a1af7d0-fa90-5f24-bebf-fe8d24c80ada",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "C009",
    "cohort": "active_control",
    "data_id": "4d721de0-b238-5daa-afff-6a492dc589bc",
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
    "claim_id": "R021",
    "cohort": "retracted_original",
    "data_id": "0b3c61b5-688d-5161-8739-a8795964101f",
    "kind": "original_claim",
    "retracted": true
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
    "claim_id": "C001",
    "cohort": "active_control",
    "data_id": "2c13440c-7ff4-59ef-aa40-290685b98ff4",
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
    "claim_id": "R009",
    "cohort": "retracted_original",
    "data_id": "fd06d41a-718c-5980-aa6d-1c99ee176224",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "C010",
    "cohort": "active_control",
    "data_id": "8f1833d6-f1a6-5a17-bab0-53c083976398",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "R021",
    "cohort": "retracted_original",
    "data_id": "5a1af7d0-fa90-5f24-bebf-fe8d24c80ada",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "R008",
    "cohort": "retracted_original",
    "data_id": "7f4d9085-c721-5aa6-b59d-f07faec035f1",
    "kind": "retraction_notice",
    "retracted": false
  },
  {
    "claim_id": "C002",
    "cohort": "active_control",
    "data_id": "7a2b1e21-7196-5b43-95d1-74d837680599",
    "kind": "original_claim",
    "retracted": false
  },
  {
    "claim_id": "C009",
    "cohort": "active_control",
    "data_id": "4d721de0-b238-5daa-afff-6a492dc589bc",
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
    "claim_id": "C008",
    "cohort": "active_control",
    "data_id": "c6bfc753-f9c4-5711-b0fd-f46ef3d5ce98",
    "kind": "original_claim",
    "retracted": false
  }
]
```

## Demo Synthesis

```json
{
  "answers": {
    "groundtruth_memory": {
      "cites_retracted": false,
      "references": [
        {
          "claim_id": "R001",
          "cohort": "retracted_original",
          "data_id": "4b2daf7b-0340-572d-adde-ce491af50f5d",
          "dataset": "groundtruth_memory",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
          "dataset_status": "retracted_forgotten",
          "doi": "10.1056/nejmoa2023386",
          "kind": "retraction_notice",
          "retracted": false,
          "retrieval_rank": 1,
          "score": 0,
          "source": "NEJM: The New England Journal of Medicine",
          "status": "retracted_forgotten"
        },
        {
          "claim_id": "R009",
          "cohort": "retracted_original",
          "data_id": "fd06d41a-718c-5980-aa6d-1c99ee176224",
          "dataset": "groundtruth_memory",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
          "dataset_status": "retracted_forgotten",
          "doi": "10.1016/j.heliyon.2023.e21222",
          "kind": "retraction_notice",
          "retracted": false,
          "retrieval_rank": 2,
          "score": 0,
          "source": "Heliyon",
          "status": "retracted_forgotten"
        },
        {
          "claim_id": "R008",
          "cohort": "retracted_original",
          "data_id": "7f4d9085-c721-5aa6-b59d-f07faec035f1",
          "dataset": "groundtruth_memory",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
          "dataset_status": "retracted_forgotten",
          "doi": "10.1016/j.heliyon.2024.e29871",
          "kind": "retraction_notice",
          "retracted": false,
          "retrieval_rank": 3,
          "score": 0,
          "source": "Heliyon",
          "status": "retracted_forgotten"
        },
        {
          "claim_id": "R014",
          "cohort": "retracted_original",
          "data_id": "07fce8c0-7a17-5e40-867b-acfcc87d2110",
          "dataset": "groundtruth_memory",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
          "dataset_status": "retracted_forgotten",
          "doi": "10.1016/j.jacadv.2025.101686",
          "kind": "retraction_notice",
          "retracted": false,
          "retrieval_rank": 4,
          "score": 0,
          "source": "JACC: Advances",
          "status": "retracted_forgotten"
        },
        {
          "claim_id": "R015",
          "cohort": "retracted_original",
          "data_id": "10dd0a00-a6f2-533b-a6af-5d4884e532ac",
          "dataset": "groundtruth_memory",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
          "dataset_status": "retracted_forgotten",
          "doi": "10.1016/j.heliyon.2025.e41964",
          "kind": "retraction_notice",
          "retracted": false,
          "retrieval_rank": 5,
          "score": 0,
          "source": "Heliyon",
          "status": "retracted_forgotten"
        },
        {
          "claim_id": "R021",
          "cohort": "retracted_original",
          "data_id": "5a1af7d0-fa90-5f24-bebf-fe8d24c80ada",
          "dataset": "groundtruth_memory",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
          "dataset_status": "retracted_forgotten",
          "doi": "10.1534/genetics.120.303481",
          "kind": "retraction_notice",
          "retracted": false,
          "retrieval_rank": 6,
          "score": 0,
          "source": "Genetics",
          "status": "retracted_forgotten"
        },
        {
          "claim_id": "R025",
          "cohort": "retracted_original",
          "data_id": "818fd588-396d-50cf-8cb7-7f38c268eb42",
          "dataset": "groundtruth_memory",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
          "dataset_status": "retracted_forgotten",
          "doi": "10.3109/14767058.2016.1154526",
          "kind": "retraction_notice",
          "retracted": false,
          "retrieval_rank": 7,
          "score": 0,
          "source": "The Journal of Maternal-Fetal & Neonatal Medicine",
          "status": "retracted_forgotten"
        },
        {
          "claim_id": "R019",
          "cohort": "retracted_original",
          "data_id": "56cb288a-2ea0-558d-8fb8-0b4faab233b3",
          "dataset": "groundtruth_memory",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
          "dataset_status": "retracted_forgotten",
          "doi": "10.1016/j.jogc.2023.102264",
          "kind": "retraction_notice",
          "retracted": false,
          "retrieval_rank": 8,
          "score": 0,
          "source": "Journal of Obstetrics and Gynaecology Canada",
          "status": "retracted_forgotten"
        },
        {
          "claim_id": "C001",
          "cohort": "active_control",
          "data_id": "2c13440c-7ff4-59ef-aa40-290685b98ff4",
          "dataset": "groundtruth_memory",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
          "dataset_status": "active",
          "doi": "10.1001/jamainternmed.2015.2558",
          "kind": "original_claim",
          "retracted": false,
          "retrieval_rank": 9,
          "score": 0,
          "source": "JAMA Internal Medicine",
          "status": "active"
        },
        {
          "claim_id": "R007",
          "cohort": "retracted_original",
          "data_id": "e0b8a838-2d0b-5eb6-b05b-22bbacb7b6a6",
          "dataset": "groundtruth_memory",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
          "dataset_status": "retracted_forgotten",
          "doi": "10.1016/j.heliyon.2023.e20232",
          "kind": "retraction_notice",
          "retracted": false,
          "retrieval_rank": 10,
          "score": 0,
          "source": "Heliyon",
          "status": "retracted_forgotten"
        }
      ],
      "retracted_dois": [],
      "status": "completed",
      "text": "The retraction notice says that Avacopan for the Treatment of ANCA-Associated Vasculitis was retracted."
    },
    "naive_memory": {
      "cites_retracted": true,
      "references": [
        {
          "claim_id": "R001",
          "cohort": "retracted_original",
          "data_id": "033e8c14-5e6e-5dbf-8a50-a7b850015cf2",
          "dataset": "naive_memory",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
          "dataset_status": "retracted_retained",
          "doi": "10.1056/nejmoa2023386",
          "kind": "original_claim",
          "retracted": true,
          "retrieval_rank": 1,
          "score": 0,
          "source": "NEJM: The New England Journal of Medicine",
          "status": "retracted_forgotten"
        },
        {
          "claim_id": "R001",
          "cohort": "retracted_original",
          "data_id": "4b2daf7b-0340-572d-adde-ce491af50f5d",
          "dataset": "naive_memory",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
          "dataset_status": "retracted_retained",
          "doi": "10.1056/nejmoa2023386",
          "kind": "retraction_notice",
          "retracted": false,
          "retrieval_rank": 2,
          "score": 0,
          "source": "NEJM: The New England Journal of Medicine",
          "status": "retracted_forgotten"
        },
        {
          "claim_id": "R009",
          "cohort": "retracted_original",
          "data_id": "fd06d41a-718c-5980-aa6d-1c99ee176224",
          "dataset": "naive_memory",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
          "dataset_status": "retracted_retained",
          "doi": "10.1016/j.heliyon.2023.e21222",
          "kind": "retraction_notice",
          "retracted": false,
          "retrieval_rank": 3,
          "score": 0,
          "source": "Heliyon",
          "status": "retracted_forgotten"
        },
        {
          "claim_id": "R008",
          "cohort": "retracted_original",
          "data_id": "7f4d9085-c721-5aa6-b59d-f07faec035f1",
          "dataset": "naive_memory",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
          "dataset_status": "retracted_retained",
          "doi": "10.1016/j.heliyon.2024.e29871",
          "kind": "retraction_notice",
          "retracted": false,
          "retrieval_rank": 4,
          "score": 0,
          "source": "Heliyon",
          "status": "retracted_forgotten"
        },
        {
          "claim_id": "R014",
          "cohort": "retracted_original",
          "data_id": "a5064084-be81-5ee2-9a52-9a955f1c5683",
          "dataset": "naive_memory",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
          "dataset_status": "retracted_retained",
          "doi": "10.1016/j.jacadv.2025.101686",
          "kind": "original_claim",
          "retracted": true,
          "retrieval_rank": 5,
          "score": 0,
          "source": "JACC: Advances",
          "status": "retracted_forgotten"
        },
        {
          "claim_id": "R005",
          "cohort": "retracted_original",
          "data_id": "26a06040-1641-5fb4-b618-aac0a99829ec",
          "dataset": "naive_memory",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
          "dataset_status": "retracted_retained",
          "doi": "10.1016/j.heliyon.2023.e19675",
          "kind": "retraction_notice",
          "retracted": false,
          "retrieval_rank": 6,
          "score": 0,
          "source": "Heliyon",
          "status": "retracted_forgotten"
        },
        {
          "claim_id": "R007",
          "cohort": "retracted_original",
          "data_id": "e0b8a838-2d0b-5eb6-b05b-22bbacb7b6a6",
          "dataset": "naive_memory",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
          "dataset_status": "retracted_retained",
          "doi": "10.1016/j.heliyon.2023.e20232",
          "kind": "retraction_notice",
          "retracted": false,
          "retrieval_rank": 7,
          "score": 0,
          "source": "Heliyon",
          "status": "retracted_forgotten"
        },
        {
          "claim_id": "R012",
          "cohort": "retracted_original",
          "data_id": "7de422b8-8606-50c3-951a-17a00330ff96",
          "dataset": "naive_memory",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
          "dataset_status": "retracted_retained",
          "doi": "10.1007/978-3-030-00524-5_6",
          "kind": "retraction_notice",
          "retracted": false,
          "retrieval_rank": 8,
          "score": 0,
          "source": "Distributed Computing and Artificial Intelligence, Special Sessions II, 15th International Conference",
          "status": "retracted_forgotten"
        },
        {
          "claim_id": "C003",
          "cohort": "active_control",
          "data_id": "d3d710dc-228a-5960-bfce-a06ad17503ce",
          "dataset": "naive_memory",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
          "dataset_status": "active",
          "doi": "10.18137/cardiometry.2022.24.10191021",
          "kind": "original_claim",
          "retracted": false,
          "retrieval_rank": 9,
          "score": 0,
          "source": "CARDIOMETRY",
          "status": "active"
        },
        {
          "claim_id": "R015",
          "cohort": "retracted_original",
          "data_id": "10dd0a00-a6f2-533b-a6af-5d4884e532ac",
          "dataset": "naive_memory",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
          "dataset_status": "retracted_retained",
          "doi": "10.1016/j.heliyon.2025.e41964",
          "kind": "retraction_notice",
          "retracted": false,
          "retrieval_rank": 10,
          "score": 0,
          "source": "Heliyon",
          "status": "retracted_forgotten"
        }
      ],
      "retracted_dois": [
        "10.1016/j.jacadv.2025.101686",
        "10.1056/nejmoa2023386"
      ],
      "status": "completed",
      "text": "The retraction notice says that Avacopan for the Treatment of ANCA-Associated Vasculitis was retracted."
    }
  },
  "question": "Does avacopan remain supported for ANCA-associated vasculitis after the retraction?",
  "question_id": "Q01"
}
```
