<?php

require_once('library.php');

$number = $argv[1];
$factorial = factorial($number);

echo sprintf('%d! = %d', $number, $factorial);