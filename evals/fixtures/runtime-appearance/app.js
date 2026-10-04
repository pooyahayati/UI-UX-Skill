"use strict";
const $ = id => document.getElementById(id);
const state = { session: null, catalog: null, published: null, draft: null, dirty: false, busy: false };
const isReader = location.pathname === "/reader";
let confirmationAction = null;
let confirmationTrigger = null;
let overlayTrigger = null;

async function request(resource, method = "GET", body) {
  const url = resource.startsWith("/") ? resource : `/api/v1/tenants/${state.session.tenant}/${resource}`;
  const options = { method, credentials: "same-origin", headers: {} };
  if (method !== "GET") {
    options.headers["Content-Type"] = "application/json";
    options.headers["X-Fixture-CSRF"] = state.session.csrf;
    options.body = JSON.stringify(body);
  }
  let response;
  try { response = await fetch(url, options); }
  catch (_) { throw new Error("Connection outcome is unknown. Inputs are preserved. Reload published values and history before retrying."); }
  let result;
  try { result = await response.json(); }
  catch (_) { throw new Error("Response could not be verified. Preserve inputs and reconcile server state before retrying."); }
  if (!response.ok) {
    const error = new Error(result.error.message);
    error.details = result.error.details;
    throw error;
  }
  return result;
}

function status(message, error = false) {
  $("status").textContent = message;
  $("status").setAttribute("role", error ? "alert" : "status");
}

async function perform(action) {
  if (state.busy) return;
  state.busy = true;
  $("manager").setAttribute("aria-busy", "true");
  updateActions();
  try { await action(); }
  catch (error) {
    status(error.message, true);
    for (const spec of (state.catalog ? state.catalog.settings : [])) {
      const control = $("setting-" + spec.key);
      const message = $("error-" + spec.key);
      if (control && message) {
        const detail = error.details && error.details[spec.key];
        control.setAttribute("aria-invalid", detail ? "true" : "false");
        message.textContent = detail || "";
      }
    }
  } finally {
    state.busy = false;
    $("manager").removeAttribute("aria-busy");
    updateActions();
  }
}

function applyTokens(root, tokens) {
  for (const [key, value] of Object.entries(tokens)) {
    if (key.startsWith("--") || key === "color-scheme") root.style.setProperty(key, value);
  }
}

function svgElement(name, attributes, text) {
  const node = document.createElementNS("http://www.w3.org/2000/svg", name);
  for (const [key, value] of Object.entries(attributes)) node.setAttribute(key, value);
  if (text !== undefined) node.textContent = text;
  return node;
}

function iconElement(icon, tokens, iconState = "default") {
  const artwork = icon.states[iconState];
  const svg = svgElement("svg", { viewBox: "0 0 24 24", "aria-hidden": "true",
    focusable: "false", class: "semantic-icon", "data-use": icon.use,
    "data-family": icon.family, "data-variant": icon.variant,
    "data-fallback": String(icon.fallback), "data-state": iconState,
    "data-mirror": String(icon.directional && iconState !== "open") });
  for (const path of artwork) {
    svg.append(svgElement("path", { d: path.d, "fill-rule": "evenodd",
      fill: path.badge || !icon.stroke ? "currentColor" : "none",
      stroke: path.badge || !icon.stroke ? "none" : "currentColor",
      "stroke-width": icon.fallback ? 2 : tokens.iconStroke,
      "stroke-linecap": "round", "stroke-linejoin": "round" }));
  }
  return svg;
}

// Every owned consumer uses this adapter, including readers and overlays.
// Only server-resolved prepared artwork reaches a fixed SVG element vocabulary.
function renderIcons(root, tokens) {
  for (const slot of root.querySelectorAll("[data-icon]")) {
    const use = slot.dataset.icon;
    const details = use === "disclosure" && slot.closest("details");
    const iconState = details ? (details.open ? "open" : "closed") : "default";
    slot.replaceChildren(iconElement(tokens.icons[use], tokens, iconState));
  }
  for (const note of root.querySelectorAll(".icon-provenance")) {
    const fallbacks = Object.values(tokens.icons).filter(icon => icon.fallback);
    note.textContent = fallbacks.length
      ? "Prepared fallback: " + fallbacks.map(icon => `${icon.use} ${icon.variant} uses ${icon.family}; unavailable in ${icon.requestedFamily}.`).join(" ")
      : "All icon assignments are available in the selected family.";
  }
}

