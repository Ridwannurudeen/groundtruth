# Phase 1 Results

Generated: 2026-07-03T20:56:54.553661+00:00

## Extraction Check

```json
[
  {
    "claim_id": "R001",
    "data_id": "b04b6801-fbfe-5b58-b362-c57bad2466ab",
    "node_count": 5,
    "node_types": [
      "DocumentChunk",
      "ScientificClaim",
      "Source",
      "TextDocument",
      "TextSummary"
    ],
    "passed": true
  },
  {
    "claim_id": "R002",
    "data_id": "d7f6a9a3-2860-5445-b193-d54c7a23466e",
    "node_count": 5,
    "node_types": [
      "DocumentChunk",
      "ScientificClaim",
      "Source",
      "TextDocument",
      "TextSummary"
    ],
    "passed": true
  },
  {
    "claim_id": "R003",
    "data_id": "5332804b-59c8-5707-a0a7-52a32ae9eeb2",
    "node_count": 5,
    "node_types": [
      "DocumentChunk",
      "ScientificClaim",
      "Source",
      "TextDocument",
      "TextSummary"
    ],
    "passed": true
  }
]
```

## Gate

- Claims in registry: 40
- Dataset entries: 80
- Unique dataset/data pairs: 80
- Unique raw data IDs: 40 (Cognee reuses the content-hash id across datasets)
- Ingestion mode: `deterministic_graph_fallback`
- Recall question: `what does the research say about Effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension?`
- Recall mode: `GRAPH_COMPLETION` with `only_context=True`, `include_references=True`
- Recall result count: 1

## Cited Answer

GroundTruth retrieved R003 from British Journal of Clinical Pharmacology (2025, DOI 10.1002/bcp.70249). The remembered claim says: The paper claimed that effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension: A randomized clinical trial. Related active controls retrieved in the same graph context cover blood-pressure diet evidence, so this Phase 1 proof has both the target claim and nearby controls available for cited recall.

Reference:

- Dataset: `groundtruth_memory`
- Dataset ID: `1870baaf-b8c5-5b21-87dd-f40ef9024f1f`
- Data ID: `e21ca4ca-0fc0-59bc-a3d4-7025db76c675`
- DOI: `10.1002/bcp.70249`

## Recall Context Excerpt

```text
Nodes:
Node: The paper claimed that effects of different... [paper, claimed, effects]
__node_content_start__
The paper claimed that effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension: A randomized clinical trial.
__node_content_end__

Node: British Journal of Clinical Pharmacology
__node_content_start__
None
__node_content_end__

Node: The active control paper reports that role... [active, control, paper]
__node_content_start__
The active control paper reports that role Of Dash Diet In Blood Pressure.
__node_content_end__

Node: CARDIOMETRY
__node_content_start__
None
__node_content_end__

Node: The active control paper reports that dietary... [active, control, paper]
__node_content_start__
The active control paper reports that dietary Sodium and Blood Pressure.
__node_content_end__

Node: JAMA
__node_content_start__
None
__node_content_end__

Node: The active control paper reports that dietary... [active, control, paper]
__node_content_start__
The active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.
__node_content_end__

Node: JAMA Internal Medicine
__node_content_start__
None
__node_content_end__

Node: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]
__node_content_start__
The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.
__node_content_end__

Node: Genetics
__node_content_start__
None
__node_content_end__

Node: The active control paper reports that intermittent... [active, control, paper]
__node_content_start__
The active control paper reports that intermittent Fasting in Weight Loss and Cardiometabolic Risk Reduction: A Randomized Controlled Trial.
__node_content_end__

Node: Journal of Nursing Research
__node_content_start__
None
__node_content_end__

Node: The active control paper reports that effects... [control, active, paper]
__node_content_start__
The active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.
__node_content_end__

Node: Journal of International Medical Research
__node_content_start__
None
__node_content_end__

Node: The paper claimed that longitudinal Data From... [plaque, paper, claimed]
__node_content_start__
The paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predicts Plaque, ApoB Does Not.
__node_content_end__

Node: JACC: Advances
__node_content_start__
None
__node_content_end__

Node: The paper claimed that avacopan for the... [paper, claimed, avacopan]
__node_content_start__
The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.
__node_content_end__

Node: NEJM: The New England Journal of Medicine
__node_content_start__
None
__node_content_end__

Node: The active control paper reports that lipoprotein(a)... [active, control, paper]
__node_content_start__
The active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.
__node_content_end__

Node: Journal of Clinical Lipidology
__node_content_start__
None
__node_content_end__


Connections:
The paper claimed that effects of different... [paper, claimed, effects] --[made_by]--> British Journal of Clinical Pharmacology  (The paper claimed that effects of different antihypertensive drug classes on cen made by British Journal of Clinical Pharmacology.)
The active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)
The active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA  (The active control paper reports that dietary Sodium and Blood Pressure. made by JAMA.)
The active control pap
```

## Recall Output

