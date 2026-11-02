// Bounded adapter for the EXISTING trusted runtime_icons catalog. Not an SVG importer.
// Prepared outline/plain pair; the regression checks equality with runtime_icons.asset.
export const DEFAULT_DISCLOSURE={use:'disclosure',variant:'plain',requestedFamily:'outline',
  family:'outline',stroke:true,fallback:false,directional:true,
  states:{closed:[{d:'M7 5L14 12L7 19',badge:false}],open:[{d:'M5 8L12 15L19 8',badge:false}]}};
export function mountDisclosure({button, panel, svg, media, loadEngine}) {
  let tokens, asset=DEFAULT_DISCLOSURE, engine, driver, disposed=false, personal='standard';
  let open=false, generation=0, mode='static', policyEvents=0, suspended=false;
  const target=()=>asset?.states[open?'open':'closed'];
  const immediate=()=>!tokens || tokens['--duration']==='0ms' || personal==='off' || media.matches;
  function stop() { driver?.destroy(); driver=undefined; }
  function paint() {
    if (!asset) return;
    svg.replaceChildren();
    svg.setAttribute('fill',asset.stroke?'none':'currentColor');
    svg.setAttribute('stroke',asset.stroke?'currentColor':'none');
    svg.style.transform=asset.directional && !open && document.documentElement.dir==='rtl'?'scaleX(-1)':'';
    for (const item of target()) {
      const path=document.createElementNS('http://www.w3.org/2000/svg','path');
      path.setAttribute('d',item.d);svg.append(path);
    }
  }
  function supported() { return asset?.stroke && asset.variant==='plain' && target()?.length===1; }
  function rebuild() {
    stop();paint();mode='static';
    if (!disposed && !suspended && engine && supported()) {
      try { driver=engine.createMorph(svg.firstElementChild,target()[0].d,{reducedMotion:immediate()?'always':'user'}); mode=immediate()?'immediate':'morph'; }
      catch { stop();paint(); }
    }
  }
  function policyChanged() {
    policyEvents++;
    if(disposed || suspended)return;
    // Stop the ACTIVE spring, not merely future transitions. Business state is already final.
    rebuild();
  }
  function toggle() {
    if(disposed || suspended)return;
    open=!open;button.setAttribute('aria-expanded',String(open));panel.hidden=!open;
    svg.style.transform=asset?.directional && !open && document.documentElement.dir==='rtl'?'scaleX(-1)':'';
    if(driver) {driver.reducedMotion=immediate()?'always':'user';driver.morphTo(target()[0].d,'snappy');}
    else paint();
  }
  paint();button.addEventListener('click',toggle);media.addEventListener('change',policyChanged);
  async function apply(next) {
    if(disposed)return;
    tokens=next;asset=next.icons.disclosure;generation++;const ticket=generation;
    if(suspended)return;
    rebuild();
    if(!engine && supported() && loadEngine) {
      try {const loaded=await loadEngine();if(disposed || suspended || ticket!==generation)return;engine=loaded;rebuild();}
      catch {if(!disposed && !suspended && ticket===generation){stop();paint();mode='static';}}
    }
  }
  return {
    apply,
    suspend() {
      if(disposed || suspended)return;
      suspended=true;generation++;stop();paint();mode='static';
    },
    resume() {if(disposed || !suspended)return;suspended=false;if(tokens)return apply(tokens);},
    setPersonal(value) {if(!['off','standard'].includes(value))throw Error('Unknown personal preset');personal=value;policyChanged();},
    state:()=>({open,mode,immediate:immediate(),progress:driver?.progress??1,disposed,suspended,policyEvents}),
    destroy() {disposed=true;generation++;stop();paint();button.removeEventListener('click',toggle);media.removeEventListener('change',policyChanged);},
  };
}
