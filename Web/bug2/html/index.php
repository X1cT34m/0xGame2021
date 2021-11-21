<?php
error_reporting(0);
echo "爷累了，爷就是不想写前端"."<br/>";
echo "嗯？？？我代码中怎么有 eval('echo '.'Welcome '.\$str.';')"."<br/>";
echo "算了不管了，试着POST一个 N1k0la 吧"."<br/>";
if(isset($_POST['N1k0la'])){
    $str = $_POST['N1k0la'];
    $blacklist = ['file','system','exec','popen',' ', '\t', '\r', '\n','\'', '"', '`', '\[', '\]','\$','\\','\^','passthru','shell_exe','\`','popen','pcntl'];
    foreach ($blacklist as $blackitem) {
        if (preg_match('/' . $blackitem . '/m', $str)) {
            die("why do u have {".$blackitem."}<br/>"."en? u want to hacker 0xGame?");
        }
    }
    eval('echo ' . 'Welcome' . $str . ';');
}
?>
