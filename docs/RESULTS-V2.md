# GroundTruth V2 Results

Generated: 2026-07-05T07:02:41.184828+00:00
Status: `complete`

## Baseline Before V2

- Full baseline `pytest -q` timed out twice before code changes: first at 180s, then at 360s.
- Split baseline before code changes: `tests/test_benchmark.py -q` passed 3 tests; `tests/test_web.py -q` passed 5 tests.
- Split baseline `tests/test_watcher.py -q` timed out at 240s even after stopping stale pytest/uvicorn workers.

## V2-4 Concrete Claim Spot Check

```json
[
  {
    "claim_id": "V2C001",
    "claim_text": "Vitamin D3 supplementation at 4000 IU per day does not significantly lower diabetes risk versus placebo in adults at high risk for type 2 diabetes.",
    "real_assertion": true
  },
  {
    "claim_id": "V2C002",
    "claim_text": "Vitamin D supplementation appears to reduce progression to type 2 diabetes in people with prediabetes.",
    "real_assertion": true
  },
  {
    "claim_id": "V2C003",
    "claim_text": "Marine n-3 fatty acid supplementation does not lower the incidence of major cardiovascular events compared with placebo.",
    "real_assertion": true
  },
  {
    "claim_id": "V2C004",
    "claim_text": "Marine omega-3 supplementation lowers risk for myocardial infarction, coronary heart disease death, cardiovascular disease death, and total cardiovascular disease.",
    "real_assertion": true
  },
  {
    "claim_id": "V2C005",
    "claim_text": "Sixteen weeks of probiotic supplementation shows no beneficial effect on glycemic control, lipid profiles, or weight in patients with type 2 diabetes.",
    "real_assertion": true
  },
  {
    "claim_id": "V2C006",
    "claim_text": "Probiotic interventions can positively modulate glucose control in type 2 diabetes, including HbA1c, insulin, and HOMA-IR at specific intervention windows.",
    "real_assertion": true
  },
  {
    "claim_id": "V2C007",
    "claim_text": "Reduced dietary sodium lowers blood pressure, and the DASH diet lowers systolic blood pressure at each tested sodium level.",
    "real_assertion": true
  },
  {
    "claim_id": "V2C008",
    "claim_text": "A low-fat dietary pattern does not significantly reduce coronary heart disease, stroke, or overall cardiovascular disease risk.",
    "real_assertion": true
  }
]
```

## V2-1 Semantic Conflict Detection

- Candidate method: `fastembed:BAAI/bge-small-en cosine`
- Judge: `LLMGateway.acreate_structured_output`

Coverage:

```json
{
  "all_pair_total": 28,
  "candidate_pairs": 28,
  "claims": 8,
  "evaluated_pairs": 28,
  "manifest_pairs": 28,
  "manifest_pairs_not_candidates": [],
  "pending_pairs": [],
  "planned_pairs": 28,
  "protocol": "exhaustive_all_pairs_over_committed_v2_claims",
  "unlabeled_candidate_pairs": []
}
```

Metrics:

```json
{
  "evaluated_pairs": 28,
  "false_negative": 1,
  "false_positive": 0,
  "precision": 1.0,
  "recall": 0.6666666666666666,
  "true_negative": 25,
  "true_positive": 2
}
```

Pairs:

