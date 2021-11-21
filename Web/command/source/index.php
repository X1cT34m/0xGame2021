<html>
<head>
    <title>
        Ai Ping wins
    </title>
    <style type="text/css">
        body{
            background: cornflowerblue;
        }
    </style>
</head>
<body>
<form action="index.php" method="post">
    <input type="text" name="host">
    <input type="submit" value="Ping" disabled="disabled">
</form>
</body>
</html>
<?php
if(isset($_POST['host'])){
    system('ping '.$_POST['host']);
}
?>