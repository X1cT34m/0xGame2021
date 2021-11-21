<?php
include("config.php");
$conn = mysqli_connect($dbhost, $dbuser, $dbpass);
if(!$conn)
    die("error");
if(isset($_POST['username']) && isset($_POST['password'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];
    $sql = "select * from test.0xgame_users where username = \"$username\" and password = \"$password\"";
    $result = mysqli_query($conn, $sql);
    if($result){
        die("0xGame{3a5y_w4n_n3ng_m1m4}");
    }else{
        die("Not this way, nothing in database");
    }
}
mysqli_close($conn);
