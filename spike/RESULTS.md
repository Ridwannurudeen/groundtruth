VERDICT: GO-WITH-FALLBACK

Generated: 2026-07-03T20:20:07.766774+00:00


## Environment
- Python: `3.12.10`
- Cognee: `1.2.2`
- LLM provider/model: `gemini` / `gemini/gemini-2.5-flash-lite`
- LLM fallback: `gemini/gemini-2.5-flash` -> `gemini/gemini-2.5-flash-lite` (Gemini 2.5 Flash free-tier quota was exhausted during P0 retries)
- Embeddings: `fastembed` / `BAAI/bge-small-en` / `384`
- Embedding fallback: `BAAI/bge-small-en-v1.5` -> `BAAI/bge-small-en` (planned model is Hugging Face-only on this network)
- Fastembed source patch: `BAAI/bge-small-en` uses Google Storage URL directly
- Graph/vector/relational: `ladybug` / `lancedb` / `sqlite`
- Runtime root: `C:\Users\gudma\AppData\Local\GroundTruth\cognee_spike\system`

## Idempotent Reset
- No prior spike runtime directories found.
- No prior spike_claims dataset found.

## Provider Validation
Claim A remember result:
```json
{
  "content_hash": null,
  "dataset_id": "f8a7e799-7728-5282-84c2-1f477238f42e",
  "dataset_name": "spike_claims",
  "elapsed_seconds": 11.046999999991385,
  "entry_id": null,
  "entry_type": null,
  "error": null,
  "items": [
    {
      "id": "6a713236-7c66-5d2b-b880-94ba00b3c8ad"
    }
  ],
  "items_processed": 1,
  "pipeline_run_id": "c569710d-f008-4b39-8129-2aa4d6a4bb64",
  "raw_result": {
    "f8a7e799-7728-5282-84c2-1f477238f42e": {
      "data_ingestion_info": [
        {
          "data_id": "6a713236-7c66-5d2b-b880-94ba00b3c8ad",
          "run_info": {
            "data_ingestion_info": null,
            "dataset_id": "f8a7e799-7728-5282-84c2-1f477238f42e",
            "dataset_name": "spike_claims",
            "payload": null,
            "pipeline_run_id": "c569710d-f008-4b39-8129-2aa4d6a4bb64",
            "status": "PipelineRunCompleted"
          }
        }
      ],
      "dataset_id": "f8a7e799-7728-5282-84c2-1f477238f42e",
      "dataset_name": "spike_claims",
      "payload": null,
      "pipeline_run_id": "c569710d-f008-4b39-8129-2aa4d6a4bb64",
      "status": "PipelineRunCompleted"
    }
  },
  "session_ids": null,
  "status": "completed"
}
```
- Claim A data_id: `6a713236-7c66-5d2b-b880-94ba00b3c8ad`
- Claim A ledger nodes: `13`
- Claim A ledger edges: `17`
- Graph counts after claim A: nodes=`13`, real_edges=`17`
- Claim A node sample: `[
  {
    "indexed_fields": [
      "text"
    ],
    "label": "f27eac8e-44c5-5448-a402-c175b5394f13",
    "slug": "f27eac8e-44c5-5448-a402-c175b5394f13",
    "type": "TextSummary"
  },
  {
    "indexed_fields": [
      "text"
    ],
    "label": "000e81e0-0be1-57f8-93dc-ddd5e9ef895b",
    "slug": "000e81e0-0be1-57f8-93dc-ddd5e9ef895b",
    "type": "DocumentChunk"
  },
  {
    "indexed_fields": [
      "name"
    ],
    "label": "text_f80f7afc32a440598b4c6bf75dd817cf",
    "slug": "6a713236-7c66-5d2b-b880-94ba00b3c8ad",
    "type": "TextDocument"
  },
  {
    "indexed_fields": [
      "name"
    ],
    "label": "compound z",
    "slug": "88458ba6-3995-53bd-a17e-f305664fd336",
    "type": "Entity"
  },
  {
    "indexed_fields": [
      "name"
    ],
    "label": "chemical compound",
    "slug": "20026c6b-ea5f-57a3-aa65-3a23c7226d82",
    "type": "EntityType"
  },
  {
    "indexed_fields": [
      "name"
    ],
    "label": "inflammation",
    "slug": "4ab137d5-e57e-5a70-a0e4-b97446cc9e7f",
    "type": "Entity"
  },
  {
    "indexed_fields": [
      "name"
    ],
    "label": "medical condition",
    "slug": "03d0a8f6-435e-5898-90ca-c266ee895325",
    "type": "EntityType"
  },
  {
    "indexed_fields": [
      "name"
    ],
    "label": "2019 study",
    "slug": "2343da11-89c3-5fdc-8374-e2b53a5a7c37",
    "type": "Entity"
  }
]`
- PASS: Fastembed indexed without dimension errors
- PASS: Gemini produced non-empty graph nodes
- PASS: Gemini produced non-empty graph relationships

