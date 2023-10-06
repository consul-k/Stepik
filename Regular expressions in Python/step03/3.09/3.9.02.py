'''

Уберите все html теги и выведите оставшийся текст.
Что нужно сделать:

Нужно удалить все теги в html-разметке:

    Начинается с <
    Потом идёт последовательность любых символов любой длины
    Заканчивается с >

Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Текст, полученный из html-разметки.

Sample Input 1:

<html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Timer ⏲</title><link rel="icon" href="./img/goes.png"><link rel="stylesheet" href="./css/normalize.css"><link rel="stylesheet" href="./css/style.css"></head><body><div class="time_wrapper"><h1 class="bold minutes">1:00:00</h1><img class="time" src="./img/start_end.png"></div><div class="buttons"><button class="buttons_button regular start" onclick="start()">Start</button><button class="buttons_button regular notshow pause" onclick="pause()">Pause</button></div></body>

Sample Output 1:

Timer ⏲1:00:00StartPause

Sample Input 2:

<span>Привет!</span>

Sample Output 2:

Привет!

'''

import re

result = re.sub(r'<.*?>', '', input())
print(result)
