# Phase 2 Results

Generated: 2026-07-03T21:10:47.998573+00:00

## Gate

- Retractions triggered: 3
- GroundTruth adds a contradiction edge, forgets the superseded original claim, and stops citing it.
- Naive memory receives the same retraction notice but retains and cites the retracted original claim.

## R001 - 10.1056/nejmoa2023386

Question: `what does the research say about Avacopan for the Treatment of ANCA-Associated Vasculitis?`

### Before

```json
{
  "groundtruth_memory": {
    "cites_retracted": false,
    "dataset": "groundtruth_memory",
    "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
    "question": "what does the research say about Avacopan for the Treatment of ANCA-Associated Vasculitis?",
    "recall_context": "Nodes:\nNode: The paper claimed that avacopan for the... [paper, claimed, avacopan]\n__node_content_start__\nThe paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.\n__node_content_end__\n\nNode: NEJM: The New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that longitudinal Data From... [plaque, paper, claimed]\n__node_content_start__\nThe paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predicts Plaque, ApoB Does Not.\n__node_content_end__\n\nNode: JACC: Advances\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that nF-\u0138B axis in... [paper, claimed, nf-\u0138b]\n__node_content_start__\nThe paper claimed that nF-\u0138B axis in diabetic neuropathy, cardiomyopathy and nephropathy: A roadmap from molecular intervention to therapeutic strategies.\n__node_content_end__\n\nNode: Heliyon\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that targeting epithelial-mesenchymal transition... [drug, paper, claimed]\n__node_content_start__\nThe paper claimed that targeting epithelial-mesenchymal transition signaling pathways with Dietary Phytocompounds and repurposed drug combinations for overcoming drug resistance in various cancers.\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium and Blood Pressure.\n__node_content_end__\n\nNode: JAMA\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe paper claimed that avacopan for the... [paper, claimed, avacopan] --[made_by]--> NEJM: The New England Journal of Medicine  (The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis. made by NEJM: The New England Journal of Medicine.)\nThe paper claimed that longitudinal Data From... [plaque, paper, claimed] --[made_by]--> JACC: Advances  (The paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predict made by JACC: Advances.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe paper claimed that nF-\u0138B axis in... [paper, claimed, nf-\u0138b] --[made_by]--> Heliyon  (The paper claimed that nF-\u0138B axis in diabetic neuropathy, cardiomyopathy and nep made by Heliyon.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe paper claimed that targeting epithelial-mesenchymal transition... [drug, paper, claimed] --[made_by]--> Heliyon  (The paper claimed that targeting epithelial-mesenchymal transition signaling pat made by Heliyon.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA  (The active control paper reports that dietary Sodium and Blood Pressure. made by JAMA.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)",
    "recall_mode": "GRAPH_COMPLETION only_context=True",
    "recall_output": [
      {
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_name": "groundtruth_memory",
        "kind": "graph_completion",
        "metadata": {},
        "raw": {
          "value": "Nodes:\nNode: The paper claimed that avacopan for the... [paper, claimed, avacopan]\n__node_content_start__\nThe paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.\n__node_content_end__\n\nNode: NEJM: The New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that longitudinal Data From... [plaque, paper, claimed]\n__node_content_start__\nThe paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predicts Plaque, ApoB Does Not.\n__node_content_end__\n\nNode: JACC: Advances\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that nF-\u0138B axis in... [paper, claimed, nf-\u0138b]\n__node_content_start__\nThe paper claimed that nF-\u0138B axis in diabetic neuropathy, cardiomyopathy and nephropathy: A roadmap from molecular intervention to therapeutic strategies.\n__node_content_end__\n\nNode: Heliyon\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that targeting epithelial-mesenchymal transition... [drug, paper, claimed]\n__node_content_start__\nThe paper claimed that targeting epithelial-mesenchymal transition signaling pathways with Dietary Phytocompounds and repurposed drug combinations for overcoming drug resistance in various cancers.\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium and Blood Pressure.\n__node_content_end__\n\nNode: JAMA\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe paper claimed that avacopan for the... [paper, claimed, avacopan] --[made_by]--> NEJM: The New England Journal of Medicine  (The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis. made by NEJM: The New England Journal of Medicine.)\nThe paper claimed that longitudinal Data From... [plaque, paper, claimed] --[made_by]--> JACC: Advances  (The paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predict made by JACC: Advances.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe paper claimed that nF-\u0138B axis in... [paper, claimed, nf-\u0138b] --[made_by]--> Heliyon  (The paper claimed that nF-\u0138B axis in diabetic neuropathy, cardiomyopathy and nep made by Heliyon.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe paper claimed that targeting epithelial-mesenchymal transition... [drug, paper, claimed] --[made_by]--> Heliyon  (The paper claimed that targeting epithelial-mesenchymal transition signaling pat made by Heliyon.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA  (The active control paper reports that dietary Sodium and Blood Pressure. made by JAMA.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)"
        },
        "score": null,
        "search_type": "GRAPH_COMPLETION",
        "source": "graph",
        "structured": null,
        "text": "Nodes:\nNode: The paper claimed that avacopan for the... [paper, claimed, avacopan]\n__node_content_start__\nThe paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.\n__node_content_end__\n\nNode: NEJM: The New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that longitudinal Data From... [plaque, paper, claimed]\n__node_content_start__\nThe paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predicts Plaque, ApoB Does Not.\n__node_content_end__\n\nNode: JACC: Advances\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that nF-\u0138B axis in... [paper, claimed, nf-\u0138b]\n__node_content_start__\nThe paper claimed that nF-\u0138B axis in diabetic neuropathy, cardiomyopathy and nephropathy: A roadmap from molecular intervention to therapeutic strategies.\n__node_content_end__\n\nNode: Heliyon\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that targeting epithelial-mesenchymal transition... [drug, paper, claimed]\n__node_content_start__\nThe paper claimed that targeting epithelial-mesenchymal transition signaling pathways with Dietary Phytocompounds and repurposed drug combinations for overcoming drug resistance in various cancers.\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium and Blood Pressure.\n__node_content_end__\n\nNode: JAMA\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe paper claimed that avacopan for the... [paper, claimed, avacopan] --[made_by]--> NEJM: The New England Journal of Medicine  (The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis. made by NEJM: The New England Journal of Medicine.)\nThe paper claimed that longitudinal Data From... [plaque, paper, claimed] --[made_by]--> JACC: Advances  (The paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predict made by JACC: Advances.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe paper claimed that nF-\u0138B axis in... [paper, claimed, nf-\u0138b] --[made_by]--> Heliyon  (The paper claimed that nF-\u0138B axis in diabetic neuropathy, cardiomyopathy and nep made by Heliyon.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe paper claimed that targeting epithelial-mesenchymal transition... [drug, paper, claimed] --[made_by]--> Heliyon  (The paper claimed that targeting epithelial-mesenchymal transition signaling pat made by Heliyon.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA  (The active control paper reports that dietary Sodium and Blood Pressure. made by JAMA.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)"
      }
    ],
    "references": [
      {
        "claim_id": "R001",
        "data_id": "033e8c14-5e6e-5dbf-8a50-a7b850015cf2",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.1056/nejmoa2023386",
        "kind": "original_claim",
        "retracted": false,
        "score": 6,
        "source": "NEJM: The New England Journal of Medicine",
        "status": "active"
      },
      {
        "claim_id": "R011",
        "data_id": "be4527b6-ee58-5b79-88a2-6a776a1aad92",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.1007/s00500-023-09482-1",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "Soft Computing",
        "status": "active"
      },
      {
        "claim_id": "R012",
        "data_id": "8b310b31-aecd-5a18-8fd5-06e67dcfe8bb",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.1007/978-3-030-00524-5_6",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "Distributed Computing and Artificial Intelligence, Special Sessions II, 15th International Conference",
        "status": "active"
      },
      {
        "claim_id": "R015",
        "data_id": "57a0c28a-fb22-579e-ad51-e0d96239ea46",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.1016/j.heliyon.2025.e41964",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "Heliyon",
        "status": "active"
      },
      {
        "claim_id": "R018",
        "data_id": "b66cdeb7-f924-54e8-90fc-14104c2dd908",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.1016/j.heliyon.2024.e37293",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "Heliyon",
        "status": "active"
      }
    ],
    "retracted_dois": [],
    "text": "groundtruth_memory cites an active remembered source for 10.1056/nejmoa2023386 from NEJM: The New England Journal of Medicine."
  },
  "naive_memory": {
    "cites_retracted": false,
    "dataset": "naive_memory",
    "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
    "question": "what does the research say about Avacopan for the Treatment of ANCA-Associated Vasculitis?",
    "recall_context": "Nodes:\nNode: The paper claimed that avacopan for the... [paper, claimed, avacopan]\n__node_content_start__\nThe paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.\n__node_content_end__\n\nNode: NEJM: The New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that longitudinal Data From... [plaque, paper, claimed]\n__node_content_start__\nThe paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predicts Plaque, ApoB Does Not.\n__node_content_end__\n\nNode: JACC: Advances\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that nF-\u0138B axis in... [paper, claimed, nf-\u0138b]\n__node_content_start__\nThe paper claimed that nF-\u0138B axis in diabetic neuropathy, cardiomyopathy and nephropathy: A roadmap from molecular intervention to therapeutic strategies.\n__node_content_end__\n\nNode: Heliyon\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that targeting epithelial-mesenchymal transition... [drug, paper, claimed]\n__node_content_start__\nThe paper claimed that targeting epithelial-mesenchymal transition signaling pathways with Dietary Phytocompounds and repurposed drug combinations for overcoming drug resistance in various cancers.\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium and Blood Pressure.\n__node_content_end__\n\nNode: JAMA\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe paper claimed that avacopan for the... [paper, claimed, avacopan] --[made_by]--> NEJM: The New England Journal of Medicine  (The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis. made by NEJM: The New England Journal of Medicine.)\nThe paper claimed that longitudinal Data From... [plaque, paper, claimed] --[made_by]--> JACC: Advances  (The paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predict made by JACC: Advances.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe paper claimed that nF-\u0138B axis in... [paper, claimed, nf-\u0138b] --[made_by]--> Heliyon  (The paper claimed that nF-\u0138B axis in diabetic neuropathy, cardiomyopathy and nep made by Heliyon.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe paper claimed that targeting epithelial-mesenchymal transition... [drug, paper, claimed] --[made_by]--> Heliyon  (The paper claimed that targeting epithelial-mesenchymal transition signaling pat made by Heliyon.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA  (The active control paper reports that dietary Sodium and Blood Pressure. made by JAMA.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)",
    "recall_mode": "GRAPH_COMPLETION only_context=True",
    "recall_output": [
      {
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_name": "naive_memory",
        "kind": "graph_completion",
        "metadata": {},
        "raw": {
          "value": "Nodes:\nNode: The paper claimed that avacopan for the... [paper, claimed, avacopan]\n__node_content_start__\nThe paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.\n__node_content_end__\n\nNode: NEJM: The New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that longitudinal Data From... [plaque, paper, claimed]\n__node_content_start__\nThe paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predicts Plaque, ApoB Does Not.\n__node_content_end__\n\nNode: JACC: Advances\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that nF-\u0138B axis in... [paper, claimed, nf-\u0138b]\n__node_content_start__\nThe paper claimed that nF-\u0138B axis in diabetic neuropathy, cardiomyopathy and nephropathy: A roadmap from molecular intervention to therapeutic strategies.\n__node_content_end__\n\nNode: Heliyon\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that targeting epithelial-mesenchymal transition... [drug, paper, claimed]\n__node_content_start__\nThe paper claimed that targeting epithelial-mesenchymal transition signaling pathways with Dietary Phytocompounds and repurposed drug combinations for overcoming drug resistance in various cancers.\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium and Blood Pressure.\n__node_content_end__\n\nNode: JAMA\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe paper claimed that avacopan for the... [paper, claimed, avacopan] --[made_by]--> NEJM: The New England Journal of Medicine  (The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis. made by NEJM: The New England Journal of Medicine.)\nThe paper claimed that longitudinal Data From... [plaque, paper, claimed] --[made_by]--> JACC: Advances  (The paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predict made by JACC: Advances.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe paper claimed that nF-\u0138B axis in... [paper, claimed, nf-\u0138b] --[made_by]--> Heliyon  (The paper claimed that nF-\u0138B axis in diabetic neuropathy, cardiomyopathy and nep made by Heliyon.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe paper claimed that targeting epithelial-mesenchymal transition... [drug, paper, claimed] --[made_by]--> Heliyon  (The paper claimed that targeting epithelial-mesenchymal transition signaling pat made by Heliyon.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA  (The active control paper reports that dietary Sodium and Blood Pressure. made by JAMA.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)"
        },
        "score": null,
        "search_type": "GRAPH_COMPLETION",
        "source": "graph",
        "structured": null,
        "text": "Nodes:\nNode: The paper claimed that avacopan for the... [paper, claimed, avacopan]\n__node_content_start__\nThe paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.\n__node_content_end__\n\nNode: NEJM: The New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that longitudinal Data From... [plaque, paper, claimed]\n__node_content_start__\nThe paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predicts Plaque, ApoB Does Not.\n__node_content_end__\n\nNode: JACC: Advances\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that nF-\u0138B axis in... [paper, claimed, nf-\u0138b]\n__node_content_start__\nThe paper claimed that nF-\u0138B axis in diabetic neuropathy, cardiomyopathy and nephropathy: A roadmap from molecular intervention to therapeutic strategies.\n__node_content_end__\n\nNode: Heliyon\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that targeting epithelial-mesenchymal transition... [drug, paper, claimed]\n__node_content_start__\nThe paper claimed that targeting epithelial-mesenchymal transition signaling pathways with Dietary Phytocompounds and repurposed drug combinations for overcoming drug resistance in various cancers.\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium and Blood Pressure.\n__node_content_end__\n\nNode: JAMA\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe paper claimed that avacopan for the... [paper, claimed, avacopan] --[made_by]--> NEJM: The New England Journal of Medicine  (The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis. made by NEJM: The New England Journal of Medicine.)\nThe paper claimed that longitudinal Data From... [plaque, paper, claimed] --[made_by]--> JACC: Advances  (The paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predict made by JACC: Advances.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe paper claimed that nF-\u0138B axis in... [paper, claimed, nf-\u0138b] --[made_by]--> Heliyon  (The paper claimed that nF-\u0138B axis in diabetic neuropathy, cardiomyopathy and nep made by Heliyon.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe paper claimed that targeting epithelial-mesenchymal transition... [drug, paper, claimed] --[made_by]--> Heliyon  (The paper claimed that targeting epithelial-mesenchymal transition signaling pat made by Heliyon.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA  (The active control paper reports that dietary Sodium and Blood Pressure. made by JAMA.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)"
      }
    ],
    "references": [
      {
        "claim_id": "R001",
        "data_id": "033e8c14-5e6e-5dbf-8a50-a7b850015cf2",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "active",
        "doi": "10.1056/nejmoa2023386",
        "kind": "original_claim",
        "retracted": false,
        "score": 6,
        "source": "NEJM: The New England Journal of Medicine",
        "status": "active"
      },
      {
        "claim_id": "R011",
        "data_id": "be4527b6-ee58-5b79-88a2-6a776a1aad92",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "active",
        "doi": "10.1007/s00500-023-09482-1",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "Soft Computing",
        "status": "active"
      },
      {
        "claim_id": "R012",
        "data_id": "8b310b31-aecd-5a18-8fd5-06e67dcfe8bb",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "active",
        "doi": "10.1007/978-3-030-00524-5_6",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "Distributed Computing and Artificial Intelligence, Special Sessions II, 15th International Conference",
        "status": "active"
      },
      {
        "claim_id": "R015",
        "data_id": "57a0c28a-fb22-579e-ad51-e0d96239ea46",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "active",
        "doi": "10.1016/j.heliyon.2025.e41964",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "Heliyon",
        "status": "active"
      },
      {
        "claim_id": "R018",
        "data_id": "b66cdeb7-f924-54e8-90fc-14104c2dd908",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "active",
        "doi": "10.1016/j.heliyon.2024.e37293",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "Heliyon",
        "status": "active"
      }
    ],
    "retracted_dois": [],
    "text": "naive_memory cites an active remembered source for 10.1056/nejmoa2023386 from NEJM: The New England Journal of Medicine."
  }
}
```

