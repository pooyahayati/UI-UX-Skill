(function () {
    "use strict";
    const {createElement: h, useState, useEffect, useRef, createRoot} = wp.element;
    const {TextControl, ToggleControl, SelectControl, Button, Notice, Modal, Spinner, PanelBody, SearchControl} = wp.components;
    const M = WPSModel, cfg = WPSConfig, fa = cfg.lang === "fa";
    const words = {
        heading: ["تنظیمات گزارش", "Report settings"], intro: ["عنوان گزارش و شیوهٔ ارسال را تنظیم کنید. هر بخش جداگانه ذخیره می‌شود.", "Set the report identity and delivery. Each section saves independently."],
        search: ["جست‌وجوی تنظیمات", "Search settings"], searchHelp: ["نام تنظیم یا عبارتی مثل «گیرنده» و «وب‌هوک» را بنویسید.", "Search a setting name or intent, such as recipient or webhook."],
        noResults: ["تنظیمی پیدا نشد. عبارت کوتاه‌تری بنویسید یا از بخش‌های زیر استفاده کنید.", "No setting found. Try a shorter phrase or use the sections below."],
        clearSearch: ["پاک کردن جست‌وجو", "Clear search"], sections: ["بخش‌های تنظیمات", "Settings sections"], results: ["نتیجه", "results"],
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
        resolution: ["انتخاب مقدار", "Resolution"], choose: ["انتخاب کنید", "Choose a value"], useLocal: ["ویرایش من حفظ شود", "Use my edit"], useStored: ["مقدار جدید ذخیره‌شده استفاده شود", "Use newer stored value"],
        localValue: ["ویرایش شما", "Your edit"], storedValue: ["مقدار جدید ذخیره‌شده", "Newer stored value"], on: ["فعال", "Enabled"], off: ["غیرفعال", "Disabled"],
        secretReview: ["مقدار حساس نمایش داده نمی‌شود و ممکن است مدیر دیگر آن را تغییر داده باشد. اقدام خود را تأیید کنید.", "Stored credentials are hidden and may have changed. Confirm your intended action."],
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
        const discovery = cfg.variant === "discovery";
        const fromLocation = () => ["general", "delivery", "advanced"].find(key => location.hash === "#wps-section-" + key) || "general";
        const [activeSection, setActiveSection] = useState(fromLocation), [query, setQuery] = useState("");
        const [focusTarget, setFocusTarget] = useState(null);
        const [server, setServer] = useState(null), [draft, setDraft] = useState(null), [status, setStatus] = useState("loading");
        const [busy, setBusy] = useState(false), [errors, setErrors] = useState({}), [fault, setFault] = useState("none");
        const [conflict, setConflict] = useState(null), [dialog, setDialog] = useState(null);
        const [resolutions, setResolutions] = useState({});
        const [advancedOpen, setAdvancedOpen] = useState(false);
        const draftRef = useRef(null), inFlight = useRef(false), pending = useRef(null);
        const updateDraft = (value) => { draftRef.current = value; setDraft(value); };
        const receiveConflict = (value) => { setConflict(value); setResolutions({}); setStatus("conflict"); };
        const dirty = server && draft ? ["general", "delivery", "advanced"].some(s => M.dirty(draft, server, s)) : false;
        useEffect(() => {
            if (!discovery) { return; }
            const back = () => { setActiveSection(fromLocation()); setFocusTarget("heading-" + fromLocation()); };
            window.addEventListener("popstate", back);
            return () => window.removeEventListener("popstate", back);
        }, []);
        useEffect(() => {
            if (!focusTarget || !draft) { return; }
            const destination = document.getElementById(focusTarget);
            const target = focusTarget === "wps-enabled" ? destination?.querySelector("input[type=checkbox]") : destination;
            if (target && !target.disabled) { target.focus(); target.scrollIntoView({block: "nearest"}); setFocusTarget(null); }
        }, [focusTarget, activeSection, advancedOpen, draft]);
        function navigate(group, field, replace = false) {
            setActiveSection(group);
            if (discovery && location.hash !== "#wps-section-" + group) {
                history[replace ? "replaceState" : "pushState"](null, "", "#wps-section-" + group);
            }
            if (group === "advanced") { setAdvancedOpen(true); }
            setFocusTarget(field ? (field === "email" && !draftRef.current.delivery.enabled ? "wps-email-dependency" : "wps-" + field) : "heading-" + group);
            setQuery("");
        }
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
                    } else { receiveConflict(current); }
                } else { setServer(current); updateDraft(M.draftFrom(current)); setStatus("ready"); }
            } catch (_) { setStatus(server ? "unknown" : "load-error"); }
            finally { inFlight.current = false; setBusy(false); }
        }
        useEffect(() => { load(true); }, []);
        function edit(section, key, value) {
            updateDraft({...draftRef.current, [section]: {...draftRef.current[section], [key]: value}});
            setResolutions({});
            setErrors(old => {
                const next = {...old}; delete next[key];
                if (section === "advanced" && key === "credentialAction") { delete next.credential; }
                return next;
            });
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
                if (detail.code === "conflict") { receiveConflict(detail.current); }
                else if (["validation", "rejected", "denied", "nonce", "invalid_fields", "invalid_values", "invalid_request", "save_failed"].includes(detail.code)) {
                    const fields = {...(detail.fields || {})};
                    // A later keep/remove choice no longer has a replacement field.
                    if (draftRef.current.advanced.credentialAction !== "replace") { delete fields.credential; }
                    setStatus("rejected"); setErrors(fields);
                    const field = Object.keys(fields)[0];
                    if (["endpoint", "credential"].includes(field)) { setAdvancedOpen(true); }
                    if (discovery && field) {
                        navigate(section, field, true);
                    } else if (field) { setTimeout(() => document.getElementById("wps-" + field)?.focus(), 0); }
                } else { pending.current = sent; setStatus("unknown"); }
            } finally { inFlight.current = false; setBusy(false); }
        }
        const button = (key, callback, extra = {}) => h(Button, {key, variant: "secondary", onClick: callback, ...extra}, t(key));
        // Core 6.8 and 7.1.3 both expose these documented styling-transition flags.
        // Explicit adoption avoids deprecated defaults; this is not an experimental control.
        const controlStyle = {__next40pxDefaultSize: true, __nextHasNoMarginBottom: true};
        const input = (section, key, label, help, extra = {}) => h(TextControl, {...controlStyle, id: "wps-" + key, label: t(label),
            help: errors[key] ? t("invalid") + " " + t(help) : t(help), value: draft[section][key], onChange: value => edit(section, key, value),
            "aria-invalid": errors[key] ? "true" : undefined, ...extra});
        const save = (section, key) => button(key, () => submit(section), {variant: "primary", disabled: busy || !M.dirty(draft, server, section) || status === "unknown" || !!conflict});
        const notice = (key, severity = "info") => h(Notice, {key, status: severity, isDismissible: false, className: "wps-status"}, t(key));
        const section = (key, children) => h("section", {key, className: "wps-section", hidden: discovery && activeSection !== key, "aria-labelledby": "heading-" + key},
            h("h2", {id: "heading-" + key, tabIndex: -1}, t(key)), h("div", {className: "wps-fields"}, ...children));
        root.dataset.state = status;
        root.dataset.variant = cfg.variant;
        if (!draft) { return h("div", null, h("h1", null, t("heading")), notice(status === "load-error" ? "loadFailed" : "loading", status === "load-error" ? "error" : "info"),
            status === "load-error" ? button("retry", () => load(false), {disabled: busy}) : h(Spinner)); }
        const review = conflict ? M.reconcile(draft, server, conflict, resolutions) : null;
        function adoptConflict() {
            const merged = M.reconcile(draftRef.current, server, conflict, resolutions);
            if (merged.conflicts.length || inFlight.current) { return; }
            updateDraft(merged.draft); setServer(conflict); setConflict(null); setResolutions({});
            pending.current = null; setDialog(null); setStatus("ready");
        }
        const nodes = [h("h1", {key: "title"}, t("heading")), h("p", {className: "wps-intro", key: "intro"}, t("intro")), h("p", {key: "synthetic"}, t("synthetic"))];
        if (discovery) {
            const results = WPSDiscovery.search(WPSDiscovery.catalog(fa), query, ["manage_options"]);
            nodes.push(h("div", {key: "search", className: "wps-search", onKeyDown: event => {
                if (event.key === "Escape") { setQuery(""); document.getElementById("wps-search")?.focus(); }
            }}, h("label", {id: "wps-search-label", htmlFor: "wps-search", className: "wps-search-label"}, t("search")),
                h(SearchControl, {id: "wps-search", __nextHasNoMarginBottom: true, label: t("search"), "aria-labelledby": "wps-search-label", value: query, onChange: setQuery, "aria-describedby": "wps-search-help"}),
                h("p", {id: "wps-search-help", className: "wps-help"}, t("searchHelp")),
                query ? h("div", {className: "wps-search-results"},
                    h("p", {role: "status"}, results.length ? new Intl.NumberFormat(fa ? "fa" : "en").format(results.length) + " " + t("results") : t("noResults")),
                    h("ul", null, ...results.map(item => h("li", {key: item.id}, h(Button, {variant: "link", onClick: () => navigate(item.group, item.id)}, item.label), h("span", {className: "wps-help"}, item.help)))),
                    button("clearSearch", () => { setQuery(""); document.getElementById("wps-search")?.focus(); })) : null));
            nodes.push(h("nav", {key: "nav", className: "wps-section-nav", "aria-label": t("sections")}, ...["general", "delivery", "advanced"].map(key =>
                h(Button, {key, variant: activeSection === key ? "primary" : "secondary", "aria-current": activeSection === key ? "page" : undefined, onClick: () => navigate(key)}, t(key)))));
        }
        if (status === "saving") { nodes.push(notice("saving")); }
        if (status === "saved") { nodes.push(notice("saved", "success")); }
        if (status === "rejected") { nodes.push(notice("rejected", "error")); }
        if (discovery && Object.keys(errors).length) {
            const errorDestinations = {title: ["general", "title"], enabled: ["delivery", "enabled"], email: ["delivery", "email"], endpoint: ["advanced", "endpoint"], credential: ["advanced", "secret"]};
            nodes.push(h("ul", {key: "field-errors", className: "wps-field-errors", "aria-label": fa ? "تنظیمات نیازمند اصلاح" : "Settings needing correction"},
                ...Object.keys(errors).filter(key => errorDestinations[key]).map(key => h("li", {key},
                    h(Button, {variant: "link", onClick: () => navigate(errorDestinations[key][0], key)},
                        (fa ? "بررسی خطا: " : "Review error: ") + t(errorDestinations[key][1]))))));
        }
        if (status === "unknown") { nodes.push(notice("unknown", "warning"), button("reconcile", () => load(false), {disabled: busy})); }
        if (conflict) { nodes.push(notice("conflict", "warning"), h("div", {className: "wps-actions"}, button("reviewCurrent", () => setDialog("conflict")),
            button("keepEdits", adoptConflict, {disabled: busy || review.conflicts.length > 0}))); }
        if (dirty) { nodes.push(h("p", {key: "unsaved", className: "wps-unsaved", role: "status"}, t("unsaved"))); }
        // ToggleControl owns its generated input/label pair; a custom input id
        // breaks that pair on supported hosts. Keep our destination on a wrapper.
        const toggle = h("div", {id: "wps-enabled"}, h(ToggleControl, {__nextHasNoMarginBottom: true, label: t("enabled"), checked: draft.delivery.enabled, onChange: value => edit("delivery", "enabled", value)}));
        nodes.push(section("general", [input("general", "title", "title", "titleHelp"), ...(cfg.variant === "simple" ? [toggle] : []), h("div", {className: "wps-actions"}, save("general", "saveGeneral"), ...(cfg.variant === "simple" ? [save("delivery", "saveDelivery")] : []))]));
        if (cfg.variant !== "simple") {
            nodes.push(section("delivery", [toggle,
                h("div", {id: discovery ? "wps-email-dependency" : undefined, tabIndex: discovery && !draft.delivery.enabled ? -1 : undefined},
                    input("delivery", "email", "email", draft.delivery.enabled ? "emailHelp" : "dependency", {type: "email", disabled: !draft.delivery.enabled, className: "wps-technical"})),
                h("div", {className: "wps-actions"}, save("delivery", "saveDelivery"), button("reset", () => setDialog("reset"), {disabled: busy || !!conflict || status === "unknown"}))]));
            nodes.push(h("section", {key: "technical", className: "wps-section", hidden: discovery && activeSection !== "advanced"},
                discovery ? h("h2", {id: "heading-advanced", tabIndex: -1}, t("advanced")) : null,
                h(discovery ? "div" : PanelBody, discovery ? {} : {title: t("advanced"), opened: advancedOpen, onToggle: setAdvancedOpen},
                h("div", {className: "wps-fields"}, input("advanced", "endpoint", "endpoint", "endpointHelp", {className: "wps-technical"}),
                    h("p", null, t(draft.advanced.credentialConfigured ? "configured" : "absent")),
                    h(SelectControl, {...controlStyle, id: "wps-credentialAction", label: t("secretAction"), value: draft.advanced.credentialAction, options: ["keep", "replace", "remove"].map(value => ({value, label: t(value)})), onChange: value => edit("advanced", "credentialAction", value)}),
                    draft.advanced.credentialAction === "replace" ? input("advanced", "credential", "secret", "absent", {type: "password", autoComplete: "new-password"}) : null,
                    h("div", {className: "wps-actions"}, save("advanced", "saveAdvanced"))))));
        }
        nodes.push(h("details", {key: "review", className: "wps-review"}, h("summary", null, t("review")), h(SelectControl, {...controlStyle, label: t("fault"), value: fault,
            options: [{value: "none", label: t("normal")}, {value: "reject", label: t("reject")}, {value: "response_loss", label: t("responseLoss")}, {value: "delay", label: t("delay")}], onChange: setFault})));
        if (dialog) {
            nodes.push(h(Modal, {key: "dialog", title: t(dialog === "reset" ? "resetTitle" : "currentValues"), onRequestClose: () => setDialog(null), className: "wps-modal" + (fa ? " wps-modal-fa" : ""), lang: cfg.lang, dir: fa ? "rtl" : "ltr"},
                h("div", {lang: cfg.lang, dir: fa ? "rtl" : "ltr"}, dialog === "reset" ? h("p", null, t("resetText")) :
                    h("div", null, ...review.changes.map(row => {
                        const label = t(row.key === "credentialAction" ? "secretAction" : row.key);
                        const display = value => row.key === "enabled" ? t(value ? "on" : "off") : row.key === "credentialAction" ? t(value) : value;
                        return h("div", {key: row.id, className: "wps-conflict-field"}, h("h3", null, label),
                            h("p", null, t("storedValue") + ": ", h("bdi", null, display(row.stored))),
                            h("p", null, t("localValue") + ": ", h("bdi", null, display(row.local))),
                            row.key === "credentialAction" ? h("p", null, t("secretReview"), " ", t(conflict.settings.advanced.credentialConfigured ? "configured" : "absent")) : null,
                            row.conflict ? h(SelectControl, {...controlStyle, label: t("resolution") + ": " + label, value: resolutions[row.id] || "",
                                options: [{value: "", label: t("choose")}, {value: "local", label: t("useLocal")}, {value: "stored", label: t("useStored")}],
                                onChange: value => setResolutions(old => ({...old, [row.id]: value}))}) : null);
                    })),
                    h("div", {className: "wps-actions"}, button(dialog === "reset" ? "cancel" : "close", () => setDialog(null)), dialog === "reset" ? button("confirm", () => submit("delivery", true), {variant: "primary"}) : button("keepEdits", adoptConflict, {variant: "primary", disabled: busy || review.conflicts.length > 0})))));
        }
        return h("div", null, ...nodes);
    }
    createRoot(root).render(h(cfg.variant === "workspace" ? WPSWorkspace : App));
})();
