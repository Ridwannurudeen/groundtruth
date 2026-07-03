# GroundTruth Benchmark

Generated: 2026-07-03T21:40:38.184923+00:00

## Headline

- Naive memory cites retracted sources in 17/20 answers.
- GroundTruth cites retracted sources in 0/20 answers.
- Control-claim retention: 5/5.
- Correctness judge: skipped because Gemini free-tier quota is exhausted; primary metric is deterministic citation status.

## Reproduction

```powershell
$env:PYTHONIOENCODING='utf-8'; .\.venv\Scripts\python.exe -m groundtruth.benchmark
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
    "action": "processed",
    "claim_id": "R004",
    "doi": "10.1038/s41598-025-96541-2",
    "result": {
      "claim_id": "R004",
      "decision": {
        "confidence": 1.0,
        "contradicts": true,
        "rationale": "Retraction Watch links original DOI 10.1038/s41598-025-96541-2 to this claim; reason: Computer-Aided Content or Computer-Generated Content;Concerns/Issues about Data;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
        "superseded_doi": "10.1038/s41598-025-96541-2"
      },
      "doi": "10.1038/s41598-025-96541-2",
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
                  "pipeline_run_id": "41839c06-dc93-430d-9b76-7131f3b1dc86",
                  "status": "PipelineRunCompleted"
                }
              }
            ],
            "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
            "dataset_name": "groundtruth_memory",
            "payload": null,
            "pipeline_run_id": "41839c06-dc93-430d-9b76-7131f3b1dc86",
            "status": "PipelineRunCompleted"
          }
        },
        "properties": {
          "confidence": 1.0,
          "edge_text": "Retraction notice for 10.1038/s41598-025-96541-2 contradicts the original claim",
          "ontology_valid": false,
          "rationale": "Retraction Watch links original DOI 10.1038/s41598-025-96541-2 to this claim; reason: Computer-Aided Content or Computer-Generated Content;Concerns/Issues about Data;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "relationship_name": "contradicts",
          "source_data_id": "33d7feae-c703-5a0a-8607-eae01f51ffff",
          "superseded_doi": "10.1038/s41598-025-96541-2",
          "target_data_id": "ea8722b5-a8b9-57f4-89e0-e18772ff635c"
        },
        "source_node_id": "e383aae5-eaad-5a2a-a001-64717c1b5b4e",
        "target_node_id": "86a5ed8b-96a9-5b67-b6c3-bf1a629ada87"
      },
      "forget_result": {
        "data_id": "ea8722b5-a8b9-57f4-89e0-e18772ff635c",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "status": "success"
      },
      "graph_edges_after_forget": 0,
      "graph_edges_before_forget": 1,
      "ledger_edges_before_forget": 1,
      "notice_entries": {
        "groundtruth_memory": {
          "data_id": "33d7feae-c703-5a0a-8607-eae01f51ffff",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
        },
        "naive_memory": {
          "data_id": "33d7feae-c703-5a0a-8607-eae01f51ffff",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
        }
      }
    }
  },
  {
    "action": "processed",
    "claim_id": "R005",
    "doi": "10.1016/j.heliyon.2023.e19675",
    "result": {
      "claim_id": "R005",
      "decision": {
        "confidence": 1.0,
        "contradicts": true,
        "rationale": "Retraction Watch links original DOI 10.1016/j.heliyon.2023.e19675 to this claim; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
        "superseded_doi": "10.1016/j.heliyon.2023.e19675"
      },
      "doi": "10.1016/j.heliyon.2023.e19675",
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
                  "pipeline_run_id": "98c0ce68-43c3-407f-b36e-7f19f982349a",
                  "status": "PipelineRunCompleted"
                }
              }
            ],
            "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
            "dataset_name": "groundtruth_memory",
            "payload": null,
            "pipeline_run_id": "98c0ce68-43c3-407f-b36e-7f19f982349a",
            "status": "PipelineRunCompleted"
          }
        },
        "properties": {
          "confidence": 1.0,
          "edge_text": "Retraction notice for 10.1016/j.heliyon.2023.e19675 contradicts the original claim",
          "ontology_valid": false,
          "rationale": "Retraction Watch links original DOI 10.1016/j.heliyon.2023.e19675 to this claim; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "relationship_name": "contradicts",
          "source_data_id": "26a06040-1641-5fb4-b618-aac0a99829ec",
          "superseded_doi": "10.1016/j.heliyon.2023.e19675",
          "target_data_id": "79f37376-cbd9-5566-80dc-1ad63e27bb39"
        },
        "source_node_id": "b3a82094-b843-5f15-9abc-bbe793d28042",
        "target_node_id": "08656f3a-8490-5ce4-90f1-21ac3697acbd"
      },
      "forget_result": {
        "data_id": "79f37376-cbd9-5566-80dc-1ad63e27bb39",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "status": "success"
      },
      "graph_edges_after_forget": 0,
      "graph_edges_before_forget": 1,
      "ledger_edges_before_forget": 1,
      "notice_entries": {
        "groundtruth_memory": {
          "data_id": "26a06040-1641-5fb4-b618-aac0a99829ec",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
        },
        "naive_memory": {
          "data_id": "26a06040-1641-5fb4-b618-aac0a99829ec",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
        }
      }
    }
  },
  {
    "action": "processed",
    "claim_id": "R006",
    "doi": "10.1371/journal.pone.0255392",
    "result": {
      "claim_id": "R006",
      "decision": {
        "confidence": 1.0,
        "contradicts": true,
        "rationale": "Retraction Watch links original DOI 10.1371/journal.pone.0255392 to this claim; reason: Concerns/Issues about Data;Concerns/Issues about Methods;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Investigation by Third Party;Objections by Author(s);Original Data and/or Images not Provided and/or not Available;Unreliable Results and/or Conclusions;",
        "superseded_doi": "10.1371/journal.pone.0255392"
      },
      "doi": "10.1371/journal.pone.0255392",
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
                  "pipeline_run_id": "be809da9-9f80-4eb7-a5b3-86c8b4a09ddf",
                  "status": "PipelineRunCompleted"
                }
              }
            ],
            "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
            "dataset_name": "groundtruth_memory",
            "payload": null,
            "pipeline_run_id": "be809da9-9f80-4eb7-a5b3-86c8b4a09ddf",
            "status": "PipelineRunCompleted"
          }
        },
        "properties": {
          "confidence": 1.0,
          "edge_text": "Retraction notice for 10.1371/journal.pone.0255392 contradicts the original claim",
          "ontology_valid": false,
          "rationale": "Retraction Watch links original DOI 10.1371/journal.pone.0255392 to this claim; reason: Concerns/Issues about Data;Concerns/Issues about Methods;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Investigation by Third Party;Objections by Author(s);Original Data and/or Images not Provided and/or not Available;Unreliable Results and/or Conclusions;",
          "relationship_name": "contradicts",
          "source_data_id": "eddb95b1-729c-5dc0-8905-78d2dbfe26fa",
          "superseded_doi": "10.1371/journal.pone.0255392",
          "target_data_id": "c37c62bc-a612-58be-af2c-2aab5c468c08"
        },
        "source_node_id": "f988f4ff-1c17-5bdd-b83a-640bbca8f934",
        "target_node_id": "9b15b006-86b7-532d-b959-1b16b5554f83"
      },
      "forget_result": {
        "data_id": "c37c62bc-a612-58be-af2c-2aab5c468c08",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "status": "success"
      },
      "graph_edges_after_forget": 0,
      "graph_edges_before_forget": 1,
      "ledger_edges_before_forget": 1,
      "notice_entries": {
        "groundtruth_memory": {
          "data_id": "eddb95b1-729c-5dc0-8905-78d2dbfe26fa",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
        },
        "naive_memory": {
          "data_id": "eddb95b1-729c-5dc0-8905-78d2dbfe26fa",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
        }
      }
    }
  },
  {
    "action": "processed",
    "claim_id": "R007",
    "doi": "10.1016/j.heliyon.2023.e20232",
    "result": {
      "claim_id": "R007",
      "decision": {
        "confidence": 1.0,
        "contradicts": true,
        "rationale": "Retraction Watch links original DOI 10.1016/j.heliyon.2023.e20232 to this claim; reason: Concerns/Issues about Authorship/Affiliation;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
        "superseded_doi": "10.1016/j.heliyon.2023.e20232"
      },
      "doi": "10.1016/j.heliyon.2023.e20232",
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
                  "pipeline_run_id": "6951d6f6-c878-4460-af4a-f72d0819adab",
                  "status": "PipelineRunCompleted"
                }
              }
            ],
            "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
            "dataset_name": "groundtruth_memory",
            "payload": null,
            "pipeline_run_id": "6951d6f6-c878-4460-af4a-f72d0819adab",
            "status": "PipelineRunCompleted"
          }
        },
        "properties": {
          "confidence": 1.0,
          "edge_text": "Retraction notice for 10.1016/j.heliyon.2023.e20232 contradicts the original claim",
          "ontology_valid": false,
          "rationale": "Retraction Watch links original DOI 10.1016/j.heliyon.2023.e20232 to this claim; reason: Concerns/Issues about Authorship/Affiliation;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "relationship_name": "contradicts",
          "source_data_id": "e0b8a838-2d0b-5eb6-b05b-22bbacb7b6a6",
          "superseded_doi": "10.1016/j.heliyon.2023.e20232",
          "target_data_id": "2d49a0d2-69a4-50b4-99ca-b13c3f8243a9"
        },
        "source_node_id": "50c65637-54e6-5b77-b227-9fce90dff868",
        "target_node_id": "c54f681c-2e24-54ee-990a-9a6fca8b87f7"
      },
      "forget_result": {
        "data_id": "2d49a0d2-69a4-50b4-99ca-b13c3f8243a9",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "status": "success"
      },
      "graph_edges_after_forget": 0,
      "graph_edges_before_forget": 1,
      "ledger_edges_before_forget": 1,
      "notice_entries": {
        "groundtruth_memory": {
          "data_id": "e0b8a838-2d0b-5eb6-b05b-22bbacb7b6a6",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
        },
        "naive_memory": {
          "data_id": "e0b8a838-2d0b-5eb6-b05b-22bbacb7b6a6",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
        }
      }
    }
  },
  {
    "action": "processed",
    "claim_id": "R008",
    "doi": "10.1016/j.heliyon.2024.e29871",
    "result": {
      "claim_id": "R008",
      "decision": {
        "confidence": 1.0,
        "contradicts": true,
        "rationale": "Retraction Watch links original DOI 10.1016/j.heliyon.2024.e29871 to this claim; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
        "superseded_doi": "10.1016/j.heliyon.2024.e29871"
      },
      "doi": "10.1016/j.heliyon.2024.e29871",
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
                  "pipeline_run_id": "3c74856b-2ead-40eb-930a-e7756e028e6e",
                  "status": "PipelineRunCompleted"
                }
              }
            ],
            "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
            "dataset_name": "groundtruth_memory",
            "payload": null,
            "pipeline_run_id": "3c74856b-2ead-40eb-930a-e7756e028e6e",
            "status": "PipelineRunCompleted"
          }
        },
        "properties": {
          "confidence": 1.0,
          "edge_text": "Retraction notice for 10.1016/j.heliyon.2024.e29871 contradicts the original claim",
          "ontology_valid": false,
          "rationale": "Retraction Watch links original DOI 10.1016/j.heliyon.2024.e29871 to this claim; reason: Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "relationship_name": "contradicts",
          "source_data_id": "7f4d9085-c721-5aa6-b59d-f07faec035f1",
          "superseded_doi": "10.1016/j.heliyon.2024.e29871",
          "target_data_id": "87da7153-d003-5008-8c6a-7e7cfacb7e5c"
        },
        "source_node_id": "3982f563-a5cb-51d4-bb66-73432f3cb486",
        "target_node_id": "e9c8b1ae-d2a1-5097-b69b-5a94db21f012"
      },
      "forget_result": {
        "data_id": "87da7153-d003-5008-8c6a-7e7cfacb7e5c",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "status": "success"
      },
      "graph_edges_after_forget": 0,
      "graph_edges_before_forget": 1,
      "ledger_edges_before_forget": 1,
      "notice_entries": {
        "groundtruth_memory": {
          "data_id": "7f4d9085-c721-5aa6-b59d-f07faec035f1",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
        },
        "naive_memory": {
          "data_id": "7f4d9085-c721-5aa6-b59d-f07faec035f1",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
        }
      }
    }
  },
  {
    "action": "processed",
    "claim_id": "R009",
    "doi": "10.1016/j.heliyon.2023.e21222",
    "result": {
      "claim_id": "R009",
      "decision": {
        "confidence": 1.0,
        "contradicts": true,
        "rationale": "Retraction Watch links original DOI 10.1016/j.heliyon.2023.e21222 to this claim; reason: Concerns/Issues about Authorship/Affiliation;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
        "superseded_doi": "10.1016/j.heliyon.2023.e21222"
      },
      "doi": "10.1016/j.heliyon.2023.e21222",
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
                  "pipeline_run_id": "8775d50d-e1f0-40e8-b979-246c3ef7d51e",
                  "status": "PipelineRunCompleted"
                }
              }
            ],
            "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
            "dataset_name": "groundtruth_memory",
            "payload": null,
            "pipeline_run_id": "8775d50d-e1f0-40e8-b979-246c3ef7d51e",
            "status": "PipelineRunCompleted"
          }
        },
        "properties": {
          "confidence": 1.0,
          "edge_text": "Retraction notice for 10.1016/j.heliyon.2023.e21222 contradicts the original claim",
          "ontology_valid": false,
          "rationale": "Retraction Watch links original DOI 10.1016/j.heliyon.2023.e21222 to this claim; reason: Concerns/Issues about Authorship/Affiliation;Concerns/Issues about Results and/or Conclusions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "relationship_name": "contradicts",
          "source_data_id": "fd06d41a-718c-5980-aa6d-1c99ee176224",
          "superseded_doi": "10.1016/j.heliyon.2023.e21222",
          "target_data_id": "36eae4ae-b0f1-519b-8ea1-d50c2e60bd5f"
        },
        "source_node_id": "4e3795a0-c200-509f-87b4-99a800ce5785",
        "target_node_id": "4137a2a3-5fbf-5b0e-bdc9-f489b3d21fb6"
      },
      "forget_result": {
        "data_id": "36eae4ae-b0f1-519b-8ea1-d50c2e60bd5f",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "status": "success"
      },
      "graph_edges_after_forget": 0,
      "graph_edges_before_forget": 1,
      "ledger_edges_before_forget": 1,
      "notice_entries": {
        "groundtruth_memory": {
          "data_id": "fd06d41a-718c-5980-aa6d-1c99ee176224",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
        },
        "naive_memory": {
          "data_id": "fd06d41a-718c-5980-aa6d-1c99ee176224",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
        }
      }
    }
  },
  {
    "action": "processed",
    "claim_id": "R010",
    "doi": "10.1007/s00500-023-09589-5",
    "result": {
      "claim_id": "R010",
      "decision": {
        "confidence": 1.0,
        "contradicts": true,
        "rationale": "Retraction Watch links original DOI 10.1007/s00500-023-09589-5 to this claim; reason: Concerns/Issues about Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;",
        "superseded_doi": "10.1007/s00500-023-09589-5"
      },
      "doi": "10.1007/s00500-023-09589-5",
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
                  "pipeline_run_id": "735eb0f7-3242-4bd4-9fe5-20aad528231b",
                  "status": "PipelineRunCompleted"
                }
              }
            ],
            "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
            "dataset_name": "groundtruth_memory",
            "payload": null,
            "pipeline_run_id": "735eb0f7-3242-4bd4-9fe5-20aad528231b",
            "status": "PipelineRunCompleted"
          }
        },
        "properties": {
          "confidence": 1.0,
          "edge_text": "Retraction notice for 10.1007/s00500-023-09589-5 contradicts the original claim",
          "ontology_valid": false,
          "rationale": "Retraction Watch links original DOI 10.1007/s00500-023-09589-5 to this claim; reason: Concerns/Issues about Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Unreliable Results and/or Conclusions;",
          "relationship_name": "contradicts",
          "source_data_id": "ceee7f78-b013-5352-93e7-084b83127a61",
          "superseded_doi": "10.1007/s00500-023-09589-5",
          "target_data_id": "d13dc0ac-adf9-536e-9b7b-ee57b4bc6066"
        },
        "source_node_id": "94240f29-a55d-512b-8f70-66df8a6fac57",
        "target_node_id": "8b7f4001-b6f3-5a19-8296-22c84dcd12ea"
      },
      "forget_result": {
        "data_id": "d13dc0ac-adf9-536e-9b7b-ee57b4bc6066",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "status": "success"
      },
      "graph_edges_after_forget": 0,
      "graph_edges_before_forget": 1,
      "ledger_edges_before_forget": 1,
      "notice_entries": {
        "groundtruth_memory": {
          "data_id": "ceee7f78-b013-5352-93e7-084b83127a61",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
        },
        "naive_memory": {
          "data_id": "ceee7f78-b013-5352-93e7-084b83127a61",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
        }
      }
    }
  },
  {
    "action": "processed",
    "claim_id": "R011",
    "doi": "10.1007/s00500-023-09482-1",
    "result": {
      "claim_id": "R011",
      "decision": {
        "confidence": 1.0,
        "contradicts": true,
        "rationale": "Retraction Watch links original DOI 10.1007/s00500-023-09482-1 to this claim; reason: Concerns/Issues about Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
        "superseded_doi": "10.1007/s00500-023-09482-1"
      },
      "doi": "10.1007/s00500-023-09482-1",
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
                  "pipeline_run_id": "5b06e91b-8247-4907-b4e7-b8aaff8488a2",
                  "status": "PipelineRunCompleted"
                }
              }
            ],
            "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
            "dataset_name": "groundtruth_memory",
            "payload": null,
            "pipeline_run_id": "5b06e91b-8247-4907-b4e7-b8aaff8488a2",
            "status": "PipelineRunCompleted"
          }
        },
        "properties": {
          "confidence": 1.0,
          "edge_text": "Retraction notice for 10.1007/s00500-023-09482-1 contradicts the original claim",
          "ontology_valid": false,
          "rationale": "Retraction Watch links original DOI 10.1007/s00500-023-09482-1 to this claim; reason: Concerns/Issues about Peer Review;Concerns/Issues about Referencing/Attributions;Investigation by Journal/Publisher;Objections by Author(s);Unreliable Results and/or Conclusions;",
          "relationship_name": "contradicts",
          "source_data_id": "7ee50471-5eca-5da5-9a46-98f60e8c6d87",
          "superseded_doi": "10.1007/s00500-023-09482-1",
          "target_data_id": "be4527b6-ee58-5b79-88a2-6a776a1aad92"
        },
        "source_node_id": "e54e6729-b7f0-57cd-b313-4803aaa5ceca",
        "target_node_id": "2ab42d07-b6be-58f4-be60-7cffd4fc4cb6"
      },
      "forget_result": {
        "data_id": "be4527b6-ee58-5b79-88a2-6a776a1aad92",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "status": "success"
      },
      "graph_edges_after_forget": 0,
      "graph_edges_before_forget": 1,
      "ledger_edges_before_forget": 1,
      "notice_entries": {
        "groundtruth_memory": {
          "data_id": "7ee50471-5eca-5da5-9a46-98f60e8c6d87",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
        },
        "naive_memory": {
          "data_id": "7ee50471-5eca-5da5-9a46-98f60e8c6d87",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
        }
      }
    }
  },
  {
    "action": "processed",
    "claim_id": "R012",
    "doi": "10.1007/978-3-030-00524-5_6",
    "result": {
      "claim_id": "R012",
      "decision": {
        "confidence": 1.0,
        "contradicts": true,
        "rationale": "Retraction Watch links original DOI 10.1007/978-3-030-00524-5_6 to this claim; reason: Concerns/Issues about Referencing/Attributions;Conflict of Interest;Date of Article and/or Notice Unknown;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;",
        "superseded_doi": "10.1007/978-3-030-00524-5_6"
      },
      "doi": "10.1007/978-3-030-00524-5_6",
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
                  "pipeline_run_id": "85c032b9-1eae-4d04-b945-d5e428b114c4",
                  "status": "PipelineRunCompleted"
                }
              }
            ],
            "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
            "dataset_name": "groundtruth_memory",
            "payload": null,
            "pipeline_run_id": "85c032b9-1eae-4d04-b945-d5e428b114c4",
            "status": "PipelineRunCompleted"
          }
        },
        "properties": {
          "confidence": 1.0,
          "edge_text": "Retraction notice for 10.1007/978-3-030-00524-5_6 contradicts the original claim",
          "ontology_valid": false,
          "rationale": "Retraction Watch links original DOI 10.1007/978-3-030-00524-5_6 to this claim; reason: Concerns/Issues about Referencing/Attributions;Conflict of Interest;Date of Article and/or Notice Unknown;Investigation by Journal/Publisher;Objections by Author(s);Rogue Editor;Unreliable Results and/or Conclusions;",
          "relationship_name": "contradicts",
          "source_data_id": "7de422b8-8606-50c3-951a-17a00330ff96",
          "superseded_doi": "10.1007/978-3-030-00524-5_6",
          "target_data_id": "8b310b31-aecd-5a18-8fd5-06e67dcfe8bb"
        },
        "source_node_id": "4ebbca9f-8ace-54ed-8588-b73b16fc05ff",
        "target_node_id": "d9d31375-86bf-5cd0-b843-6e282d21023b"
      },
      "forget_result": {
        "data_id": "8b310b31-aecd-5a18-8fd5-06e67dcfe8bb",
        "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f",
        "status": "success"
      },
      "graph_edges_after_forget": 0,
      "graph_edges_before_forget": 1,
      "ledger_edges_before_forget": 1,
      "notice_entries": {
        "groundtruth_memory": {
          "data_id": "7de422b8-8606-50c3-951a-17a00330ff96",
          "dataset_id": "1870baaf-b8c5-5b21-87dd-f40ef9024f1f"
        },
        "naive_memory": {
          "data_id": "7de422b8-8606-50c3-951a-17a00330ff96",
          "dataset_id": "4171df75-d3af-5b67-8917-74145f025f5d"
        }
      }
    }
  }
]
```

