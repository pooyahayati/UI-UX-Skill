/* Real wp-admin tests. Requires an already available Playwright/browser runtime. */
const {chromium} = require("playwright");
const {execFileSync} = require("node:child_process");
const fs = require("node:fs"), path = require("node:path"), assert = require("node:assert/strict");
const crypto = require("node:crypto");
const docker = process.env.WPS_DOCKER || "docker";
const output = process.env.WPS_EVIDENCE_DIR;
if (!output || !fs.statSync(output).isDirectory()) { throw new Error("Set an existing WPS_EVIDENCE_DIR outside product source"); }
const repo = path.resolve(__dirname, "../..");
if (path.resolve(output).startsWith(repo + path.sep)) { throw new Error("Evidence output must be outside product source"); }
const observations = [], errors = [], warnings = [];
function fixtureHashes() {
    const folder = path.join(repo, "evals/fixtures/wordpress-settings/plugin"), hashes = {};
    function walk(dir) {
        for (const name of fs.readdirSync(dir).sort()) {
            const file = path.join(dir, name);
            if (fs.statSync(file).isDirectory()) { walk(file); continue; }
            let bytes = fs.readFileSync(file);
            if (!file.endsWith(".ttf")) { bytes = Buffer.from(bytes.toString("utf8").replace(/\r\n/g, "\n")); }
            hashes[path.relative(folder, file).split(path.sep).join("/")] = crypto.createHash("sha256").update(bytes).digest("hex");
        }
    }
    walk(folder); return hashes;
}
const fixtureStart = fixtureHashes();
const password = (service) => execFileSync(docker, ["exec", "uiux-wps-specimen-" + service + "-1", "printenv", "WPS_ADMIN_PASSWORD"], {encoding: "utf8"}).trim();
async function login(context, base, user, pass) {
    const page = await context.newPage();
    page.on("pageerror", error => errors.push(error.message));
    page.on("console", message => { if (message.type() === "warning") { warnings.push(message.text()); } });
    await page.goto(base + "/wp-login.php");
    await page.locator("#user_login").fill(user); await page.locator("#user_pass").fill(pass);
    await Promise.all([page.waitForURL(/wp-admin/), page.locator("#wp-submit").click()]);
    return page;
}
async function open(page, base, suffix = "") {
    await page.goto(base + "/wp-admin/options-general.php?page=wps-specimen&lang=en" + suffix);
    await page.locator("#wps-root[data-state=ready]").waitFor();
}
async function api(page, data, nonceOverride) {
    return page.evaluate(async ({data, nonceOverride}) => {
        const response = await fetch(WPSConfig.ajaxUrl + "?action=wps_specimen", {method: "POST", credentials: "same-origin",
            headers: {"Content-Type": "application/json", "X-WPS-Nonce": nonceOverride ?? WPSConfig.nonce}, body: JSON.stringify(data)});
        return {status: response.status, body: await response.json()};
    }, {data, nonceOverride});
}
const waitState = (page, state) => page.locator("#wps-root[data-state=" + state + "]").waitFor();
const record = (id, detail) => observations.push({id, status: "passed", method: "real-admin-browser", detail});
(async () => {
    for (const service of ["current", "minimum"]) {
        execFileSync(docker, ["exec", "uiux-wps-specimen-" + service + "-1", "php", "/fixture/bootstrap.php", "--reset"], {stdio: "pipe"});
    }
    const browser = await chromium.launch({channel: process.env.WPS_BROWSER_CHANNEL || "msedge", headless: true});
    try {
        const context = await browser.newContext({viewport: {width: 1440, height: 1100}});
        const base = "http://127.0.0.1:8790", pass = password("current");
        const page = await login(context, base, "wps-admin", pass);
        await open(page, base, "&variant=simple");
        assert.equal(await page.locator("#wps-root").getByRole("textbox").count(), 1);
        assert.equal(await page.locator("#wps-root").getByRole("checkbox").count(), 1);
        assert.equal(await page.locator("#wps-root [role=tablist]").count(), 0);
        record("WP-01", "Simple form uses real TextControl/ToggleControl/Button; no tabs.");
        await open(page, base);
        for (const name of ["Report identity", "Report delivery", "Technical connection settings"]) {
            assert.equal(await page.locator("#wps-root").getByRole("heading", {level: 2, name, exact: true}).isVisible(), true);
        }
        await page.getByRole("button", {name: "Technical connection settings", exact: true}).click();
        assert.ok(await page.locator("#wps-endpoint").isVisible());
        record("WP-02", "Identity/delivery sections and secondary technical disclosure.");
        const before = (await api(page, {operation: "load"})).body.data;
        assert.equal(await page.locator("#wps-email").isDisabled(), true);
        assert.match(await page.locator("#wps-root").innerText(), /stored value is retained/);
        await page.getByRole("checkbox", {name: "Enable email delivery"}).check();
        assert.equal(await page.locator("#wps-email").isDisabled(), false);
        record("WP-03", "Dependent email explains prerequisite and retains stored value.");
        await page.goto(base + "/wp-admin/options-general.php?page=wps-specimen&lang=en&fault=load");
        await waitState(page, "load-error");
        assert.equal(await page.locator("#wps-root input").count(), 0);
        await page.getByRole("button", {name: "Retry loading settings"}).click(); await waitState(page, "ready");
        record("WP-04", "First-load failure blocks default-looking controls; retry recovers.");
        await page.getByRole("checkbox", {name: "Enable email delivery"}).check();
        await page.locator("#wps-email").fill("not-an-email");
        await page.getByRole("button", {name: "Save delivery", exact: true}).click(); await waitState(page, "rejected");
        assert.equal(await page.locator("#wps-email").inputValue(), "not-an-email");
        assert.equal((await api(page, {operation: "load"})).body.data.revision, before.revision);
        assert.equal(await page.locator("#wps-email").getAttribute("aria-invalid"), "true");
        await page.locator("#wps-email").fill("updated@example.test");
        await page.getByRole("button", {name: "Save delivery", exact: true}).click(); await waitState(page, "saved");
        await page.locator("#wps-root summary").click();
        await page.getByLabel("Test request behavior").selectOption("reject");
        await page.locator("#wps-title").fill("Rejected intention");
        await page.getByRole("button", {name: "Save report", exact: true}).click(); await waitState(page, "rejected");
        assert.equal(await page.locator("#wps-title").inputValue(), "Rejected intention");
        record("WP-05", "Server validation and confirmed rejection preserve input and avoid false success.");
        await page.getByLabel("Test request behavior").selectOption("delay");
        await page.locator("#wps-title").fill("Submitted intention");
        let saves = 0;
        const countSave = request => { if (request.url().includes("action=wps_specimen") && request.postDataJSON()?.operation === "save") { saves++; } };
        page.on("request", countSave);
        await page.getByRole("button", {name: "Save report", exact: true}).evaluate(button => { button.click(); button.click(); });
        await page.locator("#wps-title").fill("Newer intention"); await waitState(page, "saved");
        assert.equal(saves, 1); page.off("request", countSave);
        assert.equal(await page.locator("#wps-title").inputValue(), "Newer intention");
        assert.ok(await page.locator(".wps-unsaved").isVisible());
        const navigated = new Promise(resolve => page.once("dialog", async dialog => { assert.equal(dialog.type(), "beforeunload"); await dialog.dismiss(); resolve(); }));
        await page.evaluate(() => { location.href = "/wp-admin/index.php"; });
        await navigated;
        record("WP-06", "One request for duplicate clicks; newer edits and unsaved-navigation guard retained.");
        await page.getByLabel("Test request behavior").selectOption("none");
        await page.getByRole("button", {name: "Technical connection settings", exact: true}).click();
        await page.getByLabel("Credential action").selectOption("replace");
        await page.locator("#wps-credential").fill("synthetic-credential-for-testing");
        await page.getByRole("button", {name: "Save technical settings", exact: true}).click(); await waitState(page, "saved");
        const secretState = await api(page, {operation: "load"});
        assert.equal(secretState.body.data.settings.advanced.credentialConfigured, true);
        assert.ok(!JSON.stringify(secretState).includes("synthetic-credential-for-testing"));
        const deniedNonce = await api(page, {operation: "save", section: "general", values: {title: "Denied"}, revision: secretState.body.data.revision, requestId: "denied-test"}, "invalid");
        assert.equal(deniedNonce.status, 403);
        const readerContext = await browser.newContext();
        const reader = await login(readerContext, base, "wps-reader", pass);
        const denials = await reader.evaluate(async () => {
            const results = [];
            for (const operation of ["load", "save"]) {
                const r = await fetch("/wp-admin/admin-ajax.php?action=wps_specimen", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({operation, section: "general", values: {title: "Denied"}})});
                results.push({status: r.status, body: await r.json()});
            }
            return results;
        });
        assert.deepEqual(denials.map(result => result.status), [403, 403]); await readerContext.close();
        assert.deepEqual((await api(page, {operation: "load"})).body.data, secretState.body.data);
        const deliveryBeforeReset = (await api(page, {operation: "load"})).body.data;
        await page.getByRole("button", {name: "Reset delivery section", exact: true}).click();
        await page.getByRole("dialog").getByRole("button", {name: "Reset delivery section", exact: true}).click(); await waitState(page, "saved");
        const afterReset = (await api(page, {operation: "load"})).body.data;
        assert.deepEqual(afterReset.settings.general, deliveryBeforeReset.settings.general);
        assert.deepEqual(afterReset.settings.advanced, deliveryBeforeReset.settings.advanced);
        assert.equal(afterReset.settings.delivery.enabled, false);
        await page.getByLabel("Credential action").selectOption("remove");
        await page.getByRole("button", {name: "Save technical settings", exact: true}).click(); await waitState(page, "saved");
        assert.equal((await api(page, {operation: "load"})).body.data.settings.advanced.credentialConfigured, false);
        record("WP-07", "Capability/nonce denial preserves data; secret replacement/removal stays masked; reset preserves other sections.");
        await page.getByRole("checkbox", {name: "Enable email delivery"}).check();
        await page.locator("#wps-email").fill("draft-only@example.test");
        const sectionBefore = (await api(page, {operation: "load"})).body.data;
        await page.locator("#wps-title").fill("Section-only change");
        await page.getByRole("button", {name: "Save report", exact: true}).click(); await waitState(page, "saved");
        const sectionAfter = (await api(page, {operation: "load"})).body.data;
        assert.deepEqual(sectionAfter.settings.delivery, sectionBefore.settings.delivery);
        assert.equal(await page.locator("#wps-email").inputValue(), "draft-only@example.test");
        record("WP-11", "Saving identity preserves unrelated stored and unsaved delivery values.");
        let dropped = false;
        await page.route("**/admin-ajax.php?action=wps_specimen", async route => {
            const data = route.request().postDataJSON();
            if (!dropped && data.operation === "save") { dropped = true; await route.fetch(); await route.abort("failed"); }
            else { await route.continue(); }
        });
        await page.locator("#wps-title").fill("Committed before response loss");
        await page.getByRole("button", {name: "Save report", exact: true}).click(); await waitState(page, "unknown");
        assert.equal(await page.getByRole("button", {name: "Save report", exact: true}).isDisabled(), true);
        await page.locator("#wps-title").fill("Edit after unknown outcome");
        await page.getByRole("button", {name: "Check saved outcome"}).click(); await waitState(page, "saved");
        assert.equal(await page.locator("#wps-title").inputValue(), "Edit after unknown outcome");
        assert.equal((await api(page, {operation: "load"})).body.data.settings.general.title, "Committed before response loss");
        await page.unroute("**/admin-ajax.php?action=wps_specimen");
        record("WP-12", "Actual aborted response after server commit reconciles by request ID without losing newer input.");
        await open(page, base);
        const secondContext = await browser.newContext();
        const second = await login(secondContext, base, "wps-second", pass); await open(second, base);
        await page.locator("#wps-title").fill("First administrator");
        await page.getByRole("button", {name: "Save report", exact: true}).click(); await waitState(page, "saved");
        await second.locator("#wps-title").fill("Second administrator");
        await second.getByRole("button", {name: "Save report", exact: true}).click(); await waitState(second, "conflict");
        assert.equal(await second.locator("#wps-title").inputValue(), "Second administrator");
        assert.equal((await api(page, {operation: "load"})).body.data.settings.general.title, "First administrator");
        await second.getByRole("button", {name: "Review newer values"}).click();
        assert.match(await second.getByRole("dialog").innerText(), /First administrator/);
        await second.keyboard.press("Escape");
        await second.getByRole("button", {name: "Keep edits on the newer revision"}).click();
        await second.getByRole("button", {name: "Save report", exact: true}).click(); await waitState(second, "saved");
        assert.equal((await api(page, {operation: "load"})).body.data.settings.general.title, "Second administrator");
        await secondContext.close();
        record("WP-13", "Two real admin sessions expose conflict and require deliberate rebase before saving retained intent.");
        // An error returned after the user collapses the secondary panel must reopen it.
        await open(page, base);
        await page.getByRole("button", {name: "Technical connection settings", exact: true}).click();
        await page.locator("#wps-endpoint").fill("http://invalid.example.test");
        await page.route("**/admin-ajax.php?action=wps_specimen", async route => {
            if (route.request().postDataJSON()?.operation === "save") {
                const response = await route.fetch();
                await page.getByRole("button", {name: "Technical connection settings", exact: true}).click();
                await route.fulfill({response});
            } else { await route.continue(); }
        });
        await page.getByRole("button", {name: "Save technical settings", exact: true}).click(); await waitState(page, "rejected");
        assert.equal(await page.locator("#wps-endpoint").isVisible(), true);
        assert.equal(await page.locator("#wps-endpoint").getAttribute("aria-invalid"), "true");
        await page.unroute("**/admin-ajax.php?action=wps_specimen");
        observations.find(row => row.id === "WP-05").detail += " A late validation error reopens a user-collapsed secondary panel.";
        const minContext = await browser.newContext();
        const min = await login(minContext, "http://127.0.0.1:8791", "wps-admin", password("minimum"));
        await open(min, "http://127.0.0.1:8791");
        await min.locator("#wps-title").fill("Minimum-version save");
        await min.getByRole("button", {name: "Save report", exact: true}).click(); await waitState(min, "saved");
        await min.getByRole("button", {name: "Technical connection settings", exact: true}).click();
        await min.getByRole("button", {name: "Reset delivery section", exact: true}).click(); await min.keyboard.press("Escape");
        const versions = ["current", "minimum"].map(service => JSON.parse(execFileSync(docker, ["exec", "uiux-wps-specimen-" + service + "-1", "php", "/fixture/bootstrap.php"], {encoding: "utf8"})));
        assert.deepEqual(versions.map(item => item.core), ["7.1.3", "6.8"]);
        for (const version of versions) { assert.deepEqual(version.active_plugins, ["wps-specimen/wps-specimen.php"]); }
        record("WP-08", "Basic controls, save and modal run on 6.8 and 7.1.3 without Gutenberg; PHP 8.3.35.");
        await minContext.close();
        // Host-only asset isolation.
        await page.goto(base + "/wp-admin/index.php");
        assert.equal(await page.locator('script[src*="wps-specimen"],link[href*="wps-specimen"]').count(), 0);
        await page.goto(base + "/");
        assert.equal(await page.locator('script[src*="wps-specimen"],link[href*="wps-specimen"]').count(), 0);
        await open(page, base);
        await page.locator("#wps-title").fill("گزارش هفتگی");
        await page.getByRole("button", {name: "Save report", exact: true}).click(); await waitState(page, "saved");
        for (const variant of ["multi", "simple"]) {
            for (const width of [1440, 390]) {
                await page.setViewportSize({width, height: width === 390 ? 844 : 1100});
                await page.goto(base + "/wp-admin/options-general.php?page=wps-specimen&variant=" + variant);
                await waitState(page, "ready"); await page.evaluate(() => document.fonts.ready);
                const layout = await page.locator("#wps-root").evaluate(root => ({direction: getComputedStyle(root).direction,
                    font: getComputedStyle(root).fontFamily, overflow: document.documentElement.scrollWidth > innerWidth,
                    regular: document.fonts.check('16px "Vazirmatn"'), bold: document.fonts.check('700 16px "Vazirmatn"')}));
                assert.equal(layout.direction, "rtl"); assert.equal(layout.overflow, false); assert.equal(layout.regular, true); assert.equal(layout.bold, true);
                const cdp = await context.newCDPSession(page);
                await cdp.send("DOM.enable"); await cdp.send("CSS.enable");
                const documentNode = await cdp.send("DOM.getDocument");
                const fonts = {};
                for (const selector of ["#wps-root h1", "#wps-root label"]) {
                    const node = await cdp.send("DOM.querySelector", {nodeId: documentNode.root.nodeId, selector});
                    fonts[selector] = (await cdp.send("CSS.getPlatformFontsForNode", {nodeId: node.nodeId})).fonts;
                    assert.ok(fonts[selector].some(font => font.familyName === "Vazirmatn" && font.isCustomFont));
                }
                await cdp.detach(); layout.rendered_fonts = fonts;
                await page.screenshot({path: path.join(output, "persian-" + variant + "-" + width + ".png"), fullPage: true});
                observations.push({id: "VIEW-" + variant + "-" + width, status: "passed", method: "real-admin-browser", detail: layout});
            }
        }
        await page.goto(base + "/wp-admin/options-general.php?page=wps-specimen"); await waitState(page, "ready");
        const reset = page.getByRole("button", {name: "بازنشانی بخش ارسال", exact: true});
        await reset.focus(); await page.keyboard.press("Enter");
        const modal = page.getByRole("dialog"); await modal.waitFor();
        for (let i = 0; i < 7; i++) {
            await page.keyboard.press("Tab");
            assert.equal(await modal.evaluate(dialog => dialog.contains(document.activeElement)), true);
        }
        await page.screenshot({path: path.join(output, "persian-reset-dialog-390.png"), fullPage: true});
        await page.keyboard.press("Escape"); await modal.waitFor({state: "hidden"});
        assert.equal(await reset.evaluate(button => document.activeElement === button), true);
        await page.getByRole("button", {name: "تنظیمات اتصال فنی", exact: true}).click();
        assert.equal(await page.locator("#wps-endpoint").evaluate(input => getComputedStyle(input).direction), "ltr");
        await page.setViewportSize({width: 780, height: 1100});
        await page.evaluate(() => { document.querySelector("#wps-root").style.zoom = "2"; });
        const zoomLayout = await page.evaluate(() => ({zoom: getComputedStyle(document.querySelector("#wps-root")).zoom,
            overflow: document.documentElement.scrollWidth > innerWidth,
            rootWidth: document.querySelector("#wps-root").getBoundingClientRect().width}));
        assert.equal(zoomLayout.zoom, "2"); assert.equal(zoomLayout.overflow, false); assert.ok(zoomLayout.rootWidth <= 780);
        await page.screenshot({path: path.join(output, "persian-zoom-200.png"), fullPage: true});
        observations.push({id: "VIEW-zoom-200", status: "passed", method: "real-admin-browser", detail: {...zoomLayout,
            limitation: "Owned-surface CSS 200% zoom stress, not native browser zoom or assistive-technology certification"}});
        await page.evaluate(() => { document.querySelector("#wps-root").style.zoom = "1"; });
        record("WP-09", "Persian real-admin narrow layout, local regular/bold fonts, mixed-direction endpoint and modal Tab/Escape/return focus.");
        record("WP-14", "Both variants captured at 1440/390 widths and 200% CSS zoom stress; no horizontal document overflow.");
        assert.deepEqual(errors, [], "Browser JavaScript errors");
        assert.deepEqual([...new Set(warnings)], [], "Component compatibility warnings must be resolved, not hidden");
        assert.deepEqual(fixtureHashes(), fixtureStart, "Specimen source changed during browser verification");
        fs.writeFileSync(path.join(output, "browser-results.json"), JSON.stringify({schema_version: 1, browser: browser.version(), versions,
            fixture: "evals/fixtures/wordpress-settings/plugin", fixture_hashes: fixtureStart, observations, javascript_errors: errors, console_warnings: [...new Set(warnings)]}, null, 2));
        process.stdout.write(JSON.stringify({passed: observations.length, javascript_errors: errors.length, output}) + "\n");
    } finally { await browser.close(); }
})().catch(error => {
    fs.writeFileSync(path.join(output, "failed-browser-results.json"), JSON.stringify({observations, javascript_errors: errors, error: error.message}, null, 2));
    console.error(error.stack); process.exitCode = 1;
});
