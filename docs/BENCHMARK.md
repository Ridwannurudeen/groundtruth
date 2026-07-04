# GroundTruth Benchmark

Generated: 2026-07-04T19:15:26.715926+00:00

## Headline

- Naive memory retrieves retracted originals in 18/20 answers.
- GroundTruth retrieves retracted originals in 0/20 answers.
- Control-claim retention: 5/5.
- Retraction coverage: 25/25 retracted-cohort originals forgotten from GroundTruth memory.
- Correctness judge: skipped with disclosure; the primary metric is relevance-ranked graph references containing a still-present retracted original.

## V2 Semantic Conflict Addendum

The V2 semantic pass is separate from the retraction-forgetting headline metric.

- Status: `partial_quota_stop`.
- Protocol: `exhaustive_all_pairs_over_committed_v2_claims`.
- Coverage: 22/28 committed claim pairs evaluated.
- Confusion matrix: TP 2, TN 19, FP 0, FN 1.
- Precision: 1.00; recall: 0.67.
- Judge: `LLMGateway.acreate_structured_output`.
- Graph-aware answer probes: not run; V2 stopped before the answer-probe phase.
- Full V2 output: [docs/RESULTS-V2.md](RESULTS-V2.md) and `data/v2_results.json`.
- Quota stop: present; numbers above are partial and resumable.

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
[]
```

## Results

| Q | Kind | Dataset | Retrieves Retracted Original | Control Retained | Correctness | Retrieved References |
|---|---|---|---:|---:|---|---|
| Q01 | retracted | naive_memory | True | False | skipped_quota_disclosed | R001, R001, R015 |
| Q01 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R001, R015 |
| Q02 | retracted | naive_memory | True | False | skipped_quota_disclosed | R002 |
| Q02 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R002 |
| Q03 | retracted | naive_memory | True | False | skipped_quota_disclosed | R003, R003, C003, C012 |
| Q03 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R003, C003, C012 |
| Q04 | retracted | naive_memory | True | False | skipped_quota_disclosed | R004, R004, R023, R011, R020 |
| Q04 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R004, R011, R025, R018 |
| Q05 | retracted | naive_memory | True | False | skipped_quota_disclosed | R005, R005 |
| Q05 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R005, C002 |
| Q06 | retracted | naive_memory | True | False | skipped_quota_disclosed | R006, R006, R023 |
| Q06 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R006, C010 |
| Q07 | retracted | naive_memory | True | False | skipped_quota_disclosed | R007, R007 |
| Q07 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R007 |
| Q08 | retracted | naive_memory | True | False | skipped_quota_disclosed | R008, R008, R016 |
| Q08 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R008 |
| Q09 | retracted | naive_memory | True | False | skipped_quota_disclosed | R009, R009 |
| Q09 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R009 |
| Q10 | retracted | naive_memory | True | False | skipped_quota_disclosed | R010, R010, C011 |
| Q10 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R010, C011 |
| Q11 | retracted | naive_memory | True | False | skipped_quota_disclosed | R011, R011, R020, R018, R015 |
| Q11 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R011, R018, R015 |
| Q12 | retracted | naive_memory | True | False | skipped_quota_disclosed | R012, R012 |
| Q12 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R012 |
| Q13 | control | naive_memory | False | True | skipped_quota_disclosed | C001, C013, C012, C015, C004 |
| Q13 | control | groundtruth_memory | False | True | skipped_quota_disclosed | C001, C013, C012, C015, C004 |
| Q14 | control | naive_memory | True | False | skipped_quota_disclosed | C002, C010, C004, C001, R025 |
| Q14 | control | groundtruth_memory | False | True | skipped_quota_disclosed | C002, C010, C004, C011, C001 |
| Q15 | control | naive_memory | True | False | skipped_quota_disclosed | C003, C012, R021, R021, C010 |
| Q15 | control | groundtruth_memory | False | True | skipped_quota_disclosed | C003, C012, R021, C010, C005 |
| Q16 | control | naive_memory | False | True | skipped_quota_disclosed | C004, C010, C015, C002, C001 |
| Q16 | control | groundtruth_memory | False | True | skipped_quota_disclosed | C004, C010, C015, C002, C001 |
| Q17 | control | naive_memory | True | False | skipped_quota_disclosed | C005, C013, C001, C003, R021 |
| Q17 | control | groundtruth_memory | False | True | skipped_quota_disclosed | C005, C013, C001, C003, C010 |
| Q18 | mixed | naive_memory | True | False | skipped_quota_disclosed | C003, R001, C012, R001, R021 |
| Q18 | mixed | groundtruth_memory | False | False | skipped_quota_disclosed | C003, C012, R001, R003, R021 |
| Q19 | mixed | naive_memory | True | False | skipped_quota_disclosed | C004, R025, R025, R023, R004 |
| Q19 | mixed | groundtruth_memory | False | False | skipped_quota_disclosed | C004, R005, C010, C015, R025 |
| Q20 | mixed | naive_memory | True | False | skipped_quota_disclosed | R003, R003, C001, C012, C009 |
| Q20 | mixed | groundtruth_memory | False | False | skipped_quota_disclosed | R003, C001, C013, C012, C009 |

## Raw Results

Raw JSON: `C:/Users/gudma/OneDrive/Desktop/GITHUB-FILES/groundtruth/data/benchmark_results.json`
