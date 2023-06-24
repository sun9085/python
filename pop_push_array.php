<?php


$student = array("sanju","tina","mina","lina");

echo "pre";
echo "<br>";
echo "before pop array <br>";
print_r($student);
echo "<br>";

// pop : remove last item in array
echo "after pop array <br>";
array_pop($student);
echo "pre";
print_r($student);
echo "<br>";

// push : add item in last array

echo "after push <br>";
array_push($student,"rajesh");
print_r($student);
echo "<br>";


// array_shift(array): remove first item in array

echo "after array_shift remove first item in array: <br>";
echo "pre <br>";
array_shift($student);
print_r($student);
echo "<br>";



// array_unshift(array):  add item in array last 

echo "pre <br>";
print_r($student);
array_unshift($student,"brijesh");
print_r($student);
echo "pre <br>";
?>