# GroundTruth Benchmark

Generated: 2026-07-04T18:11:26.286002+00:00

## Headline

- Naive memory retrieves retracted originals in 20/20 answers.
- GroundTruth retrieves retracted originals in 0/20 answers.
- Control-claim retention: 5/5.
- Retraction coverage: 25/25 retracted-cohort originals forgotten from GroundTruth memory.
- Correctness judge: skipped with disclosure; the primary metric is retrieved graph context containing a still-present retracted original.

## V2 Semantic Conflict Addendum

The V2 semantic pass is separate from the retraction-forgetting headline metric.

- Status: `partial_quota_stop`.
- Protocol: `exhaustive_all_pairs_over_committed_v2_claims`.
- Coverage: 21/28 committed claim pairs evaluated.
- Confusion matrix: TP 2, TN 18, FP 0, FN 1.
- Precision: 1.00; recall: 0.67.
- Judge: `LLMGateway.acreate_structured_output`.
- Graph-aware answer probes: not run; V2 stopped before the answer-probe phase.
- Full V2 output: [docs/RESULTS-V2.md](RESULTS-V2.md) and `data/v2_results.json`.
- Quota stop: present; numbers above are partial and resumable.

## Metric Definition

The headline metric is the fraction of answers whose Cognee GRAPH_COMPLETION retrieved graph context includes a still-present original claim from `cohort == "retracted_original"`.

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
| Q01 | retracted | naive_memory | True | False | skipped_quota_disclosed | R001, R001, R009, R008, R015, R021, R025, R019, R003, R004, R014 |
| Q01 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R001, R009, R008, R015, R021, R025, R014, R019, C001, C002 |
| Q02 | retracted | naive_memory | True | False | skipped_quota_disclosed | R002, R016, R025, R023, R025, R009, C012, C003, R007, C010, C007 |
| Q02 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R025, R009, C012, C003, C010, C007, C005, C015, C001, R002 |
| Q03 | retracted | naive_memory | True | False | skipped_quota_disclosed | R003, R003, R009, C003, C012, C001, R025, R021, R014, C009, R001 |
| Q03 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R003, R009, C003, C012, C001, R025, R021, C009, R008, R014, C011 |
| Q04 | retracted | naive_memory | True | False | skipped_quota_disclosed | R004, R011, R020, R004, R009, R008, R008, R016, R012, R013, R011, R023, R014 |
| Q04 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R004, R009, R008, R011, C003, R025, C012, C009, R018, R014, R019 |
| Q05 | retracted | naive_memory | True | False | skipped_quota_disclosed | R005, R009, R005, R016, C012, C003, C001, R008, R021, C015, R008, R025 |
| Q05 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R005, R009, C012, C003, C001, C015, R008, R025, C011, C004, C002 |
| Q06 | retracted | naive_memory | True | False | skipped_quota_disclosed | R006, R006, R009, C003, C014, R025, R023, R014, R001, C012, C011, C005 |
| Q06 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R006, R009, C003, C014, C012, C011, C005, R025, C010, R008, C006 |
| Q07 | retracted | naive_memory | True | False | skipped_quota_disclosed | R007, R016, R025, R023, R025, R009, R001, R007, C003, R002, C012, R015 |
| Q07 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R025, R009, R007, C003, C012, C001, C010, R014, R019, C002, C004 |
| Q08 | retracted | naive_memory | True | False | skipped_quota_disclosed | R008, R016, R008, R009, R011, R020, R025, C003, R004, R021, R014, R001, R023 |
| Q08 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R008, R009, R025, C003, C012, R021, R015, C001, C014, R011, R004 |
| Q09 | retracted | naive_memory | True | False | skipped_quota_disclosed | R009, R009, R016, R012, R025, R016, R010, R022, R003, R014, R007 |
| Q09 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R009, R019, R014, C001, C002, C003, C004, C005, C006, C007 |
| Q10 | retracted | naive_memory | True | False | skipped_quota_disclosed | C003, R010, R020, C012, C001, C011, R001, C002, C015, R025, R023, R010, R009 |
| Q10 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | C003, C012, C001, C011, C002, C015, R010, R009, C004, C009, C014 |
| Q11 | retracted | naive_memory | True | False | skipped_quota_disclosed | R011, R020, R011, R009, C003, R010, R008, R018, R015, R012, R013, R014 |
| Q11 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R011, R009, C003, R008, R018, R015, C001, R021, C009, C005, R014 |
| Q12 | retracted | naive_memory | True | False | skipped_quota_disclosed | R012, R009, R011, R012, R013, R008, R005, R015, R018, R025, R010 |
| Q12 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R012, R009, R014, R019, C001, C002, C003, C004, C005, C006, C007 |
| Q13 | control | naive_memory | True | False | skipped_quota_disclosed | C012, C001, C003, C013, C015, C002, C004, C005, R014, C006 |
| Q13 | control | groundtruth_memory | False | True | skipped_quota_disclosed | C012, C001, C003, C013, C015, C002, C004, C005, C006, C010 |
| Q14 | control | naive_memory | True | False | skipped_quota_disclosed | C002, C003, C012, C010, C001, C004, R025, R023, R014, C014, R021 |
| Q14 | control | groundtruth_memory | False | True | skipped_quota_disclosed | C002, C003, C012, C010, C001, C004, C014, C006, C011, C005 |
| Q15 | control | naive_memory | True | False | skipped_quota_disclosed | C003, C012, C001, C015, R021, R021, R009, C002, C010, C006, C014 |
| Q15 | control | groundtruth_memory | False | True | skipped_quota_disclosed | C003, C012, C001, C015, R021, R009, C002, C010, C006, C014, C005 |
| Q16 | control | naive_memory | True | False | skipped_quota_disclosed | C004, C012, C010, C003, C015, C001, R014, C005, C002, R021 |
| Q16 | control | groundtruth_memory | False | True | skipped_quota_disclosed | C004, C012, C010, C003, C015, C001, C005, C002, R025, R009, C014 |
| Q17 | control | naive_memory | True | False | skipped_quota_disclosed | C005, C003, C012, C013, C001, C015, R021, C010, C002, R014 |
| Q17 | control | groundtruth_memory | False | True | skipped_quota_disclosed | C005, C003, C012, C013, C001, C015, C010, C002, C014, C004 |
| Q18 | mixed | naive_memory | True | False | skipped_quota_disclosed | R001, C003, C012, R021, R009, R014, R001, R021, R025, C001, R008 |
| Q18 | mixed | groundtruth_memory | False | False | skipped_quota_disclosed | C003, C012, R021, R009, R001, R025, C001, R008, C011, R003, C010 |
| Q19 | mixed | naive_memory | True | False | skipped_quota_disclosed | R014, R008, R009, R025, C004, R021, R008, R016, C003, R025, R023, R004, C014 |
| Q19 | mixed | groundtruth_memory | False | False | skipped_quota_disclosed | R008, R009, R025, C004, C003, C014, C012, R005, C010, C015, R021 |
| Q20 | mixed | naive_memory | True | False | skipped_quota_disclosed | C003, C012, R003, R009, R003, C001, C009, R014, R001, R021, R008 |
| Q20 | mixed | groundtruth_memory | False | False | skipped_quota_disclosed | C003, C012, R003, R009, C001, C009, R021, R008, R025, C002, C013 |

## Raw Results

Raw JSON: `C:/Users/gudma/OneDrive/Desktop/GITHUB-FILES/groundtruth/data/benchmark_results.json`
