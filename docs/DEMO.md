# Demo Script (90 seconds)

## Objective

Show end-to-end belief maintenance: morning brief, contested adjudication, time-travel diff, then benchmark close.

## Script

### 0:00-0:10 | Hangover Open

1. Start the app:

```powershell
.\.venv\Scripts\uvicorn.exe web.app:app --host 127.0.0.1 --port 8000
```

2. Open `http://127.0.0.1:8000`.
3. Point to the top metrics line and read: `0/20` GroundTruth, `18/20` naive, `5/5` controls.

### 0:10-0:30 | Morning Briefing

1. In the page input, ask:
   `Does avacopan remain supported after retraction?`
2. Click **Ask Both** once so both memory panels render.
3. On the briefing panel, open the sections:
   - learned last night
   - now revised
   - now purged
4. Mention this is the cross-memory narrative: evening/session evidence is bridged and reflected in registry-backed state.

### 0:30-0:55 | Contested Adjudication

1. In the briefing, note one contested item is present (`V2C003::V2C004`).
2. Open the Contested list and select that pair.
3. Click a verdict path (upvote/downvote path depending on your readout) to resolve it.
4. Re-run the same omega-3 question.
5. Confirm the answer text now reflects the resolution and no longer treats the claim as contested only.

### 0:55-1:25 | Time-Travel Diff

1. Set timeline range:
   - `from`: `2026-01-01`
   - `to`: `2026-07-04`
2. Click **Timeline diff**.
3. Read:
   - timeline headers: added / contested / revised / purged
   - before-vs-now answer cards
   - basis lines showing why each transition happened.
4. Say that each row is derived from registry history and evidence classes.

### 1:25-1:30 | Benchmark Close

1. Ask one short control question again.
2. Close by reading the metric row:
   - naive cites retracted in `18/20`
   - GroundTruth cites retracted in `0/20`
   - control retention `5/5`
   - disclosure: correctness judge is quota-disclosed in this phase.

## Recorder Notes

- Keep the session tight and visible: one browser, one screen.
- Confirm all numbers against `docs/RESULTS-V3-P8.md` before recording.
