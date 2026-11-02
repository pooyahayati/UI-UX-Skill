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
import {createServer} from 'node:http';
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
let browser,assetServer,appearanceFault;
let providerRequests=0;
const observations=[],served=new Map(),pageErrors=[];
const record=(id,details)=>observations.push({id,status:'passed',details});
try {
  const lines=createInterface({input:server.stdout});let timer;
  const access=await Promise.race([once(lines,'line').then(([l])=>JSON.parse(l)),
    once(server,'exit').then(()=>{throw Error('Server exited');}),
    new Promise((_,reject)=>{timer=setTimeout(()=>reject(Error('Server startup timeout')),15000);})]).finally(()=>clearTimeout(timer));
  const origin=new URL(access).origin;
  browser=await chromium.launch({headless:true,ignoreDefaultArgs:['--disable-back-forward-cache'],...(process.env.BROWSER_EXECUTABLE?{executablePath:process.env.BROWSER_EXECUTABLE}:{})});
  const context=await browser.newContext({viewport:{width:390,height:844}});
  // Real HTTP assets keep BFCache eligibility observable; request interception can disable it.
  assetServer=createServer(async(req,res)=>{
    try {
      const pathname=new URL(req.url,'http://localhost').pathname;
      if(pathname==='/api/v1/tenants/a/published') {
        const fault=appearanceFault;
        if(fault?.wait)await fault.wait;
        if(fault?.mode==='network'){res.destroy();return;}
        if(fault?.mode==='http'){res.writeHead(503,{'Content-Type':'application/json'});res.end('{}');return;}
        const upstream=await fetch(origin+pathname,{headers:{cookie:req.headers.cookie||''}});
        res.writeHead(upstream.status,{'Content-Type':'application/json'});res.end(await upstream.text());return;
      }
      if(pathname==='/icon-other') {res.setHeader('Content-Type','text/html');res.end('<title>Other page</title><p>Navigation target</p>');return;}
      if(!pathname.startsWith('/icon-specimen/')) {res.writeHead(404);res.end();return;}
      const path=pathname.slice('/icon-specimen/'.length);
      const allowed=path.startsWith('vendor/')?Object.hasOwn(pin.bundle.files,path.slice(7)):['','index.html','adapter.mjs','fixture.mjs'].includes(path);
      if(!allowed) {res.writeHead(404);res.end();return;}
      const local=path.startsWith('vendor/')?join(bundle,basename(path)):join(fixture,path||'index.html');
      if(path.startsWith('vendor/'))providerRequests++;
      const body=await readFile(local);served.set(path,body);
      res.setHeader('Content-Type',path.endsWith('.js')||path.endsWith('.mjs')?'text/javascript':'text/html');res.end(body);
    } catch(error) {pageErrors.push(error.message);res.writeHead(500);res.end('Fixture server error');}
  });
  assetServer.listen(0,'127.0.0.1');await once(assetServer,'listening');
  const specimenOrigin='http://127.0.0.1:'+assetServer.address().port;
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
  async function open(suffix='') {await page.goto(specimenOrigin+'/icon-specimen/index.html'+suffix);await page.waitForFunction(()=>window.ready);}
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
  const lifecycle=[];
  for(const suffix of ['?static','']) {
    const cached=await context.newPage();cached.on('pageerror',e=>pageErrors.push(e.message));
    await cached.addInitScript(()=>{window.restores=[];addEventListener('pageshow',e=>{if(e.persisted)window.restores.push(true);});});
    await cached.goto(specimenOrigin+'/icon-specimen/index.html'+suffix);await cached.waitForFunction(()=>window.ready);
    const control=cached.getByRole('button',{name:'Visit instructions'});
    await cached.evaluate(()=>{window.originalDocument='kept';});
    for(const expanded of [false,true]) {
      await cached.evaluate(value=>{if(fixture.view.state().open!==value)document.querySelector('button').click();},expanded);
      await control.focus();
      const count=await cached.evaluate(()=>restores.length);
      await cached.goto(specimenOrigin+'/icon-other');
      await cached.emulateMedia({reducedMotion:'reduce'});
      await cached.goBack({waitUntil:'commit'});
      await cached.waitForFunction(n=>window.restores?.length===n+1,count);
      assert.equal(await cached.evaluate(()=>originalDocument),'kept');
      assert.equal(await control.getAttribute('aria-expanded'),String(expanded));
      assert.equal(await cached.locator('#panel').isVisible(),expanded);
      await control.click();
      assert.equal(await control.getAttribute('aria-expanded'),String(!expanded));
      await cached.keyboard.press('Enter');
      assert.equal(await control.getAttribute('aria-expanded'),String(expanded));
      await cached.keyboard.press('Space');
      assert.equal(await control.getAttribute('aria-expanded'),String(!expanded));
      assert.equal(await cached.evaluate(()=>document.activeElement.id),'disclosure');
      assert.equal(await cached.evaluate(()=>fixture.view.state().immediate),true);
      const icon=await cached.evaluate(()=>({actual:document.querySelector('svg path').getAttribute('d'),
        expected:fixture.last.tokens.icons.disclosure.states[fixture.view.state().open?'open':'closed'][0].d}));
      assert.equal(icon.actual,icon.expected);
      lifecycle.push({provider:suffix?'static':'morphicons',initialOpen:expanded,persisted:true,
        pointerKeyboard:true,singleActivation:true,focus:true,reducedAfterReturn:true,geometry:true});
      await cached.emulateMedia({reducedMotion:'no-preference'});
    }
    await cached.close();
  }
  record('BFCACHE',{cycles:lifecycle});
  const coldCases=[];
  for(const mode of ['http','network']) {
    let release;
    appearanceFault={mode,wait:new Promise(r=>release=r)};
    const cold=await context.newPage();cold.on('pageerror',e=>pageErrors.push(e.message));
    await cold.addInitScript(()=>{window.restores=[];addEventListener('pageshow',e=>{if(e.persisted)window.restores.push(true);});});
    await cold.emulateMedia({reducedMotion:'reduce'});
    await cold.goto(specimenOrigin+'/icon-specimen/index.html',{waitUntil:'commit'});
    await cold.waitForFunction(()=>window.fixture);
    const coldStart=providerRequests,control=cold.getByRole('button',{name:'Visit instructions'});
    await cold.evaluate(()=>document.documentElement.dir='rtl');
    async function assertColdState(expanded) {
      assert.equal(await control.getAttribute('aria-expanded'),String(expanded));
      assert.equal(await cold.locator('#panel').isVisible(),expanded);
      assert.equal(await cold.locator('svg path').getAttribute('d'),initial.tokens.icons.disclosure.states[expanded?'open':'closed'][0].d);
      assert.equal(await cold.locator('svg').evaluate(e=>e.style.transform),expanded?'':'scaleX(-1)');
      assert.equal(await cold.evaluate(()=>fixture.view.state().immediate),true);
    }
    await control.click();await assertColdState(true);
    await cold.keyboard.press('Space');await assertColdState(false);
    release();await cold.waitForFunction(()=>window.ready);
    assert.match(await cold.locator('#load-status').textContent(),/default/);
    await control.click();await assertColdState(true);
    const expectedRequests=providerRequests-coldStart;assert.equal(expectedRequests,0);
    const count=await cold.evaluate(()=>restores.length);
    await cold.goto(specimenOrigin+'/icon-other');await cold.goBack({waitUntil:'commit'});
    await cold.waitForFunction(n=>window.restores?.length===n+1,count);
    await cold.keyboard.press('Space');await assertColdState(false);
    await control.click();await assertColdState(true);
    appearanceFault=null;
    const selected={...initial.config,motion:'reduced',iconFamily:'solid',disclosureIcon:'badge'};
    await publish(selected);await cold.evaluate(()=>fixture.reload());
    assert.equal(await control.getAttribute('aria-expanded'),'true');
    assert.equal(await cold.locator('svg path').count(),2);
    assert.equal(await cold.locator('svg').getAttribute('fill'),'currentColor');
    assert.equal(await cold.evaluate(()=>document.activeElement.id),'disclosure');
    assert.equal(await cold.evaluate(()=>fixture.view.state().immediate),true);
    assert.equal(await cold.locator('#load-status').textContent(),'Appearance loaded.');
    const retained=await cold.locator('svg').innerHTML();appearanceFault={mode:'http'};
    await cold.evaluate(()=>fixture.reload());
    assert.equal(await cold.locator('svg').innerHTML(),retained);
    assert.match(await cold.locator('#load-status').textContent(),/retaining/);
    assert.equal(await control.getAttribute('aria-expanded'),'true');
    coldCases.push({failure:mode,pendingUsable:true,failedUsable:true,directionalRTL:true,providerRequests:expectedRequests,
      persisted:true,recoveryPreservesOpen:true,recoveryPreservesFocus:true,recoveryReduced:true,selectedFamily:'solid',selectedVariant:'badge',lastValidRetained:true});
    appearanceFault=null;await cold.close();await publish({...initial.config,motion:'standard'});
  }
  record('COLD-RECOVERY',{cases:coldCases});
  await page.evaluate(()=>{document.querySelector('button').click();fixture.view.destroy();});
  const deadD=await page.locator('svg path').getAttribute('d');await page.waitForTimeout(120);
  assert.equal(await page.locator('svg path').getAttribute('d'),deadD);
  const deadState=await state();await page.emulateMedia({reducedMotion:'reduce'});await page.evaluate(()=>document.querySelector('button').click());
  assert.equal((await state()).open,deadState.open);record('CLEANUP',{disposed:true,stable:true});
  const failed=await context.newPage();await failed.route('**/vendor/**',r=>r.abort());
  await failed.goto(specimenOrigin+'/icon-specimen/index.html');await failed.waitForFunction(()=>window.ready);
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
  const report={schema_version:1,stage:'R15.3',recorded_on:'2026-11-02',engine:{name:pin.name,version:pin.version,integrity:pin.integrity},browser:browser.version(),source,observations,
    artifacts:{'mobile.png':hash(await readFile(join(out,'mobile.png')))},limitations:'Synthetic existing appearance API. Static assets served over loopback HTTP; API writes use real HTTP/session/CSRF/store. BFCache tests require actual persisted restoration. No production or WordPress runtime change; no Aria catalog asset or exporter execution; unsupported solid/badge pair is this adapter restriction, not engine 2.x limitation.'};
  await writeFile(join(out,'runtime.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({passed:observations.length,browser:report.browser,gzip_bytes:gzip,output:out}));
} finally {await browser?.close();assetServer?.closeAllConnections();assetServer?.close();server.kill();}
