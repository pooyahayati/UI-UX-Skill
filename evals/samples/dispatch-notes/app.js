"use strict";

// Authored example output, never an input/answer key for raw forward evaluations.
const COPY = {
  en: {
    skip: "Skip to visit workspace", review: "Design comparison · r1", pending: "Not selected or approved",
    direction: "Direction", language: "Language", theme: "Theme", scenario: "Simulated state",
    fail: "Fail next save (simulation)", workspace: "Visit workspace", myVisits: "My visits", assigned: "Assigned visit",
    open: "Open visit", next: "Next task", longTask: "Inspect the north ventilation unit after the replacement filter arrives.",
    back: "Back to visits", details: "Visit details", location: "Location", technician: "Technician", unit: "Unit",
    instructions: "Before you begin", instruction: "Inspect the intake filter and record the reading before restarting the unit.",
    note: "Visit note", noteHelp: "Record the work and reading. Maximum 2,000 characters. Draft saves do not complete the visit.",
    save: "Save draft", tabOnly: "Simulation · this tab only", confirm: "I have finished the work described above.",
    complete: "Mark complete", recorded: "Recorded note · simulation", reset: "Reset simulated visit",
    synthetic: "Synthetic sample. Saves are simulated in this tab only; refresh clears all notes.",
    footer: "Comparison r1 · Same workflow, records and actions in both directions.",
    draft: "Filter replaced. Reading stable after restart.", site: "North Workshop", person: "Sam Lee",
    date: "Tuesday · 09:30 (sample)", identity: "Technician · Sam Lee", assignedStatus: "Assigned", completed: "Completed · simulated",
    loading: "Loading assigned visits · simulation. Choose Ready to recover.",
    empty: "No visits assigned · simulation. Choose Ready to restore the sample visit.",
    access: "Read-only simulation. Editing is unavailable. Choose Ready to restore editing; no real permission check is performed.",
    editing: "Unsaved changes · retained while navigating in this tab.", initial: "Draft example · not saved to a server.",
    saving: "Saving draft · simulation…", finishing: "Recording completion · simulation…",
    failed: "Simulated save failed. Your note is preserved. Use Save draft to retry; no server request was sent.",
    saved: "Draft saved in this tab · simulated, not stored on a server.",
    done: "Visit marked complete in this tab · simulated. The recorded note appears below.",
    invalid: "Enter a note between 1 and 2,000 characters before saving or completing.",
    prerequisite: "Confirm that the work is finished before marking this visit complete.",
    resetQuestion: "Reset this simulated visit and discard its note? This affects only this tab.",
    recommendation: "Recommendation: A for frequent visit work: clear scan lines and a visible next action. B keeps the same task and balanced density with softer notebook surfaces; its separation relies more on spacing. Neither direction is selected or approved.",
    choices: { direction: ["A · Structured", "B · Field notebook"], theme: ["Light", "Dark"], scenario: ["Ready", "Loading", "No assigned visits", "Read only"] }
  },
  fa: {
    skip: "رفتن به بخش بازدید", review: "مقایسهٔ طراحی · نسخهٔ ۱", pending: "هنوز انتخاب یا تأیید نشده است",
    direction: "مسیر طراحی", language: "زبان", theme: "ظاهر", scenario: "حالت شبیه‌سازی",
    fail: "ذخیرهٔ بعدی ناموفق باشد؛ شبیه‌سازی", workspace: "بخش بازدید", myVisits: "بازدیدهای من", assigned: "بازدید محول‌شده",
    open: "باز کردن بازدید", next: "کار بعدی", longTask: "پس از رسیدن فیلتر جایگزین، دستگاه تهویهٔ شمالی را بررسی کنید.",
    back: "بازگشت به بازدیدها", details: "جزئیات بازدید", location: "محل", technician: "تکنسین", unit: "دستگاه",
    instructions: "پیش از شروع", instruction: "پیش از راه‌اندازی دوبارهٔ دستگاه، فیلتر ورودی را بررسی کنید و نتیجهٔ اندازه‌گیری را در یادداشت بازدید ثبت کنید.",
    note: "یادداشت بازدید", noteHelp: "کار انجام‌شده و نتیجهٔ اندازه‌گیری را ثبت کنید؛ حداکثر ۲۰۰۰ نویسه. ذخیرهٔ پیش‌نویس به معنی پایان بازدید نیست.",
    save: "ذخیرهٔ پیش‌نویس", tabOnly: "شبیه‌سازی؛ فقط در این زبانه", confirm: "کار توضیح‌داده‌شده را به پایان رسانده‌ام.",
    complete: "ثبت پایان بازدید", recorded: "یادداشت ثبت‌شده؛ شبیه‌سازی", reset: "بازنشانی بازدید شبیه‌سازی‌شده",
    synthetic: "این نمونه با داده‌های ساختگی تهیه شده است. ذخیره فقط در همین زبانه شبیه‌سازی می‌شود؛ بارگذاری دوباره، یادداشت‌ها را پاک می‌کند.",
    footer: "مقایسهٔ نسخهٔ ۱؛ فرایند، داده‌ها و کارها در هر دو مسیر یکسان‌اند.",
    draft: "فیلتر تعویض شد. پس از راه‌اندازی دوباره، نتیجهٔ اندازه‌گیری پایدار بود.", site: "کارگاه شمالی", person: "سام لی",
    date: "سه‌شنبه؛ ساعت ۰۹:۳۰؛ نمونه", identity: "تکنسین؛ سام لی", assignedStatus: "محول‌شده", completed: "پایان‌یافته؛ شبیه‌سازی",
    loading: "دریافت بازدیدها شبیه‌سازی می‌شود. برای ادامه، حالت آماده را انتخاب کنید.",
    empty: "در این شبیه‌سازی، بازدیدی محول نشده است. برای بازگرداندن نمونه، حالت آماده را انتخاب کنید.",
    access: "حالت فقط‌خواندنی شبیه‌سازی شده است. ویرایش ممکن نیست. با انتخاب حالت آماده، ویرایش برمی‌گردد؛ مجوز واقعی بررسی نمی‌شود.",
    editing: "تغییرها ذخیره نشده‌اند؛ هنگام جابه‌جایی در همین زبانه حفظ می‌شوند.", initial: "پیش‌نویس نمونه؛ روی سرور ذخیره نشده است.",
    saving: "ذخیرهٔ پیش‌نویس شبیه‌سازی می‌شود…", finishing: "ثبت پایان بازدید شبیه‌سازی می‌شود…",
    failed: "ذخیرهٔ شبیه‌سازی‌شده ناموفق بود. یادداشت شما حفظ شده است؛ برای تلاش دوباره، ذخیرهٔ پیش‌نویس را بزنید. درخواستی به سرور ارسال نشد.",
    saved: "پیش‌نویس در همین زبانه ذخیره شد؛ شبیه‌سازی است و روی سرور ذخیره نشده است.",
    done: "پایان بازدید در همین زبانه ثبت شد؛ شبیه‌سازی است. یادداشت ثبت‌شده در پایین دیده می‌شود.",
    invalid: "پیش از ذخیره یا ثبت پایان بازدید، یادداشتی با ۱ تا ۲۰۰۰ نویسه بنویسید.",
    prerequisite: "پیش از ثبت پایان بازدید، پایان کار را تأیید کنید.",
    resetQuestion: "بازدید شبیه‌سازی‌شده بازنشانی و یادداشت آن پاک شود؟ این کار فقط روی همین زبانه اثر دارد.",
    recommendation: "پیشنهاد حرفه‌ای، مسیر الف است؛ برای کار مکرر با بازدیدها، مرزبندی روشن و اقدام بعدی مشخص دارد. مسیر ب همان کار و تراکم متعادل را با کادرهای نرم‌تر ارائه می‌دهد؛ تفکیک بخش‌های آن بیشتر به فاصله‌ها متکی است. هیچ مسیری هنوز انتخاب یا تأیید نشده است.",
    choices: { direction: ["الف؛ ساختارمند", "ب؛ دفتر بازدید"], theme: ["روشن", "تاریک"], scenario: ["آماده", "در حال دریافت", "بدون بازدید", "فقط‌خواندنی"] }
  }
};
const $ = (id) => document.getElementById(id);
const options = { direction: ["a", "b"], language: ["en", "fa"], theme: ["light", "dark"], scenario: ["ready", "loading", "empty", "access"] };
const params = new URLSearchParams(location.search);
const config = Object.fromEntries(Object.entries(options).map(([key, allowed]) => [key, allowed.includes(params.get(key)) ? params.get(key) : allowed[0]]));
let note = COPY[config.language].draft;
let savedNote = null;
let edited = false;
let complete = false;
let busy = false;
let feedback = "initial";
let feedbackKind = "neutral";
const text = () => COPY[config.language];
const unavailable = () => busy || complete || config.scenario !== "ready";
const dirty = () => edited && note !== savedNote;

