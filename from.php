<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>from_dynamic_data</title>
</head>
<body>
	<form method="POST">

	enter your favorite color:<input type ="text" name="favorite_color">
	<input type="submit" name="submit" value="chekbox"

	</form>

	<p> 
		<?php

		if (isset($_POST['submit'])){
			$favorite_color = $_POST['favorite_color'];

		switch ($favorite_color) {
		case 'blue':echo "my favorite_color is blue";
							break;

		case "green": echo "my favorite_color is green";
							break;

		case "black":echo "my favorite_color is black";
							break;


		case "yellow":echo "my favorite_color is yellow";
							break;

		case "red" : echo "this is my favorite_color ";
							break;
							
		default : echo "defalut block run compulsary";	
									}







				}
	
		?>



	</p>


</body>
</html>