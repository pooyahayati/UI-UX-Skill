# Real WordPress settings specimen

Synthetic evaluation plugin, not a production settings engine. Uses WordPress's
public shared controls and a no-build JavaScript entry; no npm/Composer dependency
is added. The two hosts are WordPress 6.8 (compatibility floor) and 7.1.3 (stable
verified 2026-10-10), PHP 8.3, and MariaDB 11.4. Update execution-time versions
deliberately and retain the new compatibility evidence.

## Start

Use an existing Docker installation and set random **synthetic**
`WPS_DB_PASSWORD`, `WPS_DB_ROOT_PASSWORD`, and `WPS_ADMIN_PASSWORD` in your process
environment. Do not commit them. Inspect available images and ports first.

```sh
docker compose -f evals/fixtures/wordpress-settings/compose.yaml up -d
docker exec uiux-wps-specimen-current-1 php /fixture/bootstrap.php
docker exec uiux-wps-specimen-minimum-1 php /fixture/bootstrap.php
```

Core downloads come from WordPress.org into fresh fixture volumes. Bootstrap is
CLI-only, idempotent and cannot send mail. It creates synthetic administrator,
second administrator and subscriber accounts. `--reset` resets only this fixture's
own synthetic settings option; never run it against a real site. `--persian`
selects the administrator's Persian locale after official translation files are
available in that host's languages directory. Browser tests reset synthetic
settings on both hosts at their start to make repeat runs reproducible.

Open the owned settings page:

- [Current specimen](http://127.0.0.1:8790/wp-admin/options-general.php?page=wps-specimen)
- [Minimum-version specimen](http://127.0.0.1:8791/wp-admin/options-general.php?page=wps-specimen)

Use `variant=simple` for the short form, `lang=en` for the English compatibility
variant and `fault=load` for initial-load failure. Test review controls provide
rejection, delay and uncertain-response demonstrations. Normal requests remain
independent of them; no external service/mail request occurs.

## Verify

Using an already available Node/Playwright and Chromium-family browser runtime:

```sh
node evals/wordpress-settings/test_model.cjs
# Set WPS_EVIDENCE_DIR to an existing directory outside the product checkout.
# WPS_BROWSER_CHANNEL defaults to msedge; WPS_DOCKER defaults to docker.
node evals/wordpress-settings/run_browser.cjs
python -B -X utf8 evals/wordpress-settings/test_contracts.py
```

The browser runner reads the synthetic login credential privately from the owned
container; it does not print it or retain session cookies in Git. It exercises
server requests, two admin sessions, denied reads/writes, actual response loss after a
commit, keyboard/modal behavior, minimum/current hosts and Persian normal/narrow
captures plus an owned-surface 200% CSS zoom stress check. That stress check is not
native browser zoom or assistive-technology certification.
Generated captures/reports stay outside source; selected accepted evidence is
retained under the dedicated evaluation suite. Structural/model checks do not
replace real-admin observation. See [design criteria](DESIGN.md) and
[actual execution](../../wordpress-settings/EXECUTION.md).

Stop or remove only this Compose project's containers/volumes when finished;
verify ownership before removing synthetic data. The old compatibility host is
loopback-only for testing, not a deployment recommendation. Screenshots and
synthetic assets do not grant product-owner approval or universal accessibility
certification. Included Vazirmatn font files retain their [SIL OFL license](plugin/fonts/OFL.txt).