function announce(key, kind = "neutral") {
  feedback = key; feedbackKind = kind;
  $("note-feedback").textContent = text()[key];
  $("note-feedback").dataset.status = kind;
}

function controls() {
  $("note").readOnly = unavailable();
  $("save").disabled = unavailable();
  $("complete").disabled = unavailable();
  $("confirm-complete").disabled = unavailable();
  for (const key of Object.keys(options)) $(key).disabled = busy;
  $("fail-next").disabled = busy;
  $("reset").disabled = busy;
  $("note-form").setAttribute("aria-busy", String(busy));
}

function renderView(moveFocus = false) {
  const view = location.hash === "#visit" && !["loading", "empty"].includes(config.scenario) ? "visit" : "list";
  document.body.dataset.view = view;
  $("open-visit").setAttribute("aria-current", view === "visit" ? "true" : "false");
  if (moveFocus) (view === "visit" ? $("detail-title") : $("workspace")).focus();
}

function render() {
  const t = text();
  document.documentElement.lang = config.language;
  document.documentElement.dir = config.language === "fa" ? "rtl" : "ltr";
  document.documentElement.dataset.direction = config.direction;
  document.documentElement.dataset.theme = config.theme;
  document.title = config.language === "fa" ? "مقایسهٔ طراحی بازدید؛ نسخهٔ ۱" : "Dispatch Notes — comparison r1";
  for (const el of document.querySelectorAll("[data-copy]")) el.textContent = t[el.dataset.copy];
  for (const [key, allowed] of Object.entries(options)) {
    $(key).value = config[key];
    if (t.choices[key]) Array.from($(key).options).forEach((option, index) => { option.textContent = t.choices[key][index]; });
  }
  for (const [id, key] of Object.entries({ recommendation: "recommendation", identity: "identity", date: "date", site: "site", "detail-site": "site", schedule: "date", "instruction-short": "instruction", technician: "person" })) $(id).textContent = t[key];
  $("visit-status").textContent = complete ? t.completed : t.assignedStatus;
  $("note").value = note;
  const hiddenList = ["loading", "empty"].includes(config.scenario);
  $("visit-card").hidden = hiddenList;
  $("next-task").hidden = hiddenList;
  $("list-state").hidden = !hiddenList;
  $("list-state").textContent = hiddenList ? t[config.scenario] : "";
  $("details").hidden = hiddenList;
  $("completed-note").hidden = !complete;
  $("recorded-text").textContent = complete ? savedNote : "";
  $("note-feedback").textContent = t[config.scenario === "access" ? "access" : feedback];
  $("note-feedback").dataset.status = config.scenario === "access" ? "neutral" : feedbackKind;
  controls(); renderView();
}

