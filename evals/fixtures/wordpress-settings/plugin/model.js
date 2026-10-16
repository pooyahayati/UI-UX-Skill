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
    function reconcile(draft, base, current, choices = {}) {
        const next = copy(draft), changes = [], conflicts = [];
        for (const [section, key] of [["general", "title"], ["delivery", "enabled"], ["delivery", "email"], ["advanced", "endpoint"]]) {
            const original = base.settings[section][key], local = draft[section][key], stored = current.settings[section][key];
            const id = section + "." + key, conflict = local !== original && stored !== original && local !== stored;
            if (local !== original || stored !== original) { changes.push({id, section, key, local, stored, conflict}); }
            if (local === original || local === stored) { next[section][key] = stored; }
            else if (conflict) {
                if (choices[id] === "stored") { next[section][key] = stored; }
                else if (choices[id] !== "local") { conflicts.push(id); }
            }
        }
        next.advanced.credentialConfigured = current.settings.advanced.credentialConfigured;
        // Presence cannot reveal a peer's secret replacement. On a stale revision,
        // explicitly confirm any local replace/remove intent without exposing values.
        if (draft.advanced.credentialAction !== "keep" && current.revision !== base.revision) {
            const id = "advanced.credentialAction";
            changes.push({id, section: "advanced", key: "credentialAction", local: draft.advanced.credentialAction, stored: "keep", conflict: true});
            if (choices[id] === "stored") { next.advanced.credentialAction = "keep"; next.advanced.credential = ""; }
            else if (choices[id] !== "local") { conflicts.push(id); }
        }
        return {draft: next, changes, conflicts};
    }
    const api = {copy, draftFrom, acknowledge, dirty, reconcile};
    if (typeof module !== "undefined" && module.exports) { module.exports = api; }
    else { scope.WPSModel = api; }
})(typeof window === "undefined" ? globalThis : window);
