# WordPress settings evaluation

Raw inputs are in [briefs](../fixtures/wordpress-settings/briefs.json); required
outcomes are in the [plan](../../docs/WORDPRESS_SETTINGS_ROADMAP.md#planned-acceptance-scenarios).
The [execution record](EXECUTION.md) keeps actual evidence and limitations.

Protected Skill content is bound to [the pre-edit baseline](baseline.json). Hashes
use canonical UTF-8 Git content (CRLF normalized to LF), so a checkout line-ending
conversion is not a behavioral change. Version-only release metadata is separate.

Dedicated structural/regression command: `python -B -X utf8 evals/wordpress-settings/test_contracts.py`.
Real-admin specimen/browser commands are documented in the [runnable fixture](../fixtures/wordpress-settings/README.md).
The structural gate does not prove model decisions, rendering or WordPress runtime
behavior. No new independent agent/session is authorized by these artifacts.

[RESULTS.json](RESULTS.json) binds the nineteen accepted outcomes to their methods,
candidate content hashes and package comparison. [Source review](SOURCE_REVIEW.md)
and [actual browser observations](evidence/browser-results.json) remain distinct.

Selected real-admin captures: [simple desktop](evidence/persian-simple-1440.png),
[simple narrow](evidence/persian-simple-390.png), [multi-topic desktop](evidence/persian-multi-1440.png),
[multi-topic narrow](evidence/persian-multi-390.png), [reset dialog](evidence/persian-reset-dialog-390.png),
and [200% owned-surface CSS zoom stress](evidence/persian-zoom-200.png).
These are synthetic engineering evidence, not production design approval.
