'''

Напишите программу, которая найдёт первый хештег в тексте и выведет его в консоль.
Что нужно сделать:

 Нужно найти первый хештег в тексте:

    Начинается с символа #
    После # стоит последовательность из латинских букв нижнего регистра

Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Выведите в консоль первый найденный хештег. Если его нет - ничего выводить не нужно.

Sample Input 1:

#traveler #traveller #traveltheworld #travelblog #traveladdict #mytravelgram #travels #travelphoto #traveldiaries #travellife #travelawesome #travelpics #natgeotravel #travelholic #travelbug #travelstoke #traveldeeper #travelgirl #luxurytravel #worldtraveler #travelers #solotravel #travelpic #travelmore #travellingthroughtheworld #traveldiary #ilovetravel

Sample Output 1:

#traveler

Sample Input 2:

Some #hashtags for you

Sample Output 2:

#hashtags

Sample Input 3:

There are no hashtags :(

Sample Output 3:

'''

import re

result = re.search(r'#[a-z]+', input())
if result:
    print(result[0])
