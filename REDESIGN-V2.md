# GroundTruth Redesign V2 — "Editorial Dark + Luminous Accent"

Single source of truth for the design overhaul. Every agent reads this first and builds to it exactly.

## Why we're redoing it (the honest critique of the current site)

The current site is structurally fine (real landing + 5 routed pages) but executed like a generic dev-tool template:

1. **Stacked-boxes monotony** — every section wrapped in an identical `.section-shell` (border + `#111a2c` surface + 12px radius + 20px padding). The whole page is bordered boxes inside bordered boxes. Award-winning landings separate sections with *whitespace and rhythm*, not a border around everything.
2. **Generic palette** — `#0B1220` slate + `#38BDF8` sky-blue is the default "developer SaaS" look. No signature, no depth.
3. **Flat & lifeless** — `--shadowless`, no gradients, no motion, no hero visual beyond two plain text cards.
4. **Weak hierarchy** — everything is the same weight of gray text in gray boxes.
5. **Cramped spacing** — 20px padding / 12px gaps everywhere; premium sites use far more generous vertical rhythm.
6. **Two real bugs shipped live:** footer says **"ETHGlobal project"** (this is the **WeMakeDevs × Cognee** hackathon) and every GitHub link is a placeholder `https://github.com`.

## The chosen direction (locked with the user)

**Editorial dark + luminous accent.** Near-black canvas, ONE luminous signature color (violet), generous whitespace, refined serif-display + sans pairing, subtle scroll-reveal motion. Restrained, premium, confident — Linear / Vercel / Anthropic energy. NOT flashy gradient-aurora.

## Design tokens (use these exact values)

```
/* Canvas & surfaces — depth via lightness, NOT borders everywhere */
--bg:          #08080B;   /* near-black page canvas */
--surface:     #101015;   /* raised panels (used sparingly) */
--surface-2:   #16161D;   /* nested/inner panels */
--hairline:    rgba(255,255,255,0.08);  /* thin dividers — replaces heavy borders */

/* Text */
--text:        #F5F5F7;   /* primary */
--text-muted:  #A1A1AA;   /* secondary */
--text-faint:  #6B6B76;   /* tertiary / captions */

/* Luminous accent (violet) — the ONE signature color */
--accent:        #8B7CFF;  /* primary violet */
--accent-strong: #6D5EF5;  /* pressed / bold */
--accent-glow:   rgba(139,124,255,0.35); /* radial glow, shadows */

/* Semantic (belief states — keep, but refined) */
--ok:     #4ADE80;
--warn:   #FBBF24;
--danger: #FB7185;

/* Depth */
--shadow-sm: 0 1px 2px rgba(0,0,0,0.4);
--shadow-md: 0 8px 30px rgba(0,0,0,0.5);
--shadow-glow: 0 0 60px var(--accent-glow);
```

## Typography

- **Display (h1/h2 hero + section titles):** `"Instrument Serif", Georgia, serif` — elegant editorial serif, loaded from Google Fonts. Large, tight letter-spacing.
- **UI/body:** `"Inter", system-ui, sans-serif` (already used).
- **Mono (code paths, metrics, DOIs):** `"JetBrains Mono", monospace` (already used).
- Google Fonts import line (add Instrument Serif to the existing import):
  `@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500&display=swap");`
- Hero h1: `clamp(48px, 8vw, 88px)`, serif, line-height ~1.05.
- Section h2: `clamp(30px, 4vw, 44px)`, serif.

## Layout & spacing rules

- **Kill the universal section border.** Sections are separated by generous vertical padding (`96px–128px` desktop, `64px` mobile), NOT by wrapping every one in a bordered card.
- Use bordered/surface panels ONLY where content genuinely needs containment (the app-page interactive panels, metric cards, result panels). Marketing sections (why/how/ladder) should breathe on the bare canvas with maybe a hairline divider.
- Content width: `min(1120px, calc(100vw - 48px))`.
- Section rhythm: use a `.section` with large `padding-block`, an optional `.section--divider` that adds a top hairline.