### Watcher

```json
{
  "claim_id": "R001",
  "decision": {
    "confidence": 1.0,
    "contradicts": true,
    "rationale": "Retraction Watch links original DOI 10.1056/nejmoa2023386 to this claim; reason: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);",
    "superseded_doi": "10.1056/nejmoa2023386"
  },
  "doi": "10.1056/nejmoa2023386",
  "edge_result": {
    "memify_result": {
      "1870baaf-b8c5-5b21-87dd-f40ef9024f1f": {
        "data_ingestion_info": [
          {
            "run_info": {
              "data_ingestion_info": null,
              "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
              "dataset_name": "groundtruth_memory",
              "payload": null,
              "pipeline_run_id": "0addc10b-ba02-4514-8695-a1a5707d1c3b",
              "status": "PipelineRunCompleted"
            }
          }
        ],
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_name": "groundtruth_memory",
        "payload": null,
        "pipeline_run_id": "0addc10b-ba02-4514-8695-a1a5707d1c3b",
        "status": "PipelineRunCompleted"
      }
    },
    "properties": {
      "confidence": 1.0,
      "edge_text": "Retraction notice for 10.1056/nejmoa2023386 contradicts the original claim",
      "ontology_valid": false,
      "rationale": "Retraction Watch links original DOI 10.1056/nejmoa2023386 to this claim; reason: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);",
      "relationship_name": "contradicts",
      "source_data_id": "4b2daf7b-0340-572d-adde-ce491af50f5d",
      "superseded_doi": "10.1056/nejmoa2023386",
      "target_data_id": "033e8c14-5e6e-5dbf-8a50-a7b850015cf2"
    },
    "source_node_id": "bfd08987-1d27-5f0b-a3aa-ccc3396d3ced",
    "target_node_id": "18c70637-e1f4-5e33-8427-f46fe7f5eadf"
  },
  "forget_result": {
    "data_id": "033e8c14-5e6e-5dbf-8a50-a7b850015cf2",
    "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
    "status": "success"
  },
  "graph_edges_after_forget": 0,
  "graph_edges_before_forget": 1,
  "ledger_edges_before_forget": 1,
  "notice_entries": {
    "groundtruth_memory": {
      "data_id": "4b2daf7b-0340-572d-adde-ce491af50f5d",
      "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
    },
    "naive_memory": {
      "data_id": "4b2daf7b-0340-572d-adde-ce491af50f5d",
      "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
    }
  }
}
```

### After

