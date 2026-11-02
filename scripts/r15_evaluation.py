"""Current icon recovery evidence, separate from preserved R14 runtime history."""
from pathlib import Path
from evidence_json import load_json
from release_version_binding import content_digest
from behavior_evaluation import digest
from r14_evaluation import RUNTIME_IDS, errors as r14_errors

ROOT = Path(__file__).resolve().parents[1]
RECORD = 'evals/r15/evidence/runtime.json'
ACCEPTED = 'def8b604d23d7c3c944bec0dcb5317985bef4aa97fc25fdeab573f56fb71d81e'
SOURCES = {'scripts/test_icon_morph_browser.mjs', 'scripts/runtime_appearance.py', 'scripts/runtime_icons.py',
           *('evals/fixtures/icon-morph/' + name for name in ('index.html', 'adapter.mjs', 'fixture.mjs', 'provider.json'))}


def errors(result=None, *, root=ROOT):
    try:
        if result is None:
            result = load_json(root / RECORD)
        if result.get('schema_version') != 1 or result.get('stage') != 'R15.3':
            return ['Invalid R15 runtime scope']
        rows = result['observations']
        expected = RUNTIME_IDS | {'BFCACHE', 'COLD-RECOVERY'}
        if len(rows) != len(expected) or {row['id'] for row in rows} != expected:
            return ['Missing/duplicate/unknown R15 runtime observation']
        if any(row['status'] != 'passed' or not row['details'] for row in rows):
            return ['Non-passing R15 runtime observation']
        observations = {row['id']: row['details'] for row in rows}
        cycles = observations['BFCACHE']['cycles']
        if (len(cycles) != 4 or {(c['provider'], c['initialOpen']) for c in cycles} !=
                {(p, state) for p in ('static', 'morphicons') for state in (False, True)} or
                any(type(c['initialOpen']) is not bool or any(c.get(k) is not True for k in
                    ('persisted','pointerKeyboard','singleActivation','focus','reducedAfterReturn','geometry')) for c in cycles)):
            return ['Incomplete/contradictory BFCache recovery evidence']
        cold = observations['COLD-RECOVERY']['cases']
        if (len(cold) != 2 or {c['failure'] for c in cold} != {'http','network'} or
                any(c.get('providerRequests') != 0 or c.get('selectedFamily') != 'solid' or c.get('selectedVariant') != 'badge' or
                    any(c.get(k) is not True for k in ('pendingUsable','failedUsable','directionalRTL','persisted',
                        'recoveryPreservesOpen','recoveryPreservesFocus','recoveryReduced','lastValidRetained')) for c in cold)):
            return ['Incomplete/contradictory cold-start recovery evidence']
        pin = load_json(root/'evals/fixtures/icon-morph/provider.json')
        if result['engine'] != {k: pin[k] for k in ('name','version','integrity')} or not result.get('browser'):
            return ['Runtime provider/environment identity changed']
        payload = observations['PAYLOAD']
        if (payload['static_provider_bytes'] != 0 or payload['budget_gzip_bytes'] != pin['budget']['additional_route_gzip_bytes'] or
                not 0 < payload['additional_gzip_bytes'] <= payload['budget_gzip_bytes']):
            return ['Runtime payload budget violated']
        if set(result['source']) != SOURCES:
            return ['Runtime source inventory changed']
        for name, sha in result['source'].items():
            path = root/name
            if path.is_symlink() or digest(path.read_bytes().replace(b'\r\n',b'\n')) != sha:
                return ['Runtime producer/input changed: ' + name]
        if set(result['artifacts']) != {'mobile.png'}:
            return ['Runtime artifact inventory changed']
        for name, sha in result['artifacts'].items():
            path = root/'evals/r15/evidence'/name
            if path.is_symlink() or digest(path.read_bytes()) != sha:
                return ['Runtime artifact changed: ' + name]
        if content_digest(result) != ACCEPTED:
            return ['Reviewed R15 runtime record identity changed']
        return r14_errors('evals/r14/evidence/icon-runtime.json', root=root,
                         runtime_source_root=root/'evals/r15/r14-runtime-source')
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        return ['Invalid R15 runtime evidence: ' + str(error)]


if __name__ == '__main__':
    import sys
    problems = errors()
    print('\n'.join(problems) if problems else 'R15 current runtime and preserved R14 history verified; not a production or model evaluation.')
    sys.exit(bool(problems))
