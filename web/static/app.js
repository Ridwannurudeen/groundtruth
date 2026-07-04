const state = {
  sessionId: null,
  groundtruthQaId: null,
  lastQuestion: "",
  mutationConfirmation: null,
  contestedItems: [],
  briefing: null,
};

const el = {
  question: document.querySelector("#question"),
  askButton: document.querySelector("#askButton"),
  naiveText: document.querySelector("#naiveText"),
  groundtruthText: document.querySelector("#groundtruthText"),
  naiveRefs: document.querySelector("#naiveRefs"),
  groundtruthRefs: document.querySelector("#groundtruthRefs"),
  naiveBadge: document.querySelector("#naiveBadge"),
  groundtruthBadge: document.querySelector("#groundtruthBadge"),
  doiSelect: document.querySelector("#doiSelect"),
  retractButton: document.querySelector("#retractButton"),
  timeline: document.querySelector("#timeline"),
  activeCount: document.querySelector("#activeCount"),
  downvoteButton: document.querySelector("#downvoteButton"),
  upvoteButton: document.querySelector("#upvoteButton"),
  improveButton: document.querySelector("#improveButton"),
  metricNaive: document.querySelector("#metricNaive"),
  metricGroundtruth: document.querySelector("#metricGroundtruth"),
  metricControl: document.querySelector("#metricControl"),
  contestedCount: document.querySelector("#contestedCount"),
  contestedList: document.querySelector("#contestedList"),
  briefingGeneratedAt: document.querySelector("#briefingGeneratedAt"),
  briefingLearned: document.querySelector("#briefingLearned"),
  briefingContested: document.querySelector("#briefingContested"),
  briefingRevised: document.querySelector("#briefingRevised"),
  briefingPurged: document.querySelector("#briefingPurged"),
};

function setBusy(button, busy) {
  button.disabled = busy;
}

function badge(node, result) {
  node.classList.remove("badge-danger", "badge-safe");
  if (result.cites_retracted) {
    node.textContent = "cites retracted";
    node.classList.add("badge-danger");
    return;
  }
  if ((result.cites_by_state || {}).contested > 0) {
    node.textContent = "contested citations";
    node.classList.add("badge-danger");
    return;
  }
  node.textContent = "clean citations";
  node.classList.add("badge-safe");
}

function renderRefs(target, references) {
  target.replaceChildren();
  if (!references.length) {
    const empty = document.createElement("p");
    empty.className = "ref-title";
    empty.textContent = "No references returned.";
    target.append(empty);
    return;
  }

  for (const reference of references) {
    const item = document.createElement("div");
    item.className = "ref";

    const meta = document.createElement("div");
    meta.className = "ref-meta";
    meta.textContent = `${reference.claim_id} / ${reference.kind} / ${reference.belief_state}`;

    const title = document.createElement("p");
    title.className = "ref-title";
    title.textContent = `${reference.doi} / ${reference.source}`;

    item.append(meta, title);
    if (reference.belief_state_basis) {
      const basis = document.createElement("p");
      basis.className = "ref-basis";
      basis.textContent = reference.belief_state_basis;
      item.append(basis);
    }
    target.append(item);
  }
}

function renderAnswer(dataset, result) {
  if (dataset === "naive_memory") {
    el.naiveText.textContent = result.text;
    renderRefs(el.naiveRefs, result.references || []);
    badge(el.naiveBadge, result);
    return;
  }

  el.groundtruthText.textContent = result.text;
  renderRefs(el.groundtruthRefs, result.references || []);
  badge(el.groundtruthBadge, result);
  state.groundtruthQaId = result.qa_id;
}

function addTimeline(event, detail) {
  const row = document.createElement("div");
  row.className = "timeline-row";

  const time = document.createElement("div");
  time.className = "timeline-time";
  time.textContent = new Date().toLocaleTimeString([], {
    hour12: false,
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  });

  const text = document.createElement("div");
  text.className = "timeline-event";
  text.textContent = `${event}: ${detail}`;

  row.append(time, text);
  el.timeline.prepend(row);
}

