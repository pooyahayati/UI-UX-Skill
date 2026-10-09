<?php
// Run only inside the isolated specimen container after wp-config exists.
if (PHP_SAPI !== 'cli') { http_response_code(403); exit; }
if (!in_array(getenv('WPS_SITE_URL'), array('http://127.0.0.1:8790', 'http://127.0.0.1:8791'), true)
    || strlen((string) getenv('WPS_ADMIN_PASSWORD')) < 16) {
    fwrite(STDERR, "Missing isolated fixture environment\n"); exit(1);
}
define('WP_INSTALLING', true);
$_SERVER['HTTP_HOST'] = wp_host_for_fixture();
$_SERVER['REQUEST_URI'] = '/';
function wp_host_for_fixture() { return parse_url(getenv('WPS_SITE_URL'), PHP_URL_HOST) . ':' . parse_url(getenv('WPS_SITE_URL'), PHP_URL_PORT); }
require '/var/www/html/wp-load.php';
require_once ABSPATH . 'wp-admin/includes/upgrade.php';
require_once ABSPATH . 'wp-admin/includes/plugin.php';
add_filter('pre_wp_mail', '__return_false');
if (!is_blog_installed()) {
    wp_install('WordPress settings specimen', 'wps-admin', 'admin@example.test', true, '', getenv('WPS_ADMIN_PASSWORD'));
}
update_option('siteurl', getenv('WPS_SITE_URL'));
update_option('home', getenv('WPS_SITE_URL'));
$result = activate_plugin('wps-specimen/wps-specimen.php');
if (is_wp_error($result)) { fwrite(STDERR, $result->get_error_message()); exit(1); }
$admin = get_user_by('login', 'wps-admin');
if (in_array('--persian', $argv, true)) { update_user_meta($admin->ID, 'locale', 'fa_IR'); }
if (in_array('--reset', $argv, true)) { delete_option('wps_specimen_state'); }
foreach (array('wps-second' => 'administrator', 'wps-reader' => 'subscriber') as $login => $role) {
    $user = get_user_by('login', $login);
    $id = $user ? $user->ID : wp_create_user($login, getenv('WPS_ADMIN_PASSWORD'), $login . '@example.test');
    if (is_wp_error($id)) { exit(1); }
    (new WP_User($id))->set_role($role);
}
echo wp_json_encode(array('core' => get_bloginfo('version'), 'active_plugins' => get_option('active_plugins'), 'php' => PHP_VERSION)) . "\n";
