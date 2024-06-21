<?php
$arr = array("один", "два", "три", "четыре", "пять");
foreach ($arr as $num) {
    if ($num == "два" || $num == "четыре") {
        continue;   
    } echo $num."\n";
}
