<?php
error_reporting(0);
class Modifier {
    protected  $var;
    public function append($value){
        show_source($value);
    }
    public function __get($key){
        $this->append($this->var);
    }
}

class Show{
    public $source;
    public $str;
    public function __construct($file='look_me.php'){
        $this->source = $file;
        echo 'Welcome to '.$this->source."<br>";
    }
    public function __toString(){
        $function = $this->str;
        return $function();
    }

    public function __wakeup(){
        if(preg_match("/gopher|http|file|ftp|https|dict|\.\./i", $this->source)) {
            echo "hacker";
            $this->source = "look_me.php";
        }
    }
}

class Test{
    public $p;
    public $q;
    public function __construct(){
        $this->p = array();
    }

    public function __invoke(){
        $this->q->p;
    }
}

if(file_exists($_GET['filename'])){
    echo "emmmmmmm u find it!";     //flag is in flag.php
}
else{
    new Show();
    highlight_file(__FILE__);
}
