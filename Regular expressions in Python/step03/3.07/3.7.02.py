'''

Нужно вывести все электронные почты, которые есть в тексте.
Что нужно сделать:

Нужно найти последовательности, подходящие по следующим условиям:

    Начинается как минимум с одного из следующих символов: a-z, A-Z, 0-9, -, _
    Потом идёт @
    После @ снова идёт как минимум один из следующих символов: a-z, A-Z, 0-9
    Потом идёт .
    После . снова идёт как минимум один из следующих символов: a-z, A-Z, 0-9

Адрес почты не может быть подпоследовательностью.
Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Ваша задача вывести все адреса почт в тексте.

Sample Input 1:

test mihryutkamihryutka1@gmail.com serginio1963@gmail.com velesgod111@gmail.com ofice_plus@mail.ru borisbaranob46@gmail.com bradley@automatedmarine.com fddsfwfwefwdfwd@mail.ru

Sample Output 1:

mihryutkamihryutka1@gmail.com
serginio1963@gmail.com
velesgod111@gmail.com
ofice_plus@mail.ru
borisbaranob46@gmail.com
bradley@automatedmarine.com
fddsfwfwefwdfwd@mail.ru

Sample Input 2:

Dfashu9dasdia spam@example.com shbid@asid nbasdasoidnoasndopjasnodnwaseondfsnhf.dwas@dhnifh.nsdaifjaspdijfsadjfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasdiashbidasid nbasdasoidnoasndopjasnodnwaseondf isnhfdwasdhnifhnsdaifjaspdijfsadjf buildup@eaglemoss.ru .oasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasdiashbidasid nbasdasoidnoasndopjasnodnwaseondf isnhfdwasdhnifhnsdaifjaspdijfsadjfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasdiashbidasid nbasdasoidnoasndopjasnodnwaseondf isnhfdwasdhnifhnsdaif @@@@@.@@ jasp....@@@...dijfsadjfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasdiashbidasid n@w.@a edutrack@ijmo.ru seondf isnhfdwasdhnifhnsdaifjaspdijfsadjfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasdiashbidasid nbasdasoidnoasndopjasnodnwaseondf isnhfdwasdhnifhnsdaifjaspdijfsadjfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasdiashbidasid nbasdasoidnoasndopjasnodnwaseondf isnhfdwasdhnifhnsdaifjaspdijfsadjfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasdiashbidasid nbasdasoidnoasndopjasnodnwaseondf isnhfdwasdhnifhnsdaifjaspdijfsad ab687848@gmail.com jfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasdiashbidasid nbasdasoidnoasndopjasnodnwaseondf isnhfdwasdhnifhnsdaifjaspdijfsadjfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasdiashbidasid nbasdasoidnoasndopjasnodn vopros@prosv.ru waseondf isnhfdwasdhnifhnsdaifjaspdijfsadjfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasdiashbidasid nbas spe-elif@mail.ru dasoidnoasndopjasnodnwaseondf isnhfdwasdhnifhnsdaifjaspdijfsadjfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasd@iashbi@dasid nbasdasoi.@.dnoa@.@sndopjasnodnwaseondf isnhfdwasdhnifhnsdaifjaspdijfsadjfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasdiashbidasid nbasdasoidnoasndopjasnodn mosobleirc@clubonus.ru waseondf isnhfdwasdhnifhnsdaifjaspdijfsadjfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmi

Sample Output 2:

spam@example.com
buildup@eaglemoss.ru
edutrack@ijmo.ru
ab687848@gmail.com
vopros@prosv.ru
spe-elif@mail.ru
mosobleirc@clubonus.ru

'''

import re

result = re.findall(r'\b[a-zA-Z0-9-_]+@[a-zA-Z0-9-_]+\.[a-zA-Z0-9-_]{1,3}\b', input())
for i in result:
    print(i)
