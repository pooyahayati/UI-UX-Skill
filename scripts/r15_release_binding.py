"""Exact R15 patch-release metadata succession, not a new model evaluation."""
from pathlib import Path

from evidence_json import load_json
from release_version_binding import content_digest, tree_digest, version_digest

ROOT = Path(__file__).resolve().parents[1]
BEFORE = '08206437c937c36255cd97b2094f8a55157b4ac3d9b12d524bd75c3a10df5827'
AFTER = '87e50e72260117c4cc10683495a243f05c9596006702afa50c2f911d89d13b11'
RECORDS = {
    'evals/r14-release-version.json': 'b32cbcddf5c1cb9d43ca07f4b5cb9a1a2cb847c72cd5655b93bf21d068cbf0ac',
    'evals/r15/evidence/runtime.json': 'def8b604d23d7c3c944bec0dcb5317985bef4aa97fc25fdeab573f56fb71d81e',
}


def r15_release_predecessor(actual, binding=None, *, root=ROOT):
    """Expose the exact 3.7.0 portable tree only after checking the 3.7.1 tree.

    The caller still validates retained R14 records and their source succession.
    The separate R15 runtime gate validates its actual source, artifact and scope.
    """
    if binding is None:
        binding = load_json(root / 'evals/r15-release-version.json')
    expected = {
        'schema_version': 1, 'scope': 'r15-release-version-only', 'normalization': 'git-lf',
        'decision': 'docs/releases/3.7.1.md#authority',
        'recorded_version': '3.7.0', 'release_version': '3.7.1',
        'version_change': {'path': 'VERSION', 'previous_sha256': version_digest('3.7.0'),
                           'sha256': version_digest('3.7.1')},
        'candidate_before_sha256': BEFORE, 'candidate_after_sha256': AFTER,
        'records': RECORDS,
    }
    if (not isinstance(binding, dict) or set(binding) != set(expected) | {'notes'}
            or any(binding.get(key) != value for key, value in expected.items())
            or not isinstance(binding.get('notes'), str) or not binding['notes'].strip()):
        raise ValueError('Invalid R15 release-only identity or scope')
    if (not isinstance(actual, dict) or actual.get('VERSION') != version_digest('3.7.1')
            or tree_digest(actual) != AFTER):
        raise ValueError('R15 release source identity changed')
    previous = {**actual, 'VERSION': version_digest('3.7.0')}
    if tree_digest(previous) != BEFORE:
        raise ValueError('R15 release changes more than VERSION')
    for name, expected_digest in RECORDS.items():
        if content_digest(load_json(root / name)) != expected_digest:
            raise ValueError('Accepted R15 release record changed: ' + name)
    return previous
