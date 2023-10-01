'''

Напишите программу, которая будет искать первое слово в начале текста.
Что нужно сделать:

 Нужно найти первое слово в начале строки:

    Состоит как минимум из одной буквы
    Используются буквы латинского  алфавита обоих регистров

Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Если строка начинается с слова, то нужно вывести: Первое слово в предложении: word, где word - найденное слово.

Sample Input 1:

My car is the fastest!

Sample Output 1:

Первое слово в предложении: My

Sample Input 2:

123456

Sample Output 2:

Sample Input 3:

Choose between these two.

Sample Output 3:

Первое слово в предложении: Choose

'''

import re

result = re.match(r'[a-zA-Z]+', input())
if result:
    print('Первое слово в предложении:',result[0])
