'''

Подвиг 6. Допишите программу для нахождения числа сочетаний из n по k (значения вводятся в программе), используя формулу ., где . 
Выведите результат в консоль в виде целого числа с помощью функции print.

Для вычисления факториалов воспользуйтесь соответствующей функцией из библиотеки math.

Sample Input:

6 3

Sample Output:

20

'''

import math
n, k = map(int, input().split())

factorial_n = math.factorial(n)
factorial_k = math.factorial(k)
factorial_n_minus_k = math.factorial(n - k)

combinations = factorial_n // (factorial_k * factorial_n_minus_k)
print(combinations)
