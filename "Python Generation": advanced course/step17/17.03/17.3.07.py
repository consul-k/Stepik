'''

Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами, другой с фамилиями.

Напишите программу, которая c помощью модуля random создает 3 случайные пары имя + фамилия, а затем выводит их, каждую на отдельной строке.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести текст в формате, приведенном в примере.

Примечание 1. Если бы файлы first_names.txt и last_names.txt содержали строки:

Aaron
Abdul
Abe
Abel
Abraham
Albert

и

Abramson
Adamson
Adderiy
Addington
Adrian
Albertson
Einstein

то результатом могло быть:

Abdul Albertson
Abel Adamson
Albert Einstein

'''

import random

with open('first_names.txt') as names, open('last_names.txt') as surnames:
    name = [line.strip() for line in names.readlines()]
    surname = [line.strip() for line in surnames.readlines()]
    for _ in range(3):
        print(random.choice(name), random.choice(surname))
