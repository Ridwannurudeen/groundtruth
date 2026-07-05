# GroundTruth Benchmark

Generated: 2026-07-05T14:31:48.233814+00:00

## Headline

- Naive memory retrieves retracted originals in 18/20 answers.
- GroundTruth retrieves retracted originals in 0/20 answers.
- Control-claim retention: 5/5.
- Retraction coverage: 25/25 retracted-cohort originals forgotten from GroundTruth memory.
- Correctness judge: skipped with disclosure; the primary metric is relevance-ranked graph references containing a still-present retracted original.

## V2 Semantic Conflict Addendum

The V2 semantic pass is separate from the retraction-forgetting headline metric.

- Status: `complete`.
- Protocol: `exhaustive_all_pairs_over_committed_v2_claims`.
- Coverage: 28/28 committed claim pairs evaluated.
- Confusion matrix: TP 2, TN 25, FP 0, FN 1.
- Precision: 1.00; recall: 0.67.
- Judge: `LLMGateway.acreate_structured_output`.
- Graph-aware answer probes: 3/3 completed; 3/3 surfaced conflicted graph references.
- Full V2 output: [docs/RESULTS-V2.md](RESULTS-V2.md) and `data/v2_results.json`.

## Metric Definition

The headline metric is the fraction of answers whose relevance-ranked Cognee GRAPH_COMPLETION references include a still-present original claim from `cohort == "retracted_original"`. Raw graph references remain in the JSON for audit.

## Reproduction

```powershell
$env:PYTHONIOENCODING='utf-8'; .\.venv\Scripts\python.exe -m groundtruth.benchmark
```

## Memory Integrity

```json
{
  "active_control_total": 15,
  "retracted_original_total": 25,
  "violations": []
}
```

## Retraction Preparation

```json
[
  {
    "action": "already_prepared",
    "claim_id": "R001",
    "doi": "10.1056/nejmoa2023386",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R002",
    "doi": "10.1016/j.heliyon.2024.e30453",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R003",
    "doi": "10.1002/bcp.70249",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R004",
    "doi": "10.1038/s41598-025-96541-2",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R005",
    "doi": "10.1016/j.heliyon.2023.e19675",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R006",
    "doi": "10.1371/journal.pone.0255392",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R007",
    "doi": "10.1016/j.heliyon.2023.e20232",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R008",
    "doi": "10.1016/j.heliyon.2024.e29871",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R009",
    "doi": "10.1016/j.heliyon.2023.e21222",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R010",
    "doi": "10.1007/s00500-023-09589-5",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R011",
    "doi": "10.1007/s00500-023-09482-1",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R012",
    "doi": "10.1007/978-3-030-00524-5_6",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R013",
    "doi": "10.1007/978-3-030-00524-5_7",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R014",
    "doi": "10.1016/j.jacadv.2025.101686",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R015",
    "doi": "10.1016/j.heliyon.2025.e41964",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R016",
    "doi": "10.1016/j.heliyon.2022.e10071",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R017",
    "doi": "10.3389/fnut.2022.803913",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R018",
    "doi": "10.1016/j.heliyon.2024.e37293",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R019",
    "doi": "10.1016/j.jogc.2023.102264",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R020",
    "doi": "10.1007/s00500-021-06668-3",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R021",
    "doi": "10.1534/genetics.120.303481",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R022",
    "doi": "10.1080/14767058.2020.1814239",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R023",
    "doi": "10.1080/14767058.2019.1678132",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R024",
    "doi": "10.1080/14767058.2018.1491030",
    "status": "retracted_forgotten"
  },
  {
    "action": "already_prepared",
    "claim_id": "R025",
    "doi": "10.3109/14767058.2016.1154526",
    "status": "retracted_forgotten"
  }
]
```

## Results

| Q | Kind | Dataset | Retrieves Retracted Original | Control Retained | Correctness | Retrieved References |
|---|---|---|---:|---:|---|---|
| Q01 | retracted | naive_memory | True | False | skipped_quota_disclosed | R001, R001, R015 |
| Q01 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R001, R015 |
| Q02 | retracted | naive_memory | True | False | skipped_quota_disclosed | R002 |
| Q02 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R025, R006, C012, C007, C003 |
| Q03 | retracted | naive_memory | True | False | skipped_quota_disclosed | R003, R003, C003, C012 |
| Q03 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R003, C003, C012 |
| Q04 | retracted | naive_memory | True | False | skipped_quota_disclosed | R004, R004, R023, R011, R018 |
| Q04 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R004, R011 |
| Q05 | retracted | naive_memory | True | False | skipped_quota_disclosed | R005, R005 |
| Q05 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R005 |
| Q06 | retracted | naive_memory | True | False | skipped_quota_disclosed | R006, R006 |
| Q06 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R006, C007 |
| Q07 | retracted | naive_memory | True | False | skipped_quota_disclosed | R007, R007 |
| Q07 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R007 |
| Q08 | retracted | naive_memory | True | False | skipped_quota_disclosed | R008, R008 |
| Q08 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R008 |
| Q09 | retracted | naive_memory | True | False | skipped_quota_disclosed | R009, R009 |
| Q09 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R009 |
| Q10 | retracted | naive_memory | True | False | skipped_quota_disclosed | R010 |
| Q10 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | C007, C011 |
| Q11 | retracted | naive_memory | True | False | skipped_quota_disclosed | R011, R011, R018, R006, R015 |
| Q11 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R011, R018, R006 |
| Q12 | retracted | naive_memory | True | False | skipped_quota_disclosed | R012, R012 |
| Q12 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R012 |
| Q13 | control | naive_memory | False | True | skipped_quota_disclosed | C001, C013, C012, C015, R006 |
| Q13 | control | groundtruth_memory | False | True | skipped_quota_disclosed | C001, C013, C012, C015, R006 |
| Q14 | control | naive_memory | True | False | skipped_quota_disclosed | C002, C004, C010, R006, R025 |
| Q14 | control | groundtruth_memory | False | True | skipped_quota_disclosed | C002, C004, C010, C015, R006 |
| Q15 | control | naive_memory | True | False | skipped_quota_disclosed | C003, C012, R006, C007, R021 |
| Q15 | control | groundtruth_memory | False | True | skipped_quota_disclosed | C003, C012, R006, C007 |
| Q16 | control | naive_memory | True | False | skipped_quota_disclosed | C004, C015, C010, R006, R025 |
| Q16 | control | groundtruth_memory | False | True | skipped_quota_disclosed | C004, C015, C010, R006, R025 |
| Q17 | control | naive_memory | False | True | skipped_quota_disclosed | C005, C001, C013, R006, C003 |
| Q17 | control | groundtruth_memory | False | True | skipped_quota_disclosed | C005, C001, C013, R006, C003 |
| Q18 | mixed | naive_memory | True | False | skipped_quota_disclosed | C003, R001, C012, R006, R021 |
| Q18 | mixed | groundtruth_memory | False | False | skipped_quota_disclosed | C003, C012, R001, R006, R021 |
| Q19 | mixed | naive_memory | True | False | skipped_quota_disclosed | C004, R006, R025, R025 |
| Q19 | mixed | groundtruth_memory | False | False | skipped_quota_disclosed | C004, R005, C015, R006, R025 |
| Q20 | mixed | naive_memory | True | False | skipped_quota_disclosed | R003, C001, R003, C012, R006 |
| Q20 | mixed | groundtruth_memory | False | False | skipped_quota_disclosed | C001, R003, C012, R006, C009 |

## Raw Results

Raw JSON: `C:/Users/gudma/OneDrive/Desktop/GITHUB-FILES/groundtruth/data/benchmark_results.json`
