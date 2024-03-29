'''

Подвиг 1. Вводится двумерный список в виде таблицы целых чисел (см. пример ниже). 
С помощью list comprehension преобразовать двумерный список в одномерный так, 
чтобы значения элементов шли в обратном порядке. Результат отобразить в виде строки из чисел, записанных через пробел.

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:

1 2 3 4
5 6 7 8
9 8 7 6
5 4 3 2

Sample Output:

2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1

'''

import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
a = [j for i in lst_in[::-1] for j in i[::-1]]
print(*a)
