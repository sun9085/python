<?php

function union($a,$b){


	$merge= array_merge($a,$b);

	echo "<pre>";
	print_r($merge);

	$unikarray =array_unique($merge);
	echo "<pre>";
	print_r($unikarray);
}

$a = array("red","green","black");
$b = array("red","yellow","white","green","pink");


 union($a,$b); 








?>