import {mountDisclosure} from './adapter.mjs';
const q=s=>document.querySelector(s), params=new URLSearchParams(location.search);
const view=mountDisclosure({button:q('#disclosure'),panel:q('#panel'),svg:q('svg'),
  media:matchMedia('(prefers-reduced-motion: reduce)'),
  loadEngine:params.has('static')?null:()=>import('./vendor/dom.js')});
let last,controller,loadGeneration=0;
async function show(record) {
  last=record;
  for(const [key,value] of Object.entries(record.tokens))
    if(key.startsWith('--') && typeof value==='string')document.documentElement.style.setProperty(key,value);
  q('#provenance').textContent=`${record.source}; ${record.config.iconFamily}/${record.config.disclosureIcon}; ${record.config.motion}`;
  await view.apply(record.tokens);
}
async function reload() {
  controller?.abort();controller=new AbortController();const ticket=++loadGeneration;
  try {
    const response=await fetch('/api/v1/tenants/a/published',{signal:controller.signal});if(!response.ok)throw Error();
    const record=await response.json();if(ticket!==loadGeneration)return;
    await show(record);if(ticket===loadGeneration)q('#load-status').textContent='Appearance loaded.';
  } catch {
    if(ticket===loadGeneration)q('#load-status').textContent=last?
      'Appearance unavailable; retaining the last valid appearance.':
      'Appearance unavailable; using the static default.';
  }
}
// Test-only API; private preview uses the existing authenticated preview endpoint.
window.fixture={view,reload,show,get last(){return last;}};
function pagehide(event) {
  ++loadGeneration;controller?.abort();
  if(event.persisted)view.suspend();
  else {view.destroy();removeEventListener('pagehide',pagehide);removeEventListener('pageshow',pageshow);}
}
function pageshow(event) {if(event.persisted){view.resume();if(!last)reload();}}
addEventListener('pagehide',pagehide);addEventListener('pageshow',pageshow);
await reload();window.ready=true;
