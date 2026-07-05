# GroundTruth — Web Redesign Spec (single-page dashboard → professional multi-page product site)

**Why this exists.** The current web UI fails the owner's standard and normal professional practice: every core feature (ask/compare, controls, briefing, timeline) is stacked into ONE scrolling `index.html`. A professional product site has a **landing page** that tells a first-time visitor what the product is, and routes into **dedicated pages per concern** with shared nav. The current palette (parchment vellum/gilt/crimson on brown-black) reads muddy and dated, and the declared fonts (`Sohne`, `Geist`, `Source Serif 4`) are **never loaded** — only one `@import` exists in `styles.css` (verify which), so most text falls back to system fonts. This spec replaces all of it.

**Non-negotiables carried over:** provider lock (no LLM changes needed here — this is UI work), no AI attribution, tests green at the end, commit incrementally, do not publish/deploy/submit. All existing backend functionality must keep working.

---

## 1. Architecture (the core fix)

**⚠ Route collision warning (verified against `web/app.py`):** the API already owns `POST /ask`, `GET /briefing`, `GET /contested`, `GET /timeline`, `GET /graph`, `GET /state`, `POST /retract`, `POST /feedback`, `POST /improve`, `POST /adjudicate`. Page routes MUST NOT collide with these.

**Fix: move ALL JSON/API endpoints under `/api/*`** (`/api/ask`, `/api/briefing`, `/api/timeline`, `/api/contested`, `/api/adjudicate`, `/api/retract`, `/api/state`, `/api/feedback`, `/api/improve`; keep `GET /graph` HTML at `/api/graph` or `/graph-embed`). Update `web/static/app.js` fetches and **`tests/test_web.py`** accordingly — the test suite must pass after the move.

**Pages (server-rendered thin HTML shells + shared assets):**

| Route | Page | Content |
|---|---|---|
| `/` | **Landing** | Marketing-grade intro. NO app widgets. Hero + narrative + feature cards + benchmark proof + CTA into the app. |
| `/ask` | Ask / Compare | The side-by-side naive-vs-GroundTruth answer view + retraction trigger timeline (current query band + answer grid + retract control, redesigned). |
| `/briefing` | Morning Briefing | Learned / contested / revised / purged panels + "run briefing" action. |
| `/contested` | Contested Queue | Contested pairs list + adjudicate actions + feedback/improve controls. |
| `/timeline` | Belief Timeline | Time-travel diff: answer-then vs answer-now + added/contested/revised/purged columns. |
| `/evidence` | Evidence & Benchmarks | Benchmark tables (V2 + MemoryRot if committed), provenance graph embed, links to RESULTS docs. Turns our honest-numbers discipline into a visible feature. |

Every page: shared `<header>` nav (logo + the 5 app links + GitHub link) with **active-state highlighting**, shared footer (one line: project name, hackathon, GitHub). One shared `styles.css` + one `app.js` (page-specific code branches on `document.body.dataset.page`). FastAPI serves each page at its clean route (`@app.get("/ask")` → `ask.html`, etc.).

## 2. Design system (replaces the parchment look entirely)

**Style: precision dark — developer-tool grade.** Think Linear/Vercel-class: deep neutral surfaces, one confident accent, generous whitespace, crisp 1px borders. No parchment, no gradients-everywhere, no glassmorphism.

**Color tokens (exact — replace `:root` in `styles.css`):**
```css
--bg: #0B1220;          /* page background, near-black blue */
--surface: #111A2C;     /* cards/panels */
--surface-2: #16213A;   /* raised/hover surfaces */
--border: #24314D;      /* 1px hairlines */
--text: #E8EDF6;        /* primary text (≥4.5:1 on all surfaces) */
--text-muted: #94A3B8;  /* secondary text (≥3:1) */
--accent: #38BDF8;      /* ONE brand accent (sky) — links, active nav, primary CTA, focus rings */
--accent-strong: #0EA5E9;
--ok: #34D399;          /* FUNCTIONAL only: verified/active beliefs */
--warn: #FBBF24;        /* FUNCTIONAL only: contested */
--danger: #F87171;      /* FUNCTIONAL only: retracted/purged/cites-retracted */
```
Rules: `--accent` is the only decorative color. Green/amber/red are **semantic belief-state colors only** — never decoration, and never color-alone (always pair with a label or icon). All text/background pairs must meet 4.5:1 (check `--text-muted` usage on `--surface-2`).

