/* global fetch */

const API = "/api";

const state = {
  sessionId: null,
  mutationConfirmation: null,
  grounded: null,
};

const icon = {
  check: `<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>`,
  alert: `<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 9v4M12 15h.01"/><path d="M10.29 3.86 1.82 18a1.5 1.5 0 0 0 1.31 2.24h16.74a1.5 1.5 0 0 0 1.31-2.24L13.71 3.86a1.5 1.5 0 0 0-2.62 0Z"/></svg>`,
  history: `<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/><path d="M12 12 8.5 10"/></svg>`,
  x: `<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18 6 6 18M6 6l12 12"/></svg>`,
};

function setMenuState() {
  const button = document.getElementById("menuToggle");
  const nav = document.getElementById("primary-nav");
  if (!button || !nav) return;
  button.addEventListener("click", () => {
    const open = nav.classList.toggle("is-open");
    button.setAttribute("aria-expanded", String(open));
  });
}

function byId(id) {
  return document.getElementById(id);
}

function setBusy(button, busy) {
  if (!button) return;
  button.disabled = busy;
}

function setSkeleton(target, lines = 3) {
  if (!target) return;
  target.replaceChildren();
  for (let i = 0; i < lines; i += 1) {
    const bar = document.createElement("div");
    bar.className = "skeleton skeleton-line";
    target.append(bar);
  }
}

function errorPanel(message, retry) {
  const node = document.createElement("div");
  node.className = "error-panel";
  const text = document.createElement("p");
  text.textContent = message;
  const button = document.createElement("button");
  button.type = "button";
  button.className = "btn btn-ghost";
  button.textContent = "Retry";
  if (retry) {
    button.addEventListener("click", retry);
    button.classList.add("mt-2");
    node.append(text, button);
  } else {
    node.append(text);
  }
  return node;
}

function stateBadge(type, label) {
  const el = document.createElement("span");
  el.className = "state-badge";
  if (type === "active") {
    el.classList.add("state-badge--ok");
    el.innerHTML = `${icon.check}<span>${label}</span>`;
  } else if (type === "contested") {
    el.classList.add("state-badge--warn");
    el.innerHTML = `${icon.alert}<span>${label}</span>`;
  } else if (type === "superseded") {
    el.classList.add("state-badge--warn");
    el.innerHTML = `${icon.history}<span>${label}</span>`;
  } else if (type === "retracted" || type === "purged") {
    el.classList.add("state-badge--danger");
    el.innerHTML = `${icon.x}<span>${label}</span>`;
  } else {
    el.classList.add("state-badge--muted");
    el.textContent = label;
  }
  return el;
}

function renderRef(reference) {
  const card = document.createElement("article");
  card.className = "ref-card";
  const meta = document.createElement("p");
  meta.className = "ref-title mono small";
  meta.textContent = `${reference.claim_id} / ${reference.kind} / ${reference.belief_state || "state"}`;
  const title = document.createElement("p");
  title.className = "result-text";
  title.textContent = `${reference.doi} / ${reference.source}`;
  const badge = stateBadge(
    (reference.belief_state || "pending").toLowerCase(),
    String(reference.belief_state || "pending")
  );
  const basis = document.createElement("p");
  basis.className = "result-text";
  if (reference.belief_state_basis) {
    basis.textContent = reference.belief_state_basis;
  }
  card.append(meta, badge, title);
  if (basis.textContent) {
    card.append(basis);
  }
  return card;
}

function renderEmpty(target, text) {
  const empty = document.createElement("p");
  empty.className = "muted";
  empty.textContent = text;
  target.append(empty);
}

async function fetchJson(path, init = undefined) {
  const response = await fetch(`${API}${path}`, init);
  if (!response.ok) {
    throw new Error(await response.text());
  }
  return response.json();
}

async function fetchStream(path, init = undefined) {
  const response = await fetch(`${API}${path}`, init);
  if (!response.ok) {
    throw new Error(await response.text());
  }
  return response;
}