```json
{
  "cited_answer": "GroundTruth retrieved R003 from British Journal of Clinical Pharmacology (2025, DOI 10.1002/bcp.70249). The remembered claim says: The paper claimed that effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension: A randomized clinical trial. Related active controls retrieved in the same graph context cover blood-pressure diet evidence, so this Phase 1 proof has both the target claim and nearby controls available for cited recall.",
  "dataset_scoped_data_items": 80,
  "question": "what does the research say about Effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension?",
  "raw_data_ids": 40,
  "recall_mode": "GRAPH_COMPLETION only_context=True",
  "reference": {
    "data_id": "e21ca4ca-0fc0-59bc-a3d4-7025db76c675",
    "dataset": "groundtruth_memory",
    "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
    "doi": "10.1002/bcp.70249"
  },
  "result_count": 1,
  "results": [
    {
      "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
      "dataset_name": "groundtruth_memory",
      "kind": "graph_completion",
      "metadata": {},
      "raw": {
        "value": "Nodes:\nNode: The paper claimed that effects of different... [paper, claimed, effects]\n__node_content_start__\nThe paper claimed that effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension: A randomized clinical trial.\n__node_content_end__\n\nNode: British Journal of Clinical Pharmacology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium and Blood Pressure.\n__node_content_end__\n\nNode: JAMA\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that intermittent... [active, control, paper]\n__node_content_start__\nThe active control paper reports that intermittent Fasting in Weight Loss and Cardiometabolic Risk Reduction: A Randomized Controlled Trial.\n__node_content_end__\n\nNode: Journal of Nursing Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that longitudinal Data From... [plaque, paper, claimed]\n__node_content_start__\nThe paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predicts Plaque, ApoB Does Not.\n__node_content_end__\n\nNode: JACC: Advances\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that avacopan for the... [paper, claimed, avacopan]\n__node_content_start__\nThe paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.\n__node_content_end__\n\nNode: NEJM: The New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe paper claimed that effects of different... [paper, claimed, effects] --[made_by]--> British Journal of Clinical Pharmacology  (The paper claimed that effects of different antihypertensive drug classes on cen made by British Journal of Clinical Pharmacology.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA  (The active control paper reports that dietary Sodium and Blood Pressure. made by JAMA.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)\nThe active control paper reports that intermittent... [active, control, paper] --[made_by]--> Journal of Nursing Research  (The active control paper reports that intermittent Fasting in Weight Loss and Ca made by Journal of Nursing Research.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe paper claimed that longitudinal Data From... [plaque, paper, claimed] --[made_by]--> JACC: Advances  (The paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predict made by JACC: Advances.)\nThe paper claimed that avacopan for the... [paper, claimed, avacopan] --[made_by]--> NEJM: The New England Journal of Medicine  (The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis. made by NEJM: The New England Journal of Medicine.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)"
      },
      "score": null,
      "search_type": "GRAPH_COMPLETION",
      "source": "graph",
      "structured": null,
      "text": "Nodes:\nNode: The paper claimed that effects of different... [paper, claimed, effects]\n__node_content_start__\nThe paper claimed that effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension: A randomized clinical trial.\n__node_content_end__\n\nNode: British Journal of Clinical Pharmacology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium and Blood Pressure.\n__node_content_end__\n\nNode: JAMA\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that intermittent... [active, control, paper]\n__node_content_start__\nThe active control paper reports that intermittent Fasting in Weight Loss and Cardiometabolic Risk Reduction: A Randomized Controlled Trial.\n__node_content_end__\n\nNode: Journal of Nursing Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that longitudinal Data From... [plaque, paper, claimed]\n__node_content_start__\nThe paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predicts Plaque, ApoB Does Not.\n__node_content_end__\n\nNode: JACC: Advances\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that avacopan for the... [paper, claimed, avacopan]\n__node_content_start__\nThe paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.\n__node_content_end__\n\nNode: NEJM: The New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe paper claimed that effects of different... [paper, claimed, effects] --[made_by]--> British Journal of Clinical Pharmacology  (The paper claimed that effects of different antihypertensive drug classes on cen made by British Journal of Clinical Pharmacology.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA  (The active control paper reports that dietary Sodium and Blood Pressure. made by JAMA.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)\nThe active control paper reports that intermittent... [active, control, paper] --[made_by]--> Journal of Nursing Research  (The active control paper reports that intermittent Fasting in Weight Loss and Ca made by Journal of Nursing Research.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe paper claimed that longitudinal Data From... [plaque, paper, claimed] --[made_by]--> JACC: Advances  (The paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predict made by JACC: Advances.)\nThe paper claimed that avacopan for the... [paper, claimed, avacopan] --[made_by]--> NEJM: The New England Journal of Medicine  (The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis. made by NEJM: The New England Journal of Medicine.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)"
    }
  ],
  "target_claim_id": "R003",
  "target_doi": "10.1002/bcp.70249"
}
```
