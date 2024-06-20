<?php
    $a = readline();
    $b = readline();
    $c = readline();
    $d = readline();
    echo ((($a + $b + $c) * $d) - ((($a + $b + $c) * $d) % 10)) / 5;
