import {mountDisclosure} from './adapter.mjs';
const q=s=>document.querySelector(s), params=new URLSearchParams(location.search);
const view=mountDisclosure({button:q('#disclosure'),panel:q('#panel'),svg:q('svg'),
  media:matchMedia('(prefers-reduced-motion: reduce)'),
  loadEngine:params.has('static')?null:()=>import('./vendor/dom.js')});
let last;
async function show(record) {
  last=record;
  for(const [key,value] of Object.entries(record.tokens))
    if(key.startsWith('--') && typeof value==='string')document.documentElement.style.setProperty(key,value);
  q('#provenance').textContent=`${record.source}; ${record.config.iconFamily}/${record.config.disclosureIcon}; ${record.config.motion}`;
  await view.apply(record.tokens);
}
async function reload() {
  try {
    const response=await fetch('/api/v1/tenants/a/published');if(!response.ok)throw Error();
    await show(await response.json());q('#load-status').textContent='Appearance loaded.';
  } catch {
    q('#load-status').textContent='Appearance unavailable; retaining the last valid appearance or static default.';
  }
}
// Test-only API; private preview uses the existing authenticated preview endpoint.
window.fixture={view,reload,show,get last(){return last;}};
addEventListener('pagehide',()=>view.destroy(),{once:true});
await reload();window.ready=true;
