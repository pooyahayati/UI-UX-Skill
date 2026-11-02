"""Required runtime rows and producer identity cannot be omitted or relabelled."""
import copy
import unittest
from pathlib import Path
from unittest.mock import patch
from evidence_json import load_json
from r15_evaluation import ROOT, RECORD, errors
from r14_evaluation import errors as historical_errors


class RuntimeEvidence(unittest.TestCase):
    def setUp(self):
        self.report = load_json(ROOT/RECORD)

    def test_current_report_and_history_are_distinct(self):
        self.assertEqual(errors(), [])
        self.assertTrue(historical_errors('evals/r14/evidence/icon-runtime.json'))

    def test_required_rows_and_status(self):
        for index in range(len(self.report['observations'])):
            for mutation in ('missing','duplicate','failed','empty'):
                value=copy.deepcopy(self.report);rows=value['observations']
                if mutation=='missing':rows.pop(index)
                elif mutation=='duplicate':rows.append(rows[index])
                elif mutation=='failed':rows[index]['status']='failed'
                else:rows[index]['details']={}
                self.assertTrue(errors(value),(index,mutation))

    def test_new_scenarios_cannot_be_weakened(self):
        for ident,key in [('BFCACHE','cycles'),('COLD-RECOVERY','cases')]:
            row=next(r for r in self.report['observations'] if r['id']==ident)
            for field in row['details'][key][0]:
                for missing in (True,False):
                    value=copy.deepcopy(self.report)
                    item=next(r for r in value['observations'] if r['id']==ident)['details'][key][0]
                    if missing:item.pop(field)
                    else:item[field]='contradictory'
                    self.assertTrue(errors(value),(ident,field,missing))
            value=copy.deepcopy(self.report)
            next(r for r in value['observations'] if r['id']==ident)['details'][key].pop()
            self.assertTrue(errors(value),ident)

    def test_changed_inputs_artifacts_and_archived_sources_fail(self):
        read=Path.read_bytes
        paths=[*self.report['source'], 'evals/r15/evidence/mobile.png',
               'evals/r15/r14-runtime-source/evals/fixtures/icon-morph/adapter.mjs']
        for name in paths:
            with patch.object(Path,'read_bytes',lambda p: b'changed' if p==ROOT/name else read(p)):
                self.assertTrue(errors(),name)

    def test_source_inventory_provider_scope_and_raw_duplicates_fail(self):
        for key,value in [('stage','R14.3'),('source',{}),('artifacts',{}),('engine',{})]:
            self.assertTrue(errors({**self.report,key:value}),key)
        read=Path.read_text;target=ROOT/RECORD
        raw=target.read_text(encoding='utf-8').replace('"status": "passed"','"status": "failed", "status": "passed"',1)
        with patch.object(Path,'read_text',lambda p,*a,**kw:raw if p==target else read(p,*a,**kw)):
            self.assertIn('Duplicate JSON field: status',' '.join(errors()))


if __name__ == '__main__':
    unittest.main()