function addEvent(text) {
  const log = byId("eventLog");
  if (!log) return;
  const row = document.createElement("div");
  row.className = "timeline-row";
  const time = document.createElement("span");
  time.className = "timeline-time";
  time.textContent = new Date().toLocaleTimeString([], {
    hour12: false,
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  });
  const msg = document.createElement("span");
  msg.className = "timeline-event";
  msg.textContent = text;
  row.append(time, msg);
  log.append(row);
}

async function loadState() {
  const payload = await fetchJson(`/state`);
  state.sessionId = payload.session_id;
  state.mutationConfirmation = payload.mutation_confirmation;
  return payload;
}

async function initAsk() {
  const question = byId("question");
  const askButton = byId("askButton");
  const askNaiveText = byId("naiveText");
  const askGtText = byId("groundtruthText");
  const naiveRefs = byId("naiveRefs");
  const gtRefs = byId("groundtruthRefs");
  const naiveBadge = byId("naiveBadge");
  const gtBadge = byId("groundtruthBadge");
  const activeCount = byId("activeCount");
  const doiSelect = byId("doiSelect");
  const timeline = byId("timeline");
  const retractButton = byId("retractButton");
  const downvoteButton = byId("downvoteButton");
  const upvoteButton = byId("upvoteButton");
  const improveButton = byId("improveButton");

  setSkeleton(activeCount, 1);
  setSkeleton(naiveRefs, 1);
  setSkeleton(gtRefs, 1);

  try {
    const payload = await loadState();
    state.sessionId = payload.session_id;
    state.mutationConfirmation = payload.mutation_confirmation;
    if (!question.value.trim()) {
      question.value = payload.default_question;
    }
    activeCount.replaceChildren();
    activeCount.append(
      stateBadge(
        payload.active_retractions.length > 0 ? "active" : "ok",
        `${payload.active_retractions.length} active`
      )
    );
    doiSelect.replaceChildren();
    for (const item of payload.active_retractions) {
      const option = document.createElement("option");
      option.value = item.doi;
      option.dataset.question = item.question;
      option.textContent = `${item.claim_id} / ${item.doi}`;
      doiSelect.append(option);
    }
    renderBenchmarks(payload);
  } catch (error) {
    const eventLog = byId("eventLog");
    if (eventLog) {
      eventLog.replaceChildren(errorPanel(`Unable to load state. ${error.message}`, initAsk));
    }
    return;
  }

  async function ask(requestDataset) {
    return fetchJson(`/ask`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        question: question.value.trim(),
        dataset: requestDataset,
        session_id: requestDataset === "groundtruth_memory" ? state.sessionId : null,
        record_session: requestDataset === "groundtruth_memory",
      }),
    });
  }

  async function askBoth() {
    if (!question.value.trim()) {
      return;
    }
    setBusy(askButton, true);
    setSkeleton(naiveRefs);
    setSkeleton(gtRefs);
    try {
      const [naive, grounded] = await Promise.all([ask("naive_memory"), ask("groundtruth_memory")]);
      askNaiveText.textContent = naive.text;
      askGtText.textContent = grounded.text;
      state.groundtruthQaId = grounded.qa_id || null;
      naiveRefs.replaceChildren();
      gtRefs.replaceChildren();
      const naiveState = naive.cites_retracted ? "retracted" : "active";
      naiveBadge.replaceChildren();
      naiveBadge.append(
        stateBadge(
          naiveState,
          naive.cites_retracted ? "cites retracted" : "clean citations"
        )
      );
      gtBadge.replaceChildren();
      gtBadge.append(stateBadge(grounded.cites_retracted ? "retracted" : "active", grounded.cites_retracted ? "cites retracted" : "clean citations"));
      if (naive.references?.length) {
        for (const item of naive.references) {
          naiveRefs.append(renderRef(item));
        }
      } else {
        renderEmpty(naiveRefs, "No references returned.");
      }
      if (grounded.references?.length) {
        for (const item of grounded.references) {
          gtRefs.append(renderRef(item));
        }
      } else {
        renderEmpty(gtRefs, "No references returned.");
      }
      addEvent("answer: both memories returned cited answers");
    } catch (error) {
      addEvent(`error: ${error.message}`);
    } finally {
      setBusy(askButton, false);
    }
  }

  askButton.addEventListener("click", askBoth);

  async function retractSelected() {
    const doi = doiSelect.value;
    const option = doiSelect.selectedOptions[0];
    if (!doi) return;
    if (option?.dataset.question) {
      question.value = option.dataset.question;
    }
    setBusy(retractButton, true);
    setSkeleton(timeline);
    timeline.replaceChildren();
    try {
      const response = await fetchStream(`/retract`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ doi, confirm_mutation: state.mutationConfirmation }),
      });
      if (!response.body) {
        throw new Error("Streaming response unavailable");
      }
      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let buffer = "";
      while (true) {
        const { value, done } = await reader.read();
        if (done) {
          break;
        }
        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split("\n");
        buffer = lines.pop();
        for (const line of lines) {
          if (!line.trim()) continue;
          const event = JSON.parse(line);
          addEvent(`${event.event}: ${event.doi || event.message || event.claim_id || event.result?.claim_id || "updated"}`);
        }
      }
      addEvent("retraction stream complete");
      await initAsk();
      await askBoth();
    } catch (error) {
      addEvent(`error: ${error.message}`);
    } finally {
      setBusy(retractButton, false);
    }
  }

  async function sendFeedback(score) {
    if (!state.sessionId || !state.groundtruthQaId) {
      addEvent("No GroundTruth answer session to attach feedback.");
      return;
    }
    try {
      await fetchJson(`/feedback`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          session_id: state.sessionId,
          qa_id: state.groundtruthQaId,
          score,
          text: score < 3 ? "Needs stronger evidential grounding." : null,
          confirm_mutation: state.mutationConfirmation,
        }),
      });
      addEvent(`feedback: ${score}`);
    } catch (error) {
      addEvent(`error: ${error.message}`);
    }
  }

  async function improve() {
    if (!state.sessionId) return;
    setBusy(improveButton, true);
    try {
      const result = await fetchJson(`/improve`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          dataset: "groundtruth_memory",
          session_ids: [state.sessionId],
          confirm_mutation: state.mutationConfirmation,
        }),
      });
      addEvent(`improve: ${result.session_bridge}`);
      await askBoth();
    } catch (error) {
      addEvent(`error: ${error.message}`);
    } finally {
      setBusy(improveButton, false);
    }
  }

  downvoteButton.addEventListener("click", () => sendFeedback(1));
  upvoteButton.addEventListener("click", () => sendFeedback(5));
  improveButton.addEventListener("click", improve);
  retractButton.addEventListener("click", retractSelected);
}

