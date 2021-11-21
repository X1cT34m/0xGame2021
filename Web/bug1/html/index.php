<?php
error_reporting(0);
highlight_file(__FILE__);
if(empty($_POST['Poria']) || empty($_POST['Pupi1'] || empty($_POST['N1k0la']) )){
    die("my secret is very big, u bear it");
}

$secret_key = getenv("secret");

if(isset($_POST['N1k0la']))
    $secret_key = hash_hmac('sha256', $_POST['N1k0la'], $secret_key);

$payload = hash_hmac('sha256', $_POST['Pupi1'], $secret_key);

if($payload !== $_POST['Poria']){
    die("hahaha u can't find my secret, or maybe u don't need to find it");
}
if(empty($_POST['action'])){
    show_source(__FILE__);
}
else{
    $_POST['action']('',$_POST['Pupi1']);
}
