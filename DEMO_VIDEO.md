# GroundTruth — Demo Video Package (≤3 min, submission-format)

Structured to the required sections: **About · Tech stack & architecture · Demo · Learning**. Everything is **verified against the live site** (https://groundtruth.gudman.xyz) on 2026-07-05 — every shot produces exactly what the narration says. Target **~2:50**.

---

## WHAT I NEED FROM YOU (to produce the MP4)

I can't press record or render video myself. Pick either path:

1. **Screen-record + AI voiceover (recommended, works everywhere):** you (or an AI screen-agent) click through the SHOT LIST while screen-recording at **1920×1080** (hide the bookmarks bar, 100% zoom fits the app). Then paste the **NARRATION** into any AI voice tool (ElevenLabs, Play.ht, CapCut AI voice, HeyGen) and lay the audio over the capture, matching each block to its shot.
2. **Avatar tool (HeyGen/Synthesia):** tell me and I'll re-cut this as a talking-head script + b-roll list.

The site is live and stable — no setup. **Do NOT click the "Retract" button on /ask during recording** (that live flow is disabled on the deployed memory); the demo uses the already-correct before/after, which is instant and stronger.

Also: the **submission must disclose AI-assistant use** (hackathon rule) — content is in `docs/AI_USAGE.md`.

---

## NARRATION (word-for-word, ~370 words ≈ 2:50 at a calm pace)

> **— ABOUT THE PROJECT —**
> Every AI system that remembers has the same flaw: it only ever *adds*. It never unlearns. So when a scientific paper is retracted for fraud, your AI keeps citing it, confidently, forever. GroundTruth is a memory layer that fixes this — memory that knows when it's wrong, and corrects itself.
>
> **— TECH STACK & ARCHITECTURE —**
> GroundTruth is built on **Cognee**, an open-source memory engine, and it leans on Cognee's full lifecycle: **remember** to ingest claims and evidence into a hybrid graph-and-vector store, **recall** to answer with citations, **improve** to enrich and reweight, and **forget** to surgically remove a fact. Around that, we built a **belief-maintenance layer**: every claim carries a belief state — active, contested, superseded, or retracted — and an evidence ladder that ranks an authoritative retraction above an AI's own inference above a user's assertion. The stack is a FastAPI backend and a lightweight multi-page frontend, running fully self-hosted — local embeddings with Fastembed, Google Gemini for reasoning, and Cognee's graph-vector store underneath. No black boxes.
>
> **— DEMO —**
> Here's the same question asked to two memories. On the left, a normal append-only memory. On the right, GroundTruth. Watch the badges. The normal memory still cites the retracted study — flagged unsafe. GroundTruth forgot it, and cites the retraction notice instead. Same engine, same data — one just knows how to unlearn. And it's not only formal retractions: GroundTruth detects when two claims genuinely contradict — here, two studies disagree on whether omega-3 protects the heart — and marks the belief contested, with the evidence attached. Every change is auditable — a morning briefing of what it learned and purged, and a timeline of what it believed then versus now. And we measured it: on a twenty-question benchmark, a naive memory cited retracted science eighteen times; GroundTruth, zero — while keeping every legitimate source. Twenty-five of twenty-five retractions, unlearned.
>
> **— LEARNING & GROWTH —**
> The lesson: the easy part is remember and recall. The hard, interesting part is making *forget* and contradiction-detection actually load-bearing — and measuring it honestly instead of chasing a flashy number. Memory that knows when it's wrong. GroundTruth — built on Cognee.

---

## SHOT LIST (screen actions synced to each narration section)

| # | ~Time | Section | On screen — do exactly this | 
|---|-------|---------|------------------------------|
| 1 | 0:00–0:22 | **About** | Open **https://groundtruth.gudman.xyz** . Hold on the hero ("Most agents wake up with amnesia…"), then scroll so the red/green **side-by-side teaser card** (top-right) shows briefly. |
| 2 | 0:22–1:05 | **Tech / architecture** | Scroll down the **landing page** through the **"How it works"** row — the four cards **remember · recall · improve · forget** (each shows its purpose + the real source file). Continue to the **evidence-ladder** line (authority feed › semantic inference › user assertion). Let each card sit ~2s. |
| 3 | 1:05–1:35 | **Demo — the proof** | Click **"Ask"** in the nav. The question is **pre-filled**. Click **"Ask both."** Wait ~2s. **Hold on the badges:** left = red **"CITES RETRACTED"**, right = green **"CLEAN CITATIONS."** Zoom/point to each. *(This is the money shot — give it the most time.)* |
| 4 | 1:35–1:55 | **Demo — contested** | Click **"Contested."** Show the **1 open contested pair** (marine omega-3 / cardiovascular). Scroll so both conflicting titles + the basis text are readable. |
| 5 | 1:55–2:15 | **Demo — audit** | Click **"Briefing"** → **"Generate from latest projection"** (show Learned/Contested/Revised/Purged). Then **"Timeline"** briefly (then-vs-now columns). |
| 6 | 2:15–2:38 | **Demo — proof** | Click **"Evidence."** Hold on the stat tiles: **naive 18/20**, **GroundTruth 0/20**, **coverage 25/25**, **controls 5/5**. Optional: flash the **provenance graph** link. |
| 7 | 2:38–2:50 | **Learning / close** | Return to the landing page (**/**), end on the hero. Fade out. |

---

## ACCURACY NOTES (must match reality)
- **Shot 3 (red vs green badges) is the whole video.** If one frame carries it, that's the frame. Most screen time here.
- The **avacopan question auto-loads** — type nothing. If ever blank, paste: `Does avacopan remain supported for ANCA-associated vasculitis after the retraction?`
- **Numbers, all verified live — say/show exactly these:** naive **18/20**, GroundTruth **0/20**, coverage **25/25**, controls **5/5**. (Semantic detection is precision **1.00** / recall **0.67** on a 28-pair set — only if you extend; don't inflate.)
- Each page runs a live Cognee call — allow ~1–2s per navigation before content fills; don't cut too fast.
- **Verified true claims for narration:** built on Cognee (v1.2.2); uses remember/recall/improve/forget; FastAPI + multi-page JS; **Fastembed local embeddings + Google Gemini**; Cognee hybrid graph-vector store; self-hosted. Do not claim anything beyond this list.
- To hit a hard **90 seconds**: keep About (short) + Shot 3 + Shot 6 + close; drop shots 2, 4, 5.
