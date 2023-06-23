<?php

//user defined function:

function sunny(){echo "first userdefined function";}sunny();

echo"<br>";
echo "-----------------------<br>";


function xyz(){echo "this is second function:";}xyz(); 
echo"<br>";
echo "-----------------------<br>";

// parameter / arguments

		

				//parameter
function first($a,$b){                  

	$d = $a + $b;

	echo "addition a+b is : $d";
}first(2,4);//argument

echo"<br>";
echo "-----------------------<br>";


// echo " argument : at time user create function and set parameter lik a,b"
		
// 		parameter : at time function call passing value of a ,b 



// we can pass no times pargumnets at function

function dd1($h,$g)
{

		$v1 = $h + $g;

	echo "sum of h and g is: $v1 <br>";

}
dd1(1,2);
dd1(10,12);
dd1(12,12);
dd1(10,22);

echo"<br>";
echo "-----------------------<br>";


// default parameters
 
function rrr($a,$b=5,$c=3){   

	$result = $a + $b - $c;

	echo "result is :$result <br>";


}
rrr(1);
rrr(10);
echo"<br>";
echo "-----------------------<br>";

function yyy($a,$b,$c=2){   

	$result = $a + $b - $c;

	echo "result is :$result <br>";


}
yyy(10,3);
yyy(4,7);
?>