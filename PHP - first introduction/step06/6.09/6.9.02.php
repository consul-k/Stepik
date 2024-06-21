<?php
    $month = readline();
    switch ($month) {
        case 'Декабрь':
        case 'Январь':
        case 'Февраль':
            echo 'Зима';
            break;
        case 'Март':
        case 'Апрель':
        case 'Май':
            echo 'Весна';
            break;
        case 'Июнь':
        case 'Июль':
        case 'Август':
            echo 'Лето';
            break;
        case 'Сентябрь':
        case 'Октябрь':
        case 'Ноябрь':
            echo 'Осень';
            break;
        default:
            echo 'Такого месяца нет';
    }
?>