```json
{
  "groundtruth_memory": {
    "cites_retracted": false,
    "dataset": "groundtruth_memory",
    "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
    "question": "what does the research say about Avacopan for the Treatment of ANCA-Associated Vasculitis?",
    "recall_context": "Nodes:\nNode: The paper claimed that longitudinal Data From... [plaque, paper, claimed]\n__node_content_start__\nThe paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predicts Plaque, ApoB Does Not.\n__node_content_end__\n\nNode: JACC: Advances\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that beyond... [active, control, paper]\n__node_content_start__\nThe active control paper reports that beyond sugar-sweetened beverages.\n__node_content_end__\n\nNode: The Journal of the American Dental Association\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The retraction notice says that Avacopan for... [retraction, notice, says]\n__node_content_start__\nThe retraction notice says that Avacopan for the Treatment of ANCA-Associated Vasculitis (DOI 10.1056/nejmoa2023386) was retracted. Reason: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);.\n__node_content_end__\n\nNode: Retraction Watch / Crossref\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that vitamin... [active, control, paper]\n__node_content_start__\nThe active control paper reports that vitamin D Supplementation and Prevention of Type 2 Diabetes.\n__node_content_end__\n\nNode: New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that whole-grain... [active, control, paper]\n__node_content_start__\nThe active control paper reports that whole-grain intake and risk of type 2 diabetes.\n__node_content_end__\n\nNode: The American Journal of Clinical Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe paper claimed that longitudinal Data From... [plaque, paper, claimed] --[made_by]--> JACC: Advances  (The paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predict made by JACC: Advances.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe active control paper reports that beyond... [active, control, paper] --[made_by]--> The Journal of the American Dental Association  (The active control paper reports that beyond sugar-sweetened beverages. made by The Journal of the American Dental Association.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe retraction notice says that Avacopan for... [retraction, notice, says] --[made_by]--> Retraction Watch / Crossref  (The retraction notice says that Avacopan for the Treatment of ANCA-Associated Va made by Retraction Watch / Crossref.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe active control paper reports that vitamin... [active, control, paper] --[made_by]--> New England Journal of Medicine  (The active control paper reports that vitamin D Supplementation and Prevention o made by New England Journal of Medicine.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe active control paper reports that whole-grain... [active, control, paper] --[made_by]--> The American Journal of Clinical Nutrition  (The active control paper reports that whole-grain intake and risk of type 2 diab made by The American Journal of Clinical Nutrition.)",
    "recall_mode": "GRAPH_COMPLETION only_context=True",
    "recall_output": [
      {
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_name": "groundtruth_memory",
        "kind": "graph_completion",
        "metadata": {},
        "raw": {
          "value": "Nodes:\nNode: The paper claimed that longitudinal Data From... [plaque, paper, claimed]\n__node_content_start__\nThe paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predicts Plaque, ApoB Does Not.\n__node_content_end__\n\nNode: JACC: Advances\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that beyond... [active, control, paper]\n__node_content_start__\nThe active control paper reports that beyond sugar-sweetened beverages.\n__node_content_end__\n\nNode: The Journal of the American Dental Association\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The retraction notice says that Avacopan for... [retraction, notice, says]\n__node_content_start__\nThe retraction notice says that Avacopan for the Treatment of ANCA-Associated Vasculitis (DOI 10.1056/nejmoa2023386) was retracted. Reason: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);.\n__node_content_end__\n\nNode: Retraction Watch / Crossref\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that vitamin... [active, control, paper]\n__node_content_start__\nThe active control paper reports that vitamin D Supplementation and Prevention of Type 2 Diabetes.\n__node_content_end__\n\nNode: New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that whole-grain... [active, control, paper]\n__node_content_start__\nThe active control paper reports that whole-grain intake and risk of type 2 diabetes.\n__node_content_end__\n\nNode: The American Journal of Clinical Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe paper claimed that longitudinal Data From... [plaque, paper, claimed] --[made_by]--> JACC: Advances  (The paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predict made by JACC: Advances.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe active control paper reports that beyond... [active, control, paper] --[made_by]--> The Journal of the American Dental Association  (The active control paper reports that beyond sugar-sweetened beverages. made by The Journal of the American Dental Association.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe retraction notice says that Avacopan for... [retraction, notice, says] --[made_by]--> Retraction Watch / Crossref  (The retraction notice says that Avacopan for the Treatment of ANCA-Associated Va made by Retraction Watch / Crossref.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe active control paper reports that vitamin... [active, control, paper] --[made_by]--> New England Journal of Medicine  (The active control paper reports that vitamin D Supplementation and Prevention o made by New England Journal of Medicine.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe active control paper reports that whole-grain... [active, control, paper] --[made_by]--> The American Journal of Clinical Nutrition  (The active control paper reports that whole-grain intake and risk of type 2 diab made by The American Journal of Clinical Nutrition.)"
        },
        "score": null,
        "search_type": "GRAPH_COMPLETION",
        "source": "graph",
        "structured": null,
        "text": "Nodes:\nNode: The paper claimed that longitudinal Data From... [plaque, paper, claimed]\n__node_content_start__\nThe paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predicts Plaque, ApoB Does Not.\n__node_content_end__\n\nNode: JACC: Advances\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that beyond... [active, control, paper]\n__node_content_start__\nThe active control paper reports that beyond sugar-sweetened beverages.\n__node_content_end__\n\nNode: The Journal of the American Dental Association\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The retraction notice says that Avacopan for... [retraction, notice, says]\n__node_content_start__\nThe retraction notice says that Avacopan for the Treatment of ANCA-Associated Vasculitis (DOI 10.1056/nejmoa2023386) was retracted. Reason: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);.\n__node_content_end__\n\nNode: Retraction Watch / Crossref\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that vitamin... [active, control, paper]\n__node_content_start__\nThe active control paper reports that vitamin D Supplementation and Prevention of Type 2 Diabetes.\n__node_content_end__\n\nNode: New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that whole-grain... [active, control, paper]\n__node_content_start__\nThe active control paper reports that whole-grain intake and risk of type 2 diabetes.\n__node_content_end__\n\nNode: The American Journal of Clinical Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe paper claimed that longitudinal Data From... [plaque, paper, claimed] --[made_by]--> JACC: Advances  (The paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predict made by JACC: Advances.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe active control paper reports that beyond... [active, control, paper] --[made_by]--> The Journal of the American Dental Association  (The active control paper reports that beyond sugar-sweetened beverages. made by The Journal of the American Dental Association.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe retraction notice says that Avacopan for... [retraction, notice, says] --[made_by]--> Retraction Watch / Crossref  (The retraction notice says that Avacopan for the Treatment of ANCA-Associated Va made by Retraction Watch / Crossref.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe active control paper reports that vitamin... [active, control, paper] --[made_by]--> New England Journal of Medicine  (The active control paper reports that vitamin D Supplementation and Prevention o made by New England Journal of Medicine.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe active control paper reports that whole-grain... [active, control, paper] --[made_by]--> The American Journal of Clinical Nutrition  (The active control paper reports that whole-grain intake and risk of type 2 diab made by The American Journal of Clinical Nutrition.)"
      }
    ],
    "references": [
      {
        "claim_id": "R001",
        "data_id": "4b2daf7b-0340-572d-adde-ce491af50f5d",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "retracted_forgotten",
        "doi": "10.1056/nejmoa2023386",
        "kind": "retraction_notice",
        "retracted": false,
        "score": 6,
        "source": "NEJM: The New England Journal of Medicine",
        "status": "retracted_forgotten"
      },
      {
        "claim_id": "R011",
        "data_id": "be4527b6-ee58-5b79-88a2-6a776a1aad92",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.1007/s00500-023-09482-1",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "Soft Computing",
        "status": "active"
      },
      {
        "claim_id": "R012",
        "data_id": "8b310b31-aecd-5a18-8fd5-06e67dcfe8bb",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.1007/978-3-030-00524-5_6",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "Distributed Computing and Artificial Intelligence, Special Sessions II, 15th International Conference",
        "status": "active"
      },
      {
        "claim_id": "R015",
        "data_id": "57a0c28a-fb22-579e-ad51-e0d96239ea46",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.1016/j.heliyon.2025.e41964",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "Heliyon",
        "status": "active"
      },
      {
        "claim_id": "R018",
        "data_id": "b66cdeb7-f924-54e8-90fc-14104c2dd908",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.1016/j.heliyon.2024.e37293",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "Heliyon",
        "status": "active"
      }
    ],
    "retracted_dois": [],
    "text": "groundtruth_memory no longer cites the original retracted claim for 10.1056/nejmoa2023386. The active memory cites the retraction notice instead."
  },
  "naive_memory": {
    "cites_retracted": true,
    "dataset": "naive_memory",
    "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
    "question": "what does the research say about Avacopan for the Treatment of ANCA-Associated Vasculitis?",
    "recall_context": "Nodes:\nNode: The paper claimed that avacopan for the... [paper, claimed, avacopan]\n__node_content_start__\nThe paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.\n__node_content_end__\n\nNode: NEJM: The New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that longitudinal Data From... [plaque, paper, claimed]\n__node_content_start__\nThe paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predicts Plaque, ApoB Does Not.\n__node_content_end__\n\nNode: JACC: Advances\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that beyond... [active, control, paper]\n__node_content_start__\nThe active control paper reports that beyond sugar-sweetened beverages.\n__node_content_end__\n\nNode: The Journal of the American Dental Association\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The retraction notice says that Avacopan for... [retraction, notice, says]\n__node_content_start__\nThe retraction notice says that Avacopan for the Treatment of ANCA-Associated Vasculitis (DOI 10.1056/nejmoa2023386) was retracted. Reason: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);.\n__node_content_end__\n\nNode: Retraction Watch / Crossref\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that vitamin... [active, control, paper]\n__node_content_start__\nThe active control paper reports that vitamin D Supplementation and Prevention of Type 2 Diabetes.\n__node_content_end__\n\nNode: New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe paper claimed that avacopan for the... [paper, claimed, avacopan] --[made_by]--> NEJM: The New England Journal of Medicine  (The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis. made by NEJM: The New England Journal of Medicine.)\nThe paper claimed that longitudinal Data From... [plaque, paper, claimed] --[made_by]--> JACC: Advances  (The paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predict made by JACC: Advances.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe active control paper reports that beyond... [active, control, paper] --[made_by]--> The Journal of the American Dental Association  (The active control paper reports that beyond sugar-sweetened beverages. made by The Journal of the American Dental Association.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe retraction notice says that Avacopan for... [retraction, notice, says] --[made_by]--> Retraction Watch / Crossref  (The retraction notice says that Avacopan for the Treatment of ANCA-Associated Va made by Retraction Watch / Crossref.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe active control paper reports that vitamin... [active, control, paper] --[made_by]--> New England Journal of Medicine  (The active control paper reports that vitamin D Supplementation and Prevention o made by New England Journal of Medicine.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)",
    "recall_mode": "GRAPH_COMPLETION only_context=True",
    "recall_output": [
      {
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_name": "naive_memory",
        "kind": "graph_completion",
        "metadata": {},
        "raw": {
          "value": "Nodes:\nNode: The paper claimed that avacopan for the... [paper, claimed, avacopan]\n__node_content_start__\nThe paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.\n__node_content_end__\n\nNode: NEJM: The New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that longitudinal Data From... [plaque, paper, claimed]\n__node_content_start__\nThe paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predicts Plaque, ApoB Does Not.\n__node_content_end__\n\nNode: JACC: Advances\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that beyond... [active, control, paper]\n__node_content_start__\nThe active control paper reports that beyond sugar-sweetened beverages.\n__node_content_end__\n\nNode: The Journal of the American Dental Association\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The retraction notice says that Avacopan for... [retraction, notice, says]\n__node_content_start__\nThe retraction notice says that Avacopan for the Treatment of ANCA-Associated Vasculitis (DOI 10.1056/nejmoa2023386) was retracted. Reason: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);.\n__node_content_end__\n\nNode: Retraction Watch / Crossref\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that vitamin... [active, control, paper]\n__node_content_start__\nThe active control paper reports that vitamin D Supplementation and Prevention of Type 2 Diabetes.\n__node_content_end__\n\nNode: New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe paper claimed that avacopan for the... [paper, claimed, avacopan] --[made_by]--> NEJM: The New England Journal of Medicine  (The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis. made by NEJM: The New England Journal of Medicine.)\nThe paper claimed that longitudinal Data From... [plaque, paper, claimed] --[made_by]--> JACC: Advances  (The paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predict made by JACC: Advances.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe active control paper reports that beyond... [active, control, paper] --[made_by]--> The Journal of the American Dental Association  (The active control paper reports that beyond sugar-sweetened beverages. made by The Journal of the American Dental Association.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe retraction notice says that Avacopan for... [retraction, notice, says] --[made_by]--> Retraction Watch / Crossref  (The retraction notice says that Avacopan for the Treatment of ANCA-Associated Va made by Retraction Watch / Crossref.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe active control paper reports that vitamin... [active, control, paper] --[made_by]--> New England Journal of Medicine  (The active control paper reports that vitamin D Supplementation and Prevention o made by New England Journal of Medicine.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)"
        },
        "score": null,
        "search_type": "GRAPH_COMPLETION",
        "source": "graph",
        "structured": null,
        "text": "Nodes:\nNode: The paper claimed that avacopan for the... [paper, claimed, avacopan]\n__node_content_start__\nThe paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.\n__node_content_end__\n\nNode: NEJM: The New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that longitudinal Data From... [plaque, paper, claimed]\n__node_content_start__\nThe paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predicts Plaque, ApoB Does Not.\n__node_content_end__\n\nNode: JACC: Advances\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that beyond... [active, control, paper]\n__node_content_start__\nThe active control paper reports that beyond sugar-sweetened beverages.\n__node_content_end__\n\nNode: The Journal of the American Dental Association\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The retraction notice says that Avacopan for... [retraction, notice, says]\n__node_content_start__\nThe retraction notice says that Avacopan for the Treatment of ANCA-Associated Vasculitis (DOI 10.1056/nejmoa2023386) was retracted. Reason: Investigation by Company/Institution;Manipulation of Results;Upgrade/Update of Prior Notice(s);.\n__node_content_end__\n\nNode: Retraction Watch / Crossref\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that vitamin... [active, control, paper]\n__node_content_start__\nThe active control paper reports that vitamin D Supplementation and Prevention of Type 2 Diabetes.\n__node_content_end__\n\nNode: New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe paper claimed that avacopan for the... [paper, claimed, avacopan] --[made_by]--> NEJM: The New England Journal of Medicine  (The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis. made by NEJM: The New England Journal of Medicine.)\nThe paper claimed that longitudinal Data From... [plaque, paper, claimed] --[made_by]--> JACC: Advances  (The paper claimed that longitudinal Data From the KETO-CTA Study: Plaque Predict made by JACC: Advances.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe active control paper reports that beyond... [active, control, paper] --[made_by]--> The Journal of the American Dental Association  (The active control paper reports that beyond sugar-sweetened beverages. made by The Journal of the American Dental Association.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe retraction notice says that Avacopan for... [retraction, notice, says] --[made_by]--> Retraction Watch / Crossref  (The retraction notice says that Avacopan for the Treatment of ANCA-Associated Va made by Retraction Watch / Crossref.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe active control paper reports that vitamin... [active, control, paper] --[made_by]--> New England Journal of Medicine  (The active control paper reports that vitamin D Supplementation and Prevention o made by New England Journal of Medicine.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)"
      }
    ],
    "references": [
      {
        "claim_id": "R001",
        "data_id": "033e8c14-5e6e-5dbf-8a50-a7b850015cf2",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "retracted_retained",
        "doi": "10.1056/nejmoa2023386",
        "kind": "original_claim",
        "retracted": true,
        "score": 6,
        "source": "NEJM: The New England Journal of Medicine",
        "status": "retracted_forgotten"
      },
      {
        "claim_id": "R001",
        "data_id": "4b2daf7b-0340-572d-adde-ce491af50f5d",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "retracted_retained",
        "doi": "10.1056/nejmoa2023386",
        "kind": "retraction_notice",
        "retracted": false,
        "score": 6,
        "source": "NEJM: The New England Journal of Medicine",
        "status": "retracted_forgotten"
      },
      {
        "claim_id": "R011",
        "data_id": "be4527b6-ee58-5b79-88a2-6a776a1aad92",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "active",
        "doi": "10.1007/s00500-023-09482-1",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "Soft Computing",
        "status": "active"
      },
      {
        "claim_id": "R012",
        "data_id": "8b310b31-aecd-5a18-8fd5-06e67dcfe8bb",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "active",
        "doi": "10.1007/978-3-030-00524-5_6",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "Distributed Computing and Artificial Intelligence, Special Sessions II, 15th International Conference",
        "status": "active"
      },
      {
        "claim_id": "R015",
        "data_id": "57a0c28a-fb22-579e-ad51-e0d96239ea46",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "active",
        "doi": "10.1016/j.heliyon.2025.e41964",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "Heliyon",
        "status": "active"
      }
    ],
    "retracted_dois": [
      "10.1056/nejmoa2023386"
    ],
    "text": "naive_memory still cites the retracted original source 10.1056/nejmoa2023386 from NEJM: The New England Journal of Medicine. Treat the answer as unsafe until that source is forgotten."
  }
}
```

## R002 - 10.1016/j.heliyon.2024.e30453

Question: `what does the research say about Nutritional and bioactive properties and antioxidant potential of Amaranthus tricolor, A. lividus, A viridis, and A. spinosus leafy vegetabl?`

### Before

