import copy
import json
import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch
from behavior_evaluation import ROOT,snapshot,validate_record,tree_digest
from release_version_binding import content_digest
from r14_release_binding import r14_release_predecessor,BEFORE

class R14Release(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files=snapshot(ROOT/'skills/ui-ux-skill')
        cls.binding=json.loads((ROOT/'evals/r14-release-version.json').read_text())
        cls.name='evals/ui-foundations/r14-result.json'
        cls.result=json.loads((ROOT/cls.name).read_text())

    def test_exact_version_only_and_explicit_evidence(self):
        previous=r14_release_predecessor(self.files,self.binding,result=self.result,record=self.name)
        self.assertEqual(tree_digest(previous),BEFORE)
        self.assertEqual([p for p in previous if previous[p]!=self.files[p]],['VERSION'])
        self.assertTrue(validate_record(self.result,ROOT/'evals/ui-foundations',accept=True))
        self.assertEqual(validate_record(self.result,ROOT/'evals/ui-foundations',accept=True,r14_release_binding=self.binding),[])

    def test_metadata_inventory_and_source_mutations_rejected(self):
        for files in ({**self.files,'SKILL.md':'0'*64},{**self.files,'extra.md':'0'*64},
                      {p:h for p,h in self.files.items() if p!='LICENSE'},{**self.files,'VERSION':'0'*64}):
            with self.assertRaises(ValueError):r14_release_predecessor(files,{**self.binding,'candidate_after_sha256':tree_digest(files)})
        for key in self.binding:
            wrong=copy.deepcopy(self.binding);wrong.pop(key)
            with self.assertRaises(ValueError):r14_release_predecessor(self.files,wrong)

    def test_coupled_report_and_sidecar_relabel_rejected(self):
        result=copy.deepcopy(self.result);result['cases'][0]['evaluatorId']='new-run'
        binding=copy.deepcopy(self.binding);binding['records'][self.name]=content_digest(result)
        read=Path.read_text
        with patch.object(Path,'read_text',lambda p,*a,**k:json.dumps(result) if p==ROOT/self.name else read(p,*a,**k)):
            with self.assertRaises(ValueError):r14_release_predecessor(self.files,binding,result=result,record=self.name)

    def test_other_records_and_bridges_rejected(self):
        with self.assertRaises(ValueError):r14_release_predecessor(self.files,result=self.result,record='other')
        bad=copy.deepcopy(self.result);bad['cases'][0]['result']='fail'
        self.assertTrue(validate_record(bad,ROOT/'evals/ui-foundations',accept=True,r14_release_binding=self.binding))
        self.assertTrue(validate_record(self.result,ROOT/'evals/ui-foundations',r14_release_binding=self.binding,r13_release_binding={}))

    def test_cli_explicit_bridge(self):
        base=[sys.executable,'-B','scripts/validate_eval_result.py',self.name,'--suite','ui-foundations','--accept']
        for extra,expected in [([],1),(['--r14-release-binding','evals/r14-release-version.json'],0),(['--r14-release-binding','evals/r13-release-version.json'],1)]:
            r=subprocess.run(base+extra,cwd=ROOT,capture_output=True,text=True)
            self.assertEqual(r.returncode,expected,r.stdout+r.stderr)
            if expected==0:self.assertIn('not a fresh 3.7.0 model evaluation',r.stdout)

if __name__=='__main__':unittest.main()