```json
[
  {
    "cached": true,
    "claim_a_id": "V2C002",
    "claim_b_id": "V2C001",
    "decision": {
      "basis": "Claim A, a systematic review and meta-analysis published in 2020, synthesizes evidence that Vitamin D supplementation appears to reduce progression to type 2 diabetes in people with prediabetes. Claim B, from a 2019 randomized controlled trial (the D2d study), specifically states that Vitamin D3 supplementation at 4000 IU per day does not significantly lower diabetes risk in adults at high risk. Given that Claim A is a more recent meta-analysis, it likely incorporated the findings of the D2d study (Claim B's source) along with other relevant studies to provide a more comprehensive and statistically robust overall estimate of effect. Therefore, its conclusion, representing a broader synthesis of evidence, supersedes the finding of a single trial, even a large one.",
      "confidence": 0.9,
      "conflicts": true,
      "direction": "a_supersedes_b"
    },
    "expected_conflict": true,
    "pair_signature": "bf0564e7cac8f4bcb57501ab1cd93899bb43be96307097714d5a1762d272cab0",
    "similarity": 0.951185
  },
  {
    "cached": true,
    "claim_a_id": "V2C004",
    "claim_b_id": "V2C003",
    "decision": {
      "basis": "Both claims evaluate the effect of marine omega-3 (n-3) fatty acid supplementation on cardiovascular events. Claim A asserts that supplementation lowers the risk for several cardiovascular outcomes (myocardial infarction, coronary heart disease death, cardiovascular disease death, and total cardiovascular disease). Claim B, conversely, states that marine n-3 fatty acid supplementation does not lower the incidence of major cardiovascular events compared with placebo. These are directly contradictory findings regarding the efficacy of marine omega-3 supplementation for cardiovascular disease prevention.",
      "confidence": 1.0,
      "conflicts": true,
      "direction": "mutual"
    },
    "expected_conflict": true,
    "pair_signature": "855cc3ffaed9d311aa4e5963ddc82c807ab58b29656df4b1760b3965fe8e9071",
    "similarity": 0.943345
  },
  {
    "cached": true,
    "claim_a_id": "V2C006",
    "claim_b_id": "V2C005",
    "decision": {
      "basis": "Claim A states that probiotic interventions 'can positively modulate glucose control in type 2 diabetes... at specific intervention windows.' This implies that the beneficial effect is not universal but conditional on the intervention duration. Claim B specifies a particular intervention window (16 weeks) where 'no beneficial effect' was observed. These claims do not directly conflict because Claim B's finding for a 16-week duration could be one of the intervention windows where, according to the nuance implied by Claim A, no positive modulation occurs. Claim A's statement is conditional, allowing for findings like Claim B without creating a contradiction.",
      "confidence": 0.9,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": true,
    "pair_signature": "ddb9aef2a79a6ac00e1f04ff1bf263d340dc23c2af62ff1de7c47d3e9a4d9535",
    "similarity": 0.918426
  },
  {
    "cached": true,
    "claim_a_id": "V2C008",
    "claim_b_id": "V2C003",
    "decision": {
      "basis": "Claim A addresses a low-fat dietary pattern, while Claim B addresses marine n-3 fatty acid supplementation. These are distinct interventions/exposures, even though both relate to diet and cardiovascular disease outcomes. Therefore, they do not make incompatible assertions about the same intervention.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "e6df2583f6e30eceb2347a4b1007f6be2e05a60dc710ba478977ea742a784f59",
    "similarity": 0.908791
  },
  {
    "cached": true,
    "claim_a_id": "V2C006",
    "claim_b_id": "V2C002",
    "decision": {
      "basis": "The claims discuss different interventions (probiotics vs. vitamin D), different populations (type 2 diabetes patients vs. people with prediabetes), and different outcomes (modulating glucose control in existing T2D vs. preventing progression to T2D). There is no conflict.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "839eacec0f1085b165877b634b36f63985f8d846c87a6e72450512e3a64dad1d",
    "similarity": 0.895713
  },
  {
    "cached": true,
    "claim_a_id": "V2C005",
    "claim_b_id": "V2C001",
    "decision": {
      "basis": "Claim A examines the effect of probiotic supplementation on glycemic control, lipid profiles, and weight in patients with type 2 diabetes. Claim B investigates the effect of Vitamin D3 supplementation on diabetes risk in adults at high risk for type 2 diabetes. The interventions (probiotics vs. Vitamin D3), populations (diagnosed T2D vs. at-risk for T2D), and specific outcomes (management of existing T2D vs. prevention of T2D) are all different. Therefore, there is no direct conflict between the claims.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "39c96c05fb5ec0a5fa6205be7617b8b09a0d522a7d47c686d2d4d4b9e9ee0e7b",
    "similarity": 0.893639
  },
  {
    "cached": true,
    "claim_a_id": "V2C003",
    "claim_b_id": "V2C001",
    "decision": {
      "basis": "Claim A discusses marine n-3 fatty acid supplementation and its effect on major cardiovascular events. Claim B discusses Vitamin D3 supplementation and its effect on type 2 diabetes risk. These claims involve different interventions, different outcomes, and different diseases, so they do not conflict.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "f6e68dc1b9975b3f6a4e8930ee7d961d8045200031a249ee5b34a3a6b554ebbe",
    "similarity": 0.892784
  },
  {
    "cached": true,
    "claim_a_id": "V2C008",
    "claim_b_id": "V2C004",
    "decision": {
      "basis": "The claims discuss different interventions/exposures. Claim A is about a 'low-fat dietary pattern' and its effect on cardiovascular disease risk. Claim B is about 'marine omega-3 supplementation' and its effect on cardiovascular disease risk. Since the interventions are distinct, their findings are not in conflict but rather address different aspects of cardiovascular health management.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "cd51f9a82cbe172c54acd4ac7098c63986681c41fe527d730f3bb9e18f3de2c1",
    "similarity": 0.891279
  },
  {
    "cached": true,
    "claim_a_id": "V2C005",
    "claim_b_id": "V2C002",
    "decision": {
      "basis": "Claim A is about the effect of probiotic supplementation on glycemic control, lipid profiles, and weight in patients with type 2 diabetes. Claim B is about the effect of Vitamin D supplementation on the progression to type 2 diabetes in people with prediabetes. These claims involve different interventions (probiotics vs. Vitamin D), different populations (existing T2D patients vs. people with prediabetes), and different primary outcomes (managing existing T2D symptoms vs. preventing T2D progression). Thus, they do not make incompatible assertions.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "b04d37c7c56f46ba29a021d0bf7f70ad8eb18e311802ec9e3f0f5f63d6935efc",
    "similarity": 0.891125
  },
  {
    "cached": true,
    "claim_a_id": "V2C005",
    "claim_b_id": "V2C003",
    "decision": {
      "basis": "Claim A discusses the effect of probiotic supplementation on glycemic control, lipid profiles, and weight in patients with type 2 diabetes. Claim B discusses the effect of marine n-3 fatty acid supplementation on the incidence of major cardiovascular events. The interventions (probiotics vs. marine n-3 fatty acids), populations (type 2 diabetes patients vs. general/cardiovascular risk population), and outcomes (glycemic control/lipids/weight vs. cardiovascular events) are all distinct. Therefore, there is no conflict between the claims.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "5869fd4b4a88bd9b472e4d27ccc2463f2888c310e23ca6e77e525a8731545045",
    "similarity": 0.888121
  },
  {
    "cached": true,
    "claim_a_id": "V2C008",
    "claim_b_id": "V2C005",
    "decision": {
      "basis": "The claims discuss entirely different interventions (low-fat diet vs. probiotic supplementation), different primary outcomes (cardiovascular disease risk vs. glycemic control/lipid profiles/weight), and different populations (general population vs. patients with type 2 diabetes). There is no overlap or conflicting assertion between them.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "095b9502839f1d07ad8608ac497208e07154a843875aa43538dcb4613b2eebb1",
    "similarity": 0.884347
  },
  {
    "cached": true,
    "claim_a_id": "V2C006",
    "claim_b_id": "V2C001",
    "decision": {
      "basis": "Claim A discusses the effect of probiotic interventions on glucose control in type 2 diabetes, while Claim B discusses the effect of Vitamin D3 supplementation on diabetes risk in adults at high risk for type 2 diabetes. These claims involve different interventions (probiotics vs. Vitamin D3) and different, though related, outcomes/populations, hence they do not conflict.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "c002ef7146a570fd5029263efca9131d4f5332ffe8f87bf22e1b07b7a49a09b2",
    "similarity": 0.884037
  },
  {
    "cached": true,
    "claim_a_id": "V2C004",
    "claim_b_id": "V2C001",
    "decision": {
      "basis": "The claims discuss different interventions (marine omega-3 vs. vitamin D3 supplementation) and different health outcomes (cardiovascular disease events vs. diabetes risk). There is no overlap in the subject matter that would lead to a conflict.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "c691544213a3792c7c18d44a5fb2517c080c423fff8eac1933a0d6d0a2259209",
    "similarity": 0.883166
  },
  {
    "cached": true,
    "claim_a_id": "V2C004",
    "claim_b_id": "V2C002",
    "decision": {
      "basis": "Claim A discusses marine omega-3 supplementation and cardiovascular disease outcomes, while Claim B discusses vitamin D supplementation and progression to type 2 diabetes. They concern different interventions, different populations (general population vs. people with prediabetes), and different outcomes (cardiovascular events vs. diabetes progression). There is no overlap in their assertions that would lead to a conflict.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "6f9d0bed41f54c7c2cab06576109c26ea38b07d44ac39bba86b4344fe0c5cfbe",
    "similarity": 0.878346
  },
  {
    "cached": true,
    "claim_a_id": "V2C003",
    "claim_b_id": "V2C002",
    "decision": {
      "basis": "Claim A discusses the effect of marine n-3 fatty acid supplementation on cardiovascular events, while Claim B discusses the effect of vitamin D supplementation on progression to type 2 diabetes. They concern different interventions and different outcomes, therefore there is no conflict.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "47d8f3b54cdb68e7d722199395ea2c8352f573fd3d63ce382f24c5ee5651adcb",
    "similarity": 0.875913
  },
  {
    "cached": true,
    "claim_a_id": "V2C008",
    "claim_b_id": "V2C007",
    "decision": {
      "basis": "Claim A discusses the effect of a low-fat dietary pattern on coronary heart disease, stroke, or overall cardiovascular disease risk. Claim B discusses the effects of reduced dietary sodium and the DASH diet on blood pressure. These claims examine different dietary interventions and different outcomes, therefore they do not conflict.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "383265dace676dbcd9d013977ad8a6f0834eb537e0ea7acca0d3c31935ac934d",
    "similarity": 0.873604
  },
  {
    "cached": true,
    "claim_a_id": "V2C007",
    "claim_b_id": "V2C004",
    "decision": {
      "basis": "Claim A discusses the effect of reduced dietary sodium and the DASH diet on blood pressure. Claim B discusses the effect of marine omega-3 supplementation on various cardiovascular disease outcomes. They address different interventions/exposures (dietary patterns/sodium vs. omega-3 supplements) and different primary outcomes (blood pressure vs. cardiovascular events). There is no direct conflict in their assertions.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "248f5830823ff2abfd2af98a2e48507316e3f3e3cc24befce58929394e6f5fa8",
    "similarity": 0.870149
  },
  {
    "cached": true,
    "claim_a_id": "V2C007",
    "claim_b_id": "V2C003",
    "decision": {
      "basis": "Claim A discusses the effect of dietary sodium and the DASH diet on blood pressure. Claim B discusses the effect of marine n-3 fatty acid supplementation on the incidence of major cardiovascular events. These claims address entirely different interventions/exposures and outcomes, so there is no basis for conflict.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "7a8f862398901951a2a0ba8e65bb3be6e7c542ddbe05990693bfd73310d51c08",
    "similarity": 0.866138
  },
  {
    "cached": true,
    "claim_a_id": "V2C005",
    "claim_b_id": "V2C004",
    "decision": {
      "basis": "Claim A discusses the effect of probiotic supplementation on glycemic control, lipid profiles, and weight in type 2 diabetes patients. Claim B discusses the effect of marine omega-3 supplementation on various cardiovascular disease outcomes. The claims concern different interventions (probiotics vs. marine omega-3), different primary outcomes (glycemic/lipid/weight vs. cardiovascular events), and potentially different populations, thus there is no conflict.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "24b0343e75f720a3a6c5caca7ca2754ce0fba155d3c3b623bd3d8462f756ae3f",
    "similarity": 0.860303
  },
  {
    "cached": true,
    "claim_a_id": "V2C008",
    "claim_b_id": "V2C002",
    "decision": {
      "basis": "Claim A discusses a low-fat dietary pattern and its effect on cardiovascular disease risk, while Claim B discusses vitamin D supplementation and its effect on progression to type 2 diabetes in people with prediabetes. These claims address entirely different interventions, outcomes, and populations, and thus do not conflict.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "b60089f885fecea24cc084838f7818d3306705995bbbdc44f453c2e11dcf52aa",
    "similarity": 0.856985
  },
  {
    "cached": true,
    "claim_a_id": "V2C006",
    "claim_b_id": "V2C003",
    "decision": {
      "basis": "The claims discuss entirely different interventions (probiotics vs. marine n-3 fatty acids) and different outcomes (glucose control in type 2 diabetes vs. major cardiovascular events). There is no overlap in topic, population, or effect to suggest a conflict.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "7f973d430dac190be99813518894fe5297348d090db076ff6110e14b84eee2d1",
    "similarity": 0.85586
  },
  {
    "cached": true,
    "claim_a_id": "V2C007",
    "claim_b_id": "V2C002",
    "decision": {
      "basis": "Claim A discusses the effects of dietary sodium and the DASH diet on blood pressure. Claim B discusses the effect of Vitamin D supplementation on the progression to type 2 diabetes. These claims address entirely different interventions, outcomes, and health conditions, thus they do not conflict.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "a73bb47d12a2ce40d6181ee7b634eb89969688a4490314644326ab32e9df67eb",
    "similarity": 0.85402
  },
  {
    "cached": true,
    "claim_a_id": "V2C008",
    "claim_b_id": "V2C001",
    "decision": {
      "basis": "Claim A discusses the effect of a low-fat dietary pattern on cardiovascular disease risk, while Claim B discusses the effect of vitamin D3 supplementation on diabetes risk. These claims concern different interventions/exposures and different health outcomes, so they do not conflict.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "de50c6e8709c84de9d22849b28b4a9eea503007372b8434df79a8adc155086e7",
    "similarity": 0.85231
  },
  {
    "cached": false,
    "claim_a_id": "V2C006",
    "claim_b_id": "V2C004",
    "decision": {
      "basis": "Claim A discusses the effect of probiotic interventions on glucose control in type 2 diabetes, while Claim B discusses the effect of marine omega-3 supplementation on cardiovascular disease outcomes. They address different interventions, different outcomes, and potentially different populations, thus there is no conflict.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "b0014f8a3e032d4645d1d8bf6e283436db721b2f53df5ab20d38158e55b6ff5d",
    "similarity": 0.847804
  },
  {
    "cached": false,
    "claim_a_id": "V2C007",
    "claim_b_id": "V2C001",
    "decision": {
      "basis": "Claim A discusses the effect of dietary sodium reduction and the DASH diet on blood pressure. Claim B discusses the effect of Vitamin D3 supplementation on diabetes risk. These claims concern different interventions, different outcomes, and different diseases/conditions. There is no overlap or incompatibility between them.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "b02111f660deeea68f8a730945872af4333fe9d82633dd85be496025c88e8cfa",
    "similarity": 0.844868
  },
  {
    "cached": false,
    "claim_a_id": "V2C007",
    "claim_b_id": "V2C005",
    "decision": {
      "basis": "Claim A discusses the effects of reduced dietary sodium and the DASH diet on blood pressure. Claim B discusses the effects of probiotic supplementation on glycemic control, lipid profiles, and weight in patients with type 2 diabetes. They investigate completely different interventions, populations (general vs. type 2 diabetes patients), and outcomes (blood pressure vs. glycemic control, lipids, and weight). There is no common element to compare for a conflict.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "9a5674e08b530509c5238b10f67a3aafa9ba2a1a886e2408a2169dc5182a06d1",
    "similarity": 0.82594
  },
  {
    "cached": false,
    "claim_a_id": "V2C007",
    "claim_b_id": "V2C006",
    "decision": {
      "basis": "Claim A discusses the effects of reduced dietary sodium and the DASH diet on blood pressure. Claim B discusses the effects of probiotic interventions on glucose control in type 2 diabetes. These claims address entirely different interventions, outcomes, and populations, and therefore do not conflict.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "9788142f70ed2d773794c53747c62b36690f2213d6e1b494b14e28a3a6d9e3dc",
    "similarity": 0.825257
  },
  {
    "cached": false,
    "claim_a_id": "V2C008",
    "claim_b_id": "V2C006",
    "decision": {
      "basis": "The claims discuss entirely different interventions (low-fat diet vs. probiotics), different populations (general population for cardiovascular disease risk vs. patients with type 2 diabetes), and different outcomes (cardiovascular disease risk vs. glucose control). There is no overlap in any of the critical elements to create a conflict.",
      "confidence": 1.0,
      "conflicts": false,
      "direction": "none"
    },
    "expected_conflict": false,
    "pair_signature": "43a3ac79aa77541fe206fc57a8dfffd18c4c01648784f7b442fd79261d9471ff",
    "similarity": 0.825249
  }
]
```

