/* Pure draft reconciliation; used by the actual UI and deterministic tests. */
(function (scope) {
    "use strict";
    const copy = (value) => JSON.parse(JSON.stringify(value));
    function draftFrom(state) {
        const draft = copy(state.settings);
        draft.advanced.credentialAction = "keep";
        draft.advanced.credential = "";
        return draft;
    }
    function acknowledge(draft, submitted, reply) {
        const next = copy(draft);
        for (const [key, value] of Object.entries(reply.settings[submitted.section])) {
            if (Object.hasOwn(submitted.uiValues, key) && draft[submitted.section][key] === submitted.uiValues[key]) {
                next[submitted.section][key] = value;
            }
        }
        if (submitted.section === "advanced" && draft.advanced.credential === submitted.uiValues.credential &&
            draft.advanced.credentialAction === submitted.uiValues.credentialAction) {
            next.advanced.credential = "";
            next.advanced.credentialAction = "keep";
            next.advanced.credentialConfigured = reply.settings.advanced.credentialConfigured;
        }
        return next;
    }
    function dirty(draft, state, section) {
        const base = draftFrom(state)[section];
        return JSON.stringify(draft[section]) !== JSON.stringify(base);
    }
    const api = {copy, draftFrom, acknowledge, dirty};
    if (typeof module !== "undefined" && module.exports) { module.exports = api; }
    else { scope.WPSModel = api; }
})(typeof window === "undefined" ? globalThis : window);
