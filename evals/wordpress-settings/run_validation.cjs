/* R13 error ownership inside the owned real wp-admin hosts. */
const {chromium} = require("playwright");
const {execFileSync} = require("node:child_process");
const fs = require("node:fs"), path = require("node:path"), crypto = require("node:crypto");
const assert = require("node:assert/strict");
const repo = path.resolve(__dirname, "../.."), fixture = path.join(repo, "evals/fixtures/wordpress-settings/plugin");
const output = process.env.WPS_EVIDENCE_DIR, docker = process.env.WPS_DOCKER || "docker";
const settingsOnly = process.argv.includes("--settings-only");
if (process.argv.slice(2).some(arg => arg !== "--settings-only")) { throw new Error("Only --settings-only is supported"); }
if (!output || !fs.statSync(output).isDirectory()) { throw new Error("Set WPS_EVIDENCE_DIR to an existing directory outside product source"); }
const relativeOutput = path.relative(repo, path.resolve(output));
if (!relativeOutput || (!relativeOutput.startsWith(".." + path.sep) && !path.isAbsolute(relativeOutput))) {
    throw new Error("Evidence output must be outside product source");
}
const observations = [], errors = [], warnings = [], captures = [], compatibility = [];
function sha(file) {
    let data = fs.readFileSync(file);
    if (!file.endsWith(".ttf")) { data = Buffer.from(data.toString("utf8").replace(/\r\n/g, "\n")); }
    return crypto.createHash("sha256").update(data).digest("hex");
}
function fixtureHashes() {
    const result = {};
    function walk(folder) {
        for (const name of fs.readdirSync(folder).sort()) {
            const file = path.join(folder, name);
            if (fs.statSync(file).isDirectory()) { walk(file); }
            else { result[path.relative(fixture, file).split(path.sep).join("/")] = sha(file); }
        }
    }
    walk(fixture); return result;
}
function behaviorHashes() {
    return Object.fromEntries(["references/products/wordpress-plugin.md", "references/products/wordpress/components.md", "references/products/wordpress/settings.md"]
        .map(name => [name, sha(path.join(repo, "skills/ui-ux-skill", name))]));
}
const initialFixture = fixtureHashes(), initialBehavior = behaviorHashes(), runnerHash = sha(__filename);
const record = (id, detail) => observations.push({id, status: "passed", method: "real-admin-browser", detail});
const baseFor = service => service === "current" ? "http://127.0.0.1:8790" : "http://127.0.0.1:8791";
const containerFor = service => "uiux-wps-specimen-" + service + "-1";
const password = service => execFileSync(docker, ["exec", containerFor(service), "printenv", "WPS_ADMIN_PASSWORD"], {encoding: "utf8"}).trim();
const waitState = (page, state) => page.locator("#wps-root[data-state=" + state + "]").waitFor();
async function login(context, service, user = "wps-admin") {
    const page = await context.newPage();
    page.on("pageerror", error => errors.push(error.message));
    page.on("console", message => { if (message.type() === "warning") { warnings.push(message.text()); } });
    await page.goto(baseFor(service) + "/wp-login.php");
    await page.locator("#user_login").fill(user);
    await page.locator("#user_pass").fill(password(service));
    await Promise.all([page.waitForURL(/wp-admin/), page.locator("#wp-submit").click()]);
    return page;
}
async function open(page, service, variant = "discovery", language = "en") {
    await page.goto(baseFor(service) + "/wp-admin/options-general.php?page=wps-specimen&variant=" + variant + "&lang=" + language);
    await waitState(page, "ready");
}
async function api(page, data) {
    return page.evaluate(async data => {
        const response = await fetch(WPSConfig.ajaxUrl + "?action=wps_specimen", {method: "POST", credentials: "same-origin",
            headers: {"Content-Type": "application/json", "X-WPS-Nonce": WPSConfig.nonce}, body: JSON.stringify(data)});
        return {status: response.status, body: await response.json()};
    }, data);
}
const savedState = async page => {
    const result = await api(page, {operation: "load"});
    assert.equal(result.status, 200); assert.equal(result.body.success, true); return result.body.data;
};
const nav = (page, name) => page.getByRole("navigation", {name: "Settings sections"}).getByRole("button", {name, exact: true});
async function focusIs(page, id) { await page.waitForFunction(id => document.activeElement?.id === id, id); }
async function result(page, query, label) {
    await page.locator("#wps-search").fill(query);
    const button = page.locator(".wps-search-results").getByRole("button", {name: label, exact: true});
    await button.waitFor(); await button.click();
}
async function verifyToggleAssociation(page) {
    await result(page, "notification", "Email delivery");
    const checkbox = page.getByRole("checkbox", {name: "Enable email delivery", exact: true});
    const id = await checkbox.getAttribute("id");
    assert.ok(id, "Native toggle lacks its generated input ID"); await focusIs(page, id);
    const label = page.locator("#wps-enabled label");
    assert.equal(await label.getAttribute("for"), id, "Visible toggle label is not associated with its actual checkbox");
    const before = await checkbox.isChecked();
    await label.click(); assert.equal(await checkbox.isChecked(), !before, "Label click did not toggle the actual checkbox");
    await label.click(); assert.equal(await checkbox.isChecked(), before, "Second label click did not restore the prior toggle state");
}
async function capture(page, name, language, variant, service) {
    await page.evaluate(() => document.fonts.ready);
    const ownedModal = page.locator(".wps-modal[role=dialog]");
    let modalSettlement = null;
    if (await ownedModal.isVisible()) {
        modalSettlement = await ownedModal.evaluate(async node => {
            const animations = document.getAnimations().filter(animation => {
                const target = animation.effect?.target;
                return target instanceof Element && (node.contains(target) || target.contains(node)) &&
                    Number.isFinite(animation.effect.getComputedTiming().endTime);
            });
            let timer;
            try {
                await Promise.race([Promise.all(animations.map(animation => animation.finished.catch(() => {}))),
                    new Promise((_, reject) => { timer = setTimeout(() => reject(new Error("Owned modal animation did not settle")), 3000); })]);
            } finally { clearTimeout(timer); }
            const box = () => {
                const value = node.getBoundingClientRect(); return [value.x, value.y, value.width, value.height];
            };
            let previous = box(), stable = 0;
            for (let frame = 0; frame < 120; frame++) {
                await new Promise(requestAnimationFrame);
                const current = box();
                stable = current.every((value, index) => Math.abs(value - previous[index]) < 0.1) ? stable + 1 : 0;
                previous = current;
                if (stable >= 4) {
                    return {finiteAnimations: animations.length, stableFrames: stable,
                        box: {x: current[0], y: current[1], width: current[2], height: current[3]},
                        opacity: getComputedStyle(node).opacity, viewportHeight: innerHeight};
                }
            }
            throw new Error("Owned modal geometry did not settle");
        });
        assert.equal(modalSettlement.opacity, "1", "Settled owned modal must be opaque");
        assert.ok(modalSettlement.box.y >= -1 && modalSettlement.box.y + modalSettlement.box.height <= modalSettlement.viewportHeight + 1,
            "Settled owned modal extends beyond the viewport");
    }
    const layout = await page.locator("#wps-root").evaluate(root => ({
        direction: getComputedStyle(root).direction, font: getComputedStyle(root).fontFamily,
        viewport: {width: innerWidth, height: innerHeight}, overflow: document.documentElement.scrollWidth > innerWidth,
        state: root.dataset.state, hostDirection: getComputedStyle(document.documentElement).direction,
        toolbar: !!document.querySelector("#wpadminbar"), menu: !!document.querySelector("#adminmenuwrap"),
        hostNotices: document.querySelectorAll("#wpbody-content > .notice, #wpbody-content > .update-nag").length,
        regular: document.fonts.check('16px "Vazirmatn"'), bold: document.fonts.check('700 16px "Vazirmatn"')
    }));
    assert.equal(layout.overflow, false, name + " document overflow");
    assert.equal(layout.direction, language === "fa" ? "rtl" : "ltr");
    assert.equal(layout.toolbar, true); assert.equal(layout.menu, true);
    if (language === "fa") {
        const cdp = await page.context().newCDPSession(page);
        try {
            await cdp.send("DOM.enable"); await cdp.send("CSS.enable");
            const {root} = await cdp.send("DOM.getDocument");
            layout.renderedFonts = {};
            const bodySelector = await page.locator("#wps-root label").count() ? "#wps-root label" : "#wps-root .wps-section p";
            for (const selector of ["#wps-root h1", bodySelector]) {
                const {nodeId} = await cdp.send("DOM.querySelector", {nodeId: root.nodeId, selector});
                assert.ok(nodeId, "Missing Persian text target: " + selector);
                const {fonts} = await cdp.send("CSS.getPlatformFontsForNode", {nodeId});
                assert.ok(fonts.some(font => font.familyName === "Vazirmatn" && font.isCustomFont));
                layout.renderedFonts[selector] = fonts;
            }
        } finally { await cdp.detach(); }
    }
    const filename = name + ".png";
    await page.screenshot({path: path.join(output, filename), fullPage: !modalSettlement, animations: "disabled"});
    captures.push({file: filename, sha256: crypto.createHash("sha256").update(fs.readFileSync(path.join(output, filename))).digest("hex"),
        language, variant, service, theme: "light", modalSettlement,
        capturePolicy: "Wait for finite owned-modal animations and stable geometry; modal captures use the actual viewport, other pages use full-page. Screenshot finite animations disabled; animation aesthetics not evaluated.", ...layout});
}
async function inspectCompatibility(page, service) {
    const details = await page.evaluate(() => {
        const controls = ["TextControl", "ToggleControl", "SelectControl", "Button", "Notice", "Modal", "Spinner", "PanelBody", "SearchControl"];
        return {exports: Object.fromEntries(controls.map(name => [name, typeof wp.components[name] !== "undefined"])),
            scripts: [...document.scripts].filter(node => /wp-components|wp-element|wps-/.test(node.id)).map(node => ({id: node.id, src: node.src})),
            styles: [...document.querySelectorAll("link[rel=stylesheet]")].filter(node => /wp-components|wps-style/.test(node.id) || node.href.includes("load-styles.php"))
                .map(node => ({id: node.id, href: node.href, loadedRules: node.sheet?.cssRules.length || 0,
                    handles: [...new URL(node.href).searchParams].filter(([key]) => key.startsWith("load")).flatMap(([, value]) => value.split(","))})),
            actualOwnedLanguage: document.getElementById("wps-root").lang, hostLanguage: document.documentElement.lang,
            actualRootDirection: getComputedStyle(document.getElementById("wps-root")).direction};
    });
    assert.ok(Object.values(details.exports).every(Boolean), "Public component export absent on " + service);
    assert.ok(details.styles.some(style => (style.id === "wp-components-css" || style.handles.includes("wp-components")) && style.loadedRules > 0), "Missing loaded native components stylesheet");
    assert.ok(details.styles.some(style => style.id === "wps-style-css"), "Missing scoped fixture stylesheet");
    const version = JSON.parse(execFileSync(docker, ["exec", containerFor(service), "php", "-r",
        "require '/var/www/html/wp-load.php'; echo json_encode(array('core'=>get_bloginfo('version'),'php'=>PHP_VERSION,'plugins'=>get_option('active_plugins')));"], {encoding: "utf8"}));
    const asset = JSON.parse(execFileSync(docker, ["exec", containerFor(service), "php", "-r",
        "echo json_encode(require '/fixture/plugin/index.asset.php');"], {encoding: "utf8"}));
    assert.deepEqual(asset.dependencies, ["wp-components", "wp-element"]);
    assert.deepEqual(version.plugins, ["wps-specimen/wps-specimen.php"]);
    if (service === "minimum") { assert.equal(version.core, "6.8"); }
    compatibility.push({service, base: baseFor(service), ...version, asset_metadata: asset,
        asset_metadata_kind: "maintained no-build dependency record, not generated build evidence", ...details});
}
// R13 actual-host error ownership. Shared helper snapshot comes from the
// retained discovery runner; this file's complete bytes bind the execution.
(async () => {
    const browser = await chromium.launch({channel: process.env.WPS_BROWSER_CHANNEL || "msedge", headless: true});
    try {
        for (const [service, language, width] of [["current", "en", 1440], ["minimum", "en", 390], ["current", "fa", 390]]) {
            execFileSync(docker, ["exec", containerFor(service), "php", "/fixture/bootstrap.php", "--reset"]);
            const context = await browser.newContext({viewport: {width, height: 1000}});
            const page = await login(context, service);
            await open(page, service, "discovery", language); await inspectCompatibility(page, service);
            const root = page.locator("#wps-root"), endpoint = page.locator("#wps-endpoint");
            const section = key => page.locator('.wps-section-nav button').nth(["general", "delivery", "advanced"].indexOf(key)).click();
            const saveSection = key => root.locator(key === "advanced" ? '.wps-section:has(#wps-endpoint)' : '.wps-section:has(#heading-' + key + ')').locator(".wps-actions button").first().click();
            const before = await savedState(page);
            await section("advanced"); await endpoint.fill("http://invalid-r13.example.test");
            await saveSection("advanced"); await waitState(page, "rejected"); await focusIs(page, "wps-endpoint");
            assert.equal(await endpoint.getAttribute("aria-invalid"), "true");
            await section("general"); await page.locator("#wps-title").fill("R13 title " + service + language);
            await saveSection("general"); await waitState(page, "saved");
            assert.equal(await root.locator(".wps-field-errors button").count(), 1);
            const after = await savedState(page);
            assert.equal(after.settings.general.title, "R13 title " + service + language);
            assert.equal(after.settings.advanced.endpoint, before.settings.advanced.endpoint);
            await page.locator("#wps-search").fill("webhook");
            await root.locator(".wps-field-errors button").click(); await focusIs(page, "wps-endpoint");
            assert.equal(await endpoint.getAttribute("aria-invalid"), "true");
            assert.equal(await endpoint.inputValue(), "http://invalid-r13.example.test");
            const help = await endpoint.evaluate(node => (node.getAttribute("aria-describedby") || "").split(/\s+/).map(id => document.getElementById(id)?.textContent || "").join(" "));
            assert.match(help, language === "fa" ? /معتبر/ : /valid value/);
            await section("general"); await page.goBack(); await focusIs(page, "heading-advanced");
            assert.equal(await endpoint.getAttribute("aria-invalid"), "true");
            await capture(page, `r13-errors-${service}-${language}-${width}`, language, "discovery", service);
            record(`ERR-retained-${service}-${language}`, "Rejected endpoint remains unsaved, invalid and reachable after authoritative title save, search, section and browser-back navigation; helper text and focus verified.");
            for (const corrected of [true, false]) {
                await endpoint.fill("http://delayed-r13.example.test");
                let release; const held = new Promise(resolve => { release = resolve; });
                await page.route("**/admin-ajax.php?action=wps_specimen", async route => {
                    if (route.request().postDataJSON()?.operation === "save") { const response = await route.fetch(); await held; await route.fulfill({response}); }
                    else await route.continue();
                });
                try {
                    await saveSection("advanced"); await waitState(page, "saving");
                    if (corrected) await endpoint.fill("https://corrected-r13.example.test");
                    await section("general"); await page.locator("#wps-search").focus();
                } finally { release(); }
                await waitState(page, "rejected"); await page.unroute("**/admin-ajax.php?action=wps_specimen");
                if (corrected) {
                    await focusIs(page, "wps-search");
                    assert.equal(await endpoint.isVisible(), false, "Stale response must not jump sections/focus");
                    assert.equal(await root.locator(".wps-field-errors button").count(), 0);
                    await section("advanced");
                    assert.equal(await endpoint.getAttribute("aria-invalid"), null);
                    assert.equal(await endpoint.inputValue(), "https://corrected-r13.example.test");
                } else { await focusIs(page, "wps-endpoint"); assert.equal(await endpoint.getAttribute("aria-invalid"), "true"); }
                assert.equal((await savedState(page)).settings.advanced.endpoint, before.settings.advanced.endpoint);
                record(`ERR-delayed-${corrected ? "corrected" : "unchanged"}-${service}-${language}`, corrected ? "Newer HTTPS draft survives delayed rejection without stale field error, section reveal or focus jump; server endpoint unchanged." : "Unchanged rejected HTTP draft receives field error and reveal/focus; server endpoint unchanged.");
            }
            await context.close();
        }
        assert.deepEqual(errors, []); assert.deepEqual(warnings, []);
        assert.deepEqual(fixtureHashes(), initialFixture); assert.deepEqual(behaviorHashes(), initialBehavior);
        const now = new Date();
        const report = {schema_version: 1, recorded_on: new Intl.DateTimeFormat("en-CA", {timeZone: "Asia/Tehran", year: "numeric", month: "2-digit", day: "2-digit"}).format(now), recorded_at: now.toISOString(),
            scope: "R13 section and submitted-value error ownership", complete: true, omitted_observations: [],
            runner_sha256: runnerHash, fixture_hashes: initialFixture, behavior_hashes: initialBehavior, browser: browser.version(), compatibility, captures, observations,
            javascript_errors: errors, console_warnings: warnings};
        fs.writeFileSync(path.join(output, "r13-validation-results.json"), JSON.stringify(report, null, 2));
        console.log(JSON.stringify({passed: observations.length, captures: captures.length, complete: true}));
    } finally { await browser.close(); }
})().catch(error => { console.error(error.stack); process.exitCode = 1; });
