<?php
// put your PHP code here
    $a = readline();
    $b = readline();
    for (; $a <= $b;) {
        if ($a % 2 == 0) {
            echo $a." ";
        }
        $a++;
    }
?>