**Typography (actually load it — current site doesn't):**
```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
--ui: 'Inter', system-ui, sans-serif;       /* everything */
--mono: 'JetBrains Mono', monospace;        /* DOIs, hashes, evidence refs, numbers, badges */
```
Type scale: 14 (labels/badges, mono, uppercase +0.08em tracking) / 16 body / 18 lead / 24 h3 / 32 h2 / clamp(40px→64px) hero h1 with -0.02em tracking, weight 700. Line-height 1.6 body, 1.1 headings. Tabular numerals for all metrics.

**Spacing & shape:** 4/8px scale only (8/12/16/24/32/48/64/96). Max content width 1152px, centered. Cards: `--surface`, 1px `--border`, radius 12px, NO drop shadows (borders do the separation on dark). Sticky top nav 64px, `--bg` at 85% opacity + `backdrop-filter: blur(8px)`, 1px bottom border.

**Icons:** inline SVG only (Lucide, stroke 1.75, 20px). NO emoji anywhere in the UI. Belief states get consistent icon+color pairs: active=check-circle/`--ok`, contested=alert-triangle/`--warn`, superseded=history/`--text-muted`, retracted/purged=x-octagon/`--danger`.

**Motion:** 150–250ms ease-out micro-transitions on hover/focus/panel-reveal only; `transform`/`opacity` only; honor `prefers-reduced-motion`. Skeleton shimmer (not spinners) for any fetch >300ms.

## 3. The landing page (`/`) — section by section

Pattern: product-demo landing. Order:

1. **Nav** — wordmark "GroundTruth" (Inter 700) + links (How it works, Live demo pages, Evidence, GitHub) + primary CTA button "Open the app" → `/ask`.
2. **Hero** — headline: **"Most agents wake up with amnesia. Ours wakes up knowing what it must unlearn."** Subline (1 sentence): "GroundTruth is a belief-maintenance memory layer built on Cognee — beliefs carry evidence, get contested, superseded, and surgically forgotten." Two CTAs: primary "See it unlearn →" (`/ask`), secondary ghost "Read the evidence" (`/evidence`). Below: a **static side-by-side teaser card** (pre-rendered from real data, not live fetch): naive memory citing a retracted study (red badge) vs GroundTruth citing the retraction notice (green badge). This one visual must communicate the whole product in 5 seconds.
3. **Problem strip** — 3 short cards: "Memory only grows" / "Facts rot: retractions, CVEs, reversals" / "Your agent keeps citing them."
4. **How it works** — the 4-verb lifecycle as a horizontal 4-step diagram: `remember` (evidence in) → `recall` (belief-annotated answers) → `improve` (contested → adjudicated, session → permanent) → `forget` (surgical, per-claim). Each step: icon, verb in mono, one sentence, file reference in small mono text.
5. **Evidence ladder** — 3-tier visual: authority feed > semantic inference > user assertion, one line each.
6. **Proof band** — the honest numbers as big stat tiles (pull the exact current values from `docs/BENCHMARK.md` — do not hardcode stale ones): retracted-citation rate naive vs GroundTruth, coverage 25/25, controls 5/5, semantic P/R with sample size stated. Caption links to `/evidence`.
7. **Feature grid** — 4 cards linking to the 4 app pages (Briefing, Contested, Timeline, Ask), each with a 1-sentence value line.
8. **Footer** — hackathon credit line, Cognee link, GitHub link, AI-usage disclosure link.

Copy tone: confident, concrete, zero hype-words ("revolutionary", "game-changing" banned). Every claim on the landing page must be true of the committed code.

## 4. App pages — shared rules

- Each page: h1 + one-line description (so a judge landing mid-app knows where they are), then the content. No page renders another page's widgets.
- **Empty states**: every panel that can be empty gets a message + the action that fills it ("No contested beliefs. Trigger a retraction on Ask → or run the briefing.").
- **Loading**: skeleton blocks matching final layout (no CLS). **Errors**: inline message + Retry button — never a silent dead panel, never a raw JSON error.
- All buttons ≥44px tall, visible focus ring (`--accent`, 2px offset), `cursor: pointer`, disabled state at 0.45 opacity during async ops with in-button spinner.
- Belief-state badges everywhere a claim/reference is shown: mono 12px uppercase pill, icon + label + state color at 12% background tint.
- The naive vs GroundTruth compare on `/ask` is THE demo view: two equal columns (stack on mobile), red "cites retracted" banner on naive when true, green "clean citations" on GroundTruth, references as cards with DOI in mono + state badge. The retraction trigger + streaming timeline stays on this page, restyled as a vertical step log.

## 5. Responsive & a11y gates

- Breakpoints 375 / 768 / 1024 / 1440. Mobile: nav collapses to a simple disclosure menu (no framework), columns stack, no horizontal scroll anywhere.
- Semantic landmarks (`header/nav/main/footer`), h1→h2→h3 order, `aria-label` on icon-only buttons, keyboard-reachable everything, focus visible always.
- `<title>` + meta description per page ("GroundTruth — memory that unlearns" etc.). Add an `og:title`/`og:description` block; generate a simple `og-image` only if trivial, skip otherwise.

## 6. Deliverables & gates (audit will check these literally)

1. Six pages live at clean routes; API moved to `/api/*`; **full pytest suite green** (test_web.py updated); `git grep` shows no dead references to old API paths.
2. Old single-page layout gone; `index.html` is the landing page only.
3. Fonts actually load (network tab / `@import` present once); no `Sohne`/`Geist`/parchment tokens left in `styles.css`.
4. No emoji icons; SVG only. No color-only state signaling.
5. Every landing-page number matches `docs/BENCHMARK.md` / RESULTS docs at commit time.
6. Screenshots of all 6 pages at 1440px + 375px saved to `docs/screenshots/` (Playwright if available, else manual instructions in the RESULTS doc).
7. `docs/RESULTS-REDESIGN.md`: what changed, route map old→new, palette/type tokens, screenshot index, pytest output.
8. Commit incrementally: (a) API move + tests, (b) shared shell/design system, (c) landing, (d) app pages, (e) polish + screenshots + results doc.

**Do NOT:** add a JS framework/build step (stay vanilla), add auth, add light mode (dark only), touch the Python engine (`groundtruth/*`) except `web/app.py` routing, or invent new metrics for the landing page.