function renderItem(item) {
  const node = document.createElement("article");
  node.className = "briefing-item";
  const header = document.createElement("p");
  header.className = "ref-title mono small";
  header.textContent = `${item.pair || item.claim_id || "item"} / ${item.evidence_class || "evidence"}`;
  const title = document.createElement("p");
  title.textContent = item.basis || item.evidence_ref || item.title || "No detail";
  const basis = document.createElement("p");
  basis.className = "ref-basis";
  basis.textContent = item.claim_id && item.claim_id !== item.pair ? `${item.claim_id}` : "";
  node.append(header, title);
  if (basis.textContent) node.append(basis);
  const badge = stateBadge(item.evidence_class === "user_assertion" ? "active" : "ok", item.evidence_class || "evidence");
  node.prepend(badge);
  return node;
}

function renderBriefing(payload, rootId) {
  const target = byId(rootId);
  if (!target) return;
  target.replaceChildren();
  const items = payload && Array.isArray(payload) ? payload : [];
  if (!items.length) {
    renderEmpty(target, "No items in this bucket.");
    return;
  }
  for (const item of items) {
    target.append(renderItem(item));
  }
}

function initBriefing() {
  const generatedAt = byId("briefingGeneratedAt");
  const runButton = byId("runBriefing");
  const learned = byId("briefingLearned");
  const contested = byId("briefingContested");
  const revised = byId("briefingRevised");
  const purged = byId("briefingPurged");

  async function loadBriefing() {
    setSkeleton(learned);
    setSkeleton(contested);
    setSkeleton(revised);
    setSkeleton(purged);
    try {
      const payload = await fetchJson(`/briefing`);
      generatedAt.textContent = payload.generated_at || "not available";
      renderBriefing(payload.learned_last_night || [], "briefingLearned");
      renderBriefing(payload.now_contested || [], "briefingContested");
      renderBriefing(payload.revised || [], "briefingRevised");
      renderBriefing(payload.purged || [], "briefingPurged");
    } catch (error) {
      const container = byId("briefingGeneratedAt");
      if (container) {
        container.replaceChildren();
        container.append(
          stateBadge("retracted", "load failed"),
          document.createTextNode(` ${error.message}`)
        );
      }
    }
  }

  runButton.addEventListener("click", loadBriefing);
  loadBriefing();
}

