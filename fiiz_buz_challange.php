<?php

for($i = 1; $i <= 100; $i++){

	if (($i % 3 ==0) && ($i % 5==0)){echo "fizz_buz:mul 3 & 5	 <br>";}

	elseif($i % 3 ==0){echo "fiz_no:muliple off 3 <br>";}
	elseif($i % 5 ==0){echo "buz_no:muliple off 5 <br>";}

	else{echo $i."<br>";}



}

?>