for (const key of Object.keys(options)) $(key).addEventListener("change", () => {
  // Values remain allowlisted even when the review DOM is modified.
  const value = $(key).value;
  if (!options[key].includes(value) || busy) return;
  config[key] = value;
  // Only untouched synthetic text can change with language; never replace a person's draft.
  if (key === "language" && !edited && savedNote === null) note = text().draft;
  const query = new URLSearchParams(config);
  history.replaceState(null, "", `?${query}${location.hash}`);
  render();
});
$("note").addEventListener("input", () => {
  note = $("note").value;
  edited = true;
  $("note").removeAttribute("aria-invalid");
  announce("editing");
});

async function commit(final) {
  if (unavailable()) return;
  note = $("note").value;
  if (!note.trim() || note.length > 2000) {
    $("note").setAttribute("aria-invalid", "true");
    announce("invalid", "error"); $("note").focus(); return;
  }
  if (final && !$("confirm-complete").checked) {
    announce("prerequisite", "error"); $("confirm-complete").focus(); return;
  }
  const fail = $("fail-next").checked;
  $("fail-next").checked = false;
  busy = true; controls(); announce(final ? "finishing" : "saving");
  await new Promise((resolve) => setTimeout(resolve, 600)); // Explicitly simulated, not network latency.
  busy = false;
  if (fail) announce("failed", "error");
  else {
    savedNote = note; edited = true; complete = final;
    announce(final ? "done" : "saved", "success");
  }
  render();
  if (complete) $("detail-title").focus();
}
$("note-form").addEventListener("submit", (event) => { event.preventDefault(); commit(false); });
$("complete").addEventListener("click", () => commit(true));
$("reset").addEventListener("click", () => {
  if (busy || !confirm(text().resetQuestion)) return;
  note = text().draft; savedNote = null; edited = false; complete = false; feedback = "initial"; feedbackKind = "neutral";
  $("note").removeAttribute("aria-invalid"); $("confirm-complete").checked = false;
  render();
});
addEventListener("hashchange", () => renderView(true));
addEventListener("beforeunload", (event) => { if (dirty()) { event.preventDefault(); event.returnValue = ""; } });
render();