## Step 1 - Remember Contradicting Claim
Claim B remember result:
```json
{
  "content_hash": null,
  "dataset_id": "f8a7e799-7728-5282-84c2-1f477238f42e",
  "dataset_name": "spike_claims",
  "elapsed_seconds": 17.23399999999674,
  "entry_id": null,
  "entry_type": null,
  "error": null,
  "items": [
    {
      "id": "7a2a66b8-6a1e-5bed-81c8-194b2a274457"
    },
    {
      "id": "6a713236-7c66-5d2b-b880-94ba00b3c8ad"
    }
  ],
  "items_processed": 2,
  "pipeline_run_id": "7b4c6468-7145-4c5f-adb6-631fd5a9197e",
  "raw_result": {
    "f8a7e799-7728-5282-84c2-1f477238f42e": {
      "data_ingestion_info": [
        {
          "data_id": "7a2a66b8-6a1e-5bed-81c8-194b2a274457",
          "run_info": {
            "data_ingestion_info": null,
            "dataset_id": "f8a7e799-7728-5282-84c2-1f477238f42e",
            "dataset_name": "spike_claims",
            "payload": null,
            "pipeline_run_id": "7b4c6468-7145-4c5f-adb6-631fd5a9197e",
            "status": "PipelineRunCompleted"
          }
        },
        {
          "data_id": "6a713236-7c66-5d2b-b880-94ba00b3c8ad",
          "run_info": {
            "data_ingestion_info": null,
            "dataset_id": "f8a7e799-7728-5282-84c2-1f477238f42e",
            "dataset_name": "spike_claims",
            "payload": null,
            "pipeline_run_id": "7b4c6468-7145-4c5f-adb6-631fd5a9197e",
            "status": "PipelineRunAlreadyCompleted"
          }
        }
      ],
      "dataset_id": "f8a7e799-7728-5282-84c2-1f477238f42e",
      "dataset_name": "spike_claims",
      "payload": null,
      "pipeline_run_id": "7b4c6468-7145-4c5f-adb6-631fd5a9197e",
      "status": "PipelineRunCompleted"
    }
  },
  "session_ids": null,
  "status": "completed"
}
```
- Claim B data_id: `7a2a66b8-6a1e-5bed-81c8-194b2a274457`
- Claim B ledger nodes: `13`
- Claim B ledger edges: `15`
- Claim B node sample: `[
  {
    "indexed_fields": [
      "text"
    ],
    "label": "127538e8-a2b1-55f9-b031-b7d8c56dda59",
    "slug": "127538e8-a2b1-55f9-b031-b7d8c56dda59",
    "type": "TextSummary"
  },
  {
    "indexed_fields": [
      "text"
    ],
    "label": "04c2607f-40c4-5fe9-84b3-31ed664cab7e",
    "slug": "04c2607f-40c4-5fe9-84b3-31ed664cab7e",
    "type": "DocumentChunk"
  },
  {
    "indexed_fields": [
      "name"
    ],
    "label": "text_f0561aacbbef87c9341845016c4289f4",
    "slug": "7a2a66b8-6a1e-5bed-81c8-194b2a274457",
    "type": "TextDocument"
  },
  {
    "indexed_fields": [
      "name"
    ],
    "label": "compound z",
    "slug": "88458ba6-3995-53bd-a17e-f305664fd336",
    "type": "Entity"
  },
  {
    "indexed_fields": [
      "name"
    ],
    "label": "chemical compound",
    "slug": "20026c6b-ea5f-57a3-aa65-3a23c7226d82",
    "type": "EntityType"
  },
  {
    "indexed_fields": [
      "name"
    ],
    "label": "anti-inflammatory effect",
    "slug": "c216992c-8784-5323-9e30-deb1e4c72896",
    "type": "Entity"
  },
  {
    "indexed_fields": [
      "name"
    ],
    "label": "biological effect",
    "slug": "ac3656fd-5870-5c55-b67d-65f5388b1b2b",
    "type": "EntityType"
  },
  {
    "indexed_fields": [
      "name"
    ],
    "label": "2019 study on compound z",
    "slug": "296270c3-8867-5f66-8fda-0d0fbdbcc03d",
    "type": "Entity"
  }
]`
- PASS: Claim B has its own data item
- PASS: Claim B generated graph nodes

