(function () {
    "use strict";
    const {createElement: h, useState, useEffect, useRef, createRoot} = wp.element;
    const {TextControl, ToggleControl, SelectControl, Button, Notice, Modal, Spinner, PanelBody} = wp.components;
    const M = WPSModel, cfg = WPSConfig, fa = cfg.lang === "fa";
    const words = {
        heading: ["تنظیمات گزارش", "Report settings"], intro: ["عنوان گزارش و شیوهٔ ارسال را تنظیم کنید. هر بخش جداگانه ذخیره می‌شود.", "Set the report identity and delivery. Each section saves independently."],
        synthetic: ["نمونهٔ آزمایشی با داده‌های ساختگی؛ به سرویس بیرونی متصل نمی‌شود.", "Synthetic test specimen; no external service is contacted."],
        general: ["مشخصات گزارش", "Report identity"], title: ["عنوان گزارش", "Report title"], titleHelp: ["عنوانی کوتاه و مشخص، حداکثر ۸۰ نویسه.", "A clear title, up to 80 characters."],
        delivery: ["ارسال گزارش", "Report delivery"], enabled: ["ارسال ایمیلی گزارش فعال باشد", "Enable email delivery"], email: ["نشانی ایمیل دریافت‌کنندهٔ گزارش‌های دوره‌ای", "Recipient email address for scheduled reports"],
        emailHelp: ["گزارش به این نشانی ارسال خواهد شد؛ در این نمونه هیچ ایمیلی ارسال نمی‌شود.", "Delivery uses this address; the specimen sends no email."], dependency: ["برای تغییر نشانی، ارسال ایمیلی را فعال کنید. نشانی ذخیره‌شده حذف نمی‌شود.", "Enable email delivery to edit the address. Its stored value is retained."],
        advanced: ["تنظیمات اتصال فنی", "Technical connection settings"], endpoint: ["نشانی دریافت گزارش", "Report endpoint"], endpointHelp: ["نشانی امن با پیشوند HTTPS؛ این نمونه فقط مقدار را ذخیره می‌کند.", "An HTTPS URL; this specimen only stores the value."],
        secretAction: ["مقدار حساس", "Credential action"], keep: ["حفظ مقدار ذخیره‌شده", "Keep stored value"], replace: ["جایگزینی مقدار", "Replace value"], remove: ["حذف مقدار حساس", "Remove credential"], secret: ["مقدار جایگزین", "Replacement credential"],
        configured: ["یک مقدار ذخیره شده است؛ این وضعیت به معنی اتصال موفق نیست.", "A value is stored; this does not confirm service health."], absent: ["مقداری ذخیره نشده است.", "No value is stored."],
        saveGeneral: ["ذخیرهٔ گزارش", "Save report"], saveDelivery: ["ذخیرهٔ ارسال", "Save delivery"], saveAdvanced: ["ذخیرهٔ فنی", "Save technical settings"],
        unsaved: ["تغییرات ذخیره‌نشده دارید.", "You have unsaved changes."], saved: ["مقادیر ارسال‌شده با تأیید سرور ذخیره شدند.", "Submitted values were confirmed saved by the server."],
        saving: ["در حال ذخیره…", "Saving…"], loading: ["در حال دریافت تنظیمات…", "Loading settings…"], loadFailed: ["تنظیمات دریافت نشدند. برای جلوگیری از بازنویسی، ذخیره غیرفعال است.", "Settings could not be loaded. Saving is unavailable to prevent overwriting data."], retry: ["دریافت دوبارهٔ تنظیمات", "Retry loading settings"],
        rejected: ["ذخیره انجام نشد. ورودی‌ها حفظ شده‌اند؛ خطا را اصلاح و دوباره تلاش کنید.", "Save was rejected. Your input is retained; correct the issue and retry."], invalid: ["مقدار معتبر وارد کنید.", "Enter a valid value."],
        unknown: ["نتیجهٔ ذخیره مشخص نیست؛ ممکن است سرور آن را انجام داده باشد. پیش از ارسال دوباره، وضعیت را بررسی کنید.", "The save outcome is unknown; the server may have committed it. Check stored state before resubmitting."], reconcile: ["بررسی نتیجهٔ ذخیره", "Check saved outcome"],
        conflict: ["مدیر دیگری تنظیمات را تغییر داده است. ویرایش شما حفظ شده؛ پیش از ذخیره، مقادیر جدید را بررسی کنید.", "Another administrator changed settings. Your edits are retained; review the newer values before saving."], reviewCurrent: ["مشاهدهٔ مقادیر جدید", "Review newer values"], keepEdits: ["حفظ ویرایش با نسخهٔ جدید", "Keep edits on the newer revision"], currentValues: ["مقادیر ذخیره‌شدهٔ جدید", "Newer stored values"],
        reset: ["بازنشانی بخش ارسال", "Reset delivery section"], resetTitle: ["بازنشانی تنظیمات ارسال؟", "Reset delivery settings?"], resetText: ["فقط بخش ارسال به مقادیر اولیه برمی‌گردد. عنوان گزارش و اتصال فنی تغییر نمی‌کنند.", "Only delivery returns to defaults. Report identity and technical settings remain unchanged."], cancel: ["انصراف", "Cancel"], confirm: ["بازنشانی بخش ارسال", "Reset delivery section"], close: ["بستن", "Close"],
        review: ["کنترل‌های آزمون", "Test review controls"], fault: ["رفتار درخواست آزمایشی", "Test request behavior"], normal: ["ذخیرهٔ عادی", "Normal save"], reject: ["رد درخواست بدون تغییر داده", "Reject without modifying data"], responseLoss: ["ذخیره با پاسخ نامعلوم", "Commit with uncertain response"], delay: ["تأخیر برای آزمون ویرایش هم‌زمان", "Delay to test edits during saving"]
    };
    const t = (key) => words[key][fa ? 0 : 1];
    const root = document.getElementById("wps-root");
    root.lang = cfg.lang; root.dir = fa ? "rtl" : "ltr";
    async function request(input) {
        const controller = new AbortController(), timer = setTimeout(() => controller.abort(), 10000);
        try {
            const response = await fetch(cfg.ajaxUrl + "?action=wps_specimen", {method: "POST", credentials: "same-origin",
                headers: {"Content-Type": "application/json", "X-WPS-Nonce": cfg.nonce}, body: JSON.stringify(input), signal: controller.signal});
            const body = await response.json();
            if (!response.ok || !body.success) { throw Object.assign(new Error("Request not confirmed"), {detail: body.data || {}, status: response.status}); }
            return body.data;
        } finally { clearTimeout(timer); }
    }
    function App() {
        const [server, setServer] = useState(null), [draft, setDraft] = useState(null), [status, setStatus] = useState("loading");
        const [busy, setBusy] = useState(false), [errors, setErrors] = useState({}), [fault, setFault] = useState("none");
        const [conflict, setConflict] = useState(null), [dialog, setDialog] = useState(null);
        const [advancedOpen, setAdvancedOpen] = useState(false);
        const draftRef = useRef(null), inFlight = useRef(false), pending = useRef(null);
        const updateDraft = (value) => { draftRef.current = value; setDraft(value); };
        const dirty = server && draft ? ["general", "delivery", "advanced"].some(s => M.dirty(draft, server, s)) : false;
        useEffect(() => {
            const guard = (event) => { if (dirty || status === "unknown") { event.preventDefault(); event.returnValue = ""; } };
            window.addEventListener("beforeunload", guard);
            return () => window.removeEventListener("beforeunload", guard);
        }, [dirty, status]);
        async function load(initial = false) {
            if (inFlight.current) { return; }
            inFlight.current = true; setBusy(true);
            if (!server) { setStatus("loading"); }
            try {
                const current = await request({operation: "load", fault: initial ? cfg.initialFault : "none"});
                if (pending.current) {
                    if (current.lastRequestId === pending.current.requestId) {
                        updateDraft(M.acknowledge(draftRef.current, pending.current, current));
                        setServer(current); pending.current = null; setStatus("saved");
                    } else { setConflict(current); setStatus("conflict"); }
                } else { setServer(current); updateDraft(M.draftFrom(current)); setStatus("ready"); }
            } catch (_) { setStatus(server ? "unknown" : "load-error"); }
            finally { inFlight.current = false; setBusy(false); }
        }
        useEffect(() => { load(true); }, []);
        function edit(section, key, value) {
            updateDraft({...draftRef.current, [section]: {...draftRef.current[section], [key]: value}});
            setErrors(old => { const next = {...old}; delete next[key]; return next; });
        }
        async function submit(section, reset = false) {
            if (inFlight.current || !server || status === "unknown" || conflict) { return; }
            const uiValues = M.copy(draftRef.current[section]), values = M.copy(uiValues);
            delete values.credentialConfigured;
            const sent = {operation: reset ? "reset" : "save", section, values, uiValues, revision: server.revision,
                requestId: crypto.randomUUID(), fault};
            inFlight.current = true; setBusy(true); setErrors({}); setStatus("saving"); setDialog(null);
            try {
                const reply = await request(sent);
                updateDraft(M.acknowledge(draftRef.current, sent, reply)); setServer(reply); pending.current = null; setStatus("saved");
            } catch (error) {
                const detail = error.detail || {};
                if (detail.code === "conflict") { setConflict(detail.current); setStatus("conflict"); }
                else if (["validation", "rejected", "denied", "nonce", "invalid_fields", "invalid_values", "invalid_request", "save_failed"].includes(detail.code)) {
                    setStatus("rejected"); setErrors(detail.fields || {});
                    const field = Object.keys(detail.fields || {})[0];
                    if (["endpoint", "credential"].includes(field)) { setAdvancedOpen(true); }
                    if (field) { setTimeout(() => document.getElementById("wps-" + field)?.focus(), 0); }
                } else { pending.current = sent; setStatus("unknown"); }
            } finally { inFlight.current = false; setBusy(false); }
        }
        const button = (key, callback, extra = {}) => h(Button, {key, variant: "secondary", onClick: callback, ...extra}, t(key));
        // Core 6.8 and 7.1.3 both expose these documented styling-transition flags.
        // Explicit adoption avoids deprecated defaults; this is not an experimental control.
        const controlStyle = {__next40pxDefaultSize: true, __nextHasNoMarginBottom: true};
        const input = (section, key, label, help, extra = {}) => h(TextControl, {...controlStyle, id: "wps-" + key, label: t(label),
            help: errors[key] ? t("invalid") : t(help), value: draft[section][key], onChange: value => edit(section, key, value),
            "aria-invalid": errors[key] ? "true" : undefined, ...extra});
        const save = (section, key) => button(key, () => submit(section), {variant: "primary", disabled: busy || !M.dirty(draft, server, section) || status === "unknown" || !!conflict});
        const notice = (key, severity = "info") => h(Notice, {key, status: severity, isDismissible: false, className: "wps-status"}, t(key));
        const section = (key, children) => h("section", {key, className: "wps-section", "aria-labelledby": "heading-" + key},
            h("h2", {id: "heading-" + key}, t(key)), h("div", {className: "wps-fields"}, ...children));
        root.dataset.state = status;
        if (!draft) { return h("div", null, h("h1", null, t("heading")), notice(status === "load-error" ? "loadFailed" : "loading", status === "load-error" ? "error" : "info"),
            status === "load-error" ? button("retry", () => load(false), {disabled: busy}) : h(Spinner)); }
        const nodes = [h("h1", {key: "title"}, t("heading")), h("p", {className: "wps-intro", key: "intro"}, t("intro")), h("p", {key: "synthetic"}, t("synthetic"))];
        if (status === "saving") { nodes.push(notice("saving")); }
        if (status === "saved") { nodes.push(notice("saved", "success")); }
        if (status === "rejected") { nodes.push(notice("rejected", "error")); }
        if (status === "unknown") { nodes.push(notice("unknown", "warning"), button("reconcile", () => load(false), {disabled: busy})); }
        if (conflict) { nodes.push(notice("conflict", "warning"), h("div", {className: "wps-actions"}, button("reviewCurrent", () => setDialog("conflict")),
            button("keepEdits", () => { setServer(conflict); setConflict(null); pending.current = null; setStatus("ready"); }))); }
        if (dirty) { nodes.push(h("p", {key: "unsaved", className: "wps-unsaved", role: "status"}, t("unsaved"))); }
        const toggle = h(ToggleControl, {__nextHasNoMarginBottom: true, label: t("enabled"), checked: draft.delivery.enabled, onChange: value => edit("delivery", "enabled", value)});
        nodes.push(section("general", [input("general", "title", "title", "titleHelp"), ...(cfg.variant === "simple" ? [toggle] : []), h("div", {className: "wps-actions"}, save("general", "saveGeneral"), ...(cfg.variant === "simple" ? [save("delivery", "saveDelivery")] : []))]));
        if (cfg.variant !== "simple") {
            nodes.push(section("delivery", [toggle, input("delivery", "email", "email", draft.delivery.enabled ? "emailHelp" : "dependency", {type: "email", disabled: !draft.delivery.enabled, className: "wps-technical"}),
                h("div", {className: "wps-actions"}, save("delivery", "saveDelivery"), button("reset", () => setDialog("reset"), {disabled: busy || !!conflict || status === "unknown"}))]));
            nodes.push(h("section", {key: "technical", className: "wps-section"}, h(PanelBody, {title: t("advanced"), opened: advancedOpen, onToggle: setAdvancedOpen},
                h("div", {className: "wps-fields"}, input("advanced", "endpoint", "endpoint", "endpointHelp", {className: "wps-technical"}),
                    h("p", null, t(draft.advanced.credentialConfigured ? "configured" : "absent")),
                    h(SelectControl, {...controlStyle, label: t("secretAction"), value: draft.advanced.credentialAction, options: ["keep", "replace", "remove"].map(value => ({value, label: t(value)})), onChange: value => edit("advanced", "credentialAction", value)}),
                    draft.advanced.credentialAction === "replace" ? input("advanced", "credential", "secret", "absent", {type: "password", autoComplete: "new-password"}) : null,
                    h("div", {className: "wps-actions"}, save("advanced", "saveAdvanced"))))));
        }
        nodes.push(h("details", {key: "review", className: "wps-review"}, h("summary", null, t("review")), h(SelectControl, {...controlStyle, label: t("fault"), value: fault,
            options: [{value: "none", label: t("normal")}, {value: "reject", label: t("reject")}, {value: "response_loss", label: t("responseLoss")}, {value: "delay", label: t("delay")}], onChange: setFault})));
        if (dialog) {
            nodes.push(h(Modal, {key: "dialog", title: t(dialog === "reset" ? "resetTitle" : "currentValues"), onRequestClose: () => setDialog(null), className: "wps-modal" + (fa ? " wps-modal-fa" : ""), lang: cfg.lang, dir: fa ? "rtl" : "ltr"},
                h("div", {lang: cfg.lang, dir: fa ? "rtl" : "ltr"}, dialog === "reset" ? h("p", null, t("resetText")) :
                    h("div", null, h("p", null, t("title") + ": " + conflict.settings.general.title), h("p", null, t("email") + ": ", h("bdi", null, conflict.settings.delivery.email))),
                    h("div", {className: "wps-actions"}, button(dialog === "reset" ? "cancel" : "close", () => setDialog(null)), dialog === "reset" ? button("confirm", () => submit("delivery", true), {variant: "primary"}) : null))));
        }
        return h("div", null, ...nodes);
    }
    createRoot(root).render(h(App));
})();
