/* Actual App handlers; browser focus/host behavior is checked separately. */
const assert = require("node:assert/strict");
const {host, mount} = require("./test_conflict.cjs");
const nodes = node => !node || typeof node !== "object" ? [] : [node, ...node.children.flatMap(nodes)];
const field = (ui, label) => nodes(ui.tree).find(n => n.props.label === label);
const links = ui => nodes(ui.tree).filter(n => n.type === "Button").flatMap(n => n.children).filter(x => typeof x === "string" && x.startsWith("Review error:"));
function validatingHost(delay = null) {
    const service = host(), fetch = service.fetch;
    service.fetch = async (url, options) => {
        const sent = JSON.parse(options.body), errors = {};
        if (sent.operation === "save" && sent.revision !== service.state.revision) return fetch(url, options);
        if (sent.section === "advanced" && !sent.values.endpoint.startsWith("https://")) errors.endpoint = "invalid";
        if (sent.section === "delivery" && sent.values.enabled && !sent.values.email.includes("@")) errors.email = "invalid";
        if (Object.keys(errors).length) {
            if (delay) await delay;
            return {ok: false, status: 422, json: async () => ({success: false, data: {code: "validation", fields: errors}})};
        }
        return fetch(url, options);
    };
    return service;
}
async function retainIndependentErrors() {
    const service = validatingHost(), ui = await mount(service, "discovery");
    await ui.change("Report endpoint", "http://invalid.example.test");
    await ui.click("Save technical settings");
    assert.equal(field(ui, "Report endpoint").props["aria-invalid"], "true");
    await ui.change("Enable email delivery", true);
    await ui.change("Recipient email address for scheduled reports", "invalid");
    await ui.click("Save delivery");
    assert.equal(links(ui).length, 2, "Independent field errors survive another rejected section");
    await ui.change("Report title", "Saved report title");
    await ui.click("Save report");
    assert.equal(service.state.settings.general.title, "Saved report title");
    assert.equal(service.state.settings.advanced.endpoint, "https://old.example.test");
    assert.equal(field(ui, "Report endpoint").props["aria-invalid"], "true", "Other section save must retain endpoint error");
    assert.equal(links(ui).length, 2);
    await ui.click("Report identity");
    await ui.change("Search settings", "webhook");
    await ui.click("Review error: Report endpoint");
    assert.equal(field(ui, "Report endpoint").props["aria-invalid"], "true");
    await ui.change("Report endpoint", "https://corrected.example.test");
    assert.deepEqual(links(ui), ["Review error: Recipient email address for scheduled reports"]);
    await ui.click("Save technical settings");
    assert.equal(service.state.settings.advanced.endpoint, "https://corrected.example.test");
    assert.equal(links(ui).length, 1);
}
async function lateResponse(correct) {
    let release;
    const delayed = new Promise(resolve => { release = resolve; });
    const service = validatingHost(delayed), ui = await mount(service, "discovery");
    await ui.change("Report endpoint", "http://invalid.example.test");
    const pending = ui.click("Save technical settings");
    await new Promise(setImmediate);
    if (correct) await ui.change("Report endpoint", "https://corrected.example.test");
    release(); await pending;
    assert.equal(ui.value("Report endpoint"), correct ? "https://corrected.example.test" : "http://invalid.example.test");
    assert.equal(field(ui, "Report endpoint").props["aria-invalid"], correct ? undefined : "true", "Only the rejected submitted value may acquire an error");
    assert.equal(links(ui).length, correct ? 0 : 1);
    assert.equal(service.state.settings.advanced.endpoint, "https://old.example.test");
    assert.equal(ui.disabled("Save technical settings"), false, "Rejected/newer input remains unsaved");
}
async function deniedRetry() {
    const service = validatingHost(), fetch = service.fetch;
    let denied = false;
    service.fetch = (url, options) => denied && JSON.parse(options.body).operation === "save"
        ? Promise.resolve({ok: false, status: 403, json: async () => ({success: false, data: {code: "nonce"}})})
        : fetch(url, options);
    const ui = await mount(service, "discovery");
    await ui.change("Report endpoint", "http://invalid.example.test");
    await ui.click("Save technical settings"); denied = true;
    await ui.click("Save technical settings");
    assert.equal(field(ui, "Report endpoint").props["aria-invalid"], "true", "Denied retry does not revalidate the unchanged endpoint");
    assert.equal(links(ui).length, 1);
}
async function adoptValidatedPeer() {
    const service = validatingHost(), a = await mount(service, "discovery"), b = await mount(service);
    await a.change("Report endpoint", "http://invalid.example.test"); await a.click("Save technical settings");
    await b.change("Report endpoint", "https://peer.example.test"); await b.click("Save technical settings");
    await a.click("Save technical settings");
    assert.equal(a.state, "conflict"); await a.click("Review newer values");
    await a.change("Resolution: Report endpoint", "stored"); await a.click("Keep edits on the newer revision");
    assert.equal(a.value("Report endpoint"), "https://peer.example.test");
    assert.equal(field(a, "Report endpoint").props["aria-invalid"], undefined);
    assert.equal(links(a).length, 0);
}
(async () => {
    const failures = [];
    for (const [name, check] of [["section ownership", retainIndependentErrors], ["obsolete delayed error", () => lateResponse(true)], ["unchanged delayed rejection", () => lateResponse(false)], ["denied retry", deniedRetry], ["adopt validated peer", adoptValidatedPeer]]) {
        try { await check(); console.log("PASS: " + name); }
        catch (error) { failures.push(name); console.error("FAIL: " + name + ": " + error.message); }
    }
    assert.deepEqual(failures, []);
})().catch(error => { console.error(error); process.exitCode = 1; });
