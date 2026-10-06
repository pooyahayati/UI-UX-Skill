"use strict";
const byId = id => document.getElementById(id);
const answer = byId("answer"), status = byId("answer-status");
const save = byId("save"), finish = byId("finish");
let saved = null, busy = false, complete = false;
function feedback(text, kind = "ready") {
  status.textContent = text;
  status.dataset.kind = kind;
}
function route(moveFocus = true) {
  if (location.hash === "#main") return;
  const detail = location.hash === "#lesson";
  byId("lessons").hidden = detail;
  byId("lesson").hidden = !detail;
  if (moveFocus) byId(detail ? "lesson-title" : "list-title").focus();
}
function listMode() {
  const mode = byId("list-mode").value;
  byId("lesson-card").hidden = mode !== "ready";
  byId("list-state").hidden = mode === "ready";
  byId("list-state").textContent = mode === "loading"
    ? "دریافت درس‌ها شبیه‌سازی شده است؛ برای بازگشت، وضعیت آزمون را روی آماده بگذارید."
    : mode === "empty" ? "در این وضعیت نمایشی درسی وجود ندارد؛ وضعیت آزمون را به آماده برگردانید." : "";
}
answer.addEventListener("input", () => {
  if (busy) return;
  answer.removeAttribute("aria-invalid");
  complete = false;
  finish.disabled = saved === null || answer.value !== saved;
  byId("result").hidden = true;
  feedback(finish.disabled ? "پاسخ تغییر کرده است؛ دوباره ذخیره کنید." : "پاسخ در حافظهٔ همین صفحه است؛ تأیید سرور نیست.");
});
byId("answer-form").addEventListener("submit", event => {
  event.preventDefault();
  if (busy) return;
  if (!answer.value.trim() || answer.value.length > 600) {
    answer.setAttribute("aria-invalid", "true");
    feedback("یک پاسخ کوتاه بنویسید؛ پاسخ خالی یا بیش از ۶۰۰ نویسه پذیرفته نمی‌شود.", "error");
    answer.focus();
    return;
  }
  const snapshot = answer.value;
  const fail = byId("fail-next").checked;
  byId("fail-next").checked = false;
  answer.removeAttribute("aria-invalid");
  busy = true; save.disabled = true; finish.disabled = true;
  answer.readOnly = true;
  byId("answer-form").setAttribute("aria-busy", "true");
  byId("result").hidden = true;
  feedback("در حال شبیه‌سازی ذخیرهٔ پاسخ…");
  window.setTimeout(() => {
    busy = false; save.disabled = false; answer.readOnly = false;
    byId("answer-form").setAttribute("aria-busy", "false");
    if (fail) {
      feedback("ذخیره شبیه‌سازی‌شده ناموفق بود. پاسخ باقی مانده است؛ دوباره ذخیره کنید.", "error");
      return;
    }
    saved = snapshot; complete = false; finish.disabled = false;
    feedback("پاسخ در حافظهٔ همین صفحه ثبت شد؛ این تأیید سرور نیست.", "success");
    byId("result").hidden = false;
    byId("result-text").textContent = "پاسخ نمایشی ثبت‌شده:";
    byId("saved-answer").textContent = saved;
  }, 500);
});
finish.addEventListener("click", () => {
  if (busy || saved === null || answer.value !== saved || complete) return;
  complete = true; finish.disabled = true;
  feedback("پایان تمرین در نمونه شبیه‌سازی شد؛ پیشرفت واقعی ثبت نشده است.", "success");
  byId("result-text").textContent = "پایان این تمرین شبیه‌سازی شد. پاسخ شما:";
});
byId("list-mode").addEventListener("change", listMode);
window.addEventListener("hashchange", route);
window.addEventListener("beforeunload", event => {
  if (answer.value && answer.value !== saved) { event.preventDefault(); event.returnValue = ""; }
});
route(false); listMode();
