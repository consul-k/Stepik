'''

Напишите программу, которая будет проверять, может ли текст содержать в себе seed фразу или нет.
Что нужно сделать:

 Нужно проверить, может ли текст содержать seed-фразу:

    Seed-фраза - это последовательность из 12, 18 или 24 случайных слов
    В данном случае нужно проверять, что текст начинается как минимум с 12 слов
    Слова состоят из букв латинского алфавита нижнего регистра
    Между словами могут стоять только пробелы

Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Если строка походит по условиям, то нужно вывести: возможно, это seed-фраза.

Sample Input 1:

theme primary opinion edit dragon maid boil ankle link shield erupt melody

Sample Output 1:

возможно, это seed-фраза

Sample Input 2:

firm win pool ahead nut horse during music motion fatal unable near idle brisk prize toy gentle

Sample Output 2:

возможно, это seed-фраза

Sample Input 3:

We've got bigger problems to deal with.

Sample Output 3:

Sample Input 4:

neutral choice scout, rifle tube zone already auto cycle sing ring easily

Sample Output 4:

Sample Input 5:

neutral choice scout4 rifle tube zone already auto cycle sing ring easily

Sample Output 5:

'''

import re

result = re.match(r'(?:[^,\.\'\d][a-zA-Z ]){12}|(?:[^,\.\'\d][a-zA-Z ]){18}|(?:[^,\.\'\d][a-zA-Z ]){24}', input())
if result:
    print('возможно, это seed-фраза')
