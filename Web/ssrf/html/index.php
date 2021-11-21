<?php 
error_reporting(0);
highlight_file(__FILE__);
$url=$_GET['url'];
if(preg_match('/127.0.0.1|dict|file|ftp/',$url)){
  die('想都别想');
}//read.php
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_HEADER, 0);
$output = curl_exec($ch);
echo $output;
curl_close($ch);
