/* Execute the actual App handlers with deterministic hooks/HTTP; not a browser substitute. */
const assert = require("node:assert/strict");
const fs = require("node:fs"), path = require("node:path"), vm = require("node:vm");
const {randomUUID} = require("node:crypto");
const M = require("../fixtures/wordpress-settings/plugin/model.js");
const appSource = fs.readFileSync(path.join(__dirname, "../fixtures/wordpress-settings/plugin/app.js"), "utf8");
const initial = () => ({revision: 1, settings: {general: {title: "Initial"},
    delivery: {enabled: false, email: "stored@example.test"},
    advanced: {endpoint: "https://old.example.test", credentialConfigured: false}}});
function host() {
    let state = initial();
    const writes = [];
    return {
        get state() { return M.copy(state); }, writes,
        async fetch(_, options) {
            const input = JSON.parse(options.body);
            const result = (ok, data, status = 200) => ({ok, status, json: async () => ({success: ok, data: M.copy(data)})});
            if (input.operation === "load") { return result(true, state); }
            if (input.revision !== state.revision) { return result(false, {code: "conflict", current: state}, 409); }
            const values = M.copy(input.values);
            if (input.section === "advanced") {
                if (values.credentialAction !== "keep") { state.settings.advanced.credentialConfigured = values.credentialAction === "replace"; }
                delete values.credential; delete values.credentialAction;
            }
            Object.assign(state.settings[input.section], values);
            state.revision++; state.lastRequestId = input.requestId;
            writes.push({section: input.section, revision: input.revision, endpoint: values.endpoint});
            return result(true, state);
        }
    };
}
async function mount(service, variant = "multi") {
    const slots = [], effects = [], root = {dataset: {}};
    let cursor = 0, App, tree;
    const h = (type, props, ...children) => ({type, props: props || {}, children: children.flat(Infinity).filter(x => x != null && x !== false)});
    const context = {
        wp: {element: {
            createElement: h,
            useState(value) { const i = cursor++; if (!(i in slots)) slots[i] = value;
                return [slots[i], next => { slots[i] = typeof next === "function" ? next(slots[i]) : next; }]; },
            useRef(value) { const i = cursor++; if (!(i in slots)) slots[i] = {current: value}; return slots[i]; },
            useEffect(callback) { const i = cursor++; if (!(i in slots)) { slots[i] = true; effects.push(callback); } },
            createRoot() { return {render(node) { App = node.type; }}; }
        }, components: Object.fromEntries(["TextControl", "ToggleControl", "SelectControl", "Button", "Notice", "Modal", "Spinner", "PanelBody", "SearchControl"].map(name => [name, name]))},
        WPSModel: M, WPSDiscovery: require("../fixtures/wordpress-settings/plugin/discovery.js"),
        location: {hash: ""}, history: {pushState() {}, replaceState() {}},
        WPSConfig: {lang: "en", variant, ajaxUrl: "/ajax", nonce: "synthetic"},
        document: {getElementById: id => id === "wps-root" ? root : null},
        window: {addEventListener() {}, removeEventListener() {}},
        fetch: service.fetch, AbortController, setTimeout, clearTimeout, crypto: {randomUUID}
    };
    vm.runInNewContext(appSource, context, {filename: "app.js"});
    function render() { cursor = 0; tree = App(); }
    async function flush() { await new Promise(setImmediate); render(); }
    function nodes(node = tree) { return !node || typeof node !== "object" ? [] : [node, ...node.children.flatMap(nodes)]; }
    function find(predicate) { const found = nodes().find(predicate); assert.ok(found, "Expected UI control exists"); return found; }
    render(); for (const effect of effects) effect(); await flush();
    return {
        get state() { return root.dataset.state; },
        get tree() { return tree; },
        async change(label, value) { find(n => n.props.label === label).props.onChange(value); await flush(); },
        async click(text) { const node = find(n => n.type === "Button" && n.children.includes(text));
            assert.notEqual(node.props.disabled, true, "Action must be enabled: " + text); await node.props.onClick(); await flush(); },
        value(label) { return find(n => n.props.label === label).props.value; },
        disabled(text) { return !!find(n => n.type === "Button" && n.children.includes(text)).props.disabled; },
        async closeDialog() { find(n => n.type === "Modal").props.onRequestClose(); await flush(); }
    };
}
module.exports = {host, mount};
if (require.main === module) (async () => {
    const service = host(), a = await mount(service), b = await mount(service);
    await a.change("Credential action", "replace");
    await a.change("Replacement credential", "synthetic-only-test-value");
    await a.change("Report title", "Unrelated unsaved intention");
    await b.change("Report endpoint", "https://peer.example.test");
    await b.click("Save technical settings");
    await a.click("Save technical settings");
    assert.equal(a.state, "conflict");
    assert.equal(a.disabled("Keep edits on the newer revision"), true);
    await a.click("Review newer values");
    await a.change("Resolution: Credential action", "local");
    await a.closeDialog();
    await a.click("Keep edits on the newer revision");
    await a.click("Save technical settings");
    assert.equal(service.state.settings.advanced.endpoint, "https://peer.example.test", "Untouched peer endpoint must not be overwritten");
    assert.equal(service.writes.at(-1).endpoint, "https://peer.example.test");
    assert.equal(service.state.settings.advanced.credentialConfigured, true);
    assert.equal(a.value("Report title"), "Unrelated unsaved intention");
    assert.equal(a.value("Credential action"), "keep");
    const c = await mount(service), d = await mount(service);
    await c.change("Report title", "My title");
    await d.change("Report title", "Peer title"); await d.click("Save report");
    await c.click("Save report");
    const beforeCancel = service.state;
    await c.click("Review newer values"); await c.closeDialog();
    assert.deepEqual(service.state, beforeCancel);
    assert.equal(c.value("Report title"), "My title");
    assert.equal(c.disabled("Keep edits on the newer revision"), true);
    await c.click("Review newer values");
    await c.change("Resolution: Report title", "local");
    await c.change("Report title", "Later local edit"); // An edit invalidates stale choices.
    assert.equal(c.disabled("Keep edits on the newer revision"), true);
    await c.change("Resolution: Report title", "local");
    await c.click("Keep edits on the newer revision");
    await d.change("Report title", "Racing peer title"); await d.click("Save report");
    await c.click("Save report");
    assert.equal(c.state, "conflict");
    assert.equal(c.value("Report title"), "Later local edit");
    assert.equal(service.state.settings.general.title, "Racing peer title");
    await c.click("Review newer values");
    await c.change("Resolution: Report title", "stored");
    await c.click("Keep edits on the newer revision");
    assert.equal(c.value("Report title"), "Racing peer title");
    assert.equal(c.disabled("Save report"), true);
    console.log("PASS: actual App conflict adoption retains the peer endpoint and independent local intent.");
    console.log("PASS: actual App requires field decisions, preserves cancellation/late edits and detects a second race.");
})().catch(error => { console.error(error); process.exitCode = 1; });
