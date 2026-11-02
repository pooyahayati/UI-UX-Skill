"""Raw-file regressions for R14 evidence readers; never mutate accepted reports."""
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from behavior_evaluation import ROOT, snapshot
from r14_evaluation import ACCEPTED, errors
from r14_release_binding import RECORDS, r14_release_predecessor
from r14_source_binding import r14_predecessor, retained_r13_version_case
from release_version_binding import version_digest


def duplicate(raw, key=None, equal=False):
    pattern = r'("([^"\\]+)"\s*:\s*)("(?:[^"\\]|\\.)*"|-?\d+|true|false|null)'
    match = next(m for m in re.finditer(pattern, raw) if key is None or m[2] == key)
    earlier = match[3] if equal else ('false' if match[3] != 'false' else 'true')
    return raw[:match.start()] + match[1] + earlier + ', ' + raw[match.start():], match[2]


class RawEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = snapshot(ROOT / 'skills/ui-ux-skill')

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='uiux-r15-json-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        # Only small raw JSON inputs are needed; source snapshots are passed explicitly.
        for source in (ROOT / 'evals').rglob('*.json'):
            target = self.root / source.relative_to(ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)

    def corrupt(self, name, key=None, equal=False):
        path = self.root / name
        raw = (ROOT / name).read_text(encoding='utf-8')
        body, field = duplicate(raw, key, equal)
        # Prove why a permissive parse + semantic hash is insufficient.
        self.assertEqual(json.loads(body), json.loads(raw))
        path.write_text(body, encoding='utf-8')
        return path, field

    def test_release_rejects_raw_duplicates_in_every_read_record(self):
        for name in ['evals/r14-release-version.json', *RECORDS]:
            for equal in (False, True):
                with self.subTest(name=name, equal=equal):
                    path, key = self.corrupt(name, equal=equal)
                    with self.assertRaisesRegex(ValueError, re.escape(path.name) + '.*Duplicate JSON field: ' + key):
                        r14_release_predecessor(self.files, root=self.root)
                    shutil.copyfile(ROOT / name, path)

    def test_nested_failed_passed_reproduction_rejected(self):
        name = 'evals/r14/evidence/icon-runtime.json'
        path, key = self.corrupt(name, 'status')
        with self.assertRaisesRegex(ValueError, 'icon-runtime.json.*Duplicate JSON field: status'):
            r14_release_predecessor(self.files, root=self.root)

    def test_source_and_retained_parent_readers_reject_duplicates(self):
        files = {**self.files, 'VERSION': version_digest('3.6.1')}
        for name in ['evals/r14-source.json', 'evals/ui-foundations/r13-result.json']:
            path, key = self.corrupt(name)
            with self.assertRaisesRegex(ValueError, 'Duplicate JSON field: ' + key):
                r14_predecessor(files, root=self.root)
            shutil.copyfile(ROOT / name, path)
        name = 'evals/ui-foundations/r13-result.json'
        path, key = self.corrupt(name)
        with self.assertRaisesRegex(ValueError, 'Duplicate JSON field: ' + key):
            retained_r13_version_case({}, {}, root=self.root)

    def test_evaluation_file_entry_and_companions_reject_duplicates(self):
        for name in ACCEPTED:
            path, key = self.corrupt(name)
            self.assertRegex(' '.join(errors(name, root=self.root)), 'Duplicate JSON field: ' + key)
            shutil.copyfile(ROOT / name, path)
        for name, companion in [('evals/r14/stage2-results.json', 'evals/r14-stage2-source.json'),
                                ('evals/r14/stage3-results.json', 'evals/r14-source.json')]:
            path, key = self.corrupt(companion)
            self.assertRegex(' '.join(errors(name, root=self.root)), 'Duplicate JSON field: ' + key)
            shutil.copyfile(ROOT / companion, path)

    def test_cli_rejects_raw_nested_report_and_binding_duplicates(self):
        name = 'evals/ui-foundations/r14-result.json'
        for record, key in [(name, 'result'), ('evals/r14-release-version.json', 'scope')]:
            path, field = self.corrupt(record, key)
            result = subprocess.run([sys.executable, '-B', str(ROOT/'scripts/validate_eval_result.py'),
                str(path if record == name else ROOT/name), '--suite', 'ui-foundations', '--accept',
                '--r14-release-binding', str(path if record != name else ROOT/'evals/r14-release-version.json')],
                capture_output=True, text=True, encoding='utf-8')
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn('Duplicate JSON field: ' + field, result.stdout)
            self.assertIn(path.name, result.stdout)
            self.assertNotIn('outcomes pass', result.stdout)

    def test_formatting_and_distinct_objects_remain_valid(self):
        from evidence_json import load_json
        for path in (self.root/'evals').rglob('*.json'):
            value = load_json(path)
            path.write_text(json.dumps(value, sort_keys=True, indent=3), encoding='utf-8')
        self.assertIsInstance(r14_release_predecessor(self.files, root=self.root), dict)
        path = self.root/'separate.json'
        path.write_text('{"a":{"status":"failed"},"b":{"status":"passed"}}', encoding='utf-8')
        self.assertEqual(load_json(path), {'a':{'status':'failed'},'b':{'status':'passed'}})


if __name__ == '__main__':
    unittest.main()
