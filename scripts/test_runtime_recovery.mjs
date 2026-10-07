// Execute actual shipped handlers with a small DOM/HTTP model. Browser evidence is separate.
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import vm from 'node:vm';
const source = readFileSync(new URL('../evals/fixtures/runtime-appearance/app.js', import.meta.url), 'utf8');
const copy = value => JSON.parse(JSON.stringify(value));
function fixture() {
  const nodes = new Map();
  function node(id = '') {
    const el = { id, value: '', textContent: '', children: [], listeners: {}, disabled: false,
      setAttribute() {}, removeAttribute() {}, append(...items) { this.children.push(...items); },
      replaceChildren(...items) { this.children = items; },
      addEventListener(type, fn) { this.listeners[type] = fn; },
      focus() { document.activeElement = this; },
      showModal() { this.open = true; }, close() { this.open = false; this.listeners.close?.(); } };
    let assignedId = id;
    Object.defineProperty(el, 'id', { get: () => assignedId, set(value) { assignedId = value; nodes.set(value, el); } });
    if (id) nodes.set(id, el);
    return el;
  }
  const document = { getElementById: id => nodes.get(id) || node(id), createElement: () => node(),
    documentElement: {}, querySelectorAll: () => [] };
  const context = vm.createContext({ document, location: { pathname: '/' }, window: { addEventListener() {} },
    fetch: () => new Promise(() => {}) }); // Hold automatic startup; initialize explicitly below.
  vm.runInContext(source, context);
  const run = code => vm.runInContext(code, context);
  run(`applyTokens = () => {}; renderSurface = () => {}; updateIconGallery = () => {};
    preview = async () => {}; refreshHistory = async () => {};
    state.session = { tenant: 'a', canEdit: true };
    state.catalog = { schema: 3, settings: [
      {key:'palette', label:'Palette', values:['ocean','forest','plum']},
      {key:'spacing', label:'Spacing', values:[16,24,32]}] };
    state.published = { source:'published', revision:1, config:{schema:3,palette:'ocean',spacing:16} };
    state.draft = { draftRevision:4, baseRevision:1, config:{schema:3,palette:'forest',spacing:16} };
    state.editBaseRevision = 1; fillControls(state.draft.config);`);
  const server = { published: { source:'published', revision:2, config:{schema:3,palette:'ocean',spacing:24} },
    draft: copy(run('state.draft')), writes: [], failure: null };
  context.request = async (resource, method = 'GET', body) => {
    if (method === 'GET') return copy(server[resource]);
    if (server.failure) throw server.failure;
    if (body.baseRevision !== server.published.revision) throw Object.assign(new Error('Published moved'), { code:'BASE_CONFLICT' });
    if (body.draftRevision !== (server.draft?.draftRevision ?? 0)) throw Object.assign(new Error('Draft moved'), {code:'DRAFT_CONFLICT'});
    server.writes.push(copy(body));
    server.draft = { config:copy(body.config), baseRevision:body.baseRevision, draftRevision:(server.draft?.draftRevision ?? 0)+1 };
    return copy(server.draft);
  };
  return { run, server, nodes, document, async click(id) { await document.getElementById(id).listeners.click({currentTarget:document.getElementById(id)}); },
    choose(key, value) { document.getElementById('recovery-'+key).value = value; } };
}
let checks = 0;
async function check(name, action) { await action(); checks++; console.log('PASS:', name); }
await check('reload preserves unsaved values and the original edit base', async () => {
  const f = fixture(); f.run(`$('setting-palette').value='plum'; state.dirty=true;`);
  await f.run('reload()');
  assert.equal(f.run('readConfig().palette'), 'plum');
  assert.equal(f.run('state.editBaseRevision'), 1);
  assert.equal(f.run('state.dirty'), true);
});
await check('explicit review keeps newer unselected fields and saves a fresh private draft', async () => {
  const f = fixture(); await f.run('beginRecovery()');
  f.choose('palette','local'); f.choose('spacing','current');
  await f.run('saveRecovery()');
  assert.deepEqual(f.server.writes[0], {config:{schema:3,palette:'forest',spacing:24},baseRevision:2,draftRevision:4});
  assert.equal(f.run('state.editBaseRevision'), 2);
  assert.equal(f.run('state.dirty'), false);
  assert.equal(f.server.published.revision, 2);
});
await check('every difference needs a choice; cancel makes no writes and returns focus', async () => {
  const f = fixture(); await f.run('beginRecovery()');
  await assert.rejects(f.run('saveRecovery()'), /Choose/);
  await f.click('recovery-cancel');
  assert.equal(f.server.writes.length, 0);
  assert.equal(f.run('readConfig().palette'), 'forest');
  assert.equal(f.document.activeElement.id, 'reconcile');
});
await check('another publication during review fails without losing original inputs', async () => {
  const f = fixture(); await f.run('beginRecovery()');
  f.choose('palette','local'); f.choose('spacing','current');
  f.server.published.revision++;
  await assert.rejects(f.run('saveRecovery()'), /Published moved/);
  assert.equal(f.run('readConfig().palette'), 'forest');
  assert.equal(f.run('state.draft.baseRevision'), 1);
  assert.equal(f.run('state.recovery.stale'), true);
  await f.run('beginRecovery()'); f.choose('palette','local'); f.choose('spacing','current');
  await f.run('saveRecovery()'); assert.equal(f.server.draft.baseRevision, 3);
});
await check('same-owner draft race is rejected and explicit refreshed review can recover', async () => {
  const f = fixture(); await f.run('beginRecovery()');
  f.choose('palette','local'); f.choose('spacing','current'); f.server.draft.draftRevision++;
  await assert.rejects(f.run('saveRecovery()'), /Draft moved/);
  await f.run('beginRecovery()'); f.choose('palette','local'); f.choose('spacing','current');
  await f.run('saveRecovery()'); assert.equal(f.server.writes[0].draftRevision,5);
});
await check('network outcome unknown retains review and forces refresh before retry', async () => {
  const f = fixture(); await f.run('beginRecovery()');
  f.choose('palette','local'); f.choose('spacing','current');
  f.server.failure = new Error('Connection outcome unknown');
  await assert.rejects(f.run('saveRecovery()'), /unknown/);
  assert.equal(f.run('state.recovery.local.palette'), 'forest');
  assert.equal(f.run('state.recovery.stale'), true);
  await assert.rejects(f.run('saveRecovery()'), /Refresh/);
});
await check('degraded current storage cannot be used as a reconciliation base', async () => {
  const f = fixture(); f.server.published.source = 'history-fallback';
  await assert.rejects(f.run('beginRecovery()'), /storage/);
  assert.equal(f.server.writes.length,0);
});
await check('publication action remains disabled for a known stale saved draft', async () => {
  const f = fixture(); await f.run('reload()');
  assert.equal(f.nodes.get('publish').disabled,true);
  assert.equal(f.nodes.get('save').disabled,true);
  assert.equal(f.nodes.get('reconcile').disabled,false);
});
await check('refreshing the public reader cannot silently advance an unsaved edit base', async () => {
  const f = fixture(); f.run('state.draft=null; state.dirty=true;');
  await f.run('refreshPublished()');
  await f.click('save');
  assert.equal(f.server.writes.length,0);
  assert.equal(f.run('state.conflict'),true);
  assert.equal(f.run('readConfig().palette'),'forest');
});
await check('acknowledged recovery save is not mislabeled failed by a preview outage', async () => {
  const f = fixture(); await f.run('beginRecovery()');
  f.choose('palette','local'); f.choose('spacing','current');
  f.run(`preview=async()=>{throw new Error('preview down');};`);
  await f.run('saveRecovery()');
  assert.equal(f.run('state.draft.baseRevision'),2);
  assert.match(f.nodes.get('status').textContent,/saved.*refresh failed/);
});
await check('review with no differences still saves explicitly against the fresh base', async () => {
  const f = fixture(); f.run(`fillControls({schema:3,palette:'ocean',spacing:24});`);
  await f.run('beginRecovery()'); assert.equal(f.run('state.recovery.fields.length'),0);
  await f.run('saveRecovery()'); assert.equal(f.server.draft.baseRevision,2);
});
console.log(`PASS: ${checks} runtime recovery scenarios (actual handlers, modeled DOM/HTTP).`);
