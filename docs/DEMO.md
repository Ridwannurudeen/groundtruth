# GroundTruth Demo Script

## Run

```powershell
$env:PYTHONIOENCODING='utf-8'; .\.venv\Scripts\uvicorn.exe web.app:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000`.

The fixed corpus has already processed all 25 held-back retractions. For the
live retraction timeline in steps 3-5, start from a fresh ingest/reset where
`active_retractions` is non-empty.

## Click Path

1. Let the default question load and click `Ask Both`.
2. Point out the side-by-side split: naive memory shows `cites retracted`; GroundTruth shows `clean citations`.
3. In `Retraction wire`, keep the first active DOI selected and click `Retract`.
4. Watch the timeline advance through `detected`, `running`, `contradiction_found`, `forgotten`, and `complete`.
5. After the automatic re-ask, compare the same side-by-side panels again: GroundTruth no longer cites the forgotten original, while naive memory keeps the retracted source.
6. Click `Open Graph` to show Cognee's global memory-provenance graph. Describe it as the whole memory graph, not answer-level provenance; answer citations are the reference rows in the two panels.
7. On the GroundTruth panel, click `Downvote`, then `Improve`. The feedback loop stores the session feedback, runs Cognee's improve path, and re-asks with `feedback_influence=1`.

## Presenter Notes

- Benchmark headline: naive memory retrieves retracted originals in 19/20 answers; GroundTruth retrieves them in 0/20.
- Control retention: 5/5 active controls remain available.
- Retraction coverage: 25/25 retracted-cohort originals are forgotten from GroundTruth.
- Correctness judge is intentionally skipped because the Gemini free-tier quota is exhausted; the primary metric is retrieved graph context containing a still-present retracted original.
