/* Curated metadata only: never pass drafts, saved values or secrets to search. */
(function (root) {
    "use strict";
    function normalize(value) {
        return String(value).normalize("NFKC").toLowerCase().replace(/ي/g, "ی").replace(/ك/g, "ک")
            .replace(/[\u064b-\u065f\u0670\u0640]/g, "").replace(/[\s\u200c\u200d-]+/g, "").trim();
    }
    function search(catalog, query, capabilities) {
        const term = normalize(query);
        if (!term) { return []; }
        return catalog.filter(item => capabilities.includes(item.capability) && item.visible !== false)
            .filter(item => [item.label, item.help, ...(item.aliases || [])].some(text => normalize(text).includes(term)))
            .map(({id, group, label, help}) => ({id, group, label, help}));
    }
    function catalog(fa) {
        return [
            {id: "title", group: "general", label: fa ? "عنوان گزارش" : "Report title", help: fa ? "نامی برای شناسایی گزارش" : "Name used to identify this report", aliases: ["name", "heading", "نام گزارش"]},
            {id: "enabled", group: "delivery", label: fa ? "ارسال ایمیلی گزارش" : "Email delivery", help: fa ? "فعال‌سازی ارسال گزارش" : "Enable report delivery", aliases: ["notification", "alerts", "اعلان", "ارسال"]},
            {id: "email", group: "delivery", label: fa ? "دریافت‌کنندهٔ گزارش" : "Recipient address", help: fa ? "نشانی ایمیل دریافت‌کننده" : "Email recipient for scheduled reports", aliases: ["inbox", "recipient email", "گیرنده", "دریافت کننده"]},
            {id: "endpoint", group: "advanced", label: fa ? "نشانی دریافت گزارش" : "Report endpoint", help: fa ? "نشانی امن اتصال فنی" : "Secure technical connection address", aliases: ["webhook", "callback", "وب‌هوک", "وب هوک"]},
            {id: "credentialAction", group: "advanced", label: fa ? "کلید اتصال" : "Connection credential", help: fa ? "حفظ، جایگزینی یا حذف مقدار حساس" : "Keep, replace or remove the credential", aliases: ["API key", "token", "کلید", "توکن"]}
        ].map(item => ({...item, capability: "manage_options"}));
    }
    const api = {normalize, search, catalog};
    if (typeof module !== "undefined" && module.exports) { module.exports = api; }
    else { root.WPSDiscovery = api; }
})(typeof window === "undefined" ? globalThis : window);