```json
{
  "groundtruth_memory": {
    "cites_retracted": false,
    "dataset": "groundtruth_memory",
    "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
    "question": "what does the research say about Nutritional and bioactive properties and antioxidant potential of Amaranthus tricolor, A. lividus, A viridis, and A. spinosus leafy vegetabl?",
    "recall_context": "Nodes:\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that dietary Patterns in... [paper, claimed, dietary]\n__node_content_start__\nThe paper claimed that dietary Patterns in Adults Following the Christian Orthodox Fasting Regime in Greece.\n__node_content_end__\n\nNode: Frontiers in Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that nutritional and bioactive... [paper, claimed, nutritional]\n__node_content_start__\nThe paper claimed that nutritional and bioactive properties and antioxidant potential of Amaranthus tricolor, A. lividus, A viridis, and A. spinosus leafy vegetables.\n__node_content_end__\n\nNode: Heliyon\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals]\n__node_content_start__\nThe paper claimed that phytochemicals, therapeutic benefits and applications of chrysanthemum flower: A review.\n__node_content_end__\n\nNode: The paper claimed that efficacy of methanolic... [paper, claimed, efficacy]\n__node_content_start__\nThe paper claimed that efficacy of methanolic extracts of some medicinal plants on wound healing in diabetic rats.\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium and Blood Pressure.\n__node_content_end__\n\nNode: JAMA\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)\nThe paper claimed that dietary Patterns in... [paper, claimed, dietary] --[made_by]--> Frontiers in Nutrition  (The paper claimed that dietary Patterns in Adults Following the Christian Orthod made by Frontiers in Nutrition.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe paper claimed that nutritional and bioactive... [paper, claimed, nutritional] --[made_by]--> Heliyon  (The paper claimed that nutritional and bioactive properties and antioxidant pote made by Heliyon.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals] --[made_by]--> Heliyon  (The paper claimed that phytochemicals, therapeutic benefits and applications of  made by Heliyon.)\nThe paper claimed that efficacy of methanolic... [paper, claimed, efficacy] --[made_by]--> Heliyon  (The paper claimed that efficacy of methanolic extracts of some medicinal plants  made by Heliyon.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA  (The active control paper reports that dietary Sodium and Blood Pressure. made by JAMA.)",
    "recall_mode": "GRAPH_COMPLETION only_context=True",
    "recall_output": [
      {
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_name": "groundtruth_memory",
        "kind": "graph_completion",
        "metadata": {},
        "raw": {
          "value": "Nodes:\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that dietary Patterns in... [paper, claimed, dietary]\n__node_content_start__\nThe paper claimed that dietary Patterns in Adults Following the Christian Orthodox Fasting Regime in Greece.\n__node_content_end__\n\nNode: Frontiers in Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that nutritional and bioactive... [paper, claimed, nutritional]\n__node_content_start__\nThe paper claimed that nutritional and bioactive properties and antioxidant potential of Amaranthus tricolor, A. lividus, A viridis, and A. spinosus leafy vegetables.\n__node_content_end__\n\nNode: Heliyon\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals]\n__node_content_start__\nThe paper claimed that phytochemicals, therapeutic benefits and applications of chrysanthemum flower: A review.\n__node_content_end__\n\nNode: The paper claimed that efficacy of methanolic... [paper, claimed, efficacy]\n__node_content_start__\nThe paper claimed that efficacy of methanolic extracts of some medicinal plants on wound healing in diabetic rats.\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium and Blood Pressure.\n__node_content_end__\n\nNode: JAMA\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)\nThe paper claimed that dietary Patterns in... [paper, claimed, dietary] --[made_by]--> Frontiers in Nutrition  (The paper claimed that dietary Patterns in Adults Following the Christian Orthod made by Frontiers in Nutrition.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe paper claimed that nutritional and bioactive... [paper, claimed, nutritional] --[made_by]--> Heliyon  (The paper claimed that nutritional and bioactive properties and antioxidant pote made by Heliyon.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals] --[made_by]--> Heliyon  (The paper claimed that phytochemicals, therapeutic benefits and applications of  made by Heliyon.)\nThe paper claimed that efficacy of methanolic... [paper, claimed, efficacy] --[made_by]--> Heliyon  (The paper claimed that efficacy of methanolic extracts of some medicinal plants  made by Heliyon.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA  (The active control paper reports that dietary Sodium and Blood Pressure. made by JAMA.)"
        },
        "score": null,
        "search_type": "GRAPH_COMPLETION",
        "source": "graph",
        "structured": null,
        "text": "Nodes:\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that dietary Patterns in... [paper, claimed, dietary]\n__node_content_start__\nThe paper claimed that dietary Patterns in Adults Following the Christian Orthodox Fasting Regime in Greece.\n__node_content_end__\n\nNode: Frontiers in Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that nutritional and bioactive... [paper, claimed, nutritional]\n__node_content_start__\nThe paper claimed that nutritional and bioactive properties and antioxidant potential of Amaranthus tricolor, A. lividus, A viridis, and A. spinosus leafy vegetables.\n__node_content_end__\n\nNode: Heliyon\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals]\n__node_content_start__\nThe paper claimed that phytochemicals, therapeutic benefits and applications of chrysanthemum flower: A review.\n__node_content_end__\n\nNode: The paper claimed that efficacy of methanolic... [paper, claimed, efficacy]\n__node_content_start__\nThe paper claimed that efficacy of methanolic extracts of some medicinal plants on wound healing in diabetic rats.\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium and Blood Pressure.\n__node_content_end__\n\nNode: JAMA\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)\nThe paper claimed that dietary Patterns in... [paper, claimed, dietary] --[made_by]--> Frontiers in Nutrition  (The paper claimed that dietary Patterns in Adults Following the Christian Orthod made by Frontiers in Nutrition.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe paper claimed that nutritional and bioactive... [paper, claimed, nutritional] --[made_by]--> Heliyon  (The paper claimed that nutritional and bioactive properties and antioxidant pote made by Heliyon.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals] --[made_by]--> Heliyon  (The paper claimed that phytochemicals, therapeutic benefits and applications of  made by Heliyon.)\nThe paper claimed that efficacy of methanolic... [paper, claimed, efficacy] --[made_by]--> Heliyon  (The paper claimed that efficacy of methanolic extracts of some medicinal plants  made by Heliyon.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA  (The active control paper reports that dietary Sodium and Blood Pressure. made by JAMA.)"
      }
    ],
    "references": [
      {
        "claim_id": "R002",
        "data_id": "0d01068c-5f25-56aa-943a-63b1cd4a05ba",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.1016/j.heliyon.2024.e30453",
        "kind": "original_claim",
        "retracted": false,
        "score": 11,
        "source": "Heliyon",
        "status": "active"
      },
      {
        "claim_id": "C010",
        "data_id": "8f1833d6-f1a6-5a17-bab0-53c083976398",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.54393/df.v6i2.187",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "DIET FACTOR (Journal of Nutritional and Food Sciences)",
        "status": "active"
      }
    ],
    "retracted_dois": [],
    "text": "groundtruth_memory cites an active remembered source for 10.1016/j.heliyon.2024.e30453 from Heliyon."
  },
  "naive_memory": {
    "cites_retracted": false,
    "dataset": "naive_memory",
    "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
    "question": "what does the research say about Nutritional and bioactive properties and antioxidant potential of Amaranthus tricolor, A. lividus, A viridis, and A. spinosus leafy vegetabl?",
    "recall_context": "Nodes:\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that dietary Patterns in... [paper, claimed, dietary]\n__node_content_start__\nThe paper claimed that dietary Patterns in Adults Following the Christian Orthodox Fasting Regime in Greece.\n__node_content_end__\n\nNode: Frontiers in Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that nutritional and bioactive... [paper, claimed, nutritional]\n__node_content_start__\nThe paper claimed that nutritional and bioactive properties and antioxidant potential of Amaranthus tricolor, A. lividus, A viridis, and A. spinosus leafy vegetables.\n__node_content_end__\n\nNode: Heliyon\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that avacopan for the... [paper, claimed, avacopan]\n__node_content_start__\nThe paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.\n__node_content_end__\n\nNode: NEJM: The New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals]\n__node_content_start__\nThe paper claimed that phytochemicals, therapeutic benefits and applications of chrysanthemum flower: A review.\n__node_content_end__\n\nNode: The paper claimed that efficacy of methanolic... [paper, claimed, efficacy]\n__node_content_start__\nThe paper claimed that efficacy of methanolic extracts of some medicinal plants on wound healing in diabetic rats.\n__node_content_end__\n\n\nConnections:\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)\nThe paper claimed that dietary Patterns in... [paper, claimed, dietary] --[made_by]--> Frontiers in Nutrition  (The paper claimed that dietary Patterns in Adults Following the Christian Orthod made by Frontiers in Nutrition.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe paper claimed that nutritional and bioactive... [paper, claimed, nutritional] --[made_by]--> Heliyon  (The paper claimed that nutritional and bioactive properties and antioxidant pote made by Heliyon.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe paper claimed that avacopan for the... [paper, claimed, avacopan] --[made_by]--> NEJM: The New England Journal of Medicine  (The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis. made by NEJM: The New England Journal of Medicine.)\nThe paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals] --[made_by]--> Heliyon  (The paper claimed that phytochemicals, therapeutic benefits and applications of  made by Heliyon.)\nThe paper claimed that efficacy of methanolic... [paper, claimed, efficacy] --[made_by]--> Heliyon  (The paper claimed that efficacy of methanolic extracts of some medicinal plants  made by Heliyon.)",
    "recall_mode": "GRAPH_COMPLETION only_context=True",
    "recall_output": [
      {
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_name": "naive_memory",
        "kind": "graph_completion",
        "metadata": {},
        "raw": {
          "value": "Nodes:\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that dietary Patterns in... [paper, claimed, dietary]\n__node_content_start__\nThe paper claimed that dietary Patterns in Adults Following the Christian Orthodox Fasting Regime in Greece.\n__node_content_end__\n\nNode: Frontiers in Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that nutritional and bioactive... [paper, claimed, nutritional]\n__node_content_start__\nThe paper claimed that nutritional and bioactive properties and antioxidant potential of Amaranthus tricolor, A. lividus, A viridis, and A. spinosus leafy vegetables.\n__node_content_end__\n\nNode: Heliyon\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that avacopan for the... [paper, claimed, avacopan]\n__node_content_start__\nThe paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.\n__node_content_end__\n\nNode: NEJM: The New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals]\n__node_content_start__\nThe paper claimed that phytochemicals, therapeutic benefits and applications of chrysanthemum flower: A review.\n__node_content_end__\n\nNode: The paper claimed that efficacy of methanolic... [paper, claimed, efficacy]\n__node_content_start__\nThe paper claimed that efficacy of methanolic extracts of some medicinal plants on wound healing in diabetic rats.\n__node_content_end__\n\n\nConnections:\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)\nThe paper claimed that dietary Patterns in... [paper, claimed, dietary] --[made_by]--> Frontiers in Nutrition  (The paper claimed that dietary Patterns in Adults Following the Christian Orthod made by Frontiers in Nutrition.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe paper claimed that nutritional and bioactive... [paper, claimed, nutritional] --[made_by]--> Heliyon  (The paper claimed that nutritional and bioactive properties and antioxidant pote made by Heliyon.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe paper claimed that avacopan for the... [paper, claimed, avacopan] --[made_by]--> NEJM: The New England Journal of Medicine  (The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis. made by NEJM: The New England Journal of Medicine.)\nThe paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals] --[made_by]--> Heliyon  (The paper claimed that phytochemicals, therapeutic benefits and applications of  made by Heliyon.)\nThe paper claimed that efficacy of methanolic... [paper, claimed, efficacy] --[made_by]--> Heliyon  (The paper claimed that efficacy of methanolic extracts of some medicinal plants  made by Heliyon.)"
        },
        "score": null,
        "search_type": "GRAPH_COMPLETION",
        "source": "graph",
        "structured": null,
        "text": "Nodes:\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that dietary Patterns in... [paper, claimed, dietary]\n__node_content_start__\nThe paper claimed that dietary Patterns in Adults Following the Christian Orthodox Fasting Regime in Greece.\n__node_content_end__\n\nNode: Frontiers in Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that nutritional and bioactive... [paper, claimed, nutritional]\n__node_content_start__\nThe paper claimed that nutritional and bioactive properties and antioxidant potential of Amaranthus tricolor, A. lividus, A viridis, and A. spinosus leafy vegetables.\n__node_content_end__\n\nNode: Heliyon\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that avacopan for the... [paper, claimed, avacopan]\n__node_content_start__\nThe paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.\n__node_content_end__\n\nNode: NEJM: The New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals]\n__node_content_start__\nThe paper claimed that phytochemicals, therapeutic benefits and applications of chrysanthemum flower: A review.\n__node_content_end__\n\nNode: The paper claimed that efficacy of methanolic... [paper, claimed, efficacy]\n__node_content_start__\nThe paper claimed that efficacy of methanolic extracts of some medicinal plants on wound healing in diabetic rats.\n__node_content_end__\n\n\nConnections:\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)\nThe paper claimed that dietary Patterns in... [paper, claimed, dietary] --[made_by]--> Frontiers in Nutrition  (The paper claimed that dietary Patterns in Adults Following the Christian Orthod made by Frontiers in Nutrition.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe paper claimed that nutritional and bioactive... [paper, claimed, nutritional] --[made_by]--> Heliyon  (The paper claimed that nutritional and bioactive properties and antioxidant pote made by Heliyon.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe paper claimed that avacopan for the... [paper, claimed, avacopan] --[made_by]--> NEJM: The New England Journal of Medicine  (The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis. made by NEJM: The New England Journal of Medicine.)\nThe paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals] --[made_by]--> Heliyon  (The paper claimed that phytochemicals, therapeutic benefits and applications of  made by Heliyon.)\nThe paper claimed that efficacy of methanolic... [paper, claimed, efficacy] --[made_by]--> Heliyon  (The paper claimed that efficacy of methanolic extracts of some medicinal plants  made by Heliyon.)"
      }
    ],
    "references": [
      {
        "claim_id": "R002",
        "data_id": "0d01068c-5f25-56aa-943a-63b1cd4a05ba",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "active",
        "doi": "10.1016/j.heliyon.2024.e30453",
        "kind": "original_claim",
        "retracted": false,
        "score": 11,
        "source": "Heliyon",
        "status": "active"
      },
      {
        "claim_id": "C010",
        "data_id": "8f1833d6-f1a6-5a17-bab0-53c083976398",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "active",
        "doi": "10.54393/df.v6i2.187",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "DIET FACTOR (Journal of Nutritional and Food Sciences)",
        "status": "active"
      }
    ],
    "retracted_dois": [],
    "text": "naive_memory cites an active remembered source for 10.1016/j.heliyon.2024.e30453 from Heliyon."
  }
}
```

### Watcher

```json
{
  "claim_id": "R002",
  "decision": {
    "confidence": 1.0,
    "contradicts": true,
    "rationale": "Retraction Watch links original DOI 10.1016/j.heliyon.2024.e30453 to this claim; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
    "superseded_doi": "10.1016/j.heliyon.2024.e30453"
  },
  "doi": "10.1016/j.heliyon.2024.e30453",
  "edge_result": {
    "memify_result": {
      "1870baaf-b8c5-5b21-87dd-f40ef9024f1f": {
        "data_ingestion_info": [
          {
            "run_info": {
              "data_ingestion_info": null,
              "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
              "dataset_name": "groundtruth_memory",
              "payload": null,
              "pipeline_run_id": "705af5e2-1137-4bb6-b358-3815c9d2af5b",
              "status": "PipelineRunCompleted"
            }
          }
        ],
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_name": "groundtruth_memory",
        "payload": null,
        "pipeline_run_id": "705af5e2-1137-4bb6-b358-3815c9d2af5b",
        "status": "PipelineRunCompleted"
      }
    },
    "properties": {
      "confidence": 1.0,
      "edge_text": "Retraction notice for 10.1016/j.heliyon.2024.e30453 contradicts the original claim",
      "ontology_valid": false,
      "rationale": "Retraction Watch links original DOI 10.1016/j.heliyon.2024.e30453 to this claim; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
      "relationship_name": "contradicts",
      "source_data_id": "8f967623-fbe5-5104-bad6-53b3f7f6d931",
      "superseded_doi": "10.1016/j.heliyon.2024.e30453",
      "target_data_id": "0d01068c-5f25-56aa-943a-63b1cd4a05ba"
    },
    "source_node_id": "7e2b4c40-f6ca-5218-8817-48a600d60035",
    "target_node_id": "18fbccdb-ffe1-5c6f-875a-605078123987"
  },
  "forget_result": {
    "data_id": "0d01068c-5f25-56aa-943a-63b1cd4a05ba",
    "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
    "status": "success"
  },
  "graph_edges_after_forget": 0,
  "graph_edges_before_forget": 1,
  "ledger_edges_before_forget": 1,
  "notice_entries": {
    "groundtruth_memory": {
      "data_id": "8f967623-fbe5-5104-bad6-53b3f7f6d931",
      "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
    },
    "naive_memory": {
      "data_id": "8f967623-fbe5-5104-bad6-53b3f7f6d931",
      "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
    }
  }
}
```