function updateIconGallery() {
  if (!state.catalog) return;
  const config = readConfig(), icons = state.catalog.icons;
  for (const button of document.querySelectorAll(".icon-choice")) {
    const key = button.dataset.setting, value = button.dataset.value;
    const use = key === "iconFamily" ? "search" : key.slice(0, -4);
    const family = key === "iconFamily" ? value : config.iconFamily;
    const variant = key === "iconFamily" ? config.searchIcon : value;
    const icon = icons.assets[family][use][variant];
    const art = button.querySelector(".choice-art");
    const galleryUses = key === "iconFamily" ? ["search", "add", "delete"] : [use];
    art.replaceChildren(...galleryUses.map(semantic => {
      const preview = icons.assets[family][semantic][key === "iconFamily" ? config[semantic + "Icon"] : variant];
      return iconElement(preview, { iconStroke: family === "outline" ? config.iconStroke : 2 }, semantic === "disclosure" ? "closed" : "default");
    }));
    const selected = config[key] === value;
    button.setAttribute("aria-pressed", String(selected));
    button.querySelector(".choice-note").textContent = (selected ? "Selected · " : "") + (icon.fallback ? "Prepared outline fallback" : "Available");
    button.disabled = state.busy;
  }
  const stroke = $("setting-iconStroke");
  if (stroke) {
    stroke.disabled = state.busy || !icons.families[config.iconFamily].stroke;
    $("help-iconStroke").textContent = config.iconFamily === "solid"
      ? "Not editable for solid assets. Your outline preference is retained but dormant; a fallback uses its prepared width."
      : "Adjusts outline artwork only. Solid artwork has no stroke; control target size stays unchanged.";
  }
}

// An explicit non-CSS adapter: same resolved roles, unchanged data/relationships.
function renderVisualizations(root, tokens) {
  const chart = root.querySelector(".chart");
  chart.replaceChildren();
  chart.append(svgElement("line", { x1: 20, y1: 132, x2: 300, y2: 132, stroke: tokens["--chart-grid"] }));
  [3, 5, 4].forEach((value, index) => {
    const x = 55 + index * 90, y = 132 - value * 20;
    if (tokens.chartStyle === "bars") {
      chart.append(svgElement("rect", { x, y, width: 34, height: value * 20, fill: tokens["--chart-series"], rx: 3 }));
    } else {
      chart.append(svgElement("line", { x1: x + 17, y1: y, x2: x + 17, y2: 132, stroke: tokens["--chart-series"], "stroke-width": 3 }));
      chart.append(svgElement("circle", { cx: x + 17, cy: y, r: 8, fill: tokens["--chart-series"] }));
    }
    chart.append(svgElement("text", { x: x + 17, y: y - 8, "text-anchor": "middle", fill: tokens["--chart-label"], "font-family": tokens["--font"], "font-size": tokens["--label-size"] }, String(value)));
    chart.append(svgElement("text", { x: x + 17, y: 158, "text-anchor": "middle", fill: tokens["--chart-label"], "font-family": tokens["--font"], "font-size": tokens["--label-size"] }, ["Mon", "Tue", "Wed"][index]));
  });
  const diagram = root.querySelector(".diagram");
  diagram.replaceChildren(svgElement("line", { x1: 50, y1: 38, x2: 270, y2: 38, stroke: tokens["--chart-grid"], "stroke-width": tokens["--border-width"] }));
  ["Draft", "Review", "Publish"].forEach((name, index) => {
    const x = 5 + index * 110;
    const filled = tokens.diagramStyle === "filled";
    diagram.append(svgElement("rect", { x, y: 10, width: 90, height: 54, rx: tokens["--radius"], fill: filled ? tokens["--action"] : tokens["--surface"], stroke: tokens["--border"], "stroke-width": tokens["--border-width"] }));
    diagram.append(svgElement("text", { x: x + 45, y: 43, "text-anchor": "middle", fill: filled ? tokens["--inverse"] : tokens["--text"], "font-family": tokens["--font"], "font-size": tokens["--label-size"] }, name));
  });
}

