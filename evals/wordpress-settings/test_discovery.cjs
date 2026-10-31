const assert = require("node:assert/strict");
const D = require("../fixtures/wordpress-settings/plugin/discovery.js");
const allowed = ["manage_options"];
for (const [query, id] of [["وب هوک", "endpoint"], ["وب‌هوک", "endpoint"], ["گيرنده", "email"], ["دريافت كننده", "email"], ["كليد", "credentialAction"], ["WEBHOOK", "endpoint"]]) {
    assert.equal(D.search(D.catalog(true), query, allowed)[0]?.id, id, query);
}
assert.equal(D.search(D.catalog(false), "recipient email", allowed)[0].id, "email");
assert.deepEqual(D.search(D.catalog(true), "", allowed), []);
assert.deepEqual(D.search(D.catalog(true), "not-a-setting", allowed), []);
assert.deepEqual(D.search(D.catalog(true), "webhook", []), []);
const restricted = [...D.catalog(false), {id:"restricted", label:"webhook secret audit", help:"Restricted", aliases:[], capability:"manage_network"}];
assert.deepEqual(D.search(restricted, "secret audit", allowed), []);
assert.deepEqual(D.search([{...restricted[0], visible:false}], "title", allowed), []);
const result = D.search([{...D.catalog(false)[0], value:"private-draft", secret:"never-return"}], "title", allowed);
assert.deepEqual(Object.keys(result[0]).sort(), ["group", "help", "id", "label"]);
assert.deepEqual(D.search([{...D.catalog(false)[0], value:"private-draft"}], "private-draft", allowed), []);
console.log("PASS: Persian/English aliases, whitespace variants, empty/missing queries, capability filtering and no value/secret indexing or output.");