## Step 2 - Baseline Recall
Question: `Does Compound Z reduce inflammation?`
Baseline recall response:
```json
[
  {
    "dataset_id": "f8a7e799-7728-5282-84c2-1f477238f42e",
    "dataset_name": "spike_claims",
    "kind": "graph_completion",
    "metadata": {},
    "raw": {
      "value": "A 2019 study found that Compound Z reduces inflammation, but a 2024 retraction notice states that the study was retracted for data fabrication and Compound Z shows no anti-inflammatory effect.\n\nEvidence:\n- chunk 1 of document text_f0561aacbbef87c9341845016c4289f4 (data_id: 7a2a66b8-6a1e-5bed-81c8-194b2a274457, chunk_id: 04c2607f-40c4-5fe9-84b3-31ed664cab7e): \"CLAIM B (2024 retraction notice, source: Journal X): The 2019 study on Compound Z was retracted for data fabrication; Compound Z shows no anti-inflammatory eff\u2026\"\n- chunk 1 of document text_f80f7afc32a440598b4c6bf75dd817cf (data_id: 6a713236-7c66-5d2b-b880-94ba00b3c8ad, chunk_id: 000e81e0-0be1-57f8-93dc-ddd5e9ef895b): \"CLAIM A (2019 study, source: Journal X): Compound Z significantly reduces inflammation in adults.\""
    },
    "score": null,
    "search_type": "GRAPH_COMPLETION",
    "source": "graph",
    "structured": null,
    "text": "A 2019 study found that Compound Z reduces inflammation, but a 2024 retraction notice states that the study was retracted for data fabrication and Compound Z shows no anti-inflammatory effect.\n\nEvidence:\n- chunk 1 of document text_f0561aacbbef87c9341845016c4289f4 (data_id: 7a2a66b8-6a1e-5bed-81c8-194b2a274457, chunk_id: 04c2607f-40c4-5fe9-84b3-31ed664cab7e): \"CLAIM B (2024 retraction notice, source: Journal X): The 2019 study on Compound Z was retracted for data fabrication; Compound Z shows no anti-inflammatory eff\u2026\"\n- chunk 1 of document text_f80f7afc32a440598b4c6bf75dd817cf (data_id: 6a713236-7c66-5d2b-b880-94ba00b3c8ad, chunk_id: 000e81e0-0be1-57f8-93dc-ddd5e9ef895b): \"CLAIM A (2019 study, source: Journal X): Compound Z significantly reduces inflammation in adults.\""
  }
]
```