function renderSurface(id, snapshot) {
  const root = $(id);
  if (!root.firstElementChild) {
    root.append($("product-template").content.cloneNode(true));
    root.querySelector(".open-example").addEventListener("click", event => {
      overlayTrigger = event.currentTarget;
      applyTokens($("surface-dialog"), root._resolvedTokens);
      renderIcons($("surface-dialog"), root._resolvedTokens);
      $("surface-dialog").showModal();
    });
    for (const details of root.querySelectorAll(".product-details")) {
      details.addEventListener("toggle", () => renderIcons(root, root._resolvedTokens));
    }
  }
  root._resolvedTokens = snapshot.tokens;
  applyTokens(root, snapshot.tokens);
  renderVisualizations(root, snapshot.tokens);
  renderIcons(root, snapshot.tokens);
}

function renderControls() {
  const container = $("settings-fields");
  let group = "", content;
  for (const spec of state.catalog.settings) {
    if (spec.group !== group) {
      group = spec.group;
      const details = document.createElement("details");
      details.open = group === "Brand" || group === "Typography" || group === "Icons";
      const summary = document.createElement("summary"); summary.textContent = group;
      content = document.createElement("div"); details.append(summary, content); container.append(details);
    }
    const label = document.createElement("label"); label.htmlFor = "setting-" + spec.key; label.textContent = spec.label;
    const select = document.createElement("select"); select.id = "setting-" + spec.key;
    for (const value of spec.values) {
      const option = document.createElement("option"); option.value = String(value); option.textContent = String(value); select.append(option);
    }
    const description = document.createElement("small"); description.id = "help-" + spec.key;
    description.textContent = `Default: ${spec.default}. Affects ${spec.consumers}.`;
    const error = document.createElement("small"); error.id = "error-" + spec.key; error.className = "error-example";
    select.setAttribute("aria-describedby", `${description.id} ${error.id}`);
    select.addEventListener("change", () => { state.dirty = true; updateActions(); });
    label.append(select, description, error); content.append(label);
    if (spec.key === "iconFamily" || spec.key.endsWith("Icon")) {
      const gallery = document.createElement("div"); gallery.className = "icon-gallery";
      gallery.setAttribute("role", "group"); gallery.setAttribute("aria-label", spec.label + " visual choices");
      for (const value of spec.values) {
        const button = document.createElement("button"); button.type = "button"; button.className = "icon-choice";
        button.dataset.setting = spec.key; button.dataset.value = value;
        const art = document.createElement("span"); art.className = "choice-art";
        const name = document.createElement("span"); name.textContent = spec.key === "iconFamily" ? state.catalog.icons.families[value].label : spec.label + " · " + value;
        const note = document.createElement("small"); note.className = "choice-note";
        button.append(art, name, note);
        button.addEventListener("click", () => { select.value = value; state.dirty = true; updateActions(); });
        gallery.append(button);
      }
      content.append(gallery);
    }
  }
}

function readConfig() {
  const config = { schema: state.catalog.schema };
  for (const spec of state.catalog.settings) {
    const raw = $("setting-" + spec.key).value;
    config[spec.key] = typeof spec.values[0] === "number" ? Number(raw) : raw;
  }
  return config;
}

function fillControls(config) {
  for (const spec of state.catalog.settings) $("setting-" + spec.key).value = String(config[spec.key]);
  updateIconGallery();
}