## V2-2 Graph-Aware Answer Probes

```json
[
  {
    "cites_retracted": false,
    "cites_superseded": true,
    "question": "Does vitamin D supplementation prevent type 2 diabetes in adults with prediabetes?",
    "question_id": "V2Q01",
    "reference_claim_ids": [
      "V2C002",
      "V2C001",
      "V2C005",
      "V2C006",
      "V2C003"
    ],
    "status": "completed",
    "superseded_dois": [
      "10.1056/NEJMoa1811403",
      "10.1056/NEJMoa1900906",
      "10.1210/clinem/dgaa607",
      "10.3389/fendo.2024.1392306",
      "10.3389/fendo.2024.1440286"
    ],
    "synthesis_mode": "GRAPH_COMPLETION only_context=False include_references=True",
    "text_excerpt": "Vitamin D supplementation appears to reduce progression to type 2 diabetes in people with prediabetes.\n\ngroundtruth_v2_semantic_memory retrieved 10.1210/clinem/dgaa607, but the graph marks that source as conflicted via `contradicts`. Basis: Claim A states that vitamin D3 supplementation does not significantly lower diabetes risk in high-risk adults, while Claim B suggests that vitamin D supplementation reduces progression to type 2 diabetes in people with prediabetes. The populations (high-risk adults vs. people with prediabetes) and the outcomes (diabetes risk vs. progression to type 2 diabetes) are not identical, leading to a potential conflict in interpretation or specific application of "
  },
  {
    "cites_retracted": false,
    "cites_superseded": true,
    "question": "Should omega-3 supplementation be described as reducing cardiovascular events?",
    "question_id": "V2Q02",
    "reference_claim_ids": [
      "V2C004",
      "V2C003",
      "V2C002",
      "V2C008",
      "V2C001"
    ],
    "status": "completed",
    "superseded_dois": [
      "10.1056/NEJMoa1811403",
      "10.1056/NEJMoa1900906",
      "10.1161/JAHA.119.013543",
      "10.1210/clinem/dgaa607"
    ],
    "synthesis_mode": "GRAPH_COMPLETION only_context=False include_references=True",
    "text_excerpt": "Marine omega-3 supplementation lowers risk for myocardial infarction, coronary heart disease death, cardiovascular disease death, and total cardiovascular disease. However, marine n-3 fatty acid supplementation does not lower the incidence of major cardiovascular events compared with placebo.\n\ngroundtruth_v2_semantic_memory retrieved 10.1161/JAHA.119.013543, but the graph marks that source as conflicted via `contradicts`. Basis: Claim B states that marine omega-3 supplementation lowers risk for myocardial infarction, coronary heart disease death, cardiovascular disease death, and total cardiovascular disease, directly contradicting Claim A, which states that marine n-3 fatty acid supplementa"
  },
  {
    "cites_retracted": false,
    "cites_superseded": true,
    "question": "Do probiotics improve glycemic control in type 2 diabetes?",
    "question_id": "V2Q03",
    "reference_claim_ids": [
      "V2C006",
      "V2C005",
      "V2C002",
      "V2C001"
    ],
    "status": "completed",
    "superseded_dois": [
      "10.1056/NEJMoa1900906",
      "10.1210/clinem/dgaa607",
      "10.3389/fendo.2024.1392306",
      "10.3389/fendo.2024.1440286"
    ],
    "synthesis_mode": "GRAPH_COMPLETION only_context=False include_references=True",
    "text_excerpt": "Probiotic interventions can positively modulate glucose control in type 2 diabetes, including HbA1c, insulin, and HOMA-IR. However, sixteen weeks of probiotic supplementation shows no beneficial effect on glycemic control in patients with type 2 diabetes.\n\ngroundtruth_v2_semantic_memory retrieved 10.3389/fendo.2024.1392306, but the graph marks that source as conflicted via `contradicts`. Basis: Claim A asserts no beneficial effect of probiotic supplementation on glycemic control in patients with type 2 diabetes, while Claim B states that probiotic interventions can positively modulate glucose control in the same population. The claims directly contradict each other regarding the efficacy of "
  }
]
```