### After

```json
{
  "groundtruth_memory": {
    "cites_retracted": false,
    "dataset": "groundtruth_memory",
    "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
    "question": "what does the research say about Nutritional and bioactive properties and antioxidant potential of Amaranthus tricolor, A. lividus, A viridis, and A. spinosus leafy vegetabl?",
    "recall_context": "Nodes:\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that dietary Patterns in... [paper, claimed, dietary]\n__node_content_start__\nThe paper claimed that dietary Patterns in Adults Following the Christian Orthodox Fasting Regime in Greece.\n__node_content_end__\n\nNode: Frontiers in Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals]\n__node_content_start__\nThe paper claimed that phytochemicals, therapeutic benefits and applications of chrysanthemum flower: A review.\n__node_content_end__\n\nNode: Heliyon\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that efficacy of methanolic... [paper, claimed, efficacy]\n__node_content_start__\nThe paper claimed that efficacy of methanolic extracts of some medicinal plants on wound healing in diabetic rats.\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium and Blood Pressure.\n__node_content_end__\n\nNode: JAMA\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that whole-grain... [active, control, paper]\n__node_content_start__\nThe active control paper reports that whole-grain intake and risk of type 2 diabetes.\n__node_content_end__\n\nNode: The American Journal of Clinical Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)\nThe paper claimed that dietary Patterns in... [paper, claimed, dietary] --[made_by]--> Frontiers in Nutrition  (The paper claimed that dietary Patterns in Adults Following the Christian Orthod made by Frontiers in Nutrition.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals] --[made_by]--> Heliyon  (The paper claimed that phytochemicals, therapeutic benefits and applications of  made by Heliyon.)\nThe paper claimed that efficacy of methanolic... [paper, claimed, efficacy] --[made_by]--> Heliyon  (The paper claimed that efficacy of methanolic extracts of some medicinal plants  made by Heliyon.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA  (The active control paper reports that dietary Sodium and Blood Pressure. made by JAMA.)\nThe active control paper reports that whole-grain... [active, control, paper] --[made_by]--> The American Journal of Clinical Nutrition  (The active control paper reports that whole-grain intake and risk of type 2 diab made by The American Journal of Clinical Nutrition.)",
    "recall_mode": "GRAPH_COMPLETION only_context=True",
    "recall_output": [
      {
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_name": "groundtruth_memory",
        "kind": "graph_completion",
        "metadata": {},
        "raw": {
          "value": "Nodes:\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that dietary Patterns in... [paper, claimed, dietary]\n__node_content_start__\nThe paper claimed that dietary Patterns in Adults Following the Christian Orthodox Fasting Regime in Greece.\n__node_content_end__\n\nNode: Frontiers in Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals]\n__node_content_start__\nThe paper claimed that phytochemicals, therapeutic benefits and applications of chrysanthemum flower: A review.\n__node_content_end__\n\nNode: Heliyon\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that efficacy of methanolic... [paper, claimed, efficacy]\n__node_content_start__\nThe paper claimed that efficacy of methanolic extracts of some medicinal plants on wound healing in diabetic rats.\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium and Blood Pressure.\n__node_content_end__\n\nNode: JAMA\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that whole-grain... [active, control, paper]\n__node_content_start__\nThe active control paper reports that whole-grain intake and risk of type 2 diabetes.\n__node_content_end__\n\nNode: The American Journal of Clinical Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)\nThe paper claimed that dietary Patterns in... [paper, claimed, dietary] --[made_by]--> Frontiers in Nutrition  (The paper claimed that dietary Patterns in Adults Following the Christian Orthod made by Frontiers in Nutrition.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals] --[made_by]--> Heliyon  (The paper claimed that phytochemicals, therapeutic benefits and applications of  made by Heliyon.)\nThe paper claimed that efficacy of methanolic... [paper, claimed, efficacy] --[made_by]--> Heliyon  (The paper claimed that efficacy of methanolic extracts of some medicinal plants  made by Heliyon.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA  (The active control paper reports that dietary Sodium and Blood Pressure. made by JAMA.)\nThe active control paper reports that whole-grain... [active, control, paper] --[made_by]--> The American Journal of Clinical Nutrition  (The active control paper reports that whole-grain intake and risk of type 2 diab made by The American Journal of Clinical Nutrition.)"
        },
        "score": null,
        "search_type": "GRAPH_COMPLETION",
        "source": "graph",
        "structured": null,
        "text": "Nodes:\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that dietary Patterns in... [paper, claimed, dietary]\n__node_content_start__\nThe paper claimed that dietary Patterns in Adults Following the Christian Orthodox Fasting Regime in Greece.\n__node_content_end__\n\nNode: Frontiers in Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals]\n__node_content_start__\nThe paper claimed that phytochemicals, therapeutic benefits and applications of chrysanthemum flower: A review.\n__node_content_end__\n\nNode: Heliyon\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that efficacy of methanolic... [paper, claimed, efficacy]\n__node_content_start__\nThe paper claimed that efficacy of methanolic extracts of some medicinal plants on wound healing in diabetic rats.\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium and Blood Pressure.\n__node_content_end__\n\nNode: JAMA\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that whole-grain... [active, control, paper]\n__node_content_start__\nThe active control paper reports that whole-grain intake and risk of type 2 diabetes.\n__node_content_end__\n\nNode: The American Journal of Clinical Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)\nThe paper claimed that dietary Patterns in... [paper, claimed, dietary] --[made_by]--> Frontiers in Nutrition  (The paper claimed that dietary Patterns in Adults Following the Christian Orthod made by Frontiers in Nutrition.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals] --[made_by]--> Heliyon  (The paper claimed that phytochemicals, therapeutic benefits and applications of  made by Heliyon.)\nThe paper claimed that efficacy of methanolic... [paper, claimed, efficacy] --[made_by]--> Heliyon  (The paper claimed that efficacy of methanolic extracts of some medicinal plants  made by Heliyon.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA  (The active control paper reports that dietary Sodium and Blood Pressure. made by JAMA.)\nThe active control paper reports that whole-grain... [active, control, paper] --[made_by]--> The American Journal of Clinical Nutrition  (The active control paper reports that whole-grain intake and risk of type 2 diab made by The American Journal of Clinical Nutrition.)"
      }
    ],
    "references": [
      {
        "claim_id": "R002",
        "data_id": "8f967623-fbe5-5104-bad6-53b3f7f6d931",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "retracted_forgotten",
        "doi": "10.1016/j.heliyon.2024.e30453",
        "kind": "retraction_notice",
        "retracted": false,
        "score": 11,
        "source": "Heliyon",
        "status": "retracted_forgotten"
      },
      {
        "claim_id": "C010",
        "data_id": "8f1833d6-f1a6-5a17-bab0-53c083976398",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.54393/df.v6i2.187",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "DIET FACTOR (Journal of Nutritional and Food Sciences)",
        "status": "active"
      }
    ],
    "retracted_dois": [],
    "text": "groundtruth_memory no longer cites the original retracted claim for 10.1016/j.heliyon.2024.e30453. The active memory cites the retraction notice instead."
  },
  "naive_memory": {
    "cites_retracted": true,
    "dataset": "naive_memory",
    "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
    "question": "what does the research say about Nutritional and bioactive properties and antioxidant potential of Amaranthus tricolor, A. lividus, A viridis, and A. spinosus leafy vegetabl?",
    "recall_context": "Nodes:\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that dietary Patterns in... [paper, claimed, dietary]\n__node_content_start__\nThe paper claimed that dietary Patterns in Adults Following the Christian Orthodox Fasting Regime in Greece.\n__node_content_end__\n\nNode: Frontiers in Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that nutritional and bioactive... [paper, claimed, nutritional]\n__node_content_start__\nThe paper claimed that nutritional and bioactive properties and antioxidant potential of Amaranthus tricolor, A. lividus, A viridis, and A. spinosus leafy vegetables.\n__node_content_end__\n\nNode: Heliyon\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that avacopan for the... [paper, claimed, avacopan]\n__node_content_start__\nThe paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.\n__node_content_end__\n\nNode: NEJM: The New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals]\n__node_content_start__\nThe paper claimed that phytochemicals, therapeutic benefits and applications of chrysanthemum flower: A review.\n__node_content_end__\n\nNode: The paper claimed that efficacy of methanolic... [paper, claimed, efficacy]\n__node_content_start__\nThe paper claimed that efficacy of methanolic extracts of some medicinal plants on wound healing in diabetic rats.\n__node_content_end__\n\n\nConnections:\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)\nThe paper claimed that dietary Patterns in... [paper, claimed, dietary] --[made_by]--> Frontiers in Nutrition  (The paper claimed that dietary Patterns in Adults Following the Christian Orthod made by Frontiers in Nutrition.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe paper claimed that nutritional and bioactive... [paper, claimed, nutritional] --[made_by]--> Heliyon  (The paper claimed that nutritional and bioactive properties and antioxidant pote made by Heliyon.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe paper claimed that avacopan for the... [paper, claimed, avacopan] --[made_by]--> NEJM: The New England Journal of Medicine  (The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis. made by NEJM: The New England Journal of Medicine.)\nThe paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals] --[made_by]--> Heliyon  (The paper claimed that phytochemicals, therapeutic benefits and applications of  made by Heliyon.)\nThe paper claimed that efficacy of methanolic... [paper, claimed, efficacy] --[made_by]--> Heliyon  (The paper claimed that efficacy of methanolic extracts of some medicinal plants  made by Heliyon.)",
    "recall_mode": "GRAPH_COMPLETION only_context=True",
    "recall_output": [
      {
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_name": "naive_memory",
        "kind": "graph_completion",
        "metadata": {},
        "raw": {
          "value": "Nodes:\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that dietary Patterns in... [paper, claimed, dietary]\n__node_content_start__\nThe paper claimed that dietary Patterns in Adults Following the Christian Orthodox Fasting Regime in Greece.\n__node_content_end__\n\nNode: Frontiers in Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that nutritional and bioactive... [paper, claimed, nutritional]\n__node_content_start__\nThe paper claimed that nutritional and bioactive properties and antioxidant potential of Amaranthus tricolor, A. lividus, A viridis, and A. spinosus leafy vegetables.\n__node_content_end__\n\nNode: Heliyon\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that avacopan for the... [paper, claimed, avacopan]\n__node_content_start__\nThe paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.\n__node_content_end__\n\nNode: NEJM: The New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals]\n__node_content_start__\nThe paper claimed that phytochemicals, therapeutic benefits and applications of chrysanthemum flower: A review.\n__node_content_end__\n\nNode: The paper claimed that efficacy of methanolic... [paper, claimed, efficacy]\n__node_content_start__\nThe paper claimed that efficacy of methanolic extracts of some medicinal plants on wound healing in diabetic rats.\n__node_content_end__\n\n\nConnections:\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)\nThe paper claimed that dietary Patterns in... [paper, claimed, dietary] --[made_by]--> Frontiers in Nutrition  (The paper claimed that dietary Patterns in Adults Following the Christian Orthod made by Frontiers in Nutrition.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe paper claimed that nutritional and bioactive... [paper, claimed, nutritional] --[made_by]--> Heliyon  (The paper claimed that nutritional and bioactive properties and antioxidant pote made by Heliyon.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe paper claimed that avacopan for the... [paper, claimed, avacopan] --[made_by]--> NEJM: The New England Journal of Medicine  (The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis. made by NEJM: The New England Journal of Medicine.)\nThe paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals] --[made_by]--> Heliyon  (The paper claimed that phytochemicals, therapeutic benefits and applications of  made by Heliyon.)\nThe paper claimed that efficacy of methanolic... [paper, claimed, efficacy] --[made_by]--> Heliyon  (The paper claimed that efficacy of methanolic extracts of some medicinal plants  made by Heliyon.)"
        },
        "score": null,
        "search_type": "GRAPH_COMPLETION",
        "source": "graph",
        "structured": null,
        "text": "Nodes:\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that dietary Patterns in... [paper, claimed, dietary]\n__node_content_start__\nThe paper claimed that dietary Patterns in Adults Following the Christian Orthodox Fasting Regime in Greece.\n__node_content_end__\n\nNode: Frontiers in Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that nutritional and bioactive... [paper, claimed, nutritional]\n__node_content_start__\nThe paper claimed that nutritional and bioactive properties and antioxidant potential of Amaranthus tricolor, A. lividus, A viridis, and A. spinosus leafy vegetables.\n__node_content_end__\n\nNode: Heliyon\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that avacopan for the... [paper, claimed, avacopan]\n__node_content_start__\nThe paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.\n__node_content_end__\n\nNode: NEJM: The New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals]\n__node_content_start__\nThe paper claimed that phytochemicals, therapeutic benefits and applications of chrysanthemum flower: A review.\n__node_content_end__\n\nNode: The paper claimed that efficacy of methanolic... [paper, claimed, efficacy]\n__node_content_start__\nThe paper claimed that efficacy of methanolic extracts of some medicinal plants on wound healing in diabetic rats.\n__node_content_end__\n\n\nConnections:\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)\nThe paper claimed that dietary Patterns in... [paper, claimed, dietary] --[made_by]--> Frontiers in Nutrition  (The paper claimed that dietary Patterns in Adults Following the Christian Orthod made by Frontiers in Nutrition.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe paper claimed that nutritional and bioactive... [paper, claimed, nutritional] --[made_by]--> Heliyon  (The paper claimed that nutritional and bioactive properties and antioxidant pote made by Heliyon.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe paper claimed that avacopan for the... [paper, claimed, avacopan] --[made_by]--> NEJM: The New England Journal of Medicine  (The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis. made by NEJM: The New England Journal of Medicine.)\nThe paper claimed that phytochemicals, therapeutic benefits... [paper, claimed, phytochemicals] --[made_by]--> Heliyon  (The paper claimed that phytochemicals, therapeutic benefits and applications of  made by Heliyon.)\nThe paper claimed that efficacy of methanolic... [paper, claimed, efficacy] --[made_by]--> Heliyon  (The paper claimed that efficacy of methanolic extracts of some medicinal plants  made by Heliyon.)"
      }
    ],
    "references": [
      {
        "claim_id": "R002",
        "data_id": "0d01068c-5f25-56aa-943a-63b1cd4a05ba",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "retracted_retained",
        "doi": "10.1016/j.heliyon.2024.e30453",
        "kind": "original_claim",
        "retracted": true,
        "score": 11,
        "source": "Heliyon",
        "status": "retracted_forgotten"
      },
      {
        "claim_id": "R002",
        "data_id": "8f967623-fbe5-5104-bad6-53b3f7f6d931",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "retracted_retained",
        "doi": "10.1016/j.heliyon.2024.e30453",
        "kind": "retraction_notice",
        "retracted": false,
        "score": 11,
        "source": "Heliyon",
        "status": "retracted_forgotten"
      },
      {
        "claim_id": "C010",
        "data_id": "8f1833d6-f1a6-5a17-bab0-53c083976398",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "active",
        "doi": "10.54393/df.v6i2.187",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "DIET FACTOR (Journal of Nutritional and Food Sciences)",
        "status": "active"
      }
    ],
    "retracted_dois": [
      "10.1016/j.heliyon.2024.e30453"
    ],
    "text": "naive_memory still cites the retracted original source 10.1016/j.heliyon.2024.e30453 from Heliyon. Treat the answer as unsafe until that source is forgotten."
  }
}
```