function updateActions() {
  const locked = state.busy;
  for (const id of ["save", "preview", "reset", "reload", "compact", "preset", "rollback", "icon-defaults"]) $(id).disabled = locked;
  $("publish").disabled = locked || !state.draft || state.dirty;
  $("discard").disabled = locked || !state.draft;
  for (const spec of (state.catalog ? state.catalog.settings : [])) $("setting-" + spec.key).disabled = locked;
  updateIconGallery();
  $("draft-state").textContent = state.dirty ? "Unsaved edits. Save before publication; refresh can lose these edits." : state.draft ? `Saved private draft ${state.draft.draftRevision}; based on published version ${state.draft.baseRevision}.` : "No saved draft. Published values remain active.";
  if (state.catalog && state.published && !isReader && state.session.canEdit) {
    const config = readConfig();
    const changes = state.catalog.settings.filter(spec => config[spec.key] !== state.published.config[spec.key]);
    $("diff").textContent = changes.length ? "Changes from published: " + changes.map(spec => `${spec.label}: ${state.published.config[spec.key]} → ${config[spec.key]}`).join("; ") : "No differences from published appearance.";
  }
}

async function refreshPublished() {
  state.published = await request("published");
  applyTokens(document.documentElement, state.published.tokens);
  renderSurface("published-preview", state.published);
  $("published-state").textContent = `Tenant ${state.session.tenant.toUpperCase()} · ${state.published.source} · version ${state.published.revision ?? "unavailable"}. This surface never reads a private draft.`;
  if (state.published.source !== "published") status("Appearance storage is degraded. Safe fallback is visible; no private draft was applied. Restore valid storage before publishing.", true);
}

async function refreshHistory() {
  const [history, audit] = await Promise.all([request("history"), request("audit")]);
  $("history").replaceChildren(); $("history-choice").replaceChildren(); $("audit").replaceChildren();
  for (const version of history.items) {
    const labels = version.changedFields === null ? "difference unavailable" : version.changedFields.length ? version.changedFields.map(key => state.catalog.settings.find(spec => spec.key === key).label).join(", ") : "no changed fields";
    const item = document.createElement("li"); item.textContent = `Version ${version.revision} · ${version.action} · ${version.actor} · ${version.created} · ${version.valid ? "valid" : "invalid; cannot restore"} · ${labels}`; $("history").append(item);
    if (version.valid) {
      const option = document.createElement("option"); option.value = String(version.revision); option.textContent = `Version ${version.revision} · ${version.action}`; $("history-choice").append(option);
    }
  }
  for (const entry of audit.items) {
    const item = document.createElement("li"); item.textContent = `${entry.action} · ${entry.actor} · ${entry.created}`; $("audit").append(item);
  }
}

async function preview() {
  const snapshot = await request("previews", "POST", { config: readConfig() });
  renderSurface("admin-preview", snapshot);
  $("preview-state").textContent = "PRIVATE PREVIEW · not published · visible to this owner only";
}

async function reload() {
  await refreshPublished();
  state.draft = await request("draft");
  fillControls(state.draft ? state.draft.config : state.published.config);
  state.dirty = false;
  await preview(); await refreshHistory();
  updateActions();
}

function confirmChange(title, description, trigger, action) {
  confirmationAction = action; confirmationTrigger = trigger;
  $("confirmation-title").textContent = title; $("confirmation-text").textContent = description;
  $("confirmation").returnValue = "cancel"; $("confirmation").showModal();
}