Full raw V2 JSON: `C:/Users/gudma/OneDrive/Desktop/GITHUB-FILES/groundtruth/data/v2_results.json`

## Edge Writes

```json
[
  {
    "action": "already_exists",
    "edges": [],
    "pair": [
      "V2C002",
      "V2C001"
    ],
    "semantic_action": "auto_act",
    "state_result": {
      "basis": "Semantic inference for V2C001::V2C002 auto-superseded V2C001 with confidence 0.90; basis: Claim A, a systematic review and meta-analysis published in 2020, synthesizes evidence that Vitamin D supplementation appears to reduce progression to type 2 diabetes in people with prediabetes. Claim B, from a 2019 randomized controlled trial (the D2d study), specifically states that Vitamin D3 supplementation at 4000 IU per day does not significantly lower diabetes risk in adults at high risk. Given that Claim A is a more recent meta-analysis, it likely incorporated the findings of the D2d study (Claim B's source) along with other relevant studies to provide a more comprehensive and statistically robust overall estimate of effect. Therefore, its conclusion, representing a broader synthesis of evidence, supersedes the finding of a single trial, even a large one.",
      "evidence_ref": "pair:V2C001::V2C002",
      "pair": "V2C001::V2C002",
      "state_changes": [
        {
          "basis": "Semantic inference for V2C001::V2C002 auto-superseded V2C001 with confidence 0.90; basis: Claim A, a systematic review and meta-analysis published in 2020, synthesizes evidence that Vitamin D supplementation appears to reduce progression to type 2 diabetes in people with prediabetes. Claim B, from a 2019 randomized controlled trial (the D2d study), specifically states that Vitamin D3 supplementation at 4000 IU per day does not significantly lower diabetes risk in adults at high risk. Given that Claim A is a more recent meta-analysis, it likely incorporated the findings of the D2d study (Claim B's source) along with other relevant studies to provide a more comprehensive and statistically robust overall estimate of effect. Therefore, its conclusion, representing a broader synthesis of evidence, supersedes the finding of a single trial, even a large one.",
          "claim_id": "V2C002",
          "evidence_class": "semantic_inference",
          "evidence_ref": "pair:V2C001::V2C002",
          "state": "active"
        },
        {
          "basis": "Semantic inference for V2C001::V2C002 auto-superseded V2C001 with confidence 0.90; basis: Claim A, a systematic review and meta-analysis published in 2020, synthesizes evidence that Vitamin D supplementation appears to reduce progression to type 2 diabetes in people with prediabetes. Claim B, from a 2019 randomized controlled trial (the D2d study), specifically states that Vitamin D3 supplementation at 4000 IU per day does not significantly lower diabetes risk in adults at high risk. Given that Claim A is a more recent meta-analysis, it likely incorporated the findings of the D2d study (Claim B's source) along with other relevant studies to provide a more comprehensive and statistically robust overall estimate of effect. Therefore, its conclusion, representing a broader synthesis of evidence, supersedes the finding of a single trial, even a large one.",
          "claim_id": "V2C001",
          "evidence_class": "semantic_inference",
          "evidence_ref": "pair:V2C001::V2C002",
          "state": "superseded"
        }
      ],
      "superseded_claim_id": "V2C001",
      "winner_claim_id": "V2C002"
    }
  },
  {
    "action": "already_exists",
    "edges": [],
    "pair": [
      "V2C004",
      "V2C003"
    ],
    "semantic_action": "contested",
    "state_result": {
      "basis": "Semantic inference for V2C003::V2C004 landed in the contested band (confidence 1.00, direction mutual); basis: Both claims evaluate the effect of marine omega-3 (n-3) fatty acid supplementation on cardiovascular events. Claim A asserts that supplementation lowers the risk for several cardiovascular outcomes (myocardial infarction, coronary heart disease death, cardiovascular disease death, and total cardiovascular disease). Claim B, conversely, states that marine n-3 fatty acid supplementation does not lower the incidence of major cardiovascular events compared with placebo. These are directly contradictory findings regarding the efficacy of marine omega-3 supplementation for cardiovascular disease prevention.",
      "claim_a_data_id": "f11ad17a-7d73-519d-a3a0-cd63a2f6d047",
      "claim_a_id": "V2C004",
      "claim_b_data_id": "c82e05d1-0ba4-596b-bde2-e320488f31e4",
      "claim_b_id": "V2C003",
      "created_at": "2026-07-04T21:03:35.457405+00:00",
      "dataset": "groundtruth_v2_semantic_memory",
      "decision": {
        "basis": "Both claims evaluate the effect of marine omega-3 (n-3) fatty acid supplementation on cardiovascular events. Claim A asserts that supplementation lowers the risk for several cardiovascular outcomes (myocardial infarction, coronary heart disease death, cardiovascular disease death, and total cardiovascular disease). Claim B, conversely, states that marine n-3 fatty acid supplementation does not lower the incidence of major cardiovascular events compared with placebo. These are directly contradictory findings regarding the efficacy of marine omega-3 supplementation for cardiovascular disease prevention.",
        "confidence": 1.0,
        "conflicts": true,
        "direction": "mutual"
      },
      "evidence_ref": "pair:V2C003::V2C004",
      "pair": "V2C003::V2C004",
      "registry_path": "C:\\Users\\gudma\\OneDrive\\Desktop\\GITHUB-FILES\\groundtruth\\data\\v2_claims.json",
      "state_changes": [
        {
          "basis": "Semantic inference for V2C003::V2C004 landed in the contested band (confidence 1.00, direction mutual); basis: Both claims evaluate the effect of marine omega-3 (n-3) fatty acid supplementation on cardiovascular events. Claim A asserts that supplementation lowers the risk for several cardiovascular outcomes (myocardial infarction, coronary heart disease death, cardiovascular disease death, and total cardiovascular disease). Claim B, conversely, states that marine n-3 fatty acid supplementation does not lower the incidence of major cardiovascular events compared with placebo. These are directly contradictory findings regarding the efficacy of marine omega-3 supplementation for cardiovascular disease prevention.",
          "claim_id": "V2C004",
          "evidence_class": "semantic_inference",
          "evidence_ref": "pair:V2C003::V2C004",
          "state": "contested"
        },
        {
          "basis": "Semantic inference for V2C003::V2C004 landed in the contested band (confidence 1.00, direction mutual); basis: Both claims evaluate the effect of marine omega-3 (n-3) fatty acid supplementation on cardiovascular events. Claim A asserts that supplementation lowers the risk for several cardiovascular outcomes (myocardial infarction, coronary heart disease death, cardiovascular disease death, and total cardiovascular disease). Claim B, conversely, states that marine n-3 fatty acid supplementation does not lower the incidence of major cardiovascular events compared with placebo. These are directly contradictory findings regarding the efficacy of marine omega-3 supplementation for cardiovascular disease prevention.",
          "claim_id": "V2C003",
          "evidence_class": "semantic_inference",
          "evidence_ref": "pair:V2C003::V2C004",
          "state": "contested"
        }
      ],
      "status": "open",
      "updated_at": "2026-07-05T07:01:38.292549+00:00"
    }
  }
]
```
