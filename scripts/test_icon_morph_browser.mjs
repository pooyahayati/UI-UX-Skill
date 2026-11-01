// Explicit, optional local browser acceptance; no install/download. Real existing
// appearance API + routed static specimen files, in a disposable loopback store.
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {spawn} from 'node:child_process';
import {readFile,mkdir,writeFile,mkdtemp} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {resolve,dirname,join,basename} from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {gzipSync} from 'node:zlib';
import {createInterface} from 'node:readline';
import {once} from 'node:events';
const require=createRequire(import.meta.url);
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const root=resolve(dirname(fileURLToPath(import.meta.url)),'..');
const fixture=join(root,'evals/fixtures/icon-morph');
const vendor=resolve(process.env.MORPHICONS_PACKAGE||'missing-provider');
const bundle=resolve(process.env.MORPHICONS_BUNDLE||'missing-bundle');
const out=resolve(process.env.ICON_ARTIFACT_DIR||'missing-artifact-directory');
assert.ok(process.env.ICON_ARTIFACT_DIR && !out.startsWith(root), 'Artifacts must be outside source');
const hash=b=>createHash('sha256').update(b).digest('hex');
const pin=JSON.parse(await readFile(join(fixture,'provider.json')));
assert.equal(JSON.parse(await readFile(join(vendor,'package.json'))).version,pin.version);
for(const [file,expected] of Object.entries(pin.files))assert.equal(hash(await readFile(join(vendor,file))),expected,file);
for(const [file,expected] of Object.entries(pin.bundle.files))assert.equal(hash(await readFile(join(bundle,file))),expected,file);
await mkdir(out,{recursive:true});
const temporary=await mkdtemp(join(tmpdir(),'uiux-icon-'));
const code=`import sys,json
from pathlib import Path
sys.path.insert(0,str(Path.cwd()/'scripts'))
from runtime_appearance import Store,FixtureServer
s=FixtureServer(Store(Path(sys.argv[1])/'appearance.sqlite'))
s.principal='owner-a'
print(json.dumps(s.access_link()),flush=True)
s.serve_forever()
`;
const server=spawn(process.env.PYTHON||'python',['-B','-u','-c',code,temporary],{cwd:root,stdio:['ignore','pipe','pipe'],windowsHide:true});
let browser;
const observations=[],served=new Map(),pageErrors=[];
const record=(id,details)=>observations.push({id,status:'passed',details});
try {
  const lines=createInterface({input:server.stdout});let timer;
  const access=await Promise.race([once(lines,'line').then(([l])=>JSON.parse(l)),
    once(server,'exit').then(()=>{throw Error('Server exited');}),
    new Promise((_,reject)=>{timer=setTimeout(()=>reject(Error('Server startup timeout')),15000);})]).finally(()=>clearTimeout(timer));
  const origin=new URL(access).origin;
  browser=await chromium.launch({headless:true,...(process.env.BROWSER_EXECUTABLE?{executablePath:process.env.BROWSER_EXECUTABLE}:{})});
  const context=await browser.newContext({viewport:{width:390,height:844}});
  await context.route('**/icon-specimen/**',async route=>{
    const path=new URL(route.request().url()).pathname.slice('/icon-specimen/'.length);
    const local=path.startsWith('vendor/')?join(bundle,basename(path)):join(fixture,path||'index.html');
    const allowed=path.startsWith('vendor/')?Object.hasOwn(pin.bundle.files,basename(path)):['','index.html','adapter.mjs','fixture.mjs'].includes(path);
    assert.ok(allowed,'Unexpected asset request '+path);
    const body=await readFile(local);served.set(path,body);
    await route.fulfill({body,contentType:path.endsWith('.js')||path.endsWith('.mjs')?'text/javascript':'text/html'});
  });
  const owner=await context.newPage();await owner.goto(access);
  const session=await (await owner.request.get(origin+'/api/v1/session')).json();
  const csrf={'X-Fixture-CSRF':session.csrf,Origin:origin};
  async function api(resource,method='GET',data) {
    const response=await owner.request.fetch(origin+'/api/v1/tenants/a/'+resource,{method,data,headers:csrf});
    return {status:response.status(),body:await response.json()};
  }
  const initial=(await api('published')).body;
  async function save(config) {
    const active=(await api('published')).body,draft=(await api('draft')).body;
    const r=await api('draft','PUT',{config,baseRevision:active.revision,draftRevision:draft?.draftRevision??0});
    assert.equal(r.status,200,JSON.stringify(r));return r.body;
  }
  async function publish(config) {
    const draft=await save(config),r=await api('publications','POST',{draftRevision:draft.draftRevision});
    assert.equal(r.status,200,JSON.stringify(r));return r.body;
  }
  const page=await context.newPage();page.on('pageerror',e=>pageErrors.push(e.message));
  async function open(suffix='') {await page.goto(origin+'/icon-specimen/index.html'+suffix);await page.waitForFunction(()=>window.ready);}
  const state=()=>page.evaluate(()=>fixture.view.state());
  async function settle(){await page.waitForFunction(()=>{
    const state=fixture.view.state(),asset=fixture.last.tokens.icons.disclosure;
    return state.progress===1 && document.querySelector('svg path').getAttribute('d')===asset.states[state.open?'open':'closed'][0].d;
  });}
  await open('?static');
  const baselineVendor=[...served.keys()].filter(p=>p.startsWith('vendor/'));assert.equal(baselineVendor.length,0);
  const baseline=[];
  for(let i=0;i<12;i++)baseline.push(await page.evaluate(()=>{const t=performance.now();document.querySelector('button').click();return performance.now()-t;}));
  record('STATIC',{provider_requests:0,usable:await page.getByRole('button',{name:'Visit instructions'}).count()===1});
  await publish({...initial.config,motion:'standard'});
  served.clear();await open();
  await page.getByRole('button',{name:'Visit instructions'}).focus();await page.keyboard.press('Enter');
  assert.equal(await page.locator('button').getAttribute('aria-expanded'),'true');assert.equal(await page.locator('#panel').isVisible(),true);
  assert.equal(await page.evaluate(()=>document.activeElement.id),'disclosure');
  await settle();assert.equal((await state()).mode,'morph');
  const morphDurations=[];
  for(let i=0;i<12;i++) {morphDurations.push(await page.evaluate(()=>{const t=performance.now();document.querySelector('button').click();return performance.now()-t;}));await settle();}
  record('NORMAL',{name:'Visit instructions',keyboard:'Enter',focus:'disclosure',state:await state()});
  await page.evaluate(()=>{for(let i=0;i<21;i++)document.querySelector('button').click();});await settle();
  assert.equal((await state()).open,false);record('INTERRUPT',{activations:21,state:await state()});
  await page.evaluate(()=>document.querySelector('button').click());
  await page.waitForFunction(()=>fixture.view.state().progress>0 && fixture.view.state().progress<1,null,{polling:10});
  await page.emulateMedia({reducedMotion:'reduce'});
  await page.waitForFunction(()=>fixture.view.state().mode==='immediate',null,{polling:50});await settle();
  const reducedD=await page.locator('svg path').getAttribute('d');await page.waitForTimeout(120);
  assert.equal(await page.locator('svg path').getAttribute('d'),reducedD);
  await page.keyboard.press('Space');assert.equal((await state()).open,false);
  record('REDUCED-LIVE',{state:await state(),stable:true});
  await page.emulateMedia({reducedMotion:'no-preference'});
  await page.evaluate(()=>{document.querySelector('button').click();fixture.view.setPersonal('off');});
  assert.equal((await state()).progress,1);record('PERSONAL-OFF',{state:await state()});
  await page.evaluate(()=>fixture.view.setPersonal('standard'));
  const preview=await api('previews','POST',{config:{...initial.config,motion:'reduced',iconFamily:'solid',disclosureIcon:'badge'}});
  assert.equal(preview.status,200);await page.evaluate(r=>fixture.show(r),preview.body);
  assert.equal((await api('published')).body.config.iconFamily,'outline');
  assert.equal((await state()).mode,'static');assert.equal(await page.locator('svg path').count(),2);
  await page.getByRole('button',{name:'Visit instructions'}).click();assert.equal((await state()).open,false);
  record('PRIVATE-UNSUPPORTED',{source:preview.body.source,publicFamily:'outline',staticFamily:'solid',variant:'badge',paths:2,state:await state()});
  const stored=await save(preview.body.config);const reopened=(await api('draft')).body;
  assert.deepEqual(reopened.config,preview.body.config);
  await page.reload();await page.waitForFunction(()=>window.ready);assert.equal((await state()).mode,'morph');
  await api('publications','POST',{draftRevision:stored.draftRevision});await page.evaluate(()=>fixture.reload());
  assert.equal((await state()).mode,'static');assert.equal(await page.locator('svg').getAttribute('fill'),'currentColor');
  record('SAVE-REOPEN-PUBLISH',{privateDraftReopened:true,publishedFamily:'solid',consumerMode:(await state()).mode});
  const before=(await api('published')).body;
  for(const bad of [{...before.config,motion:'wild'},{...before.config,disclosureIcon:'remote-url'}]) {
    const r=await api('draft','PUT',{config:bad,baseRevision:before.revision,draftRevision:0});assert.equal(r.status,422);
    assert.deepEqual((await api('published')).body,before);
  }
  const anon=await browser.newContext();const denied=await anon.request.put(origin+'/api/v1/tenants/a/draft',{data:{}});assert.equal(denied.status(),401);await anon.close();
  record('INVALID-DENIED',{invalidPreset:422,unknownId:422,anonymous:401,publishedUnchanged:true});
  const reset=await api('resets','POST',{baseRevision:before.revision,draftRevision:0});assert.equal(reset.status,200);
  assert.equal((await api('published')).body.config.iconFamily,'solid');
  await api('publications','POST',{draftRevision:reset.body.draftRevision});await page.evaluate(()=>fixture.reload());
  assert.equal((await state()).mode,'immediate');
  const resetPublished=(await api('published')).body;
  const rollback=await api('rollbacks','POST',{baseRevision:resetPublished.revision,revision:1});assert.equal(rollback.status,200);
  await page.evaluate(()=>fixture.reload());assert.equal((await state()).mode,'morph');
  assert.ok((await api('history')).body.items.length>=4);
  record('RESET-ROLLBACK',{resetPrivate:true,resetMode:'immediate',rollbackMode:'morph',historyRetained:true});
  await page.route('**/published',r=>r.fulfill({status:503,body:'{}',contentType:'application/json'}));
  await page.evaluate(()=>fixture.reload());assert.equal((await state()).mode,'morph');
  assert.match(await page.locator('#load-status').textContent(),/retaining/);await page.unroute('**/published');
  record('CONFIG-FAILURE',{lastValidRetained:true});
  await publish({...initial.config,motion:'reduced'});await page.evaluate(()=>fixture.reload());
  assert.equal((await state()).mode,'immediate');await page.evaluate(()=>document.querySelector('button').click());
  assert.equal((await state()).progress,1);record('OWNER-OFF',{persistedEquivalent:'reduced (0ms)',state:await state()});
  await page.screenshot({path:join(out,'mobile.png'),fullPage:true});
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  record('MOBILE',{width:390,height:844,overflow:false});
  await publish({...initial.config,motion:'standard'});await page.evaluate(()=>fixture.reload());
  await page.evaluate(()=>{document.querySelector('button').click();fixture.view.destroy();});
  const deadD=await page.locator('svg path').getAttribute('d');await page.waitForTimeout(120);
  assert.equal(await page.locator('svg path').getAttribute('d'),deadD);
  const deadState=await state();await page.emulateMedia({reducedMotion:'reduce'});await page.evaluate(()=>document.querySelector('button').click());
  assert.equal((await state()).open,deadState.open);record('CLEANUP',{disposed:true,stable:true});
  const failed=await context.newPage();await failed.route('**/vendor/**',r=>r.abort());
  await failed.goto(origin+'/icon-specimen/index.html');await failed.waitForFunction(()=>window.ready);
  await failed.getByRole('button',{name:'Visit instructions'}).click();
  assert.equal(await failed.locator('#panel').isVisible(),true);assert.equal(await failed.evaluate(()=>fixture.view.state().mode),'static');
  record('PROVIDER-FAILURE',{usable:true,mode:'static'});
  const resources=[...served].filter(([p])=>p.startsWith('vendor/')).map(([path,b])=>({path,bytes:b.length,gzip_bytes:gzipSync(b).length,sha256:hash(b)}));
  const gzip=resources.reduce((n,r)=>n+r.gzip_bytes,0);assert.ok(gzip<=pin.budget.additional_route_gzip_bytes);
  assert.equal(pageErrors.length,0,pageErrors.join('\n'));
  record('PAYLOAD',{static_provider_bytes:0,additional_raw_bytes:resources.reduce((n,r)=>n+r.bytes,0),additional_gzip_bytes:gzip,budget_gzip_bytes:pin.budget.additional_route_gzip_bytes,resources,
    click_handler_ms:{baseline,morph:morphDurations},measurement:'Local installed Chromium-family browser, 390x844 emulation; synchronous handler durations, not FPS, INP, physical device or user task time. gzip per served module; no bundler saving claim.'});
  const source={};
  for(const file of ['scripts/test_icon_morph_browser.mjs','scripts/runtime_appearance.py','scripts/runtime_icons.py',...['index.html','adapter.mjs','fixture.mjs','provider.json'].map(p=>'evals/fixtures/icon-morph/'+p)])
    source[file]=hash((await readFile(join(root,file))).toString().replaceAll('\r\n','\n'));
  const report={schema_version:1,stage:'R14.3',recorded_on:'2026-11-02',engine:{name:pin.name,version:pin.version,integrity:pin.integrity},browser:browser.version(),source,observations,
    artifacts:{'mobile.png':hash(await readFile(join(out,'mobile.png')))},limitations:'Synthetic existing appearance API. Static assets routed by Playwright; API writes use real HTTP/session/CSRF/store. No production or WordPress runtime change; no Aria catalog asset or exporter execution; unsupported solid/badge pair is this adapter restriction, not engine 2.x limitation.'};
  await writeFile(join(out,'runtime.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({passed:observations.length,browser:report.browser,gzip_bytes:gzip,output:out}));
} finally {await browser?.close();server.kill();}