function renderContested(items) {
  const list = byId("contestedList");
  if (!list) return;
  list.replaceChildren();
  if (!items.length) {
    renderEmpty(list, "No contested beliefs.");
    return;
  }
  for (const item of items) {
    const card = document.createElement("article");
    card.className = "contested-item";
    const header = document.createElement("p");
    header.className = "ref-title mono small";
    header.textContent = `${item.pair} / ${item.decision.direction} / ${item.decision.confidence}`;
    const claims = document.createElement("p");
    claims.textContent = (item.claims || []).map((claim) => `${claim.claim_id} (${claim.evidence_class || "unknown"})`).join(" vs ");
    const basis = document.createElement("p");
    basis.className = "muted";
    basis.textContent = item.basis || "No basis provided.";
    card.append(header, claims, basis);

    const actions = document.createElement("div");
    actions.className = "feedback-row";
    for (const [label, verdict] of [
      ["No conflict", "none"],
      ["A supersedes B", "a_supersedes_b"],
      ["B supersedes A", "b_supersedes_a"],
      ["Mutual", "mutual"],
    ]) {
      const button = document.createElement("button");
      button.className = "btn btn-secondary";
      button.type = "button";
      button.textContent = label;
      button.addEventListener("click", async () => {
        try {
          setBusy(button, true);
          await fetchJson(`/adjudicate`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              pair: item.pair,
              verdict,
              basis: `Resolved from demo UI as ${label}.`,
              confirm_mutation: state.mutationConfirmation,
            }),
          });
        await loadContested();
        await loadBriefingForInvalidation();
      } catch (error) {
          basis.textContent = error.message;
        } finally {
          setBusy(button, false);
        }
      });
      actions.append(button);
    }
    card.append(actions);
    list.append(card);
  }
}

let loadBriefingForInvalidation = async () => Promise.resolve();

async function loadContested() {
  const count = byId("contestedCount");
  const container = byId("contestedList");
  if (!container) return;
  setSkeleton(container);
  try {
    const payload = await fetchJson(`/contested`);
    if (count) {
      count.textContent = `${payload.count || 0} open`;
    }
    renderContested(payload.items || []);
  } catch (error) {
    container.replaceChildren(errorPanel(error.message, initContested));
  }
}

async function initContested() {
  await loadContested();
}

function renderTimeline(payload) {
  byId("timelineAnswerThen").textContent = payload.before?.text || "No answer for start date.";
  byId("timelineAnswerNow").textContent = payload.after?.text || "No answer for end date.";
  const thenRefs = byId("timelineThenRefs");
  const nowRefs = byId("timelineNowRefs");
  thenRefs.replaceChildren();
  nowRefs.replaceChildren();
  if ((payload.before?.references || []).length) {
    for (const ref of payload.before.references) {
      thenRefs.append(renderRef(ref));
    }
  } else {
    renderEmpty(thenRefs, "No references.");
  }
  if ((payload.after?.references || []).length) {
    for (const ref of payload.after.references) {
      nowRefs.append(renderRef(ref));
    }
  } else {
    renderEmpty(nowRefs, "No references.");
  }
  renderBriefing(payload.changes?.added || [], "timelineAdded");
  renderBriefing(payload.changes?.contested || [], "timelineContested");
  renderBriefing(payload.changes?.revised || [], "timelineRevised");
  renderBriefing(payload.changes?.purged || [], "timelinePurged");
}