## Results

| Q | Kind | Dataset | Cites Retracted | Control Retained | Correctness | References |
|---|---|---|---:|---:|---|---|
| Q01 | retracted | naive_memory | True | False | skipped_gemini_quota_fallback | R001, R001, R011, R012, R015 |
| Q01 | retracted | groundtruth_memory | False | False | skipped_gemini_quota_fallback | R001, R015, R018, R020, R022 |
| Q02 | retracted | naive_memory | True | False | skipped_gemini_quota_fallback | R002, R002 |
| Q02 | retracted | groundtruth_memory | False | False | skipped_gemini_quota_fallback | R002 |
| Q03 | retracted | naive_memory | True | False | skipped_gemini_quota_fallback | R003, R003, C003, C012, R015 |
| Q03 | retracted | groundtruth_memory | False | False | skipped_gemini_quota_fallback | R003, C003, C012, R015, R019 |
| Q04 | retracted | naive_memory | True | False | skipped_gemini_quota_fallback | R004, R004, R022, R023, C002 |
| Q04 | retracted | groundtruth_memory | False | False | skipped_gemini_quota_fallback | R004, R022, R023, C002, C011 |
| Q05 | retracted | naive_memory | True | False | skipped_gemini_quota_fallback | R005, R005, R012, R024, C002 |
| Q05 | retracted | groundtruth_memory | False | False | skipped_gemini_quota_fallback | R005, R024, C002, R012 |
| Q06 | retracted | naive_memory | True | False | skipped_gemini_quota_fallback | R006, R006, R012, R019, R022 |
| Q06 | retracted | groundtruth_memory | False | False | skipped_gemini_quota_fallback | R006, R019, R022, R023, C007 |
| Q07 | retracted | naive_memory | True | False | skipped_gemini_quota_fallback | R007, R007, R008, R008 |
| Q07 | retracted | groundtruth_memory | False | False | skipped_gemini_quota_fallback | R007, R008 |
| Q08 | retracted | naive_memory | True | False | skipped_gemini_quota_fallback | R008, R008, R016, R018 |
| Q08 | retracted | groundtruth_memory | False | False | skipped_gemini_quota_fallback | R008, R016, R018 |
| Q09 | retracted | naive_memory | True | False | skipped_gemini_quota_fallback | R009, R009 |
| Q09 | retracted | groundtruth_memory | False | False | skipped_gemini_quota_fallback | R009 |
| Q10 | retracted | naive_memory | True | False | skipped_gemini_quota_fallback | R010, R010, R003, C007, C011 |
| Q10 | retracted | groundtruth_memory | False | False | skipped_gemini_quota_fallback | R010, C007, C011, R003 |
| Q11 | retracted | naive_memory | True | False | skipped_gemini_quota_fallback | R011, R011, R018, R020, R001 |
| Q11 | retracted | groundtruth_memory | False | False | skipped_gemini_quota_fallback | R011, R018, R020, R015, R022 |
| Q12 | retracted | naive_memory | True | False | skipped_gemini_quota_fallback | R012, R012 |
| Q12 | retracted | groundtruth_memory | False | False | skipped_gemini_quota_fallback | R012 |
| Q13 | control | naive_memory | False | True | skipped_gemini_quota_fallback | C001, C013, C004, C005, C012 |
| Q13 | control | groundtruth_memory | False | True | skipped_gemini_quota_fallback | C001, C013, C004, C005, C012 |
| Q14 | control | naive_memory | False | True | skipped_gemini_quota_fallback | C002, C004, C010, C008, C011 |
| Q14 | control | groundtruth_memory | False | True | skipped_gemini_quota_fallback | C002, C004, C010, C008, C011 |
| Q15 | control | naive_memory | True | False | skipped_gemini_quota_fallback | C003, R003, C012, R003, R006 |
| Q15 | control | groundtruth_memory | False | True | skipped_gemini_quota_fallback | C003, C012, R003, R019, R021 |
| Q16 | control | naive_memory | False | True | skipped_gemini_quota_fallback | C004, C002, C010, C015, C001 |
| Q16 | control | groundtruth_memory | False | True | skipped_gemini_quota_fallback | C004, C002, C010, C015, C001 |
| Q17 | control | naive_memory | True | False | skipped_gemini_quota_fallback | C005, C001, C013, R006, R021 |
| Q17 | control | groundtruth_memory | False | True | skipped_gemini_quota_fallback | C005, C001, C013, R021, C003 |
| Q18 | mixed | naive_memory | True | False | skipped_gemini_quota_fallback | C003, R001, R003, C012, R001 |
| Q18 | mixed | groundtruth_memory | False | False | skipped_gemini_quota_fallback | C003, C012, R001, R003, R019 |
| Q19 | mixed | naive_memory | True | False | skipped_gemini_quota_fallback | C004, R005, C002, C008, C010 |
| Q19 | mixed | groundtruth_memory | False | False | skipped_gemini_quota_fallback | C004, C002, C008, C010, C011 |
| Q20 | mixed | naive_memory | True | False | skipped_gemini_quota_fallback | R003, C001, R003, C013, R006 |
| Q20 | mixed | groundtruth_memory | False | False | skipped_gemini_quota_fallback | C001, R003, C013, R015, C002 |

## Raw Results

Raw JSON: `C:/Users/gudma/OneDrive/Desktop/GITHUB-FILES/groundtruth/data/benchmark_results.json`