## Depth, glow & motion

- **Hero:** a soft radial violet glow behind the headline (`radial-gradient` blob, low opacity, blurred), giving the near-black canvas life. Big type on top.
- **Panels:** subtle `--shadow-md`; on hover, lift + faint accent ring (`box-shadow: var(--shadow-md), 0 0 0 1px var(--accent-glow)`).
- **Accent usage:** sparingly — primary CTA, active nav item, key numbers, one underline/keyline. Do NOT color everything violet.
- **Scroll-reveal:** fade-up on scroll via IntersectionObserver (add `.reveal` class, toggle `.is-visible`). MUST be gated behind `@media (prefers-reduced-motion: reduce)` (no motion) and must not hide content if JS fails (default visible, JS opts into hidden-then-reveal only when supported). Keep it lightweight — this goes in `app.js` in a page-agnostic init that runs on every page.
- Buttons/links: smooth 150ms transitions; primary CTA has a soft glow.

## HARD CONSTRAINTS — do not break the app

`app.js` reads element IDs and generates DOM with fixed class names. **Preserve ALL of these** (change wrappers/visuals around them, never remove the hooks):

**IDs that MUST remain (by page):**
- Nav (every page): `menuToggle`, `primary-nav`
- Ask: `question`, `askButton`, `naiveText`, `groundtruthText`, `naiveRefs`, `groundtruthRefs`, `naiveBadge`, `groundtruthBadge`, `activeCount`, `doiSelect`, `timeline`, `retractButton`, `downvoteButton`, `upvoteButton`, `improveButton`, `eventLog`
- Briefing: `briefingGeneratedAt`, `runBriefing`, `briefingLearned`, `briefingContested`, `briefingRevised`, `briefingPurged`
- Contested: `contestedList`, `contestedCount`
- Timeline: `timelineButton`, `timelineFrom`, `timelineTo`, `timelineQuestion`, `timelineAnswerThen`, `timelineAnswerNow`, `timelineThenRefs`, `timelineNowRefs`, `timelineAdded`, `timelineContested`, `timelineRevised`, `timelinePurged`
- Evidence: `metricNaive`, `metricGroundtruth`, `metricControl`, `metricCoverage`, `evidenceContestedCount`
- `<body data-page="...">` attribute MUST stay (landing/ask/briefing/contested/timeline/evidence) — `app.js` routes on it.

**Class SELECTORS that MUST stay styled (JS creates these dynamically):**
`state-badge`, `state-badge--ok`, `state-badge--warn`, `state-badge--danger`, `state-badge--muted`, `skeleton`, `skeleton-line`, `error-panel`, `ref-card`, `ref-title`, `ref-basis`, `result-text`, `briefing-item`, `contested-item`, `timeline-row`, `timeline-time`, `timeline-event`, `empty`, `muted`, `mono`, `refs`, `feedback-row`, `btn`, `btn-primary`, `btn-secondary`, `btn-ghost`, `is-open` (nav open state).

You MAY rename/restructure purely-presentational marketing markup (hero, feature grids, etc.). You may NOT remove the hooks above.

## Global fixes (Wave 1 applies to every page's shared parts)

- Footer text: **"GroundTruth — WeMakeDevs × Cognee hackathon · Built on Cognee"** (remove "ETHGlobal").
- GitHub links: point to `https://github.com/Ridwannurudeen/groundtruth` (repo not public yet, but this is the intended URL — no more bare `https://github.com`).
- Keep accessibility: skip-link, `aria-*`, focus-visible outlines, 44px min tap targets, `prefers-reduced-motion` honored.

## Verification bar (every agent)

- Page renders with no console errors.
- All JS hooks intact (grep the page for each required ID; confirm dynamic classes still have CSS rules).
- Responsive at 375 / 768 / 1280.
- Looks like the chosen direction: near-black, violet accent used sparingly, serif display, whitespace rhythm, no stacked-box monotony.
</content>
</invoke>
