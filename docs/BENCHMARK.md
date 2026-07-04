# GroundTruth Benchmark

Generated: 2026-07-04T13:35:27.294840+00:00

## Headline

- Naive memory retrieves retracted originals in 19/20 answers.
- GroundTruth retrieves retracted originals in 0/20 answers.
- Control-claim retention: 5/5.
- Retraction coverage: 25/25 retracted-cohort originals forgotten from GroundTruth memory.
- Correctness judge: skipped with disclosure; the primary metric is retrieved graph context containing a still-present retracted original.

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
    "action": "processed",
    "claim_id": "R013",
    "doi": "10.1007/978-3-030-00524-5_7",
    "result": {
      "claim_id": "R013",
      "decision": {
        "confidence": 1.0,
        "contradicts": true,
        "rationale": "Retraction Watch links original DOI 10.1007/978-3-030-00524-5_7 to this claim; reason: Concerns/Issues about Referencing/Attributions;Conflict of Interest;Date of Article and/or Notice Unknown;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;",
        "superseded_doi": "10.1007/978-3-030-00524-5_7"
      },
      "doi": "10.1007/978-3-030-00524-5_7",
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
                  "pipeline_run_id": "b4eb6c2a-92f7-4607-b640-60c156388bb8",
                  "status": "PipelineRunCompleted"
                }
              }
            ],
            "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
            "dataset_name": "groundtruth_memory",
            "payload": null,
            "pipeline_run_id": "b4eb6c2a-92f7-4607-b640-60c156388bb8",
            "status": "PipelineRunCompleted"
          }
        },
        "properties": {
          "confidence": 1.0,
          "edge_text": "Retraction notice for 10.1007/978-3-030-00524-5_7 contradicts the original claim",
          "ontology_valid": false,
          "rationale": "Retraction Watch links original DOI 10.1007/978-3-030-00524-5_7 to this claim; reason: Concerns/Issues about Referencing/Attributions;Conflict of Interest;Date of Article and/or Notice Unknown;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;",
          "relationship_name": "contradicts",
          "source_data_id": "c5783413-5ccc-5877-9d83-049b21dca5a5",
          "superseded_doi": "10.1007/978-3-030-00524-5_7",
          "target_data_id": "d4b61a3d-722d-5dd8-988f-af173e8ebee1"
        },
        "source_node_id": "a6f78f94-4dcf-5021-b496-c26f59f2a6ad",
        "target_node_id": "0a0acbf5-9d12-55c9-b1a6-6134bdcc77b7"
      },
      "forget_result": {
        "data_id": "d4b61a3d-722d-5dd8-988f-af173e8ebee1",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "status": "success"
      },
      "graph_edges_after_forget": 1,
      "graph_edges_before_forget": 2,
      "ledger_edges_before_forget": 1,
      "notice_entries": {
        "groundtruth_memory": {
          "data_id": "c5783413-5ccc-5877-9d83-049b21dca5a5",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
        },
        "naive_memory": {
          "data_id": "c5783413-5ccc-5877-9d83-049b21dca5a5",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
        }
      }
    }
  },
  {
    "action": "already_prepared",
    "claim_id": "R014",
    "doi": "10.1016/j.jacadv.2025.101686",
    "status": "retracted_forgotten"
  },
  {
    "action": "processed",
    "claim_id": "R015",
    "doi": "10.1016/j.heliyon.2025.e41964",
    "result": {
      "claim_id": "R015",
      "decision": {
        "confidence": 1.0,
        "contradicts": true,
        "rationale": "Retraction Watch links original DOI 10.1016/j.heliyon.2025.e41964 to this claim; reason: Computer-Aided Content or Computer-Generated Content;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
        "superseded_doi": "10.1016/j.heliyon.2025.e41964"
      },
      "doi": "10.1016/j.heliyon.2025.e41964",
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
                  "pipeline_run_id": "f28429d6-b179-4e89-8e1a-f3e8aa33bb96",
                  "status": "PipelineRunCompleted"
                }
              }
            ],
            "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
            "dataset_name": "groundtruth_memory",
            "payload": null,
            "pipeline_run_id": "f28429d6-b179-4e89-8e1a-f3e8aa33bb96",
            "status": "PipelineRunCompleted"
          }
        },
        "properties": {
          "confidence": 1.0,
          "edge_text": "Retraction notice for 10.1016/j.heliyon.2025.e41964 contradicts the original claim",
          "ontology_valid": false,
          "rationale": "Retraction Watch links original DOI 10.1016/j.heliyon.2025.e41964 to this claim; reason: Computer-Aided Content or Computer-Generated Content;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "relationship_name": "contradicts",
          "source_data_id": "10dd0a00-a6f2-533b-a6af-5d4884e532ac",
          "superseded_doi": "10.1016/j.heliyon.2025.e41964",
          "target_data_id": "57a0c28a-fb22-579e-ad51-e0d96239ea46"
        },
        "source_node_id": "7eff0eb1-ba90-5b6b-92fa-89ff78aef7c4",
        "target_node_id": "224fe172-f852-50e2-8fa3-0e4be54730a4"
      },
      "forget_result": {
        "data_id": "57a0c28a-fb22-579e-ad51-e0d96239ea46",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "status": "success"
      },
      "graph_edges_after_forget": 1,
      "graph_edges_before_forget": 2,
      "ledger_edges_before_forget": 1,
      "notice_entries": {
        "groundtruth_memory": {
          "data_id": "10dd0a00-a6f2-533b-a6af-5d4884e532ac",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
        },
        "naive_memory": {
          "data_id": "10dd0a00-a6f2-533b-a6af-5d4884e532ac",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
        }
      }
    }
  },
  {
    "action": "processed",
    "claim_id": "R016",
    "doi": "10.1016/j.heliyon.2022.e10071",
    "result": {
      "claim_id": "R016",
      "decision": {
        "confidence": 1.0,
        "contradicts": true,
        "rationale": "Retraction Watch links original DOI 10.1016/j.heliyon.2022.e10071 to this claim; reason: Duplication of/in Image;Investigation by Journal/Publisher;Investigation by Third Party;Objections by Author(s);Unreliable Results and/or Conclusions;",
        "superseded_doi": "10.1016/j.heliyon.2022.e10071"
      },
      "doi": "10.1016/j.heliyon.2022.e10071",
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
                  "pipeline_run_id": "54951bd5-6bbc-4776-874c-7fec0da99ca5",
                  "status": "PipelineRunCompleted"
                }
              }
            ],
            "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
            "dataset_name": "groundtruth_memory",
            "payload": null,
            "pipeline_run_id": "54951bd5-6bbc-4776-874c-7fec0da99ca5",
            "status": "PipelineRunCompleted"
          }
        },
        "properties": {
          "confidence": 1.0,
          "edge_text": "Retraction notice for 10.1016/j.heliyon.2022.e10071 contradicts the original claim",
          "ontology_valid": false,
          "rationale": "Retraction Watch links original DOI 10.1016/j.heliyon.2022.e10071 to this claim; reason: Duplication of/in Image;Investigation by Journal/Publisher;Investigation by Third Party;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "relationship_name": "contradicts",
          "source_data_id": "8129f5bb-c4dd-5ba4-96e8-c64bfda8929d",
          "superseded_doi": "10.1016/j.heliyon.2022.e10071",
          "target_data_id": "ded0db36-085e-58b9-a93a-0faf32567f2d"
        },
        "source_node_id": "f330b435-d8cd-5d14-ae35-4b7ecfd97098",
        "target_node_id": "54e9f54f-db85-5ecc-b7fb-e722f93b38ae"
      },
      "forget_result": {
        "data_id": "ded0db36-085e-58b9-a93a-0faf32567f2d",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "status": "success"
      },
      "graph_edges_after_forget": 1,
      "graph_edges_before_forget": 2,
      "ledger_edges_before_forget": 1,
      "notice_entries": {
        "groundtruth_memory": {
          "data_id": "8129f5bb-c4dd-5ba4-96e8-c64bfda8929d",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
        },
        "naive_memory": {
          "data_id": "8129f5bb-c4dd-5ba4-96e8-c64bfda8929d",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
        }
      }
    }
  },
  {
    "action": "processed",
    "claim_id": "R017",
    "doi": "10.3389/fnut.2022.803913",
    "result": {
      "claim_id": "R017",
      "decision": {
        "confidence": 1.0,
        "contradicts": true,
        "rationale": "Retraction Watch links original DOI 10.3389/fnut.2022.803913 to this claim; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Lack of Approval from Company/Institution;",
        "superseded_doi": "10.3389/fnut.2022.803913"
      },
      "doi": "10.3389/fnut.2022.803913",
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
                  "pipeline_run_id": "99de7835-d3c3-4b99-bf80-8183c20166c6",
                  "status": "PipelineRunCompleted"
                }
              }
            ],
            "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
            "dataset_name": "groundtruth_memory",
            "payload": null,
            "pipeline_run_id": "99de7835-d3c3-4b99-bf80-8183c20166c6",
            "status": "PipelineRunCompleted"
          }
        },
        "properties": {
          "confidence": 1.0,
          "edge_text": "Retraction notice for 10.3389/fnut.2022.803913 contradicts the original claim",
          "ontology_valid": false,
          "rationale": "Retraction Watch links original DOI 10.3389/fnut.2022.803913 to this claim; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Lack of Approval from Company/Institution;",
          "relationship_name": "contradicts",
          "source_data_id": "93692e6f-5787-54b3-913a-c3d1fc8808cd",
          "superseded_doi": "10.3389/fnut.2022.803913",
          "target_data_id": "13481387-d756-5462-ab6e-d8a3dbe08581"
        },
        "source_node_id": "d82c26ec-e0d1-5b15-a368-771f9b27687c",
        "target_node_id": "b8265c1f-9fff-5613-a9af-fc4e5a073cdf"
      },
      "forget_result": {
        "data_id": "13481387-d756-5462-ab6e-d8a3dbe08581",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "status": "success"
      },
      "graph_edges_after_forget": 1,
      "graph_edges_before_forget": 2,
      "ledger_edges_before_forget": 1,
      "notice_entries": {
        "groundtruth_memory": {
          "data_id": "93692e6f-5787-54b3-913a-c3d1fc8808cd",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
        },
        "naive_memory": {
          "data_id": "93692e6f-5787-54b3-913a-c3d1fc8808cd",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
        }
      }
    }
  },
  {
    "action": "processed",
    "claim_id": "R018",
    "doi": "10.1016/j.heliyon.2024.e37293",
    "result": {
      "claim_id": "R018",
      "decision": {
        "confidence": 1.0,
        "contradicts": true,
        "rationale": "Retraction Watch links original DOI 10.1016/j.heliyon.2024.e37293 to this claim; reason: Author Unresponsive;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;",
        "superseded_doi": "10.1016/j.heliyon.2024.e37293"
      },
      "doi": "10.1016/j.heliyon.2024.e37293",
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
                  "pipeline_run_id": "c81d807c-6754-4c89-8d60-57aae3269347",
                  "status": "PipelineRunCompleted"
                }
              }
            ],
            "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
            "dataset_name": "groundtruth_memory",
            "payload": null,
            "pipeline_run_id": "c81d807c-6754-4c89-8d60-57aae3269347",
            "status": "PipelineRunCompleted"
          }
        },
        "properties": {
          "confidence": 1.0,
          "edge_text": "Retraction notice for 10.1016/j.heliyon.2024.e37293 contradicts the original claim",
          "ontology_valid": false,
          "rationale": "Retraction Watch links original DOI 10.1016/j.heliyon.2024.e37293 to this claim; reason: Author Unresponsive;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;",
          "relationship_name": "contradicts",
          "source_data_id": "5c55498c-b1e0-5849-a775-90619c77163b",
          "superseded_doi": "10.1016/j.heliyon.2024.e37293",
          "target_data_id": "b66cdeb7-f924-54e8-90fc-14104c2dd908"
        },
        "source_node_id": "52c896d5-9e7e-5be7-9636-2ebd76e680fd",
        "target_node_id": "c18fb749-794b-5bec-8de6-7e4f239f891b"
      },
      "forget_result": {
        "data_id": "b66cdeb7-f924-54e8-90fc-14104c2dd908",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "status": "success"
      },
      "graph_edges_after_forget": 1,
      "graph_edges_before_forget": 2,
      "ledger_edges_before_forget": 1,
      "notice_entries": {
        "groundtruth_memory": {
          "data_id": "5c55498c-b1e0-5849-a775-90619c77163b",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
        },
        "naive_memory": {
          "data_id": "5c55498c-b1e0-5849-a775-90619c77163b",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
        }
      }
    }
  },
  {
    "action": "processed",
    "claim_id": "R019",
    "doi": "10.1016/j.jogc.2023.102264",
    "result": {
      "claim_id": "R019",
      "decision": {
        "confidence": 1.0,
        "contradicts": true,
        "rationale": "Retraction Watch links original DOI 10.1016/j.jogc.2023.102264 to this claim; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Investigation by Third Party;Notice - Limited or No Information;",
        "superseded_doi": "10.1016/j.jogc.2023.102264"
      },
      "doi": "10.1016/j.jogc.2023.102264",
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
                  "pipeline_run_id": "92c82547-f3f0-4711-af0a-bbb00d1c0862",
                  "status": "PipelineRunCompleted"
                }
              }
            ],
            "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
            "dataset_name": "groundtruth_memory",
            "payload": null,
            "pipeline_run_id": "92c82547-f3f0-4711-af0a-bbb00d1c0862",
            "status": "PipelineRunCompleted"
          }
        },
        "properties": {
          "confidence": 1.0,
          "edge_text": "Retraction notice for 10.1016/j.jogc.2023.102264 contradicts the original claim",
          "ontology_valid": false,
          "rationale": "Retraction Watch links original DOI 10.1016/j.jogc.2023.102264 to this claim; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Investigation by Third Party;Notice - Limited or No Information;",
          "relationship_name": "contradicts",
          "source_data_id": "56cb288a-2ea0-558d-8fb8-0b4faab233b3",
          "superseded_doi": "10.1016/j.jogc.2023.102264",
          "target_data_id": "862102b8-eb18-5287-9414-11adfd4c7430"
        },
        "source_node_id": "57340ca5-b984-53ab-9306-24fb2849a101",
        "target_node_id": "57340ca5-b984-53ab-9306-24fb2849a101"
      },
      "forget_result": {
        "data_id": "862102b8-eb18-5287-9414-11adfd4c7430",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "status": "success"
      },
      "graph_edges_after_forget": 2,
      "graph_edges_before_forget": 2,
      "ledger_edges_before_forget": 1,
      "notice_entries": {
        "groundtruth_memory": {
          "data_id": "56cb288a-2ea0-558d-8fb8-0b4faab233b3",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
        },
        "naive_memory": {
          "data_id": "56cb288a-2ea0-558d-8fb8-0b4faab233b3",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
        }
      }
    }
  },
  {
    "action": "processed",
    "claim_id": "R020",
    "doi": "10.1007/s00500-021-06668-3",
    "result": {
      "claim_id": "R020",
      "decision": {
        "confidence": 1.0,
        "contradicts": true,
        "rationale": "Retraction Watch links original DOI 10.1007/s00500-021-06668-3 to this claim; reason: Compromised Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;",
        "superseded_doi": "10.1007/s00500-021-06668-3"
      },
      "doi": "10.1007/s00500-021-06668-3",
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
                  "pipeline_run_id": "558c1304-7f36-489b-911c-dfd16dcc6380",
                  "status": "PipelineRunCompleted"
                }
              }
            ],
            "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
            "dataset_name": "groundtruth_memory",
            "payload": null,
            "pipeline_run_id": "558c1304-7f36-489b-911c-dfd16dcc6380",
            "status": "PipelineRunCompleted"
          }
        },
        "properties": {
          "confidence": 1.0,
          "edge_text": "Retraction notice for 10.1007/s00500-021-06668-3 contradicts the original claim",
          "ontology_valid": false,
          "rationale": "Retraction Watch links original DOI 10.1007/s00500-021-06668-3 to this claim; reason: Compromised Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;",
          "relationship_name": "contradicts",
          "source_data_id": "01e7a371-dbe1-566b-9e19-94bc48e5ab29",
          "superseded_doi": "10.1007/s00500-021-06668-3",
          "target_data_id": "eb56d69a-6313-5dd0-93d8-1d73c161dd3e"
        },
        "source_node_id": "8ca18c7e-ee28-5ca7-8392-484c295e5e60",
        "target_node_id": "90c2b614-9291-588b-8035-5e4e8c38bf59"
      },
      "forget_result": {
        "data_id": "eb56d69a-6313-5dd0-93d8-1d73c161dd3e",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "status": "success"
      },
      "graph_edges_after_forget": 2,
      "graph_edges_before_forget": 3,
      "ledger_edges_before_forget": 1,
      "notice_entries": {
        "groundtruth_memory": {
          "data_id": "01e7a371-dbe1-566b-9e19-94bc48e5ab29",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
        },
        "naive_memory": {
          "data_id": "01e7a371-dbe1-566b-9e19-94bc48e5ab29",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
        }
      }
    }
  },
  {
    "action": "processed",
    "claim_id": "R021",
    "doi": "10.1534/genetics.120.303481",
    "result": {
      "claim_id": "R021",
      "decision": {
        "confidence": 1.0,
        "contradicts": true,
        "rationale": "Retraction Watch links original DOI 10.1534/genetics.120.303481 to this claim; reason: Error in Data;Retract and Replace;",
        "superseded_doi": "10.1534/genetics.120.303481"
      },
      "doi": "10.1534/genetics.120.303481",
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
                  "pipeline_run_id": "6ad0590c-f337-44b9-8a8e-182f95f296e7",
                  "status": "PipelineRunCompleted"
                }
              }
            ],
            "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
            "dataset_name": "groundtruth_memory",
            "payload": null,
            "pipeline_run_id": "6ad0590c-f337-44b9-8a8e-182f95f296e7",
            "status": "PipelineRunCompleted"
          }
        },
        "properties": {
          "confidence": 1.0,
          "edge_text": "Retraction notice for 10.1534/genetics.120.303481 contradicts the original claim",
          "ontology_valid": false,
          "rationale": "Retraction Watch links original DOI 10.1534/genetics.120.303481 to this claim; reason: Error in Data;Retract and Replace;",
          "relationship_name": "contradicts",
          "source_data_id": "5a1af7d0-fa90-5f24-bebf-fe8d24c80ada",
          "superseded_doi": "10.1534/genetics.120.303481",
          "target_data_id": "0b3c61b5-688d-5161-8739-a8795964101f"
        },
        "source_node_id": "b54ef7f0-27bc-58a5-87a6-af3ab067058d",
        "target_node_id": "61ddd47b-469e-5167-9bb3-f993b31cb0a2"
      },
      "forget_result": {
        "data_id": "0b3c61b5-688d-5161-8739-a8795964101f",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "status": "success"
      },
      "graph_edges_after_forget": 2,
      "graph_edges_before_forget": 3,
      "ledger_edges_before_forget": 1,
      "notice_entries": {
        "groundtruth_memory": {
          "data_id": "5a1af7d0-fa90-5f24-bebf-fe8d24c80ada",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
        },
        "naive_memory": {
          "data_id": "5a1af7d0-fa90-5f24-bebf-fe8d24c80ada",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
        }
      }
    }
  },
  {
    "action": "processed",
    "claim_id": "R022",
    "doi": "10.1080/14767058.2020.1814239",
    "result": {
      "claim_id": "R022",
      "decision": {
        "confidence": 1.0,
        "contradicts": true,
        "rationale": "Retraction Watch links original DOI 10.1080/14767058.2020.1814239 to this claim; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Investigation by Third Party;Unreliable Results and/or Conclusions;",
        "superseded_doi": "10.1080/14767058.2020.1814239"
      },
      "doi": "10.1080/14767058.2020.1814239",
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
                  "pipeline_run_id": "9c678738-ee05-478f-8aca-9e83c44ef0c2",
                  "status": "PipelineRunCompleted"
                }
              }
            ],
            "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
            "dataset_name": "groundtruth_memory",
            "payload": null,
            "pipeline_run_id": "9c678738-ee05-478f-8aca-9e83c44ef0c2",
            "status": "PipelineRunCompleted"
          }
        },
        "properties": {
          "confidence": 1.0,
          "edge_text": "Retraction notice for 10.1080/14767058.2020.1814239 contradicts the original claim",
          "ontology_valid": false,
          "rationale": "Retraction Watch links original DOI 10.1080/14767058.2020.1814239 to this claim; reason: Concerns/Issues about Data;Investigation by Journal/Publisher;Investigation by Third Party;Unreliable Results and/or Conclusions;",
          "relationship_name": "contradicts",
          "source_data_id": "91aa65f3-9c58-520a-9133-a4caa283428e",
          "superseded_doi": "10.1080/14767058.2020.1814239",
          "target_data_id": "76a51f40-5e8e-5f6b-bb4a-5587be84fbb9"
        },
        "source_node_id": "95fb4352-f9de-58ef-8490-44338612dc60",
        "target_node_id": "fa299621-17a3-5f06-9df4-63d93c0eda3d"
      },
      "forget_result": {
        "data_id": "76a51f40-5e8e-5f6b-bb4a-5587be84fbb9",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "status": "success"
      },
      "graph_edges_after_forget": 2,
      "graph_edges_before_forget": 3,
      "ledger_edges_before_forget": 1,
      "notice_entries": {
        "groundtruth_memory": {
          "data_id": "91aa65f3-9c58-520a-9133-a4caa283428e",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
        },
        "naive_memory": {
          "data_id": "91aa65f3-9c58-520a-9133-a4caa283428e",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
        }
      }
    }
  },
  {
    "action": "processed",
    "claim_id": "R023",
    "doi": "10.1080/14767058.2019.1678132",
    "result": {
      "claim_id": "R023",
      "decision": {
        "confidence": 1.0,
        "contradicts": true,
        "rationale": "Retraction Watch links original DOI 10.1080/14767058.2019.1678132 to this claim; reason: Author Unresponsive;Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Original Data and/or Images not Provided and/or not Available;Unreliable Results and/or Conclusions;",
        "superseded_doi": "10.1080/14767058.2019.1678132"
      },
      "doi": "10.1080/14767058.2019.1678132",
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
                  "pipeline_run_id": "9901e6ae-003b-4f51-b6f2-04a27ce31fd4",
                  "status": "PipelineRunCompleted"
                }
              }
            ],
            "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
            "dataset_name": "groundtruth_memory",
            "payload": null,
            "pipeline_run_id": "9901e6ae-003b-4f51-b6f2-04a27ce31fd4",
            "status": "PipelineRunCompleted"
          }
        },
        "properties": {
          "confidence": 1.0,
          "edge_text": "Retraction notice for 10.1080/14767058.2019.1678132 contradicts the original claim",
          "ontology_valid": false,
          "rationale": "Retraction Watch links original DOI 10.1080/14767058.2019.1678132 to this claim; reason: Author Unresponsive;Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Original Data and/or Images not Provided and/or not Available;Unreliable Results and/or Conclusions;",
          "relationship_name": "contradicts",
          "source_data_id": "0da65837-1f72-5bfc-b521-42bf55eedbf9",
          "superseded_doi": "10.1080/14767058.2019.1678132",
          "target_data_id": "ceb8698f-0cd6-5114-8ba5-e098418bd9b2"
        },
        "source_node_id": "d0710821-16bc-58dc-8d2d-4a714f252c5e",
        "target_node_id": "e77c42e5-d795-5e45-83bb-5aa903084ac1"
      },
      "forget_result": {
        "data_id": "ceb8698f-0cd6-5114-8ba5-e098418bd9b2",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "status": "success"
      },
      "graph_edges_after_forget": 2,
      "graph_edges_before_forget": 3,
      "ledger_edges_before_forget": 1,
      "notice_entries": {
        "groundtruth_memory": {
          "data_id": "0da65837-1f72-5bfc-b521-42bf55eedbf9",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
        },
        "naive_memory": {
          "data_id": "0da65837-1f72-5bfc-b521-42bf55eedbf9",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
        }
      }
    }
  },
  {
    "action": "processed",
    "claim_id": "R024",
    "doi": "10.1080/14767058.2018.1491030",
    "result": {
      "claim_id": "R024",
      "decision": {
        "confidence": 1.0,
        "contradicts": true,
        "rationale": "Retraction Watch links original DOI 10.1080/14767058.2018.1491030 to this claim; reason: Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;Upgrade/Update of Prior Notice(s);",
        "superseded_doi": "10.1080/14767058.2018.1491030"
      },
      "doi": "10.1080/14767058.2018.1491030",
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
                  "pipeline_run_id": "76c29a2a-ff9c-4ce6-9030-5cdb6d17b5cf",
                  "status": "PipelineRunCompleted"
                }
              }
            ],
            "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
            "dataset_name": "groundtruth_memory",
            "payload": null,
            "pipeline_run_id": "76c29a2a-ff9c-4ce6-9030-5cdb6d17b5cf",
            "status": "PipelineRunCompleted"
          }
        },
        "properties": {
          "confidence": 1.0,
          "edge_text": "Retraction notice for 10.1080/14767058.2018.1491030 contradicts the original claim",
          "ontology_valid": false,
          "rationale": "Retraction Watch links original DOI 10.1080/14767058.2018.1491030 to this claim; reason: Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;Upgrade/Update of Prior Notice(s);",
          "relationship_name": "contradicts",
          "source_data_id": "2d282f1a-c086-5d39-b1c1-047ec5d00e5f",
          "superseded_doi": "10.1080/14767058.2018.1491030",
          "target_data_id": "859fb844-7a20-5938-9d2c-fec6e18ed93d"
        },
        "source_node_id": "42464504-3bc8-58d0-a9c6-89a004fd5a32",
        "target_node_id": "1f9e7f95-2583-5061-9e59-42185a2559d0"
      },
      "forget_result": {
        "data_id": "859fb844-7a20-5938-9d2c-fec6e18ed93d",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "status": "success"
      },
      "graph_edges_after_forget": 2,
      "graph_edges_before_forget": 3,
      "ledger_edges_before_forget": 1,
      "notice_entries": {
        "groundtruth_memory": {
          "data_id": "2d282f1a-c086-5d39-b1c1-047ec5d00e5f",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
        },
        "naive_memory": {
          "data_id": "2d282f1a-c086-5d39-b1c1-047ec5d00e5f",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
        }
      }
    }
  },
  {
    "action": "processed",
    "claim_id": "R025",
    "doi": "10.3109/14767058.2016.1154526",
    "result": {
      "claim_id": "R025",
      "decision": {
        "confidence": 1.0,
        "contradicts": true,
        "rationale": "Retraction Watch links original DOI 10.3109/14767058.2016.1154526 to this claim; reason: Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;Upgrade/Update of Prior Notice(s);",
        "superseded_doi": "10.3109/14767058.2016.1154526"
      },
      "doi": "10.3109/14767058.2016.1154526",
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
                  "pipeline_run_id": "ce5663ef-785b-42ad-917b-79cfc46b2111",
                  "status": "PipelineRunCompleted"
                }
              }
            ],
            "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
            "dataset_name": "groundtruth_memory",
            "payload": null,
            "pipeline_run_id": "ce5663ef-785b-42ad-917b-79cfc46b2111",
            "status": "PipelineRunCompleted"
          }
        },
        "properties": {
          "confidence": 1.0,
          "edge_text": "Retraction notice for 10.3109/14767058.2016.1154526 contradicts the original claim",
          "ontology_valid": false,
          "rationale": "Retraction Watch links original DOI 10.3109/14767058.2016.1154526 to this claim; reason: Concerns/Issues about Data;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;Upgrade/Update of Prior Notice(s);",
          "relationship_name": "contradicts",
          "source_data_id": "818fd588-396d-50cf-8cb7-7f38c268eb42",
          "superseded_doi": "10.3109/14767058.2016.1154526",
          "target_data_id": "65ffea2b-248b-5e27-b82f-c74fa1c8eeb6"
        },
        "source_node_id": "abc1502d-b677-5f30-9531-79ac9f6564cf",
        "target_node_id": "0d5ba7e9-bfde-5896-9333-81a788ba5bfe"
      },
      "forget_result": {
        "data_id": "65ffea2b-248b-5e27-b82f-c74fa1c8eeb6",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "status": "success"
      },
      "graph_edges_after_forget": 2,
      "graph_edges_before_forget": 3,
      "ledger_edges_before_forget": 1,
      "notice_entries": {
        "groundtruth_memory": {
          "data_id": "818fd588-396d-50cf-8cb7-7f38c268eb42",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
        },
        "naive_memory": {
          "data_id": "818fd588-396d-50cf-8cb7-7f38c268eb42",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
        }
      }
    }
  }
]
```

## Results

| Q | Kind | Dataset | Retrieves Retracted Original | Control Retained | Correctness | Retrieved References |
|---|---|---|---:|---:|---|---|
| Q01 | retracted | naive_memory | True | False | skipped_quota_disclosed | R001, R001, R009, R008, R014, R005, R007, R012, C003, R015 |
| Q01 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R001, R009, R008, R014, R015, R021, R025, R019, C001, R007 |
| Q02 | retracted | naive_memory | True | False | skipped_quota_disclosed | C003, R016, R007, C013, R021, R008, C002, R017, C010, R002 |
| Q02 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | C003, C013, C012, R009, C014, R002, C001, C002, C010, C005 |
| Q03 | retracted | naive_memory | True | False | skipped_quota_disclosed | C003, R001, C009, C001, C011, R025, R023, R021, C002, R003, R003, R009 |
| Q03 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | C003, R003, R009, C009, C001, C011, R021, C014, C002, C012, R005 |
| Q04 | retracted | naive_memory | True | False | skipped_quota_disclosed | C003, R012, R013, R001, R004, R011, R020, C013, C009, R010, R017 |
| Q04 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | C003, R008, R009, C013, C009, C008, C011, C014, R004, R021, R011 |
| Q05 | retracted | naive_memory | True | False | skipped_quota_disclosed | C002, C001, C003, R001, C012, C009, C004, R005, R009, R021, C008 |
| Q05 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | C002, C001, C003, C012, R005, R009, R008, C009, C004, C008, C011 |
| Q06 | retracted | naive_memory | True | False | skipped_quota_disclosed | R017, C003, R001, C011, R012, R013, R006, C014, R006, R009, R025, R023, C008 |
| Q06 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | C003, C011, R006, R009, C015, C012, R008, C014, C008, C010, C005 |
| Q07 | retracted | naive_memory | True | False | skipped_quota_disclosed | C001, R007, R016, C003, R001, C002, R025, R023, C008, C009, R003 |
| Q07 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | C001, C003, R007, R009, C002, C008, C010, C013, C011, R025, R001 |
| Q08 | retracted | naive_memory | True | False | skipped_quota_disclosed | C003, R001, R021, C014, R008, R016, R008, R009, C013, C008, R021, R004 |
| Q08 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | C003, R008, R009, C014, R021, C001, R015, C013, C008, C011, C002 |
| Q09 | retracted | naive_memory | True | False | skipped_quota_disclosed | R007, R009, R017, R001, R012, R025, R009, R016, R016, R010, R022 |
| Q09 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R009, R006, C002, R001, R017, R007, R005, R008, R002, R012 |
| Q10 | retracted | naive_memory | True | False | skipped_quota_disclosed | C003, R001, C009, C001, C002, R014, C011, C008, C013, C004 |
| Q10 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | C003, C009, C001, C002, C012, R008, R009, C011, C008, C013, C004 |
| Q11 | retracted | naive_memory | True | False | skipped_quota_disclosed | C003, R012, R013, C001, R011, R020, C013, R010, R001, C008 |
| Q11 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | C003, R021, R009, C001, R008, C013, R011, C008, C009, R001, C011 |
| Q12 | retracted | naive_memory | False | False | skipped_quota_disclosed | R012, R009, R008, R005, R013, R016, R011, R006, R007, R002 |
| Q12 | retracted | groundtruth_memory | False | False | skipped_quota_disclosed | R012, R009, R006, R005, R013, R008, R007, R002, R016, R015 |
| Q13 | control | naive_memory | True | False | skipped_quota_disclosed | C003, C002, C013, C001, R021, C004, C010, C005, C009, C006 |
| Q13 | control | groundtruth_memory | False | True | skipped_quota_disclosed | C003, C002, C013, C001, C012, C011, R021, R009, C004, C010, C005 |
| Q14 | control | naive_memory | True | False | skipped_quota_disclosed | C002, C003, C013, C010, C001, C011, R021, C004, C005, C014 |
| Q14 | control | groundtruth_memory | False | True | skipped_quota_disclosed | C002, C003, C013, C010, C001, C011, C012, C015, R008, R009, C004 |
| Q15 | control | naive_memory | True | False | skipped_quota_disclosed | C003, C002, C013, C001, R001, R021, R009, C010, C004, C012, C009 |
| Q15 | control | groundtruth_memory | False | True | skipped_quota_disclosed | C003, C002, C013, C010, C001, C012, R021, R009, C011, C004, C009 |
| Q16 | control | naive_memory | True | False | skipped_quota_disclosed | C002, C003, C013, R021, C001, C011, C004, C010, C005, R017 |
| Q16 | control | groundtruth_memory | False | True | skipped_quota_disclosed | C002, C003, C013, C001, C011, C014, C012, C015, R008, R009, C004 |
| Q17 | control | naive_memory | True | False | skipped_quota_disclosed | C013, C003, C002, C010, R017, R021, C001, C005, C004, C009 |
| Q17 | control | groundtruth_memory | False | True | skipped_quota_disclosed | C013, C003, C002, C010, C001, C011, R021, R009, C012, C005, C004 |
| Q18 | mixed | naive_memory | True | False | skipped_quota_disclosed | R001, C003, C002, C001, C010, R001, R009, R021, C009, C013, R021 |
| Q18 | mixed | groundtruth_memory | False | False | skipped_quota_disclosed | C003, C001, R001, R009, C010, R021, R008, C002, C009, C013, C008 |
| Q19 | mixed | naive_memory | True | False | skipped_quota_disclosed | C003, R001, R021, R004, C014, C011, C004, C008, C002, C013 |
| Q19 | mixed | groundtruth_memory | False | False | skipped_quota_disclosed | C003, C014, R021, R009, C012, C015, C004, C008, C002, C013, C010 |
| Q20 | mixed | naive_memory | True | False | skipped_quota_disclosed | C003, C013, R001, C001, C002, R021, R003, C009, C008, C012 |
| Q20 | mixed | groundtruth_memory | False | False | skipped_quota_disclosed | C003, C013, C009, C001, C002, R021, R009, C014, C012, R008, C008 |

## Raw Results

Raw JSON: `C:/Users/gudma/OneDrive/Desktop/GITHUB-FILES/groundtruth/data/benchmark_results.json`
