<?php
  // Vars
  define('COMMAND', '/home/pi/Documents/examples/scripts/relay_test.py');

  // Init
  ini_set('display_errors', 1);
  error_reporting(E_ALL);

  // Check if command is running and create lock file otherwise
  if (file_exists(COMMAND . '.lock')) die ('Command already running.');
  fopen(COMMAND . '.lock', "w");

  // Execute python script
  $output = array();
  exec('sudo python3 '. COMMAND .' 2>&1', $output);

  // Remove lock file and output result
  unlink(COMMAND . '.lock');
  die($output[0]);
?>
