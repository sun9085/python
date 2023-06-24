<?php 
//sort - asending order;
//rsort - desending order; 

$s = array("45,78,6,32,45,6");

sort($s);


echo "<ol>";
foreach ($s as $b){

	echo "<li> $b </li>";
}	
echo "</ol>"




?>