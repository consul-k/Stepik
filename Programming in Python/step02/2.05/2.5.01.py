'''

Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.

Используйте метод split строки. ﻿﻿

Sample Input:

4 -1 9 3

Sample Output:

15

'''

a = [int(i) for i in input().split()]
numsum = sum(list(a))
print(numsum)