async function postJson(path, payload) {
  const response = await fetch(path, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  if (!response.ok) {
    throw new Error(await response.text());
  }
  return response.json();
}

async function askDataset(dataset, feedbackInfluence = 0) {
  return postJson("/ask", {
    question: el.question.value.trim(),
    dataset,
    session_id: dataset === "groundtruth_memory" ? state.sessionId : null,
    record_session: dataset === "groundtruth_memory" && feedbackInfluence === 0,
    feedback_influence: feedbackInfluence,
  });
}

async function askBoth(feedbackInfluence = 0) {
  const question = el.question.value.trim();
  if (!question) {
    return;
  }
  state.lastQuestion = question;
  setBusy(el.askButton, true);
  try {
    const [naive, groundtruth] = await Promise.all([
      askDataset("naive_memory", 0),
      askDataset("groundtruth_memory", feedbackInfluence),
    ]);
    renderAnswer("naive_memory", naive);
    renderAnswer("groundtruth_memory", groundtruth);
    addTimeline("answer", "both memories returned cited answers");
  } catch (error) {
    addTimeline("error", error.message);
  } finally {
    setBusy(el.askButton, false);
  }
}

async function loadState(resetQuestion = false) {
  const response = await fetch("/state");
  if (!response.ok) {
    throw new Error(await response.text());
  }
  const payload = await response.json();
  state.sessionId = payload.session_id;
  state.mutationConfirmation = payload.mutation_confirmation;
  if (resetQuestion || !el.question.value.trim()) {
    el.question.value = payload.default_question;
  }
  el.activeCount.textContent = `${payload.active_retractions.length} active`;
  el.doiSelect.replaceChildren();
  for (const item of payload.active_retractions) {
    const option = document.createElement("option");
    option.value = item.doi;
    option.dataset.question = item.question;
    option.textContent = `${item.claim_id} / ${item.doi}`;
    el.doiSelect.append(option);
  }
  if (payload.benchmark) {
    el.metricNaive.textContent = `${payload.benchmark.naive_cites_retracted}/20 naive`;
    el.metricGroundtruth.textContent = `${payload.benchmark.groundtruth_cites_retracted}/20 GroundTruth`;
    el.metricControl.textContent = `${payload.benchmark.control_claim_retention}/${payload.benchmark.control_claim_total} controls`;
  }
}

async function loadContested() {
  const response = await fetch("/contested");
  if (!response.ok) {
    throw new Error(await response.text());
  }
  const payload = await response.json();
  state.contestedItems = payload.items || [];
  renderContested(state.contestedItems);
}

async function loadBriefing() {
  const response = await fetch("/briefing");
  if (!response.ok) {
    throw new Error(await response.text());
  }
  const payload = await response.json();
  state.briefing = payload;
  renderBriefing(payload);
}

function renderBriefingItem(item) {
  const card = document.createElement("div");
  card.className = "briefing-item";

  const meta = document.createElement("div");
  meta.className = "ref-meta";
  const subject = item.pair || item.claim_id || "item";
  meta.textContent = `${subject} / ${item.belief_state || "state"} / ${item.evidence_class || "evidence"}`;

  const title = document.createElement("p");
  title.className = "ref-title";
  title.textContent = item.title || item.doi || item.evidence_ref || "Untitled evidence";

  card.append(meta, title);
  if (item.basis) {
    const basis = document.createElement("p");
    basis.className = "ref-basis";
    basis.textContent = item.basis;
    card.append(basis);
  }
  return card;
}

function renderBriefingList(target, items) {
  target.replaceChildren();
  if (!items.length) {
    const empty = document.createElement("p");
    empty.className = "contest-empty";
    empty.textContent = "None.";
    target.append(empty);
    return;
  }
  for (const item of items) {
    target.append(renderBriefingItem(item));
  }
}

function renderBriefing(payload) {
  el.briefingGeneratedAt.textContent = payload.generated_at || "not generated";
  renderBriefingList(el.briefingLearned, payload.learned_last_night || []);
  renderBriefingList(el.briefingContested, payload.now_contested || []);
  renderBriefingList(el.briefingRevised, payload.revised || []);
  renderBriefingList(el.briefingPurged, payload.purged || []);
}

function renderContested(items) {
  el.contestedCount.textContent = `${items.length} open`;
  el.contestedList.replaceChildren();
  if (!items.length) {
    const empty = document.createElement("p");
    empty.className = "contest-empty";
    empty.textContent = "No contested semantic pairs.";
    el.contestedList.append(empty);
    return;
  }

  for (const item of items) {
    const card = document.createElement("div");
    card.className = "contest-item";

    const meta = document.createElement("div");
    meta.className = "ref-meta";
    meta.textContent = `${item.pair} / ${item.decision.direction} / ${item.decision.confidence}`;

    const claims = document.createElement("p");
    claims.className = "ref-title";
    claims.textContent = item.claims
      .map((claim) => `${claim.claim_id}: ${claim.title}`)
      .join(" vs ");

    const basis = document.createElement("p");
    basis.className = "ref-basis";
    basis.textContent = item.basis;

    const actions = document.createElement("div");
    actions.className = "contest-actions";
    for (const [label, verdict] of [
      ["No conflict", "none"],
      ["A supersedes B", "a_supersedes_b"],
      ["B supersedes A", "b_supersedes_a"],
      ["Mutual", "mutual"],
    ]) {
      const button = document.createElement("button");
      button.type = "button";
      button.textContent = label;
      button.addEventListener("click", () => adjudicate(item.pair, verdict));
      actions.append(button);
    }

    card.append(meta, claims, basis, actions);
    el.contestedList.append(card);
  }
}

async function adjudicate(pair, verdict) {
  try {
    const result = await postJson("/adjudicate", {
      pair,
      verdict,
      basis: `UI adjudication selected ${verdict}.`,
      confirm_mutation: state.mutationConfirmation,
    });
    addTimeline("adjudicated", `${result.pair} -> ${result.verdict}`);
    await loadContested();
    await loadBriefing();
    if (state.lastQuestion) {
      await askBoth();
    }
  } catch (error) {
    addTimeline("error", error.message);
  }
}

async function retractSelected() {
  const doi = el.doiSelect.value;
  if (!doi) {
    return;
  }
  const selectedOption = el.doiSelect.selectedOptions[0];
  const selectedQuestion = selectedOption
    ? selectedOption.dataset.question
    : null;
  setBusy(el.retractButton, true);
  addTimeline("request", doi);
  try {
    const response = await fetch("/retract", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        doi,
        confirm_mutation: state.mutationConfirmation,
      }),
    });
    if (!response.ok || !response.body) {
      throw new Error(await response.text());
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
        if (!line.trim()) {
          continue;
        }
        const message = JSON.parse(line);
        const detail =
          message.doi || message.message || message.claim_id || "updated";
        addTimeline(message.event, detail);
      }
    }
    await loadState(false);
    await loadContested();
    await loadBriefing();
    if (selectedQuestion) {
      el.question.value = selectedQuestion;
    }
    await askBoth();
  } catch (error) {
    addTimeline("error", error.message);
  } finally {
    setBusy(el.retractButton, false);
  }
}

