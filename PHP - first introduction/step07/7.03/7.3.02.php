function win_or_lose($a)
{
    if ($a == 3) {
        return "Победа";
    } elseif ($a == 0) {
        return "Поражение";
    } elseif ($a == 1) {
        return "Ничья";
    } else {
        return "Странное число";
    }
}
