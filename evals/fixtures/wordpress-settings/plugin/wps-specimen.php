<?php
/**
 * Plugin Name: WPS Settings Specimen
 * Description: Isolated synthetic UI/UX evaluation; not a production settings engine.
 * Version: 0.1.0
 * Requires at least: 6.8
 * Requires PHP: 8.0
 */
if (!defined('ABSPATH')) { exit; }

function wps_defaults() {
    return array('general' => array('title' => 'Weekly report'),
        'delivery' => array('enabled' => false, 'email' => 'reports@example.test'),
        'advanced' => array('endpoint' => 'https://example.test/hooks/WPS-A2', 'secret' => ''));
}
function wps_state() {
    $raw = get_option('wps_specimen_state', false);
    if ($raw === false) {
        $raw = wp_json_encode(array('revision' => 1, 'settings' => wps_defaults(), 'lastRequestId' => '', 'lastRequestHash' => ''));
        add_option('wps_specimen_state', $raw, '', false);
    }
    return array($raw, json_decode($raw, true));
}
function wps_public_state($state) {
    $settings = $state['settings'];
    $settings['advanced']['credentialConfigured'] = $settings['advanced']['secret'] !== '';
    unset($settings['advanced']['secret']);
    return array('revision' => $state['revision'], 'settings' => $settings, 'lastRequestId' => $state['lastRequestId']);
}
add_action('admin_menu', function () {
    add_options_page('WPS specimen', 'WPS specimen', 'manage_options', 'wps-specimen', function () {
        if (!current_user_can('manage_options')) { wp_die('Access denied', '', array('response' => 403)); }
        echo '<div class="wrap"><div id="wps-root"></div></div>';
    });
});
add_action('admin_enqueue_scripts', function ($hook) {
    if ($hook !== 'settings_page_wps-specimen' || !current_user_can('manage_options')) { return; }
    $asset = require __DIR__ . '/index.asset.php';
    wp_enqueue_script('wps-model', plugins_url('model.js', __FILE__), array(), $asset['version'], true);
    wp_enqueue_script('wps-app', plugins_url('app.js', __FILE__), array_merge(array('wps-model'), $asset['dependencies']), $asset['version'], true);
    wp_enqueue_style('wps-style', plugins_url('style.css', __FILE__), array('wp-components'), $asset['version']);
    $lang = isset($_GET['lang']) && sanitize_key(wp_unslash($_GET['lang'])) === 'en' ? 'en' : 'fa';
    wp_localize_script('wps-app', 'WPSConfig', array('ajaxUrl' => admin_url('admin-ajax.php'),
        'nonce' => wp_create_nonce('wps_specimen'), 'lang' => $lang,
        'variant' => isset($_GET['variant']) && sanitize_key(wp_unslash($_GET['variant'])) === 'simple' ? 'simple' : 'multi',
        'initialFault' => isset($_GET['fault']) && sanitize_key(wp_unslash($_GET['fault'])) === 'load' ? 'load' : 'none'));
});