$("confirmation").addEventListener("close", () => {
  const action = confirmationAction; confirmationAction = null;
  if (confirmationTrigger) confirmationTrigger.focus();
  if ($("confirmation").returnValue === "confirm" && action) perform(action);
});
$("surface-dialog").addEventListener("close", () => { if (overlayTrigger) overlayTrigger.focus(); });
$("settings-form").addEventListener("submit", event => event.preventDefault());
$("preview").addEventListener("click", () => perform(preview));
$("save").addEventListener("click", () => perform(async () => {
  state.draft = await request("draft", "PUT", { config: readConfig(), baseRevision: state.draft ? state.draft.baseRevision : state.published.revision, draftRevision: state.draft ? state.draft.draftRevision : 0 });
  state.dirty = false; await preview(); await refreshHistory(); status("Private draft saved. Published appearance is unchanged.");
}));
$("publish").addEventListener("click", event => confirmChange("Publish appearance for this tenant?", $("diff").textContent + " Other owners' drafts are not published. A new history version will be created.", event.currentTarget, async () => {
  const accepted = await request("publications", "POST", { draftRevision: state.draft.draftRevision });
  await reload();
  if (state.published.source !== "published" || state.published.revision !== accepted.revision) {
    status("Publication was acknowledged, but the active reader is degraded or has moved. Reconcile history before retrying.", true);
  } else status("Appearance published and confirmed by the server. Readers can refresh to see this version.");
}));
$("discard").addEventListener("click", () => perform(async () => {
  await request("draft", "DELETE", { draftRevision: state.draft.draftRevision });
  await reload(); status("Your saved draft was discarded. Published appearance and history are unchanged.");
}));
$("preset").addEventListener("click", () => { fillControls(state.catalog.defaults); state.dirty = true; updateActions(); });
$("compact").addEventListener("click", () => { $("setting-density").value = "compact"; state.dirty = true; updateActions(); });
$("icon-defaults").addEventListener("click", () => {
  for (const spec of state.catalog.settings.filter(spec => spec.group === "Icons")) {
    $("setting-" + spec.key).value = String(state.catalog.defaults[spec.key]);
  }
  state.dirty = true; updateActions();
  status("Icon defaults staged locally. Other appearance choices are preserved; preview and save before publishing.");
});
$("reset").addEventListener("click", event => confirmChange("Stage appearance defaults?", "This replaces your private draft with prepared defaults. It does not publish or delete history. Unsaved local edits will be replaced.", event.currentTarget, async () => {
  state.draft = await request("resets", "POST", { baseRevision: state.published.revision, draftRevision: state.draft ? state.draft.draftRevision : 0 });
  fillControls(state.draft.config); state.dirty = false; await preview(); await refreshHistory(); status("Defaults saved as a private draft. Review before publishing.");
}));
$("rollback").addEventListener("click", event => {
  const revision = Number($("history-choice").value);
  confirmChange("Restore a prior published version?", `Version ${revision} will be copied into a new active version for this tenant. Current history and your private draft remain.`, event.currentTarget, async () => {
    const accepted = await request("rollbacks", "POST", { revision, baseRevision: state.published.revision });
    await reload();
    if (state.published.source !== "published" || state.published.revision !== accepted.revision) {
      status("Rollback was acknowledged, but the active reader is degraded or has moved. Reconcile history before retrying.", true);
    } else status("Rollback confirmed. A new active version was appended; history is preserved.");
  });
});
$("reload").addEventListener("click", event => {
  if (state.dirty) confirmChange("Replace unsaved edits with server state?", "Unsaved local edits will be lost. Saved private draft and published history remain.", event.currentTarget, async () => { await reload(); status("Server state reloaded."); });
  else perform(async () => { await reload(); status("Server state reloaded."); });
});
$("refresh-reader").addEventListener("click", () => perform(async () => { await refreshPublished(); if (state.published.source === "published") status("Published values refreshed. Private drafts remain private."); }));
window.addEventListener("beforeunload", event => { if (state.dirty) { event.preventDefault(); event.returnValue = ""; } });

(async () => {
  try {
    state.session = await request("/api/v1/session");
    $("identity").textContent = `Tenant ${state.session.tenant.toUpperCase()} · ${state.session.actor} · ${state.session.canEdit ? "synthetic owner" : "read-only"}`;
    if (isReader) $("page-title").textContent = "Published reader";
    await refreshPublished();
    if (!isReader && state.session.canEdit) {
      state.catalog = await request("catalog"); renderControls(); $("manager").hidden = false;
      await reload();
    }
    if (state.published.source === "published") status("Published appearance loaded. Drafts are never public.");
  } catch (error) { status(error.message, true); }
})();