## R003 - 10.1002/bcp.70249

Question: `what does the research say about Effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension?`

### Before

```json
{
  "groundtruth_memory": {
    "cites_retracted": false,
    "dataset": "groundtruth_memory",
    "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
    "question": "what does the research say about Effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension?",
    "recall_context": "Nodes:\nNode: The paper claimed that effects of different... [paper, claimed, effects]\n__node_content_start__\nThe paper claimed that effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension: A randomized clinical trial.\n__node_content_end__\n\nNode: British Journal of Clinical Pharmacology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that role of antioxidants... [paper, claimed, role]\n__node_content_start__\nThe paper claimed that role of antioxidants in gestational diabetes mellitus and relation to fetal outcome: a randomized controlled trial.\n__node_content_end__\n\nNode: The Journal of Maternal-Fetal & Neonatal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that whole-grain... [active, control, paper]\n__node_content_start__\nThe active control paper reports that whole-grain intake and risk of type 2 diabetes.\n__node_content_end__\n\nNode: The American Journal of Clinical Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe paper claimed that effects of different... [paper, claimed, effects] --[made_by]--> British Journal of Clinical Pharmacology  (The paper claimed that effects of different antihypertensive drug classes on cen made by British Journal of Clinical Pharmacology.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)\nThe paper claimed that role of antioxidants... [paper, claimed, role] --[made_by]--> The Journal of Maternal-Fetal & Neonatal Medicine  (The paper claimed that role of antioxidants in gestational diabetes mellitus and made by The Journal of Maternal-Fetal & Neonatal Medicine.)\nThe active control paper reports that whole-grain... [active, control, paper] --[made_by]--> The American Journal of Clinical Nutrition  (The active control paper reports that whole-grain intake and risk of type 2 diab made by The American Journal of Clinical Nutrition.)\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)",
    "recall_mode": "GRAPH_COMPLETION only_context=True",
    "recall_output": [
      {
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_name": "groundtruth_memory",
        "kind": "graph_completion",
        "metadata": {},
        "raw": {
          "value": "Nodes:\nNode: The paper claimed that effects of different... [paper, claimed, effects]\n__node_content_start__\nThe paper claimed that effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension: A randomized clinical trial.\n__node_content_end__\n\nNode: British Journal of Clinical Pharmacology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that role of antioxidants... [paper, claimed, role]\n__node_content_start__\nThe paper claimed that role of antioxidants in gestational diabetes mellitus and relation to fetal outcome: a randomized controlled trial.\n__node_content_end__\n\nNode: The Journal of Maternal-Fetal & Neonatal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that whole-grain... [active, control, paper]\n__node_content_start__\nThe active control paper reports that whole-grain intake and risk of type 2 diabetes.\n__node_content_end__\n\nNode: The American Journal of Clinical Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe paper claimed that effects of different... [paper, claimed, effects] --[made_by]--> British Journal of Clinical Pharmacology  (The paper claimed that effects of different antihypertensive drug classes on cen made by British Journal of Clinical Pharmacology.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)\nThe paper claimed that role of antioxidants... [paper, claimed, role] --[made_by]--> The Journal of Maternal-Fetal & Neonatal Medicine  (The paper claimed that role of antioxidants in gestational diabetes mellitus and made by The Journal of Maternal-Fetal & Neonatal Medicine.)\nThe active control paper reports that whole-grain... [active, control, paper] --[made_by]--> The American Journal of Clinical Nutrition  (The active control paper reports that whole-grain intake and risk of type 2 diab made by The American Journal of Clinical Nutrition.)\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)"
        },
        "score": null,
        "search_type": "GRAPH_COMPLETION",
        "source": "graph",
        "structured": null,
        "text": "Nodes:\nNode: The paper claimed that effects of different... [paper, claimed, effects]\n__node_content_start__\nThe paper claimed that effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension: A randomized clinical trial.\n__node_content_end__\n\nNode: British Journal of Clinical Pharmacology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that role of antioxidants... [paper, claimed, role]\n__node_content_start__\nThe paper claimed that role of antioxidants in gestational diabetes mellitus and relation to fetal outcome: a randomized controlled trial.\n__node_content_end__\n\nNode: The Journal of Maternal-Fetal & Neonatal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that whole-grain... [active, control, paper]\n__node_content_start__\nThe active control paper reports that whole-grain intake and risk of type 2 diabetes.\n__node_content_end__\n\nNode: The American Journal of Clinical Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe paper claimed that effects of different... [paper, claimed, effects] --[made_by]--> British Journal of Clinical Pharmacology  (The paper claimed that effects of different antihypertensive drug classes on cen made by British Journal of Clinical Pharmacology.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)\nThe paper claimed that role of antioxidants... [paper, claimed, role] --[made_by]--> The Journal of Maternal-Fetal & Neonatal Medicine  (The paper claimed that role of antioxidants in gestational diabetes mellitus and made by The Journal of Maternal-Fetal & Neonatal Medicine.)\nThe active control paper reports that whole-grain... [active, control, paper] --[made_by]--> The American Journal of Clinical Nutrition  (The active control paper reports that whole-grain intake and risk of type 2 diab made by The American Journal of Clinical Nutrition.)\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)"
      }
    ],
    "references": [
      {
        "claim_id": "R003",
        "data_id": "e21ca4ca-0fc0-59bc-a3d4-7025db76c675",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.1002/bcp.70249",
        "kind": "original_claim",
        "retracted": false,
        "score": 11,
        "source": "British Journal of Clinical Pharmacology",
        "status": "active"
      },
      {
        "claim_id": "C003",
        "data_id": "d3d710dc-228a-5960-bfce-a06ad17503ce",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.18137/cardiometry.2022.24.10191021",
        "kind": "original_claim",
        "retracted": false,
        "score": 2,
        "source": "CARDIOMETRY",
        "status": "active"
      },
      {
        "claim_id": "C012",
        "data_id": "eec39b26-e7a8-5064-bd34-eca24c47b414",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.1001/jama.2024.1907",
        "kind": "original_claim",
        "retracted": false,
        "score": 2,
        "source": "JAMA",
        "status": "active"
      },
      {
        "claim_id": "R010",
        "data_id": "d13dc0ac-adf9-536e-9b7b-ee57b4bc6066",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.1007/s00500-023-09589-5",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "Soft Computing",
        "status": "active"
      },
      {
        "claim_id": "R015",
        "data_id": "57a0c28a-fb22-579e-ad51-e0d96239ea46",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.1016/j.heliyon.2025.e41964",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "Heliyon",
        "status": "active"
      }
    ],
    "retracted_dois": [],
    "text": "groundtruth_memory cites an active remembered source for 10.1002/bcp.70249 from British Journal of Clinical Pharmacology."
  },
  "naive_memory": {
    "cites_retracted": false,
    "dataset": "naive_memory",
    "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
    "question": "what does the research say about Effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension?",
    "recall_context": "Nodes:\nNode: The paper claimed that effects of different... [paper, claimed, effects]\n__node_content_start__\nThe paper claimed that effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension: A randomized clinical trial.\n__node_content_end__\n\nNode: British Journal of Clinical Pharmacology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that avacopan for the... [paper, claimed, avacopan]\n__node_content_start__\nThe paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.\n__node_content_end__\n\nNode: NEJM: The New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that role of antioxidants... [paper, claimed, role]\n__node_content_start__\nThe paper claimed that role of antioxidants in gestational diabetes mellitus and relation to fetal outcome: a randomized controlled trial.\n__node_content_end__\n\nNode: The Journal of Maternal-Fetal & Neonatal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that whole-grain... [active, control, paper]\n__node_content_start__\nThe active control paper reports that whole-grain intake and risk of type 2 diabetes.\n__node_content_end__\n\nNode: The American Journal of Clinical Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe paper claimed that effects of different... [paper, claimed, effects] --[made_by]--> British Journal of Clinical Pharmacology  (The paper claimed that effects of different antihypertensive drug classes on cen made by British Journal of Clinical Pharmacology.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe paper claimed that avacopan for the... [paper, claimed, avacopan] --[made_by]--> NEJM: The New England Journal of Medicine  (The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis. made by NEJM: The New England Journal of Medicine.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe paper claimed that role of antioxidants... [paper, claimed, role] --[made_by]--> The Journal of Maternal-Fetal & Neonatal Medicine  (The paper claimed that role of antioxidants in gestational diabetes mellitus and made by The Journal of Maternal-Fetal & Neonatal Medicine.)\nThe active control paper reports that whole-grain... [active, control, paper] --[made_by]--> The American Journal of Clinical Nutrition  (The active control paper reports that whole-grain intake and risk of type 2 diab made by The American Journal of Clinical Nutrition.)\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)",
    "recall_mode": "GRAPH_COMPLETION only_context=True",
    "recall_output": [
      {
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_name": "naive_memory",
        "kind": "graph_completion",
        "metadata": {},
        "raw": {
          "value": "Nodes:\nNode: The paper claimed that effects of different... [paper, claimed, effects]\n__node_content_start__\nThe paper claimed that effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension: A randomized clinical trial.\n__node_content_end__\n\nNode: British Journal of Clinical Pharmacology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that avacopan for the... [paper, claimed, avacopan]\n__node_content_start__\nThe paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.\n__node_content_end__\n\nNode: NEJM: The New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that role of antioxidants... [paper, claimed, role]\n__node_content_start__\nThe paper claimed that role of antioxidants in gestational diabetes mellitus and relation to fetal outcome: a randomized controlled trial.\n__node_content_end__\n\nNode: The Journal of Maternal-Fetal & Neonatal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that whole-grain... [active, control, paper]\n__node_content_start__\nThe active control paper reports that whole-grain intake and risk of type 2 diabetes.\n__node_content_end__\n\nNode: The American Journal of Clinical Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe paper claimed that effects of different... [paper, claimed, effects] --[made_by]--> British Journal of Clinical Pharmacology  (The paper claimed that effects of different antihypertensive drug classes on cen made by British Journal of Clinical Pharmacology.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe paper claimed that avacopan for the... [paper, claimed, avacopan] --[made_by]--> NEJM: The New England Journal of Medicine  (The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis. made by NEJM: The New England Journal of Medicine.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe paper claimed that role of antioxidants... [paper, claimed, role] --[made_by]--> The Journal of Maternal-Fetal & Neonatal Medicine  (The paper claimed that role of antioxidants in gestational diabetes mellitus and made by The Journal of Maternal-Fetal & Neonatal Medicine.)\nThe active control paper reports that whole-grain... [active, control, paper] --[made_by]--> The American Journal of Clinical Nutrition  (The active control paper reports that whole-grain intake and risk of type 2 diab made by The American Journal of Clinical Nutrition.)\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)"
        },
        "score": null,
        "search_type": "GRAPH_COMPLETION",
        "source": "graph",
        "structured": null,
        "text": "Nodes:\nNode: The paper claimed that effects of different... [paper, claimed, effects]\n__node_content_start__\nThe paper claimed that effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension: A randomized clinical trial.\n__node_content_end__\n\nNode: British Journal of Clinical Pharmacology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that avacopan for the... [paper, claimed, avacopan]\n__node_content_start__\nThe paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.\n__node_content_end__\n\nNode: NEJM: The New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that role of antioxidants... [paper, claimed, role]\n__node_content_start__\nThe paper claimed that role of antioxidants in gestational diabetes mellitus and relation to fetal outcome: a randomized controlled trial.\n__node_content_end__\n\nNode: The Journal of Maternal-Fetal & Neonatal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that whole-grain... [active, control, paper]\n__node_content_start__\nThe active control paper reports that whole-grain intake and risk of type 2 diabetes.\n__node_content_end__\n\nNode: The American Journal of Clinical Nutrition\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe paper claimed that effects of different... [paper, claimed, effects] --[made_by]--> British Journal of Clinical Pharmacology  (The paper claimed that effects of different antihypertensive drug classes on cen made by British Journal of Clinical Pharmacology.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe paper claimed that avacopan for the... [paper, claimed, avacopan] --[made_by]--> NEJM: The New England Journal of Medicine  (The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis. made by NEJM: The New England Journal of Medicine.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe paper claimed that role of antioxidants... [paper, claimed, role] --[made_by]--> The Journal of Maternal-Fetal & Neonatal Medicine  (The paper claimed that role of antioxidants in gestational diabetes mellitus and made by The Journal of Maternal-Fetal & Neonatal Medicine.)\nThe active control paper reports that whole-grain... [active, control, paper] --[made_by]--> The American Journal of Clinical Nutrition  (The active control paper reports that whole-grain intake and risk of type 2 diab made by The American Journal of Clinical Nutrition.)\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)"
      }
    ],
    "references": [
      {
        "claim_id": "R003",
        "data_id": "e21ca4ca-0fc0-59bc-a3d4-7025db76c675",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "active",
        "doi": "10.1002/bcp.70249",
        "kind": "original_claim",
        "retracted": false,
        "score": 11,
        "source": "British Journal of Clinical Pharmacology",
        "status": "active"
      },
      {
        "claim_id": "C003",
        "data_id": "d3d710dc-228a-5960-bfce-a06ad17503ce",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "active",
        "doi": "10.18137/cardiometry.2022.24.10191021",
        "kind": "original_claim",
        "retracted": false,
        "score": 2,
        "source": "CARDIOMETRY",
        "status": "active"
      },
      {
        "claim_id": "C012",
        "data_id": "eec39b26-e7a8-5064-bd34-eca24c47b414",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "active",
        "doi": "10.1001/jama.2024.1907",
        "kind": "original_claim",
        "retracted": false,
        "score": 2,
        "source": "JAMA",
        "status": "active"
      },
      {
        "claim_id": "R010",
        "data_id": "d13dc0ac-adf9-536e-9b7b-ee57b4bc6066",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "active",
        "doi": "10.1007/s00500-023-09589-5",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "Soft Computing",
        "status": "active"
      },
      {
        "claim_id": "R015",
        "data_id": "57a0c28a-fb22-579e-ad51-e0d96239ea46",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "active",
        "doi": "10.1016/j.heliyon.2025.e41964",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "Heliyon",
        "status": "active"
      }
    ],
    "retracted_dois": [],
    "text": "naive_memory cites an active remembered source for 10.1002/bcp.70249 from British Journal of Clinical Pharmacology."
  }
}
```

