/* Synthetic operational examples. No external requests, persistence or job engine. */
(function () {
    "use strict";
    const {createElement: h, useState, useEffect} = wp.element;
    const {TextControl, SelectControl, Button, Notice, Modal, Spinner} = wp.components;
    const words = {
        heading: ["مدیریت گزارش‌ها", "Report workspace"], intro: ["گزارش‌ها را مرور کنید و وضعیت اتصال و پردازش را ببینید.", "Review reports and inspect connection and processing status."],
        demo: ["نمونهٔ تعاملی با داده‌های ساختگی؛ تغییر وضعیت‌ها نمایشی است و کاری به سرور ارسال نمی‌شود.", "Interactive demonstration with synthetic data; state changes are simulated and no work is sent to a server."],
        sections: ["بخش‌های مدیریت گزارش", "Workspace sections"], reports: ["گزارش‌ها", "Reports"], connection: ["اتصال سرویس", "Connection"], jobs: ["پردازش گزارش", "Background work"],
        filter: ["جست‌وجوی گزارش", "Find a report"], status: ["وضعیت گزارش", "Report status"], all: ["همهٔ گزارش‌ها", "All reports"], ready: ["آمادهٔ بررسی", "Ready for review"], draft: ["پیش‌نویس", "Draft"],
        first: ["گزارش هفتگی فروش", "Weekly sales report"], second: ["گزارش تحویل سفارش‌ها", "Order delivery report"],
        view: ["مشاهدهٔ گزارش", "View report"], details: ["جزئیات گزارش", "Report details"], close: ["بستن", "Close"],
        noMatch: ["گزارشی با این فیلتر پیدا نشد. جست‌وجو یا وضعیت را تغییر دهید.", "No reports match. Change the search or status filter."],
        clear: ["پاک کردن فیلترها", "Clear filters"], scope: ["فقط گزارش‌های همین سایت آزمایشی نمایش داده می‌شوند.", "Only records from this synthetic site are shown."],
        detail: ["این گزارش ساختگی برای بررسی مسیر فهرست تا جزئیات است؛ دادهٔ واقعی مشتری ندارد.", "This synthetic report demonstrates list-to-detail navigation; it contains no real customer data."],
        configured: ["وضعیت نمایشی: اطلاعات اتصال تنظیم شده است.", "Demonstration: connection configuration is present."],
        health: ["سلامت اتصال بررسی نشده است. وجود کلید به معنی اتصال موفق نیست.", "Connection health has not been checked. A stored credential does not confirm a healthy connection."],
        configure: ["رفتن به تنظیمات اتصال", "Open connection settings"],
        queued: ["در صف نمایشی؛ پردازش هنوز شروع نشده است.", "Demonstration queued; processing has not started."],
        running: ["پردازش نمایشی در جریان است؛ هنوز تکمیل نشده است.", "Demonstration processing; not yet complete."],
        failed: ["پردازش نمایشی ناموفق بود؛ داده‌های گزارش حفظ شده‌اند.", "Demonstration processing failed; report data is retained."],
        completed: ["پردازش نمایشی تکمیل شد؛ این وضعیت تأیید انجام کار در سرور نیست.", "Demonstration completed; this does not confirm a server-side job."],
        start: ["نمایش حالت پردازش", "Simulate processing"], fail: ["نمایش حالت خطا", "Simulate failure"], finish: ["نمایش حالت تکمیل", "Simulate completion"], retry: ["تلاش دوبارهٔ نمایشی", "Retry demonstration"],
        loading: ["در حال آماده‌سازی نمایشی فهرست…", "Preparing the demonstration list…"], loadDemo: ["نمایش حالت بارگذاری", "Simulate loading"],
        export: ["دریافت فایل در این نمونه فعال نیست", "Download is unavailable in this specimen"]
    };
    const t = key => words[key][WPSConfig.lang === "fa" ? 0 : 1];
    const controlStyle = {__next40pxDefaultSize: true, __nextHasNoMarginBottom: true};
    window.WPSWorkspace = function () {
        const fa = WPSConfig.lang === "fa";
        const [tab, setTab] = useState("reports"), [filter, setFilter] = useState(""), [status, setStatus] = useState("all");
        const [selected, setSelected] = useState(null), [job, setJob] = useState("queued"), [loading, setLoading] = useState(false);
        const [focusTarget, setFocusTarget] = useState(null);
        useEffect(() => {
            if (!focusTarget) { return; }
            document.getElementById(focusTarget)?.focus();
            setFocusTarget(null);
        }, [focusTarget, job, filter, status]);
        const changeJob = next => { setJob(next); setFocusTarget("wps-job-state"); };
        useEffect(() => {
            if (!loading) { return; }
            const timer = setTimeout(() => setLoading(false), 600);
            return () => clearTimeout(timer);
        }, [loading]);
        const records = [{id: "REP-204", title: t("first"), status: "ready"}, {id: "REP-205", title: t("second"), status: "draft"}];
        const rows = records.filter(row => (status === "all" || row.status === status) && row.title.toLocaleLowerCase().includes(filter.toLocaleLowerCase().trim()));
        const button = (key, onClick, props = {}) => h(Button, {onClick, variant: "secondary", ...props}, t(key));
        const root = document.getElementById("wps-root"); root.dataset.variant = "workspace"; root.dataset.state = "ready";
        const settings = "options-general.php?page=wps-specimen&variant=discovery&lang=" + WPSConfig.lang + "#wps-section-advanced";
        return h("div", null, h("h1", null, t("heading")), h("p", {className: "wps-intro"}, t("intro")), h("p", null, t("demo")),
            h("nav", {className: "wps-section-nav", "aria-label": t("sections")}, ...["reports", "connection", "jobs"].map(key => button(key, () => setTab(key), {key, variant: tab === key ? "primary" : "secondary", "aria-current": tab === key ? "page" : undefined}))),
            tab === "reports" ? h("section", {className: "wps-section", "aria-labelledby": "wps-reports-heading"}, h("h2", {id: "wps-reports-heading"}, t("reports")), h("p", {className: "wps-help"}, t("scope")),
                h("div", {className: "wps-filters"}, h(TextControl, {...controlStyle, id: "wps-report-filter", label: t("filter"), value: filter, onChange: setFilter}),
                    h(SelectControl, {...controlStyle, id: "wps-report-status", label: t("status"), value: status, onChange: setStatus, options: ["all", "ready", "draft"].map(value => ({value, label: t(value)}))})),
                loading ? h("p", {role: "status"}, h(Spinner), t("loading")) : rows.length ? h("ul", {className: "wps-records"}, ...rows.map(row => h("li", {key: row.id},
                    h("div", null, h("h3", null, row.title), h("p", {className: "wps-help"}, h("bdi", null, row.id), " · ", t(row.status))), button("view", () => setSelected(row), {"aria-label": t("view") + ": " + row.title})))) :
                    h(Notice, {status: "info", isDismissible: false}, t("noMatch"), button("clear", () => {setFilter(""); setStatus("all"); setFocusTarget("wps-report-filter");})),
                button("loadDemo", () => setLoading(true), {disabled: loading})) : null,
            tab === "connection" ? h("section", {className: "wps-section", "aria-labelledby": "wps-connection-heading"}, h("h2", {id: "wps-connection-heading"}, t("connection")),
                h("p", null, t("configured")), h(Notice, {status: "warning", isDismissible: false}, t("health")), h(Button, {variant: "secondary", href: settings}, t("configure"))) : null,
            tab === "jobs" ? h("section", {className: "wps-section", "aria-labelledby": "wps-jobs-heading"}, h("h2", {id: "wps-jobs-heading"}, t("jobs")),
                h("p", null, h("bdi", null, "JOB-204")), h("div", {id: "wps-job-state", tabIndex: -1, role: "status", "data-state": job},
                    h(Notice, {status: job === "failed" ? "error" : job === "completed" ? "success" : "info", isDismissible: false}, t(job))),
                h("div", {className: "wps-actions"}, job === "queued" ? button("start", () => changeJob("running"), {variant: "primary"}) : null,
                    job === "running" ? [button("fail", () => changeJob("failed"), {key: "fail"}), button("finish", () => changeJob("completed"), {key: "finish", variant: "primary"})] : null,
                    job === "failed" ? button("retry", () => changeJob("queued"), {variant: "primary"}) : null),
                h("p", {className: "wps-help"}, t("export"))) : null,
            selected ? h(Modal, {title: t("details"), onRequestClose: () => setSelected(null), className: "wps-modal" + (fa ? " wps-modal-fa" : ""), dir: fa ? "rtl" : "ltr", lang: WPSConfig.lang},
                h("h2", null, selected.title), h("p", null, h("bdi", null, selected.id)), h("p", null, t("detail")), button("close", () => setSelected(null))) : null);
    };
})();
