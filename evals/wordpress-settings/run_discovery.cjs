/* R12 discovery and internal-page observations inside the owned real wp-admin host. */
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
async function workspaceChecks(browser) {
    const context = await browser.newContext({viewport: {width: 1440, height: 1100}});
    try {
        const page = await login(context, "current"); await open(page, "current", "workspace");
        const calls = [];
        const observeWork = request => {
            if (request.url().includes("action=wps_specimen") ||
                (["fetch", "xhr"].includes(request.resourceType()) && new URL(request.url()).origin !== baseFor("current"))) {
                calls.push({url: request.url(), method: request.method()});
            }
        };
        page.on("request", observeWork);
        const workspaceNav = name => page.getByRole("navigation", {name: "Workspace sections"}).getByRole("button", {name, exact: true});
        assert.match(await page.locator("#wps-root").innerText(), /synthetic data.*state changes are simulated/);
        assert.equal(await page.locator(".wps-records li").count(), 2);
        await page.locator("#wps-report-filter").fill("Weekly"); await page.locator("#wps-report-status").selectOption("ready");
        assert.equal(await page.locator(".wps-records li").count(), 1);
        assert.match(await page.locator(".wps-records").innerText(), /REP-204/);
        const opener = page.getByRole("button", {name: "View report: Weekly sales report", exact: true});
        await opener.focus(); await page.keyboard.press("Enter");
        const modal = page.getByRole("dialog", {name: "Report details", exact: true});
        await modal.waitFor(); assert.match(await modal.innerText(), /REP-204/); assert.match(await modal.innerText(), /no real customer data/);
        for (let step = 0; step < 6; step++) {
            await page.keyboard.press("Tab"); assert.equal(await modal.evaluate(node => node.contains(document.activeElement)), true);
        }
        await page.keyboard.press("Escape"); await modal.waitFor({state: "hidden"});
        assert.equal(await opener.evaluate(node => node === document.activeElement), true);
        assert.equal(await page.locator("#wps-report-filter").inputValue(), "Weekly");
        assert.equal(await page.locator("#wps-report-status").inputValue(), "ready");
        await opener.click(); await modal.getByRole("button", {name: "Close", exact: true}).click();
        assert.equal(await opener.evaluate(node => node === document.activeElement), true);
        await page.locator("#wps-report-filter").fill("missing-report");
        assert.match(await page.locator("#wps-root").innerText(), /No reports match/);
        assert.equal(await page.locator(".wps-records li").count(), 0);
        await page.getByRole("button", {name: "Clear filters", exact: true}).focus(); await page.keyboard.press("Enter");
        await focusIs(page, "wps-report-filter");
        assert.equal(await page.locator("#wps-report-filter").inputValue(), "");
        assert.equal(await page.locator("#wps-report-status").inputValue(), "all");
        assert.equal(await page.locator(".wps-records li").count(), 2);
        await page.getByRole("button", {name: "Simulate loading", exact: true}).click();
        const loading = page.getByRole("status").filter({hasText: "Preparing the demonstration list"});
        await loading.waitFor(); assert.equal(await page.getByRole("button", {name: "Simulate loading", exact: true}).isDisabled(), true);
        assert.equal(await page.locator(".wps-records li").count(), 0);
        await loading.waitFor({state: "hidden"}); assert.equal(await page.locator(".wps-records li").count(), 2);
        await workspaceNav("Connection").click();
        assert.match(await page.locator("#wps-root").innerText(), /configuration is present/);
        assert.match(await page.locator("#wps-root").innerText(), /health has not been checked/);
        const settingsLink = page.getByRole("link", {name: "Open connection settings", exact: true});
        assert.match(await settingsLink.getAttribute("href"), /variant=discovery&lang=en#wps-section-advanced$/);
        await workspaceNav("Background work").click();
        const job = page.locator("#wps-job-state");
        assert.equal(await job.getAttribute("data-state"), "queued"); assert.match(await job.innerText(), /not started/);
        await page.getByRole("button", {name: "Simulate processing", exact: true}).focus(); await page.keyboard.press("Enter");
        await focusIs(page, "wps-job-state");
        assert.equal(await job.getAttribute("data-state"), "running"); assert.match(await job.innerText(), /not yet complete/);
        await page.getByRole("button", {name: "Simulate failure", exact: true}).focus(); await page.keyboard.press("Enter");
        await focusIs(page, "wps-job-state");
        assert.equal(await job.getAttribute("data-state"), "failed"); assert.match(await job.innerText(), /data is retained/);
        await page.getByRole("button", {name: "Retry demonstration", exact: true}).focus(); await page.keyboard.press("Enter");
        await focusIs(page, "wps-job-state");
        assert.equal(await job.getAttribute("data-state"), "queued");
        await page.getByRole("button", {name: "Simulate processing", exact: true}).focus(); await page.keyboard.press("Enter");
        await focusIs(page, "wps-job-state");
        await page.getByRole("button", {name: "Simulate completion", exact: true}).focus(); await page.keyboard.press("Enter");
        await focusIs(page, "wps-job-state");
        assert.equal(await job.getAttribute("data-state"), "completed"); assert.match(await job.innerText(), /does not confirm a server-side job/);
        assert.match(await page.locator("#wps-root").innerText(), /Download is unavailable/);
        assert.equal(await page.getByRole("button", {name: "Simulate processing", exact: true}).count(), 0);
        await workspaceNav("Reports").click(); assert.equal(await page.locator(".wps-records li").count(), 2);
        assert.deepEqual(calls, [], "Synthetic workspace interactions sent work/external requests");
        page.off("request", observeWork);
        await workspaceNav("Connection").click(); await settingsLink.click(); await waitState(page, "ready");
        assert.equal(await page.locator("#wps-root").getAttribute("data-variant"), "discovery");
        assert.equal(await nav(page, "Technical connection settings").getAttribute("aria-current"), "page");
        assert.equal(await page.locator("#wps-endpoint").isVisible(), true, "Connection destination did not reveal its settings field");

        for (const width of [1440, 390]) {
            await page.setViewportSize({width, height: width === 390 ? 844 : 1100});
            await open(page, "current", "workspace", "fa");
            await capture(page, "workspace-current-fa-" + width, "fa", "workspace", "current");
        }
        const faOpener = page.getByRole("button", {name: "مشاهدهٔ گزارش: گزارش هفتگی فروش", exact: true});
        await faOpener.click(); const faModal = page.getByRole("dialog", {name: "جزئیات گزارش", exact: true});
        const modalLayout = await faModal.evaluate(node => ({direction: getComputedStyle(node).direction, overflow: node.scrollWidth > node.clientWidth + 1}));
        assert.equal(modalLayout.direction, "rtl"); assert.equal(modalLayout.overflow, false);
        await capture(page, "workspace-detail-current-fa-390", "fa", "workspace-modal", "current");
        await page.keyboard.press("Escape"); assert.equal(await faOpener.evaluate(node => node === document.activeElement), true);
        const faNav = name => page.getByRole("navigation", {name: "بخش‌های مدیریت گزارش"}).getByRole("button", {name, exact: true});
        await faNav("اتصال سرویس").click(); await capture(page, "workspace-connection-current-fa-390", "fa", "workspace-connection", "current");
        await faNav("پردازش گزارش").click();
        await page.getByRole("button", {name: "نمایش حالت پردازش", exact: true}).click();
        await page.getByRole("button", {name: "نمایش حالت خطا", exact: true}).click();
        await capture(page, "workspace-failed-current-fa-390", "fa", "workspace-failed", "current");

        const minimumContext = await browser.newContext({viewport: {width: 390, height: 844}});
        try {
            const minimum = await login(minimumContext, "minimum"); await open(minimum, "minimum", "workspace");
            await minimum.locator("#wps-report-status").selectOption("draft");
            assert.equal(await minimum.locator(".wps-records li").count(), 1);
            const minOpener = minimum.getByRole("button", {name: "View report: Order delivery report", exact: true});
            await minOpener.click(); const minModal = minimum.getByRole("dialog", {name: "Report details", exact: true});
            assert.match(await minModal.innerText(), /REP-205/);
            assert.equal(await minModal.evaluate(node => node.scrollWidth > node.clientWidth + 1), false);
            await minimum.keyboard.press("Escape"); assert.equal(await minOpener.evaluate(node => node === document.activeElement), true);
            await capture(minimum, "workspace-minimum-en-390", "en", "workspace", "minimum");
        } finally { await minimumContext.close(); }
        record("D10", "Real current/minimum-host workspace: report name/status filters, no-match clear, loading disable/recovery, details modal Tab/Escape/close focus return and retained filters. Keyboard clear focuses the report filter; keyboard start/failure/retry/completion transitions focus the persistent job status instead of the document body. Configuration is separate from unchecked connection health and its link reveals actual technical settings. Synthetic queued/running/failure/retry/completion states remain truthful, retain report rows and send no work/external requests. Persian 1440/390, RTL modal/connection/failure and minimum-host English narrow captures have no document/modal overflow.");
    } finally { await context.close(); }
}
(async () => {
    // Only the two verified synthetic fixture options are reset; never a customer site.
    for (const service of ["current", "minimum"]) {
        execFileSync(docker, ["exec", containerFor(service), "php", "/fixture/bootstrap.php", "--reset"], {stdio: "pipe"});
    }
    const browser = await chromium.launch({channel: process.env.WPS_BROWSER_CHANNEL || "msedge", headless: true});
    try {
        const context = await browser.newContext({viewport: {width: 1440, height: 1100}});
        const page = await login(context, "current");
        await open(page, "current");
        assert.equal(await page.getByRole("searchbox", {name: "Search settings", exact: true}).getAttribute("id"), "wps-search", "Search control name must not be doubled");
        await inspectCompatibility(page, "current");
        await result(page, "webhook", "Report endpoint"); await focusIs(page, "wps-endpoint");
        assert.equal(await page.locator("#wps-endpoint").isVisible(), true);
        assert.equal(await nav(page, "Technical connection settings").getAttribute("aria-current"), "page");
        assert.equal(await page.locator("#wps-search").inputValue(), "");
        await open(page, "current", "discovery", "fa");
        assert.equal(await page.getByRole("searchbox", {name: "جست‌وجوی تنظیمات", exact: true}).getAttribute("id"), "wps-search", "Persian search control name must not be doubled");
        await result(page, "وب هوك", "نشانی دریافت گزارش"); await focusIs(page, "wps-endpoint");
        await result(page, "كليد", "کلید اتصال"); await focusIs(page, "wps-credentialAction");
        record("D01", "English and Persian search controls have exact single accessible names. English webhook and Persian spacing/Arabic-character alias queries reveal the actual advanced endpoint/credential controls and move focus to them.");

        await open(page, "current");
        await page.locator("#wps-title").fill("R12 retained title draft");
        await nav(page, "Report delivery").click(); await page.getByRole("checkbox", {name: "Enable email delivery", exact: true}).check();
        await page.locator("#wps-email").fill("draft-r12@example.test");
        await nav(page, "Technical connection settings").click(); await page.goBack();
        await focusIs(page, "heading-delivery");
        assert.equal(await page.locator("#wps-email").inputValue(), "draft-r12@example.test");
        await page.goBack(); await focusIs(page, "heading-general");
        assert.equal(await page.locator("#wps-title").inputValue(), "R12 retained title draft");
        await page.locator("#wps-root summary").click(); await page.getByLabel("Test request behavior").selectOption("delay");
        let releaseSave;
        const holdSave = new Promise(resolve => { releaseSave = resolve; });
        await page.route("**/admin-ajax.php?action=wps_specimen", async route => {
            if (route.request().postDataJSON()?.operation === "save") {
                const response = await route.fetch(); await holdSave; await route.fulfill({response});
            } else { await route.continue(); }
        });
        try {
            await page.getByRole("button", {name: "Save report", exact: true}).click(); await waitState(page, "saving");
            await nav(page, "Report delivery").click();
            assert.equal(await page.locator("#wps-email").inputValue(), "draft-r12@example.test");
            await nav(page, "Report identity").click(); await page.locator("#wps-title").fill("R12 edit during save");
        } finally { releaseSave(); }
        await waitState(page, "saved"); await page.unroute("**/admin-ajax.php?action=wps_specimen");
        assert.equal(await page.locator("#wps-title").inputValue(), "R12 edit during save");
        await nav(page, "Report delivery").click(); assert.equal(await page.locator("#wps-email").inputValue(), "draft-r12@example.test");
        const committed = await savedState(page);
        assert.equal(committed.settings.general.title, "R12 retained title draft");
        assert.equal(committed.settings.delivery.email, "reports@example.test");
        assert.equal(committed.settings.delivery.enabled, false);
        record("D02", "Section changes and browser Back preserve title/recipient drafts. During a delayed real save, navigation and newer edits survive; server stores only the submitted title and leaves unsaved delivery values unchanged.");

        await open(page, "current");
        await result(page, "inbox", "Recipient address"); await focusIs(page, "wps-email-dependency");
        assert.equal(await page.locator("#wps-email").isDisabled(), true);
        assert.match(await page.locator("#wps-email-dependency").innerText(), /Enable email delivery/);
        assert.equal(await page.locator("#wps-email").inputValue(), "reports@example.test");
        await verifyToggleAssociation(page);
        await page.getByRole("checkbox", {name: "Enable email delivery", exact: true}).check();
        await result(page, "inbox", "Recipient address"); await focusIs(page, "wps-email");
        assert.equal(await page.locator("#wps-email").isEnabled(), true);
        record("D03", "A disabled recipient result reveals/focuses its prerequisite explanation while retaining the saved address. Notification alias discovery focuses the actual checkbox with its accessible name and native matching label/input IDs; visible-label clicks toggle and restore state. After enabling delivery, the recipient result focuses the editable field.");

        await page.locator("#wps-search").fill("no-setting-has-this-name");
        assert.match(await page.locator(".wps-search-results").innerText(), /No setting found/);
        assert.equal(await page.locator(".wps-search-results li").count(), 0);
        await page.getByRole("button", {name: "Clear search", exact: true}).click(); await focusIs(page, "wps-search");
        assert.equal(await page.locator("#wps-search").inputValue(), "");
        await page.locator("#wps-search").fill("reports@example.test");
        assert.equal(await page.locator(".wps-search-results li").count(), 0);
        await page.keyboard.press("Escape"); await focusIs(page, "wps-search");
        record("D04", "No-result guidance is actionable, clearing/Escape restores search focus, and a saved recipient value is not indexed as searchable metadata.");

        await nav(page, "Technical connection settings").click(); await page.locator("#wps-endpoint").fill("http://invalid-r12.example.test");
        const beforeInvalid = await savedState(page);
        let releaseValidation;
        const holdValidation = new Promise(resolve => { releaseValidation = resolve; });
        await page.route("**/admin-ajax.php?action=wps_specimen", async route => {
            if (route.request().postDataJSON()?.operation === "save") {
                const response = await route.fetch(); await holdValidation; await route.fulfill({response});
            } else { await route.continue(); }
        });
        try {
            await page.getByRole("button", {name: "Save technical settings", exact: true}).click(); await waitState(page, "saving");
            await nav(page, "Report identity").click(); assert.equal(await page.locator("#wps-endpoint").isVisible(), false);
        } finally { releaseValidation(); }
        await waitState(page, "rejected"); await page.unroute("**/admin-ajax.php?action=wps_specimen"); await focusIs(page, "wps-endpoint");
        assert.equal(await page.locator("#wps-endpoint").isVisible(), true);
        assert.equal(await page.locator("#wps-endpoint").inputValue(), "http://invalid-r12.example.test");
        assert.equal(await page.locator("#wps-endpoint").getAttribute("aria-invalid"), "true");
        assert.equal(await nav(page, "Technical connection settings").getAttribute("aria-current"), "page");
        assert.equal(new URL(page.url()).hash, "#wps-section-advanced", "Late validation revealed a section inconsistent with its URL destination");
        const endpointHelp = await page.locator("#wps-endpoint").evaluate(node => (node.getAttribute("aria-describedby") || "").split(/\s+/)
            .map(id => document.getElementById(id)?.textContent || "").join(" "));
        assert.match(endpointHelp, /HTTPS/, "Validation replaced the actionable endpoint format guidance");
        await nav(page, "Report identity").click(); assert.equal(await page.locator("#wps-endpoint").isVisible(), false);
        const errorLink = page.getByRole("button", {name: "Review error: Report endpoint", exact: true});
        await errorLink.focus(); await page.keyboard.press("Enter"); await focusIs(page, "wps-endpoint");
        assert.equal(await page.locator("#wps-endpoint").isVisible(), true);
        assert.equal(new URL(page.url()).hash, "#wps-section-advanced");
        assert.equal(await page.locator("#wps-endpoint").inputValue(), "http://invalid-r12.example.test");
        assert.deepEqual(await savedState(page), beforeInvalid);
        const retainedEndpoint = "https://retained-credential-error.example.test/hook";
        await page.locator("#wps-endpoint").fill(retainedEndpoint);
        const credentialAction = page.getByLabel("Credential action", {exact: true});
        const credentialError = page.getByRole("button", {name: "Review error: Replacement credential", exact: true});
        for (const nextAction of ["keep", "remove"]) {
            await credentialAction.selectOption("replace"); await page.locator("#wps-credential").fill("");
            await page.getByRole("button", {name: "Save technical settings", exact: true}).click(); await waitState(page, "rejected");
            await focusIs(page, "wps-credential");
            assert.equal(await page.locator("#wps-credential").getAttribute("aria-invalid"), "true");
            assert.equal(await credentialError.isVisible(), true);
            await credentialAction.selectOption(nextAction);
            assert.equal(await page.locator("#wps-credential").count(), 0);
            assert.equal(await credentialError.count(), 0, "A credential error link still targets an absent replacement field");
            assert.equal(await credentialAction.inputValue(), nextAction);
            assert.equal(await page.locator("#wps-endpoint").inputValue(), retainedEndpoint);
            assert.deepEqual(await savedState(page), beforeInvalid);
        }
        await credentialAction.selectOption("replace"); await page.locator("#wps-credential").fill("");
        let releaseCredentialValidation;
        const holdCredentialValidation = new Promise(resolve => { releaseCredentialValidation = resolve; });
        await page.route("**/admin-ajax.php?action=wps_specimen", async route => {
            if (route.request().postDataJSON()?.operation === "save") {
                const response = await route.fetch(); await holdCredentialValidation; await route.fulfill({response});
            } else { await route.continue(); }
        });
        try {
            await page.getByRole("button", {name: "Save technical settings", exact: true}).click(); await waitState(page, "saving");
            await credentialAction.selectOption("keep");
            assert.equal(await page.locator("#wps-credential").count(), 0);
        } finally { releaseCredentialValidation(); }
        await waitState(page, "rejected"); await page.unroute("**/admin-ajax.php?action=wps_specimen");
        assert.equal(await credentialError.count(), 0, "Late validation restored a dangling credential error link");
        assert.equal(await page.locator("#wps-credential").count(), 0);
        assert.equal(await credentialAction.inputValue(), "keep");
        assert.equal(await page.locator("#wps-endpoint").inputValue(), retainedEndpoint);
        assert.deepEqual(await savedState(page), beforeInvalid);
        record("D05", "A real validation response arriving after navigation away reopens the hidden technical section, synchronizes its URL destination, focuses the invalid endpoint and preserves HTTPS guidance in its associated help. After further navigation, keyboard activation of the persistent field-error link returns to that field/destination. Empty replacement-credential validation creates a real field error; choosing keep/remove removes both field and error destination. A delayed replacement validation arriving after a keep choice cannot restore a dangling field/error link. Current action and endpoint drafts survive; server state remains unchanged.");

        const beforeDenied = await savedState(page), readerContext = await browser.newContext();
        try {
            const reader = await login(readerContext, "current", "wps-reader");
            await reader.goto(baseFor("current") + "/wp-admin/options-general.php?page=wps-specimen&variant=discovery&lang=en");
            assert.equal(await reader.locator("#wps-root").count(), 0);
            assert.equal(await reader.locator('script[src*="wps-specimen"],link[href*="wps-specimen"]').count(), 0);
            const denials = await reader.evaluate(async () => {
                const results = [];
                for (const operation of ["load", "save"]) {
                    const response = await fetch("/wp-admin/admin-ajax.php?action=wps_specimen", {method: "POST", credentials: "same-origin", headers: {"Content-Type": "application/json"},
                        body: JSON.stringify({operation, section: "general", values: {title: "Denied R12 write"}})});
                    results.push({status: response.status, body: await response.json()});
                }
                return results;
            });
            assert.deepEqual(denials.map(item => item.status), [403, 403]);
            assert.ok(denials.every(item => item.body.data.code === "denied" && !item.body.data.settings));
            assert.deepEqual(await savedState(page), beforeDenied);
        } finally { await readerContext.close(); }
        record("D06", "Subscriber page access exposes neither settings root nor owned metadata scripts; read/write requests return denial without state, and saved settings remain unchanged.");

        await open(page, "current", "discovery", "fa");
        for (const width of [1440, 390]) {
            await page.setViewportSize({width, height: width === 390 ? 844 : 1100});
            await capture(page, "discovery-current-fa-" + width, "fa", "discovery", "current");
            await result(page, "گیرنده", "دریافت‌کنندهٔ گزارش");
            await capture(page, "discovery-recipient-fa-" + width, "fa", "discovery", "current");
        }
        record("D07", "Persian discovery and recipient dependency states at 1440/390px retain the real host toolbar/menu, local rendered Vazirmatn regular/bold and no document overflow; captures identify language, viewport and state.");

        const minimumContext = await browser.newContext({viewport: {width: 390, height: 844}});
        try {
            const minimum = await login(minimumContext, "minimum"); await open(minimum, "minimum");
            assert.equal(await minimum.getByRole("searchbox", {name: "Search settings", exact: true}).getAttribute("id"), "wps-search");
            await inspectCompatibility(minimum, "minimum");
            await verifyToggleAssociation(minimum);
            await result(minimum, "webhook", "Report endpoint"); await focusIs(minimum, "wps-endpoint");
            await minimum.locator("#wps-endpoint").fill("https://minimum-r12.example.test/hook");
            await minimum.getByRole("button", {name: "Save technical settings", exact: true}).click(); await waitState(minimum, "saved");
            assert.equal((await savedState(minimum)).settings.advanced.endpoint, "https://minimum-r12.example.test/hook");
            await capture(minimum, "discovery-minimum-en-390", "en", "discovery", "minimum");
        } finally { await minimumContext.close(); }
        record("D08", "WordPress 6.8 loads the actual public controls/styles/dependency metadata; English LTR alias discovery, focus and endpoint save work at 390px. Notification discovery focuses the named native checkbox; matching label/input IDs and label-click toggling both directions are verified. Actual host/runtime/export metadata retained separately.");

        await page.setViewportSize({width: 1440, height: 1000}); await open(page, "current", "simple");
        assert.equal(await page.locator("#wps-root").getByRole("textbox").count(), 1);
        assert.equal(await page.locator("#wps-root").getByRole("checkbox").count(), 1);
        assert.equal(await page.locator('#wps-root [role="tablist"], #wps-search, #wps-root .wps-section-nav').count(), 0);
        assert.equal(await page.locator('script[src*="discovery.js"],script[src*="workspace.js"]').count(), 0);
        record("D09", "The short form retains one title and one toggle with its existing save scopes; no search, tabs, local navigation or discovery/workspace script is loaded.");

        if (!settingsOnly) { await workspaceChecks(browser); }

        await open(page, "current"); await page.locator("#wps-search").focus(); await page.keyboard.type("webhook");
        const endpointResult = page.locator(".wps-search-results").getByRole("button", {name: "Report endpoint", exact: true});
        for (let step = 0; step < 12 && !(await endpointResult.evaluate(node => node === document.activeElement)); step++) { await page.keyboard.press("Tab"); }
        assert.equal(await endpointResult.evaluate(node => node === document.activeElement), true, "Keyboard did not reach the matching result");
        await page.keyboard.press("Enter"); await focusIs(page, "wps-endpoint");
        await page.locator("#wps-search").focus(); await page.keyboard.type("webhook");
        for (let step = 0; step < 12 && !(await endpointResult.evaluate(node => node === document.activeElement)); step++) { await page.keyboard.press("Tab"); }
        assert.equal(await endpointResult.evaluate(node => node === document.activeElement), true);
        await page.keyboard.press("Escape"); await focusIs(page, "wps-search");
        assert.equal(await page.locator(".wps-search-results").count(), 0);
        record("D11", "Keyboard Tab reaches native search result controls, Enter reveals/focuses the actual field, and Escape from a result dismisses results and returns focus to search.");

        assert.deepEqual(errors, [], "Browser JavaScript errors");
        assert.deepEqual([...new Set(warnings)], [], "Component warnings must be resolved rather than suppressed");
        assert.deepEqual(fixtureHashes(), initialFixture, "Fixture source changed during verification");
        assert.deepEqual(behaviorHashes(), initialBehavior, "Skill behavior source changed during verification");
        assert.equal(sha(__filename), runnerHash, "Runner changed during verification");
        const recordedAt = new Date();
        const report = {schema_version: 1,
            recorded_on: new Intl.DateTimeFormat("en-CA", {timeZone: "Asia/Tehran", year: "numeric", month: "2-digit", day: "2-digit"}).format(recordedAt),
            recorded_at: recordedAt.toISOString(), recorded_timezone: "Asia/Tehran",
            git_head: execFileSync("git", ["rev-parse", "HEAD"], {cwd: repo, encoding: "utf8"}).trim(),
            scope: settingsOnly ? "settings-only partial; D10 workspace not executed" : "full R12 discovery and workspace",
            complete: !settingsOnly, omitted_observations: settingsOnly ? ["D10"] : [],
            runner_sha256: runnerHash, fixture_hashes: initialFixture, behavior_hashes: initialBehavior,
            browser: browser.version(), compatibility, captures, observations, javascript_errors: errors, console_warnings: [...new Set(warnings)]};
        const filename = settingsOnly ? "r12-settings-partial.json" : "r12-browser-results.json";
        fs.writeFileSync(path.join(output, filename), JSON.stringify(report, null, 2));
        console.log(JSON.stringify({passed: observations.length, complete: !settingsOnly, omitted: report.omitted_observations, output: path.join(output, filename)}));
        await context.close();
    } finally { await browser.close(); }
})().catch(error => {
    fs.writeFileSync(path.join(output, "failed-discovery-results.json"), JSON.stringify({observations, javascript_errors: errors,
        console_warnings: [...new Set(warnings)], error: error.message, fixture_hashes: initialFixture, behavior_hashes: initialBehavior}, null, 2));
    console.error(error.stack); process.exitCode = 1;
});
