<?php 
include('flag.php');
$req_method = $_SERVER['REQUEST_METHOD'];
if($req_method!='POST')
    die("打开方式不对噢，再试试吧");
if(!preg_match('/N1k0la/i',$_SERVER['HTTP_USER_AGENT']))
    die("你需要使用戴教授刚开发的N1k0la浏览器来访问"."<br/>"."什么？没有？"."<br/>"."那还不赶紧去下一个！");
if(!preg_match('/127\.0\.0\.1/i',$_SERVER['HTTP_X_FORWARDED_FOR']))
	die(" 必须从本地来噢~");

print("JGE9JF9HRVRbJzB4R2FtZTIwMjEnXTskYj0kX1BPU1RbJ1gxY1QzNG0nXTskZD0kX1BPU1RbJ1B1cGkxJ107JGM9J3dlbGNvbWUgdG8gdGhlIDB4R2FtZTIwMjEnO2lmKG1kNSgkYik9PW1kNSgkZCkmJiRhPT09JGMpe2VjaG8gJGZsYWc7fQ==");
$a=$_GET['0xGame2021'];
$b=$_POST['X1cT34m'];
$d=$_POST['Pupi1'];
$c='welcome to the 0xGame2021';
if(md5($b)==md5($d)&&$a===$c)
    echo $flag;
