<?php
add_action('admin_menu', function(){
  add_menu_page('Sync Pro','Sync Pro','administrator','sync-pro','sync_pro_page');
});
function sync_pro_page(){
  $connected = !empty(get_option('sync_api_key'));
  echo '<div class="wrap"><h1>Modules</h1>';
  echo $connected ? '<div class="notice notice-success"><p>Connected</p></div>' : '';
  echo '<input name="api_key" value="********">';
  echo '<button class="button">Save</button><button class="danger">Reset</button>';
  echo '<div id="spinner">Syncing...</div></div>';
}