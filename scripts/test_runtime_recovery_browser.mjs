// Optional real-browser acceptance. Uses an already installed Playwright and browser;
// never downloads dependencies. Synthetic loopback server and owned disposable store only.
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import { spawn } from 'node:child_process';
import { mkdtemp, rm, mkdir } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { dirname, basename, resolve, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { once } from 'node:events';
import { createInterface } from 'node:readline';

const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const temporary = await mkdtemp(join(tmpdir(), 'uiux-recovery-browser-'));
const serverCode = `import sys,json
from pathlib import Path
sys.path.insert(0,str(Path.cwd()/'scripts'))
from runtime_appearance import Store,FixtureServer
server=FixtureServer(Store(Path(sys.argv[1])/'appearance.sqlite'))
urls=[]
for actor in ('owner-a','owner-a-peer'):
 server.principal=actor
 urls.append(server.access_link())
print(json.dumps(urls),flush=True)
server.serve_forever()
`;
const server = spawn(process.env.PYTHON || 'python', ['-B','-u','-c',serverCode,temporary],
  {cwd:root, stdio:['ignore','pipe','pipe'], windowsHide:true});
let browser;
try {
  const lines = createInterface({input:server.stdout});
  let timer;
  const urls = await Promise.race([
    once(lines,'line').then(([line]) => JSON.parse(line)),
    once(server,'exit').then(() => { throw new Error('Fixture server exited before startup'); }),
    new Promise((_,reject) => { timer=setTimeout(() => reject(new Error('Fixture startup timeout')),15000); })
  ]).finally(() => clearTimeout(timer));
  browser = await chromium.launch({headless:true, ...(process.env.BROWSER_EXECUTABLE ? {executablePath:process.env.BROWSER_EXECUTABLE} : {})});
  console.log('Browser:', browser.version());
  const contexts = await Promise.all([browser.newContext(),browser.newContext()]);
  const [owner,peer] = await Promise.all(contexts.map(context => context.newPage()));
  const pageErrors=[];
  for (const page of [owner,peer]) page.on('pageerror', error => pageErrors.push(error.message));
  async function idle(page) { await page.waitForFunction(() => document.querySelector('#manager')?.getAttribute('aria-busy') !== 'true'); }
  async function click(page,id) {
    const control=page.locator('#'+id), details=control.locator('xpath=ancestor::details');
    if (await details.count() && !(await details.evaluate(el=>el.open))) await details.locator('summary').click();
    await control.click(); await idle(page);
  }
  async function setting(page,key,value) {
    const control=page.locator('#setting-'+key);
    const details=control.locator('xpath=ancestor::details');
    if (!(await details.evaluate(el=>el.open))) await details.locator('summary').click();
    await control.selectOption(String(value));
  }
  async function confirm(page,id) { await click(page,id); await page.locator('#confirm-action').click(); await idle(page); }
  async function publish(page) { await click(page,'save'); await confirm(page,'publish'); }
  async function data(page,resource,tenant='a') {
    const response=await page.request.get(new URL(`/api/v1/tenants/${tenant}/${resource}`,urls[0]).href);
    assert.equal(response.status(),200); return response.json();
  }
  async function choices(page,localKeys) {
    for (const select of await page.locator('#recovery-fields select').all()) {
      const key=(await select.getAttribute('id')).slice('recovery-'.length);
      await select.selectOption(localKeys.includes(key)?'local':'current');
    }
  }
  async function screenshot(page,name) {
    if (!process.env.RECOVERY_ARTIFACT_DIR) return;
    const out=resolve(process.env.RECOVERY_ARTIFACT_DIR);
    assert.ok(out !== root && !out.startsWith(root + '\\') && !out.startsWith(root + '/'), 'Artifacts must stay outside source');
    await mkdir(out,{recursive:true});
    await page.screenshot({path:join(out,name),fullPage:false});
  }
  for (const [i,page] of [owner,peer].entries()) {
    await page.goto(urls[i]);
    await page.waitForFunction(() => !document.querySelector('#manager').hidden && document.querySelector('#setting-palette'));
    await page.waitForFunction(() => document.querySelector('#status').textContent.includes('loaded'));
  }
  const tenantB=await data(owner,'published','b');
  await setting(owner,'palette','forest'); await click(owner,'save');
  const originalDraft=await data(owner,'draft');
  assert.equal(await data(peer,'draft'),null);
  await setting(peer,'spacing',24); await publish(peer);
  await setting(owner,'palette','plum');
  await click(owner,'reload');
  assert.equal(await owner.locator('#setting-palette').inputValue(),'plum');
  assert.equal(await owner.locator('#save').isDisabled(),true);
  assert.deepEqual(await data(owner,'draft'),originalDraft);
  await click(owner,'reconcile');
  assert.equal(await owner.locator('#recovery').isVisible(),true);
  assert.equal(await owner.locator('#recovery').evaluate(el=>el.contains(document.activeElement)),true);
  await owner.keyboard.press('Escape');
  await owner.waitForFunction(() => !document.querySelector('#recovery').open);
  assert.equal(await owner.evaluate(() => document.activeElement.id),'reconcile');
  assert.deepEqual(await data(owner,'draft'),originalDraft);
  await click(owner,'reconcile');
  await click(owner,'recovery-save');
  assert.match(await owner.locator('#recovery-error').innerText(),/Choose/);
  await choices(owner,['palette']);
  await owner.locator('#recovery-save').focus(); await owner.keyboard.press('Tab');
  assert.equal(await owner.evaluate(() => document.activeElement.id),'recovery-palette');
  await owner.keyboard.press('Shift+Tab');
  assert.equal(await owner.evaluate(() => document.activeElement.id),'recovery-save');
  await screenshot(owner,'recovery-desktop.png');
  await setting(peer,'bodySize',18); await publish(peer);
  await click(owner,'recovery-save');
  assert.match(await owner.locator('#recovery-error').innerText(),/Published appearance changed/);
  assert.equal(await owner.locator('#recovery-save').isDisabled(),true);
  assert.deepEqual(await data(owner,'draft'),originalDraft);
  await click(owner,'recovery-refresh'); await choices(owner,['palette']);
  await owner.setViewportSize({width:390,height:844});
  assert.equal(await owner.locator('#recovery').evaluate(el=>el.scrollWidth <= el.clientWidth+1),true);
  await screenshot(owner,'recovery-mobile.png');
  await click(owner,'recovery-save');
  const reconciled=await data(owner,'draft');
  assert.equal(reconciled.baseRevision,2);
  assert.equal(reconciled.config.palette,'plum'); assert.equal(reconciled.config.spacing,24); assert.equal(reconciled.config.bodySize,18);
  assert.equal((await data(owner,'published')).config.palette,'ocean');
  await confirm(owner,'publish');
  assert.equal((await data(owner,'published')).revision,3);
  assert.equal(await data(owner,'draft'),null);
  console.log('PASS: two-owner conflict, cancel, required choices, keyboard wrap/return, race rejection, mobile review, private save and publication');

  await owner.setViewportSize({width:1280,height:900});
  await setting(owner,'spacing',12); await click(owner,'save');
  await setting(owner,'bodySize',20);
  const beforeRollback=await data(owner,'draft');
  const history=owner.getByText('Version history and recovery',{exact:true});
  if (!(await history.locator('..').evaluate(el=>el.open))) await history.click();
  await owner.locator('#history-choice').selectOption('0'); await confirm(owner,'rollback');
  assert.equal(await owner.locator('#setting-bodySize').inputValue(),'20');
  assert.equal(await owner.locator('#setting-spacing').inputValue(),'12');
  assert.deepEqual(await data(owner,'draft'),beforeRollback);
  assert.equal((await data(owner,'published')).revision,4);
  await click(owner,'reconcile'); await choices(owner,['bodySize','spacing']);
  await click(owner,'recovery-save'); await confirm(owner,'publish');
  const final=await data(owner,'published');
  assert.equal(final.revision,5); assert.equal(final.config.bodySize,20); assert.equal(final.config.spacing,12); assert.equal(final.config.palette,'ocean');
  assert.equal((await data(owner,'history')).items.length,6);
  assert.deepEqual(await data(owner,'published','b'),tenantB);
  await screenshot(owner,'recovery-final.png');
  await setting(owner,'theme','dark'); await publish(owner);
  await owner.setViewportSize({width:390,height:844});
  await click(owner,'reconcile');
  assert.equal(await owner.locator('#recovery').evaluate(el=>el.contains(document.activeElement)),true);
  assert.equal(await owner.locator('#recovery').evaluate(el=>el.scrollWidth <= el.clientWidth+1),true);
  await screenshot(owner,'recovery-dark-mobile.png');
  await click(owner,'recovery-cancel');
  assert.deepEqual(pageErrors,[]);
  console.log('PASS: rollback with saved/unsaved edits, recovery and publication, immutable history, other tenant unchanged, dark mobile large-text dialog, no browser script errors');
} finally {
  if (browser) await browser.close();
  if (server.exitCode === null && server.signalCode === null) {
    const exited=once(server,'exit'); server.kill(); await exited;
  }
  assert.equal(dirname(resolve(temporary)),resolve(tmpdir()));
  assert.ok(basename(temporary).startsWith('uiux-recovery-browser-'));
  await rm(temporary,{recursive:true});
}
