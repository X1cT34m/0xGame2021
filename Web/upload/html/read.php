<?php
error_reporting(0);
$a=$_GET["filename"];
if(preg_match('/flag/i',$a)){
  exit("nononono");
}
include($a);

?>
