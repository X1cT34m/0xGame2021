<?php
if('127.0.0.1'!=$_SERVER['REMOTE_ADDR']){
	die('Allow local only');
}
if('GET' === $_SERVER['REQUEST_METHOD']){
  highlight_file(__FILE__);
  die('Invalid request mode');
}

$filename=$_POST['filename'];
if(preg_match('/..\//',$filename)){
	die('nonono');
}
echo file_get_contents(urldecode($filename));