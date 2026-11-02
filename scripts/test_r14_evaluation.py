"""Accepted outputs/runtime provenance cannot be relabelled or detached from inputs."""
import copy
import json
import unittest
from pathlib import Path
from unittest.mock import patch
from behavior_evaluation import ROOT
from r14_evaluation import ACCEPTED, errors
from evidence_json import load_json

HISTORICAL_RUNTIME = ROOT/'evals/r15/r14-runtime-source'

class R14Evaluation(unittest.TestCase):
    def test_all_reviewed_records_and_bound_artifacts(self):
        for name in ACCEPTED:
            self.assertEqual(errors(name,runtime_source_root=HISTORICAL_RUNTIME),[],name)

    def test_missing_relabelled_or_contradictory_rows_are_rejected(self):
        for name in ACCEPTED:
            original=load_json(ROOT/name)
            key="observations" if "observations" in original else "cases"
            for mutation in ("missing","duplicate","status","details"):
                changed=copy.deepcopy(original)
                if mutation=="missing": changed[key].pop()
                elif mutation=="duplicate": changed[key].append(changed[key][0])
                elif mutation=="status": changed[key][0]["status"]="failed"
                else: changed[key][0]["details"]={"overflow":True}
                self.assertTrue(errors(name,changed),(name,mutation))

    def test_changed_outputs_images_raw_requests_and_producer_fail(self):
        targets={
            "evals/r14/stage2-results.json":["evals/r14/outputs/C01-baseline.md","evals/r14/evidence/C01.png","evals/r14/CASES.md"],
            "evals/r14/stage3-results.json":["evals/r14/outputs/I02.md"],
            "evals/r14/evidence/icon-runtime.json":["scripts/test_icon_morph_browser.mjs","scripts/runtime_icons.py","evals/r14/evidence/mobile.png"],
        }
        original_bytes=Path.read_bytes;original_text=Path.read_text
        for name,paths in targets.items():
            result=load_json(ROOT/name)
            for path in paths:
                target=(HISTORICAL_RUNTIME if name.endswith('icon-runtime.json') and not path.startswith('evals/r14/') else ROOT)/path
                with patch.object(Path,"read_bytes",lambda p: b"tampered" if p==target else original_bytes(p)), \
                     patch.object(Path,"read_text",lambda p,*a,**k: "tampered" if p==target else original_text(p,*a,**k)):
                    self.assertTrue(errors(name,result,runtime_source_root=HISTORICAL_RUNTIME),path)

if __name__=="__main__":unittest.main()