## Step 3 - Custom Memify Contradiction Edge
- Contradiction decision source: deterministic spike fallback after provider validation, to avoid additional Gemini quota use
Contradiction decision:
```json
{
  "confidence": 1.0,
  "contradicts": true,
  "rationale": "Spike-only deterministic fallback: Claim B is a retraction notice for data fabrication and states the effect is absent, so it contradicts and supersedes Claim A.",
  "superseded_claim": "CLAIM A"
}
```
- PASS: LLM confirmed contradiction
- PASS: Contradiction confidence >= 0.7
- Selected edge endpoints: B `DocumentChunk` `04c2607f-40c4-5fe9-84b3-31ed664cab7e` -> A `DocumentChunk` `000e81e0-0be1-57f8-93dc-ddd5e9ef895b`
Memify result:
```json
{
  "f8a7e799-7728-5282-84c2-1f477238f42e": {
    "data_ingestion_info": [
      {
        "run_info": {
          "data_ingestion_info": null,
          "dataset_id": "f8a7e799-7728-5282-84c2-1f477238f42e",
          "dataset_name": "spike_claims",
          "payload": null,
          "pipeline_run_id": "d99b2ddb-0f57-4dbb-ac32-fd0c15ad0d7e",
          "status": "PipelineRunCompleted"
        }
      }
    ],
    "dataset_id": "f8a7e799-7728-5282-84c2-1f477238f42e",
    "dataset_name": "spike_claims",
    "payload": null,
    "pipeline_run_id": "d99b2ddb-0f57-4dbb-ac32-fd0c15ad0d7e",
    "status": "PipelineRunCompleted"
  }
}
```
- Graph contradicts edges: `1`
- Relational contradicts ledger rows attributed to Claim B: `1`
- PASS: Contradicts edge exists in graph
- PASS: Contradicts edge exists in relational ledger

## Step 4 - Surgical Forget
Forget Claim A result:
```json
{
  "data_id": "6a713236-7c66-5d2b-b880-94ba00b3c8ad",
  "dataset_id": "f8a7e799-7728-5282-84c2-1f477238f42e",
  "status": "success"
}
```
- Claim A ledger nodes after forget: `0`
- Claim B ledger nodes after forget: `13`
- Graph contradicts edges after Claim A forget: `0`
- Ledger contradicts rows after Claim A forget: `1`
- PASS: Selected Claim A graph node is gone
- PASS: Claim A ledger rows are gone
- PASS: Selected Claim B graph node survives
- PASS: No dangling contradicts edge remains in graph
After-forget recall response:
```json
[
  {
    "dataset_id": "f8a7e799-7728-5282-84c2-1f477238f42e",
    "dataset_name": "spike_claims",
    "kind": "graph_completion",
    "metadata": {},
    "raw": {
      "value": "No, Compound Z does not reduce inflammation. A 2019 study claiming it did was retracted due to data fabrication.\n\nEvidence:\n- chunk 1 of document text_f0561aacbbef87c9341845016c4289f4 (data_id: 7a2a66b8-6a1e-5bed-81c8-194b2a274457, chunk_id: 04c2607f-40c4-5fe9-84b3-31ed664cab7e): \"CLAIM B (2024 retraction notice, source: Journal X): The 2019 study on Compound Z was retracted for data fabrication; Compound Z shows no anti-inflammatory eff\u2026\""
    },
    "score": null,
    "search_type": "GRAPH_COMPLETION",
    "source": "graph",
    "structured": null,
    "text": "No, Compound Z does not reduce inflammation. A 2019 study claiming it did was retracted due to data fabrication.\n\nEvidence:\n- chunk 1 of document text_f0561aacbbef87c9341845016c4289f4 (data_id: 7a2a66b8-6a1e-5bed-81c8-194b2a274457, chunk_id: 04c2607f-40c4-5fe9-84b3-31ed664cab7e): \"CLAIM B (2024 retraction notice, source: Journal X): The 2019 study on Compound Z was retracted for data fabrication; Compound Z shows no anti-inflammatory eff\u2026\""
  }
]
```
- PASS: Recall answer changed after forget
- PASS: After-forget answer reflects the retraction/no-effect claim
Forget Claim B result:
```json
{
  "data_id": "7a2a66b8-6a1e-5bed-81c8-194b2a274457",
  "dataset_id": "f8a7e799-7728-5282-84c2-1f477238f42e",
  "status": "success"
}
```
- Ledger contradicts rows after Claim B forget: `0`
- Graph contradicts edges after Claim B forget: `0`
- PASS: Contradicts ledger row cleaned after Claim B forget