### Watcher

```json
{
  "claim_id": "R003",
  "decision": {
    "confidence": 1.0,
    "contradicts": true,
    "rationale": "Retraction Watch links original DOI 10.1002/bcp.70249 to this claim; reason: Concerns/Issues about Human Subject Welfare;Concerns/Issues about Methods;Error in Analyses;Investigation by Journal/Publisher;Investigation by Third Party;Unreliable Results and/or Conclusions;",
    "superseded_doi": "10.1002/bcp.70249"
  },
  "doi": "10.1002/bcp.70249",
  "edge_result": {
    "memify_result": {
      "1870baaf-b8c5-5b21-87dd-f40ef9024f1f": {
        "data_ingestion_info": [
          {
            "run_info": {
              "data_ingestion_info": null,
              "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
              "dataset_name": "groundtruth_memory",
              "payload": null,
              "pipeline_run_id": "2ad8bc83-315f-408f-89ef-6dc013c3ca44",
              "status": "PipelineRunCompleted"
            }
          }
        ],
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_name": "groundtruth_memory",
        "payload": null,
        "pipeline_run_id": "2ad8bc83-315f-408f-89ef-6dc013c3ca44",
        "status": "PipelineRunCompleted"
      }
    },
    "properties": {
      "confidence": 1.0,
      "edge_text": "Retraction notice for 10.1002/bcp.70249 contradicts the original claim",
      "ontology_valid": false,
      "rationale": "Retraction Watch links original DOI 10.1002/bcp.70249 to this claim; reason: Concerns/Issues about Human Subject Welfare;Concerns/Issues about Methods;Error in Analyses;Investigation by Journal/Publisher;Investigation by Third Party;Unreliable Results and/or Conclusions;",
      "relationship_name": "contradicts",
      "source_data_id": "99e5a7e4-1f8d-588b-8317-c7a32aa727ce",
      "superseded_doi": "10.1002/bcp.70249",
      "target_data_id": "e21ca4ca-0fc0-59bc-a3d4-7025db76c675"
    },
    "source_node_id": "47d556d2-9954-5fd3-a634-12634b18fe2f",
    "target_node_id": "40ad3d4b-8121-5305-97cb-fadba4dab1e9"
  },
  "forget_result": {
    "data_id": "e21ca4ca-0fc0-59bc-a3d4-7025db76c675",
    "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
    "status": "success"
  },
  "graph_edges_after_forget": 0,
  "graph_edges_before_forget": 1,
  "ledger_edges_before_forget": 1,
  "notice_entries": {
    "groundtruth_memory": {
      "data_id": "99e5a7e4-1f8d-588b-8317-c7a32aa727ce",
      "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
    },
    "naive_memory": {
      "data_id": "99e5a7e4-1f8d-588b-8317-c7a32aa727ce",
      "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
    }
  }
}
```

### After