function wps_error($code, $status, $extra = array()) {
    wp_send_json_error(array_merge(array('code' => $code), $extra), $status);
}
add_action('wp_ajax_wps_specimen', function () {
    if (!current_user_can('manage_options')) { wps_error('denied', 403); }
    if (!wp_verify_nonce(isset($_SERVER['HTTP_X_WPS_NONCE']) ? $_SERVER['HTTP_X_WPS_NONCE'] : '', 'wps_specimen')) { wps_error('nonce', 403); }
    $input = json_decode(file_get_contents('php://input'), true);
    if (!is_array($input) || strlen(wp_json_encode($input)) > 12000) { wps_error('invalid_request', 400); }
    $operation = $input['operation'] ?? '';
    list($raw, $state) = wps_state();
    if ($operation === 'load') {
        if (($input['fault'] ?? '') === 'load') { wps_error('load_failed', 503); }
        wp_send_json_success(wps_public_state($state));
    }
    if (!in_array($operation, array('save', 'reset'), true)) { wps_error('invalid_operation', 400); }
    $section = $input['section'] ?? '';
    if (!is_string($section) || !array_key_exists($section, wps_defaults())) { wps_error('invalid_section', 400); }
    $request_id = $input['requestId'] ?? '';
    if (!is_string($request_id) || !preg_match('/^[a-zA-Z0-9-]{1,80}$/D', $request_id)) { wps_error('invalid_request_id', 400); }
    $values = $input['values'] ?? null;
    if (!is_array($values)) { wps_error('invalid_values', 400); }
    $hash = hash('sha256', wp_json_encode(array($operation, $section, $values)));
    if ($request_id === $state['lastRequestId']) {
        if ($hash !== $state['lastRequestHash']) { wps_error('request_id_reuse', 409); }
        wp_send_json_success(wps_public_state($state));
    }
    if (!isset($input['revision']) || !is_int($input['revision']) || $input['revision'] !== $state['revision']) {
        wps_error('conflict', 409, array('current' => wps_public_state($state)));
    }
    $next = $state;
    if ($operation === 'reset') {
        $next['settings'][$section] = wps_defaults()[$section];
    } else {
        $allowed = array('general' => array('title'), 'delivery' => array('enabled', 'email'),
            'advanced' => array('endpoint', 'credentialAction', 'credential'));
        if (array_diff(array_keys($values), $allowed[$section])) { wps_error('invalid_fields', 400); }
        $errors = array();
        foreach ($values as $key => $value) {
            if ($key === 'enabled') {
                if (!is_bool($value)) { $errors[$key] = 'invalid'; } else { $next['settings'][$section][$key] = $value; }
            } elseif (!is_string($value) || strlen($value) > ($key === 'credential' ? 256 : 500)) {
                $errors[$key] = 'invalid';
            } elseif ($key === 'title') {
                $clean = sanitize_text_field($value);
                if ($clean === '' || mb_strlen($clean) > 80) { $errors[$key] = 'invalid'; } else { $next['settings'][$section][$key] = $clean; }
            } elseif ($key === 'email') {
                if ($value !== '' && !is_email($value)) { $errors[$key] = 'invalid'; } else { $next['settings'][$section][$key] = sanitize_email($value); }
            } elseif ($key === 'endpoint') {
                $url = esc_url_raw($value, array('https'));
                if ($value !== '' && ($url === '' || wp_parse_url($url, PHP_URL_SCHEME) !== 'https' || !wp_parse_url($url, PHP_URL_HOST))) {
                    $errors[$key] = 'invalid';
                } else { $next['settings'][$section][$key] = $url; }
            }
        }
        if ($section === 'advanced') {
            $action = $values['credentialAction'] ?? 'keep';
            if (!in_array($action, array('keep', 'replace', 'remove'), true)) { $errors['credential'] = 'invalid'; }
            if ($action === 'replace') {
                if (!isset($values['credential']) || !is_string($values['credential']) || $values['credential'] === '') { $errors['credential'] = 'invalid'; }
                else { $next['settings']['advanced']['secret'] = $values['credential']; }
            } elseif ($action === 'remove') { $next['settings']['advanced']['secret'] = ''; }
        }
        if ($errors) { wps_error('validation', 422, array('fields' => $errors)); }
    }
    if (($input['fault'] ?? '') === 'reject') { wps_error('rejected', 503); }
    $next['revision']++;
    $next['lastRequestId'] = $request_id;
    $next['lastRequestHash'] = $hash;
    global $wpdb;
    $updated = $wpdb->query($wpdb->prepare("UPDATE $wpdb->options SET option_value = %s WHERE option_name = %s AND option_value = %s",
        wp_json_encode($next), 'wps_specimen_state', $raw));
    if ($updated === false) { wps_error('save_failed', 503); }
    wp_cache_delete('wps_specimen_state', 'options');
    if ($updated !== 1) {
        list($_, $fresh) = wps_state();
        wps_error('conflict', 409, array('current' => wps_public_state($fresh)));
    }
    if (($input['fault'] ?? '') === 'delay') { usleep(700000); }
    if (($input['fault'] ?? '') === 'response_loss') { wps_error('outcome_unknown', 504); }
    wp_send_json_success(wps_public_state($next));
});