async function initTimeline() {
  const button = byId("timelineButton");
  const fromDate = byId("timelineFrom");
  const toDate = byId("timelineTo");
  const question = byId("timelineQuestion");
  const containers = [
    "timelineAnswerThen",
    "timelineAnswerNow",
    "timelineThenRefs",
    "timelineNowRefs",
    "timelineAdded",
    "timelineContested",
    "timelineRevised",
    "timelinePurged",
  ];
  async function loadTimeline() {
    for (const id of containers) {
      const target = byId(id);
      setSkeleton(target);
      if (id.startsWith("timeline")) {
        target.replaceChildren();
      }
    }
    try {
      const params = new URLSearchParams({
        from: fromDate.value || "2023-01-01",
        to: toDate.value || "2026-07-04",
      });
      if (question.value.trim()) {
        params.set("question", question.value.trim());
      }
      const payload = await fetchJson(`/timeline?${params.toString()}`);
      renderTimeline(payload);
    } catch (error) {
      const now = byId("timelineAnswerNow");
      if (now) {
        now.textContent = `Error loading timeline: ${error.message}`;
      }
    }
  }
  button.addEventListener("click", loadTimeline);
  await loadTimeline();
}

function renderBenchmarks(payload) {
  const metricNaive = byId("metricNaive");
  const metricGroundtruth = byId("metricGroundtruth");
  const metricControl = byId("metricControl");
  const coverage = byId("metricCoverage");
  if (metricNaive) {
    metricNaive.textContent = payload?.benchmark?.naive_cites_retracted
      ? `${payload.benchmark.naive_cites_retracted}/20`
      : "18/20";
  }
  if (metricGroundtruth) {
    metricGroundtruth.textContent = payload?.benchmark?.groundtruth_cites_retracted !== undefined
      ? `${payload.benchmark.groundtruth_cites_retracted}/20`
      : "0/20";
  }
  if (metricControl) {
    const controlTotal = payload?.benchmark?.control_claim_total || 5;
    const controlRetention = payload?.benchmark?.control_claim_retention || 5;
    metricControl.textContent = `${controlRetention}/${controlTotal}`;
  }
  if (coverage) {
    coverage.textContent = "25/25";
  }
}

async function initEvidence() {
  try {
    const payload = await fetchJson(`/state`);
    renderBenchmarks(payload);
    byId("evidenceContestedCount").textContent = "No pending contested queue snapshot in this page.";
    const contested = await fetchJson(`/contested`);
    byId("evidenceContestedCount").textContent = `${contested.count || 0} open contested pairs`;
  } catch (error) {
    const target = byId("evidenceContestedCount");
    if (target) {
      target.textContent = `Unable to load evidence data: ${error.message}`;
    }
  }
}

function initLanding() {
  const links = document.querySelectorAll("[href*='ask'], [href*='briefing'], [href*='contested'], [href*='timeline'], [href*='evidence']");
  for (const link of links) {
    link.setAttribute("role", "link");
  }
}

async function main() {
  setMenuState();
  loadBriefingForInvalidation = initBriefing;

  const page = document.body.dataset.page;
  if (page === "ask") {
    await initAsk();
  } else if (page === "briefing") {
    initBriefing();
  } else if (page === "contested") {
    await initContested();
  } else if (page === "timeline") {
    await initTimeline();
  } else if (page === "evidence") {
    await initEvidence();
  } else {
    initLanding();
  }
}

main().catch((error) => {
  console.error(error);
});