```json
{
  "groundtruth_memory": {
    "cites_retracted": false,
    "dataset": "groundtruth_memory",
    "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
    "question": "what does the research say about Effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension?",
    "recall_context": "Nodes:\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The retraction notice says that Effects of... [retraction, notice, says]\n__node_content_start__\nThe retraction notice says that Effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension: A randomized clinical trial (DOI 10.1002/bcp.70249) was retracted. Reason: Concerns/Issues about Human Subject Welfare;Concerns/Issues about Methods;Error in Analyses;Investigation by Journal/Publisher;Investigation by Third Party;Unreliable Results and/or Conclusions;.\n__node_content_end__\n\nNode: Retraction Watch / Crossref\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that role of antioxidants... [paper, claimed, role]\n__node_content_start__\nThe paper claimed that role of antioxidants in gestational diabetes mellitus and relation to fetal outcome: a randomized controlled trial.\n__node_content_end__\n\nNode: The Journal of Maternal-Fetal & Neonatal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that vitamin... [active, control, paper]\n__node_content_start__\nThe active control paper reports that vitamin D Supplementation and Prevention of Type 2 Diabetes.\n__node_content_end__\n\nNode: New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe retraction notice says that Effects of... [retraction, notice, says] --[made_by]--> Retraction Watch / Crossref  (The retraction notice says that Effects of different antihypertensive drug class made by Retraction Watch / Crossref.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)\nThe paper claimed that role of antioxidants... [paper, claimed, role] --[made_by]--> The Journal of Maternal-Fetal & Neonatal Medicine  (The paper claimed that role of antioxidants in gestational diabetes mellitus and made by The Journal of Maternal-Fetal & Neonatal Medicine.)\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)\nThe active control paper reports that vitamin... [active, control, paper] --[made_by]--> New England Journal of Medicine  (The active control paper reports that vitamin D Supplementation and Prevention o made by New England Journal of Medicine.)",
    "recall_mode": "GRAPH_COMPLETION only_context=True",
    "recall_output": [
      {
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_name": "groundtruth_memory",
        "kind": "graph_completion",
        "metadata": {},
        "raw": {
          "value": "Nodes:\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The retraction notice says that Effects of... [retraction, notice, says]\n__node_content_start__\nThe retraction notice says that Effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension: A randomized clinical trial (DOI 10.1002/bcp.70249) was retracted. Reason: Concerns/Issues about Human Subject Welfare;Concerns/Issues about Methods;Error in Analyses;Investigation by Journal/Publisher;Investigation by Third Party;Unreliable Results and/or Conclusions;.\n__node_content_end__\n\nNode: Retraction Watch / Crossref\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that role of antioxidants... [paper, claimed, role]\n__node_content_start__\nThe paper claimed that role of antioxidants in gestational diabetes mellitus and relation to fetal outcome: a randomized controlled trial.\n__node_content_end__\n\nNode: The Journal of Maternal-Fetal & Neonatal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that vitamin... [active, control, paper]\n__node_content_start__\nThe active control paper reports that vitamin D Supplementation and Prevention of Type 2 Diabetes.\n__node_content_end__\n\nNode: New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe retraction notice says that Effects of... [retraction, notice, says] --[made_by]--> Retraction Watch / Crossref  (The retraction notice says that Effects of different antihypertensive drug class made by Retraction Watch / Crossref.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)\nThe paper claimed that role of antioxidants... [paper, claimed, role] --[made_by]--> The Journal of Maternal-Fetal & Neonatal Medicine  (The paper claimed that role of antioxidants in gestational diabetes mellitus and made by The Journal of Maternal-Fetal & Neonatal Medicine.)\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)\nThe active control paper reports that vitamin... [active, control, paper] --[made_by]--> New England Journal of Medicine  (The active control paper reports that vitamin D Supplementation and Prevention o made by New England Journal of Medicine.)"
        },
        "score": null,
        "search_type": "GRAPH_COMPLETION",
        "source": "graph",
        "structured": null,
        "text": "Nodes:\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The retraction notice says that Effects of... [retraction, notice, says]\n__node_content_start__\nThe retraction notice says that Effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension: A randomized clinical trial (DOI 10.1002/bcp.70249) was retracted. Reason: Concerns/Issues about Human Subject Welfare;Concerns/Issues about Methods;Error in Analyses;Investigation by Journal/Publisher;Investigation by Third Party;Unreliable Results and/or Conclusions;.\n__node_content_end__\n\nNode: Retraction Watch / Crossref\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that genetic Architecture Modulates... [paper, claimed, genetic]\n__node_content_start__\nThe paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA and miRNA Expression Profiles in Diversity Outbred Mice.\n__node_content_end__\n\nNode: Genetics\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that role of antioxidants... [paper, claimed, role]\n__node_content_start__\nThe paper claimed that role of antioxidants in gestational diabetes mellitus and relation to fetal outcome: a randomized controlled trial.\n__node_content_end__\n\nNode: The Journal of Maternal-Fetal & Neonatal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that vitamin... [active, control, paper]\n__node_content_start__\nThe active control paper reports that vitamin D Supplementation and Prevention of Type 2 Diabetes.\n__node_content_end__\n\nNode: New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe retraction notice says that Effects of... [retraction, notice, says] --[made_by]--> Retraction Watch / Crossref  (The retraction notice says that Effects of different antihypertensive drug class made by Retraction Watch / Crossref.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe paper claimed that genetic Architecture Modulates... [paper, claimed, genetic] --[made_by]--> Genetics  (The paper claimed that genetic Architecture Modulates Diet-Induced Hepatic mRNA  made by Genetics.)\nThe paper claimed that role of antioxidants... [paper, claimed, role] --[made_by]--> The Journal of Maternal-Fetal & Neonatal Medicine  (The paper claimed that role of antioxidants in gestational diabetes mellitus and made by The Journal of Maternal-Fetal & Neonatal Medicine.)\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)\nThe active control paper reports that vitamin... [active, control, paper] --[made_by]--> New England Journal of Medicine  (The active control paper reports that vitamin D Supplementation and Prevention o made by New England Journal of Medicine.)"
      }
    ],
    "references": [
      {
        "claim_id": "R003",
        "data_id": "99e5a7e4-1f8d-588b-8317-c7a32aa727ce",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "retracted_forgotten",
        "doi": "10.1002/bcp.70249",
        "kind": "retraction_notice",
        "retracted": false,
        "score": 11,
        "source": "British Journal of Clinical Pharmacology",
        "status": "retracted_forgotten"
      },
      {
        "claim_id": "C003",
        "data_id": "d3d710dc-228a-5960-bfce-a06ad17503ce",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.18137/cardiometry.2022.24.10191021",
        "kind": "original_claim",
        "retracted": false,
        "score": 2,
        "source": "CARDIOMETRY",
        "status": "active"
      },
      {
        "claim_id": "C012",
        "data_id": "eec39b26-e7a8-5064-bd34-eca24c47b414",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.1001/jama.2024.1907",
        "kind": "original_claim",
        "retracted": false,
        "score": 2,
        "source": "JAMA",
        "status": "active"
      },
      {
        "claim_id": "R010",
        "data_id": "d13dc0ac-adf9-536e-9b7b-ee57b4bc6066",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.1007/s00500-023-09589-5",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "Soft Computing",
        "status": "active"
      },
      {
        "claim_id": "R015",
        "data_id": "57a0c28a-fb22-579e-ad51-e0d96239ea46",
        "dataset": "groundtruth_memory",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "dataset_status": "active",
        "doi": "10.1016/j.heliyon.2025.e41964",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "Heliyon",
        "status": "active"
      }
    ],
    "retracted_dois": [],
    "text": "groundtruth_memory no longer cites the original retracted claim for 10.1002/bcp.70249. The active memory cites the retraction notice instead."
  },
  "naive_memory": {
    "cites_retracted": true,
    "dataset": "naive_memory",
    "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
    "question": "what does the research say about Effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension?",
    "recall_context": "Nodes:\nNode: The paper claimed that effects of different... [paper, claimed, effects]\n__node_content_start__\nThe paper claimed that effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension: A randomized clinical trial.\n__node_content_end__\n\nNode: British Journal of Clinical Pharmacology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The retraction notice says that Effects of... [retraction, notice, says]\n__node_content_start__\nThe retraction notice says that Effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension: A randomized clinical trial (DOI 10.1002/bcp.70249) was retracted. Reason: Concerns/Issues about Human Subject Welfare;Concerns/Issues about Methods;Error in Analyses;Investigation by Journal/Publisher;Investigation by Third Party;Unreliable Results and/or Conclusions;.\n__node_content_end__\n\nNode: Retraction Watch / Crossref\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that avacopan for the... [paper, claimed, avacopan]\n__node_content_start__\nThe paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.\n__node_content_end__\n\nNode: NEJM: The New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that role of antioxidants... [paper, claimed, role]\n__node_content_start__\nThe paper claimed that role of antioxidants in gestational diabetes mellitus and relation to fetal outcome: a randomized controlled trial.\n__node_content_end__\n\nNode: The Journal of Maternal-Fetal & Neonatal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe paper claimed that effects of different... [paper, claimed, effects] --[made_by]--> British Journal of Clinical Pharmacology  (The paper claimed that effects of different antihypertensive drug classes on cen made by British Journal of Clinical Pharmacology.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe retraction notice says that Effects of... [retraction, notice, says] --[made_by]--> Retraction Watch / Crossref  (The retraction notice says that Effects of different antihypertensive drug class made by Retraction Watch / Crossref.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe paper claimed that avacopan for the... [paper, claimed, avacopan] --[made_by]--> NEJM: The New England Journal of Medicine  (The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis. made by NEJM: The New England Journal of Medicine.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe paper claimed that role of antioxidants... [paper, claimed, role] --[made_by]--> The Journal of Maternal-Fetal & Neonatal Medicine  (The paper claimed that role of antioxidants in gestational diabetes mellitus and made by The Journal of Maternal-Fetal & Neonatal Medicine.)\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)",
    "recall_mode": "GRAPH_COMPLETION only_context=True",
    "recall_output": [
      {
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_name": "naive_memory",
        "kind": "graph_completion",
        "metadata": {},
        "raw": {
          "value": "Nodes:\nNode: The paper claimed that effects of different... [paper, claimed, effects]\n__node_content_start__\nThe paper claimed that effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension: A randomized clinical trial.\n__node_content_end__\n\nNode: British Journal of Clinical Pharmacology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The retraction notice says that Effects of... [retraction, notice, says]\n__node_content_start__\nThe retraction notice says that Effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension: A randomized clinical trial (DOI 10.1002/bcp.70249) was retracted. Reason: Concerns/Issues about Human Subject Welfare;Concerns/Issues about Methods;Error in Analyses;Investigation by Journal/Publisher;Investigation by Third Party;Unreliable Results and/or Conclusions;.\n__node_content_end__\n\nNode: Retraction Watch / Crossref\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that avacopan for the... [paper, claimed, avacopan]\n__node_content_start__\nThe paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.\n__node_content_end__\n\nNode: NEJM: The New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that role of antioxidants... [paper, claimed, role]\n__node_content_start__\nThe paper claimed that role of antioxidants in gestational diabetes mellitus and relation to fetal outcome: a randomized controlled trial.\n__node_content_end__\n\nNode: The Journal of Maternal-Fetal & Neonatal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe paper claimed that effects of different... [paper, claimed, effects] --[made_by]--> British Journal of Clinical Pharmacology  (The paper claimed that effects of different antihypertensive drug classes on cen made by British Journal of Clinical Pharmacology.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe retraction notice says that Effects of... [retraction, notice, says] --[made_by]--> Retraction Watch / Crossref  (The retraction notice says that Effects of different antihypertensive drug class made by Retraction Watch / Crossref.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe paper claimed that avacopan for the... [paper, claimed, avacopan] --[made_by]--> NEJM: The New England Journal of Medicine  (The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis. made by NEJM: The New England Journal of Medicine.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe paper claimed that role of antioxidants... [paper, claimed, role] --[made_by]--> The Journal of Maternal-Fetal & Neonatal Medicine  (The paper claimed that role of antioxidants in gestational diabetes mellitus and made by The Journal of Maternal-Fetal & Neonatal Medicine.)\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)"
        },
        "score": null,
        "search_type": "GRAPH_COMPLETION",
        "source": "graph",
        "structured": null,
        "text": "Nodes:\nNode: The paper claimed that effects of different... [paper, claimed, effects]\n__node_content_start__\nThe paper claimed that effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension: A randomized clinical trial.\n__node_content_end__\n\nNode: British Journal of Clinical Pharmacology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that role... [active, control, paper]\n__node_content_start__\nThe active control paper reports that role Of Dash Diet In Blood Pressure.\n__node_content_end__\n\nNode: CARDIOMETRY\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The retraction notice says that Effects of... [retraction, notice, says]\n__node_content_start__\nThe retraction notice says that Effects of different antihypertensive drug classes on central and ambulatory blood pressure in resistant hypertension: A randomized clinical trial (DOI 10.1002/bcp.70249) was retracted. Reason: Concerns/Issues about Human Subject Welfare;Concerns/Issues about Methods;Error in Analyses;Investigation by Journal/Publisher;Investigation by Third Party;Unreliable Results and/or Conclusions;.\n__node_content_end__\n\nNode: Retraction Watch / Crossref\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that nuts... [active, control, paper]\n__node_content_start__\nThe active control paper reports that nuts reduce risk of cardiovascular disease.\n__node_content_end__\n\nNode: Nature Reviews Cardiology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that avacopan for the... [paper, claimed, avacopan]\n__node_content_start__\nThe paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis.\n__node_content_end__\n\nNode: NEJM: The New England Journal of Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that lipoprotein(a)... [active, control, paper]\n__node_content_start__\nThe active control paper reports that lipoprotein(a) Cholesterol, Randomized Omega-3 Fatty Acid Supplementation, and Cardiovascular Events: Extended Follow-up in the VITamin D and OmegA 3 TriaL.\n__node_content_end__\n\nNode: Journal of Clinical Lipidology\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that dietary... [active, control, paper]\n__node_content_start__\nThe active control paper reports that dietary Sodium Intake and Risk of Cardiovascular Disease.\n__node_content_end__\n\nNode: JAMA Internal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that effects... [control, active, paper]\n__node_content_start__\nThe active control paper reports that effects of probiotic supplementation on glycemic control in children with type 1 diabetes: A systematic review and meta-analysis.\n__node_content_end__\n\nNode: Journal of International Medical Research\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The paper claimed that role of antioxidants... [paper, claimed, role]\n__node_content_start__\nThe paper claimed that role of antioxidants in gestational diabetes mellitus and relation to fetal outcome: a randomized controlled trial.\n__node_content_end__\n\nNode: The Journal of Maternal-Fetal & Neonatal Medicine\n__node_content_start__\nNone\n__node_content_end__\n\nNode: The active control paper reports that coffee... [active, control, paper]\n__node_content_start__\nThe active control paper reports that coffee consumption and reduced risk of developing type 2 diabetes: a systematic review with meta-analysis.\n__node_content_end__\n\nNode: Nutrition Reviews\n__node_content_start__\nNone\n__node_content_end__\n\n\nConnections:\nThe paper claimed that effects of different... [paper, claimed, effects] --[made_by]--> British Journal of Clinical Pharmacology  (The paper claimed that effects of different antihypertensive drug classes on cen made by British Journal of Clinical Pharmacology.)\nThe active control paper reports that role... [active, control, paper] --[made_by]--> CARDIOMETRY  (The active control paper reports that role Of Dash Diet In Blood Pressure. made by CARDIOMETRY.)\nThe retraction notice says that Effects of... [retraction, notice, says] --[made_by]--> Retraction Watch / Crossref  (The retraction notice says that Effects of different antihypertensive drug class made by Retraction Watch / Crossref.)\nThe active control paper reports that nuts... [active, control, paper] --[made_by]--> Nature Reviews Cardiology  (The active control paper reports that nuts reduce risk of cardiovascular disease made by Nature Reviews Cardiology.)\nThe paper claimed that avacopan for the... [paper, claimed, avacopan] --[made_by]--> NEJM: The New England Journal of Medicine  (The paper claimed that avacopan for the Treatment of ANCA-Associated Vasculitis. made by NEJM: The New England Journal of Medicine.)\nThe active control paper reports that lipoprotein(a)... [active, control, paper] --[made_by]--> Journal of Clinical Lipidology  (The active control paper reports that lipoprotein(a) Cholesterol, Randomized Ome made by Journal of Clinical Lipidology.)\nThe active control paper reports that dietary... [active, control, paper] --[made_by]--> JAMA Internal Medicine  (The active control paper reports that dietary Sodium Intake and Risk of Cardiova made by JAMA Internal Medicine.)\nThe active control paper reports that effects... [control, active, paper] --[made_by]--> Journal of International Medical Research  (The active control paper reports that effects of probiotic supplementation on gl made by Journal of International Medical Research.)\nThe paper claimed that role of antioxidants... [paper, claimed, role] --[made_by]--> The Journal of Maternal-Fetal & Neonatal Medicine  (The paper claimed that role of antioxidants in gestational diabetes mellitus and made by The Journal of Maternal-Fetal & Neonatal Medicine.)\nThe active control paper reports that coffee... [active, control, paper] --[made_by]--> Nutrition Reviews  (The active control paper reports that coffee consumption and reduced risk of dev made by Nutrition Reviews.)"
      }
    ],
    "references": [
      {
        "claim_id": "R003",
        "data_id": "e21ca4ca-0fc0-59bc-a3d4-7025db76c675",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "retracted_retained",
        "doi": "10.1002/bcp.70249",
        "kind": "original_claim",
        "retracted": true,
        "score": 11,
        "source": "British Journal of Clinical Pharmacology",
        "status": "retracted_forgotten"
      },
      {
        "claim_id": "R003",
        "data_id": "99e5a7e4-1f8d-588b-8317-c7a32aa727ce",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "retracted_retained",
        "doi": "10.1002/bcp.70249",
        "kind": "retraction_notice",
        "retracted": false,
        "score": 11,
        "source": "British Journal of Clinical Pharmacology",
        "status": "retracted_forgotten"
      },
      {
        "claim_id": "C003",
        "data_id": "d3d710dc-228a-5960-bfce-a06ad17503ce",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "active",
        "doi": "10.18137/cardiometry.2022.24.10191021",
        "kind": "original_claim",
        "retracted": false,
        "score": 2,
        "source": "CARDIOMETRY",
        "status": "active"
      },
      {
        "claim_id": "C012",
        "data_id": "eec39b26-e7a8-5064-bd34-eca24c47b414",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "active",
        "doi": "10.1001/jama.2024.1907",
        "kind": "original_claim",
        "retracted": false,
        "score": 2,
        "source": "JAMA",
        "status": "active"
      },
      {
        "claim_id": "R010",
        "data_id": "d13dc0ac-adf9-536e-9b7b-ee57b4bc6066",
        "dataset": "naive_memory",
        "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d",
        "dataset_status": "active",
        "doi": "10.1007/s00500-023-09589-5",
        "kind": "original_claim",
        "retracted": false,
        "score": 1,
        "source": "Soft Computing",
        "status": "active"
      }
    ],
    "retracted_dois": [
      "10.1002/bcp.70249"
    ],
    "text": "naive_memory still cites the retracted original source 10.1002/bcp.70249 from British Journal of Clinical Pharmacology. Treat the answer as unsafe until that source is forgotten."
  }
}
```
