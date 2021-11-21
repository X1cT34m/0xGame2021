<div class="light"><span class="glow">
			<form enctype="multipart/form-data" method="post">
				爷又摊牌了，爷就是懒，爷直接偷了 Pupi1 的题目<br/>嘿伙计，传个火？！
                <input class="input_file" type="file" name="upload_file"/>
                <input class="button" type="submit" name="submit" value="upload"/>
            </form>
      </span><span class="flare"></span><div>
	  <!--look_me.php-->
<?php
	error_reporting(0);
	//设置上传目录
	define("UPLOAD_PATH", "./uplo4d");
	$msg = "Upload Success!";
	if (isset($_POST['submit'])) {
        $temp_file = $_FILES['upload_file']['tmp_name'];
        $file_name = $_FILES['upload_file']['name'];
        $ext = pathinfo($file_name,PATHINFO_EXTENSION);
      if(!(preg_match("/jpg/i", strtolower($ext)))){
        die("不是好康的jpg我不要！");
    }
        $new_file_name = md5($file_name).".".$ext;
        $img_path = UPLOAD_PATH . '/' . $new_file_name;


        if (move_uploaded_file($temp_file, $img_path)){
            $is_upload = true;
        } else {
            $msg = 'Upload Failed!';
        }
        echo '<div style="color:#F00">'.$msg." Look here~ ".$img_path."</div>";
    }


?>