async function sendFeedback(score) {
  if (!state.sessionId || !state.groundtruthQaId) {
    addTimeline("feedback", "ask GroundTruth once before sending feedback");
    return;
  }
  const result = await postJson("/feedback", {
    session_id: state.sessionId,
    qa_id: state.groundtruthQaId,
    score,
    text:
      score < 3 ? "Answer should lean harder on post-retraction memory." : null,
    confirm_mutation: state.mutationConfirmation,
  });
  addTimeline("feedback", `${result.qa_id} score ${result.feedback_score}`);
}

async function improve() {
  if (!state.sessionId) {
    return;
  }
  setBusy(el.improveButton, true);
  try {
    const result = await postJson("/improve", {
      dataset: "groundtruth_memory",
      session_ids: [state.sessionId],
      feedback_alpha: 1,
      confirm_mutation: state.mutationConfirmation,
    });
    addTimeline("improve", result.session_bridge);
    await askBoth(1);
  } catch (error) {
    addTimeline("error", error.message);
  } finally {
    setBusy(el.improveButton, false);
  }
}

el.askButton.addEventListener("click", () => askBoth());
el.retractButton.addEventListener("click", retractSelected);
el.downvoteButton.addEventListener("click", () => sendFeedback(1));
el.upvoteButton.addEventListener("click", () => sendFeedback(5));
el.improveButton.addEventListener("click", improve);

loadState(true)
  .then(() => loadContested())
  .then(() => loadBriefing())
  .then(() => askBoth())
  .catch((error) => addTimeline("error", error.message));
