// Controlled late-provider and cleanup regressions; real BFCache is checked in the browser runner.
import assert from 'node:assert/strict';
import {mountDisclosure,DEFAULT_DISCLOSURE} from '../evals/fixtures/icon-morph/adapter.mjs';
import {execFileSync} from 'node:child_process';
class Element extends EventTarget {
  constructor(){super();this.attrs={};this.children=[];this.style={};}
  setAttribute(k,v){this.attrs[k]=v;}
  getAttribute(k){return this.attrs[k];}
  replaceChildren(){this.children=[];}
  append(child){this.children.push(child);}
  get firstElementChild(){return this.children[0];}
}
globalThis.document={documentElement:{dir:'ltr'},createElementNS:()=>new Element()};
const tokens={'--duration':'150ms',icons:{disclosure:{stroke:true,variant:'plain',directional:true,
  states:{closed:[{d:'M7 5L14 12L7 19'}],open:[{d:'M5 8L12 15L19 8'}]}}}};
function harness(loadEngine){
  const button=new Element(),svg=new Element(),panel={hidden:true},media=new EventTarget();media.matches=false;
  const view=mountDisclosure({button,svg,panel,media,loadEngine});
  return {view,button,svg,panel,media,click:()=>button.dispatchEvent(new Event('click'))};
}
function engine(){
  const drivers=[];
  return {drivers,createMorph(path,d,options){
    const driver={progress:1,dead:false,reducedMotion:options.reducedMotion,
      morphTo(next){this.progress=.4;path.setAttribute('d',next);},destroy(){this.dead=true;}};
    drivers.push(driver);return driver;
  }};
}
// Pending work cannot revive suspended or permanently destroyed views.
for(const permanent of [false,true]){
  let release;const provider=engine(),pending=new Promise(r=>release=r),h=harness(()=>pending);
  const applying=h.view.apply(tokens);h.click();
  permanent?h.view.destroy():h.view.suspend();
  const frozen=h.svg.firstElementChild.getAttribute('d');release(provider);await applying;
  assert.equal(provider.drivers.length,0);h.click();
  assert.equal(h.view.state().open,true);assert.equal(h.svg.firstElementChild.getAttribute('d'),frozen);
  h.media.matches=true;h.media.dispatchEvent(new Event('change'));
  await h.view.resume();
  if(permanent){assert.equal(provider.drivers.length,0);assert.equal(h.view.state().disposed,true);}
  else {assert.equal(provider.drivers.length,1);assert.equal(provider.drivers[0].reducedMotion,'always');h.click();assert.equal(h.panel.hidden,true);}
  h.view.destroy();assert.ok(provider.drivers.every(d=>d.dead));
}
// Stop active work; apply current owner/user/OS policy, preserving state and one listener.
for(const policy of ['owner','personal','os']){
  const provider=engine(),h=harness(async()=>provider);
  await h.view.apply(policy==='owner'?{...tokens,'--duration':'0ms'}:tokens);
  if(policy==='personal')h.view.setPersonal('off');
  for(let cycle=0;cycle<3;cycle++){
    h.click();const before=h.view.state().open;h.view.suspend();h.view.suspend();
    assert.ok(provider.drivers.every(d=>d.dead));assert.equal(h.view.state().progress,1);
    if(policy==='os')h.media.matches=true;
    await h.view.resume();await h.view.resume();
    assert.equal(h.view.state().open,before);assert.equal(h.view.state().immediate,true);
    assert.equal(provider.drivers.at(-1).reducedMotion,'always');
    h.click();assert.equal(h.view.state().open,!before);
    assert.equal(h.svg.firstElementChild.getAttribute('d'),tokens.icons.disclosure.states[!before?'open':'closed'][0].d);
  }
  h.view.destroy();const before=h.view.state();h.click();h.media.dispatchEvent(new Event('change'));
  assert.deepEqual(h.view.state(),before);assert.ok(provider.drivers.every(d=>d.dead));
}
// Settings arriving during suspension are retained without DOM or provider mutation.
{
  const provider=engine(),h=harness(async()=>provider);await h.view.apply(tokens);h.click();h.view.suspend();
  const before=h.svg.firstElementChild;await h.view.apply({...tokens,'--duration':'0ms'});
  assert.equal(h.svg.firstElementChild,before);assert.ok(provider.drivers.every(d=>d.dead));
  await h.view.resume();assert.equal(h.view.state().open,true);assert.equal(provider.drivers.at(-1).reducedMotion,'always');h.view.destroy();
}
const catalog=JSON.parse(execFileSync(process.env.PYTHON||'python3',['-B','-c',
  "import sys,json;sys.path.insert(0,'scripts');from runtime_icons import asset;print(json.dumps(asset('outline','disclosure','plain')))"],
  {cwd:new URL('../',import.meta.url),encoding:'utf8',windowsHide:true}));
assert.deepEqual(DEFAULT_DISCLOSURE,catalog);
for(const dir of ['ltr','rtl']){
  document.documentElement.dir=dir;let requests=0;const h=harness(()=>{requests++;throw Error('Must stay static');});
  assert.equal(h.view.state().immediate,true);assert.equal(h.view.state().mode,'static');
  assert.equal(h.svg.style.transform,dir==='rtl'?'scaleX(-1)':'');
  h.click();assert.equal(h.svg.firstElementChild.getAttribute('d'),catalog.states.open[0].d);
  assert.equal(h.svg.style.transform,'');h.click();
  assert.equal(h.svg.firstElementChild.getAttribute('d'),catalog.states.closed[0].d);
  assert.equal(h.svg.style.transform,dir==='rtl'?'scaleX(-1)':'');assert.equal(requests,0);h.view.destroy();
}
console.log('PASS: lifecycle, pending settings, approved cold-start fallback and directional RTL.');
