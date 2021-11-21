<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="UTF-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge"> 
<meta name="viewport" content="width=device-width, initial-scale=1"> 
<title>login</title>
<link rel="stylesheet" type="text/css" href="css/normalize.css" />
<link rel="stylesheet" type="text/css" href="css/demo.css" />
<!--必要样式-->
<link rel="stylesheet" type="text/css" href="css/component.css" />
<!--[if IE]>
<script src="js/html5.js"></script>
<![endif]-->
</head>
<body>
		<div class="container demo-1">
			<div class="content">
				<div id="large-header" class="large-header">
					<canvas id="demo-canvas"></canvas>
					<div class="logo_box">
						<h3>Administrator</h3>
						<h3 style='text-align:center'>神圣的后台</h3>
						<h3 style='text-align:center'>登陆就给flag</h3>
						<h5 style='text-align:center'>听说密码是个4位纯数字</h5>
						
						
						
						
						<form action="" name="f" method="post">
							<div class="input_outer">
								<span class="u_user"></span>
								<input name="logname" class="text" style="color: #FFFFFF !important" type="text" placeholder="username">
							</div>
							<div class="input_outer">
								<span class="us_uer"></span>
								<input name="logpass" class="text" style="color: #FFFFFF !important; position:absolute; z-index:100;"value="" type="password" placeholder="password">
								
							</div>
							<div class="mb2"><input class="act-but submit" type="submit" value="登录" style="color: #FFFFFF"></div>
						</form>
						<div id="php">
						<?php
                          $flag ='0xGame{y0u_brut3_f0rc3_successfully}';
                          $a=$_POST['logname'];
                          $b=$_POST['logpass'];
                          #echo "<h1>asfjalsd</h1>";
							if($a==='admin' && $b==='0310'){echo "<h1>$flag</h1>";}
                          	else{print("error username or password!");}
                          ?>
                      	</div>
					</div>
				</div>
			</div>
		</div><!-- /container -->
		<script src="js/TweenLite.min.js"></script>
		<script src="js/EasePack.min.js"></script>
		<script src="js/rAF.js"></script>
		<script src="js/demo-1.js"></script>
		<script src="js/anime.js"></script>
		<script src="js/jquery.js"></script>
		
		<script src="js/main.js"></script>
		
	</body>
</html>
