'''

Напишите программу, которая считывает переменные a, b, c и вычисляет формулу: a3+bcca3+b

На вход вашей программе идут 3 числа a, b, c типа float.

В качестве результата выведите ответ для формулы.

Sample Input:

20.01219512195122
40.02777777777778
87.1

Sample Output:

92.0892057678584

'''

import math
a, b, c = float(input()), float(input()), float(input())
print((a**3 + math.sqrt(b)) / c)
