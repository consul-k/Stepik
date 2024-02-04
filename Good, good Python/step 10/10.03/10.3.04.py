'''

Подвиг 5. Вводится таблица целых чисел, записанных через пробел. 
Необходимо перемешать столбцы этой таблицы, используя функции shuffle и zip и вывести результат на экран (также в виде таблицы).

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:

1 2 3 4
5 6 7 8
9 8 6 7

Sample Output:

4 1 3 2
8 5 7 6
7 9 6 8

'''

import sys
import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

lst_in = list(map(str.strip, sys.stdin.readlines()))

lst = list(zip(*map(str.split, lst_in)))

random.shuffle(lst)

for row in zip(*lst):
    print(*row)
