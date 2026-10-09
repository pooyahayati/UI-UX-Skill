#!/usr/bin/env bash
set -euo pipefail
case "$WPS_CORE_VERSION" in 6.8|7.1.3) ;; *) echo "Unsupported specimen version" >&2; exit 1;; esac
# Fresh fixture volumes only. Never replace an installed site's core.
if [ ! -e /var/www/html/wp-includes/version.php ]; then
  curl --fail --location --silent --show-error "https://wordpress.org/wordpress-$WPS_CORE_VERSION.tar.gz" -o /tmp/wps-core.tar.gz
  sha256sum /tmp/wps-core.tar.gz
  tar -xzf /tmp/wps-core.tar.gz --strip-components=1 -C /var/www/html
  chown -R www-data:www-data /var/www/html/wp-admin /var/www/html/wp-includes
fi
exec docker-entrypoint.sh apache2-foreground
