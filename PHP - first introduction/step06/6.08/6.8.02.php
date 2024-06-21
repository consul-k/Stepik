<?php
for ($x = 1; $x <= 10; $x++) {
  if ($x % 2 != 0) {
    continue;
  }
  echo $x."\n";
}
