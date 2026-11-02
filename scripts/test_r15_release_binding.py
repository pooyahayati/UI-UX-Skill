"""Patch release succession preserves original evidence and rejects raw drift."""
import copy
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from behavior_evaluation import ROOT, snapshot
from evidence_json import load_json
from r15_release_binding import BEFORE, RECORDS, r15_release_predecessor
from release_version_binding import content_digest, tree_digest, version_digest
from test_r15_evidence import duplicate


class R15Release(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = snapshot(ROOT / 'skills/ui-ux-skill')
        cls.binding = load_json(ROOT / 'evals/r15-release-version.json')

    def test_only_version_changes_and_retained_chain_passes(self):
        from r14_release_binding import r14_release_predecessor
        from r13_source_binding import r13_predecessor
        original = copy.deepcopy(self.binding)
        previous = r15_release_predecessor(self.files, self.binding)
        self.assertEqual(tree_digest(previous), BEFORE)
        self.assertEqual([p for p in previous if previous[p] != self.files[p]], ['VERSION'])
        self.assertEqual(previous['VERSION'], version_digest('3.7.0'))
        self.assertEqual(self.binding, original)
        self.assertEqual(r14_release_predecessor(self.files), r14_release_predecessor(previous))
        self.assertEqual(r13_predecessor(self.files), r13_predecessor(previous))

    def test_tree_or_version_drift_cannot_be_rebound(self):
        for files in ({**self.files, 'SKILL.md': '0' * 64}, {**self.files, 'extra.md': '0' * 64},
                      {p: h for p, h in self.files.items() if p != 'LICENSE'},
                      {**self.files, 'VERSION': version_digest('3.7.2')}):
            for binding in (self.binding, {**self.binding, 'candidate_after_sha256': tree_digest(files)}):
                with self.assertRaises(ValueError):
                    r15_release_predecessor(files, binding)

    def test_every_scope_field_is_required(self):
        bad = [[], {}, {**self.binding, 'extra': True}]
        for key in self.binding:
            value = copy.deepcopy(self.binding); value.pop(key); bad.append(value)
        for key in self.binding:
            bad.append({**self.binding, key: None})
        for binding in bad:
            with self.assertRaises(ValueError):
                r15_release_predecessor(self.files, binding)

    def test_raw_duplicates_and_joint_record_relabel_are_rejected(self):
        with tempfile.TemporaryDirectory(prefix='uiux-r15-release-') as temp:
            root = Path(temp)
            names = ['evals/r15-release-version.json', *RECORDS]
            for name in names:
                target = root / name; target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / name, target)
            for name in names:
                original = (ROOT / name).read_text(encoding='utf-8')
                for equal in (False, True):
                    (root / name).write_text(duplicate(original, equal=equal)[0], encoding='utf-8')
                    with self.assertRaisesRegex(ValueError, 'Duplicate JSON field'):
                        r15_release_predecessor(self.files, root=root)
                (root / name).write_text(original, encoding='utf-8')
            for name in RECORDS:
                changed = load_json(ROOT / name); changed['notes'] = 'relabeled as new acceptance'
                (root / name).write_text(json.dumps(changed), encoding='utf-8')
                with self.assertRaisesRegex(ValueError, 'record changed'):
                    r15_release_predecessor(self.files, root=root)
                binding = copy.deepcopy(self.binding); binding['records'][name] = content_digest(changed)
                with self.assertRaisesRegex(ValueError, 'identity or scope'):
                    r15_release_predecessor(self.files, binding, root=root)
                shutil.copyfile(ROOT / name, root / name)

    def test_cli_keeps_fresh_evaluation_distinct(self):
        for stage in ('r13', 'r14'):
            result = subprocess.run([sys.executable, '-B', 'scripts/validate_eval_result.py',
                f'evals/ui-foundations/{stage}-result.json', '--suite', 'ui-foundations', '--accept',
                f'--{stage}-release-binding', f'evals/{stage}-release-version.json'],
                cwd=ROOT, capture_output=True, text=True, encoding='utf-8')
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn('not a fresh 3.7.1 model evaluation', result.stdout)


if __name__ == '__main__':
    unittest.main()
