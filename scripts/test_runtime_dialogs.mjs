// Execute the shipped handler using a DOM model, not a browser/conformance test.
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import vm from 'node:vm';
const source = readFileSync(new URL('../evals/fixtures/runtime-appearance/dialog-focus.js', import.meta.url), 'utf8');
let checks = 0;
function fixture(count = 2) {
  const document = { activeElement: null };
  const stops = Array.from({ length: count }, () => ({
    disabled: false, tabIndex: 0, visible: true,
    getClientRects() { return this.visible ? [{}] : []; },
    focus() { document.activeElement = this; }
  }));
  let handler;
  const dialog = { open: true, modal: true, matches(selector) { assert.equal(selector, ':modal'); return this.modal; },
    addEventListener(type, fn) { assert.equal(type, 'keydown'); handler = fn; },
    querySelectorAll() { return stops; }, contains(node) { return stops.includes(node); } };
  document.querySelectorAll = () => [dialog];
  vm.runInNewContext(source, { document });
  return { document, stops, dialog, key(key = 'Tab', shiftKey = false) {
    const event = { key, shiftKey, prevented: false, preventDefault() { this.prevented = true; } };
    handler(event); return event.prevented;
  } };
}
let f = fixture(1);
f.document.activeElement = f.stops[0];
assert.equal(f.key(), true); assert.equal(f.document.activeElement, f.stops[0]); checks++;
assert.equal(f.key('Tab', true), true); assert.equal(f.document.activeElement, f.stops[0]); checks++;
f = fixture(); f.document.activeElement = f.stops[1];
assert.equal(f.key(), true); assert.equal(f.document.activeElement, f.stops[0]); checks++;
assert.equal(f.key('Tab', true), true); assert.equal(f.document.activeElement, f.stops[1]); checks++;
f.document.activeElement = f.stops[0]; assert.equal(f.key(), false); checks++;
assert.equal(f.key('Escape'), false); checks++;
f.dialog.open = false; assert.equal(f.key('Tab', true), false); checks++;
f.dialog.open = true; f.dialog.modal = false; assert.equal(f.key('Tab', true), false); checks++;
f = fixture(4); f.stops[1].disabled = true; f.stops[2].tabIndex = -1; f.stops[3].visible = false;
f.document.activeElement = f.stops[0]; assert.equal(f.key(), true); assert.equal(f.document.activeElement, f.stops[0]); checks++;
f.document.activeElement = {}; assert.equal(f.key(), true); assert.equal(f.document.activeElement, f.stops[0]); checks++;
f = fixture(0); assert.equal(f.key(), false); checks++;
console.log(`PASS: ${checks} dialog keyboard behavior assertions (DOM model, not browser QA).`);
