'''

На вход вашей программе поступает список целых чисел через пробел.

Удалите из массива все элементы, значения которых являются нечетными.

Ввод:

Список целых чисел через пробел

Вывод:

Четные элементы массива

Sample Input 1:

1 2 3 4 5

Sample Output 1:

2 4

Sample Input 2:

0 0 0 0

Sample Output 2:

0 0 0 0

Sample Input 3:

1 1 1

Sample Output 3:

Sample Input 4:

0

Sample Output 4:

0

Sample Input 5:

1

Sample Output 5:

'''

n = [int(i) for i in input().split() if int(i)%2 == 0]
print(*n)
