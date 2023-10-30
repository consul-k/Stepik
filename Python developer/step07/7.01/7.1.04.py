'''

На вход вашей программе поступает список целых чисел через пробел.

Отсортируйте массив так, чтобы все нули в нем оказались в конце массива, сохранив при этом порядок чисел.

Ввод:

Список целых чисел через пробел

Вывод:

Список чисел в котором нули находятся в конце.

Sample Input 1:

10 0 3 0 4 0 0 5 6 7 8

Sample Output 1:

10 3 4 5 6 7 8 0 0 0 0

Sample Input 2:

0 0 0

Sample Output 2:

0 0 0

Sample Input 3:

0

Sample Output 3:

0

Sample Input 4:

2

Sample Output 4:

2

Sample Input 5:

0 1

Sample Output 5:

1 0

Sample Input 6:

2 0 1

Sample Output 6:

2 1 0

'''

n = [int(i) for i in input().split()]
m = []
for i in n:
    if i != 0:
        m.append(i)
for i in n:
    if i == 0:
        m.append(i)
print(*m)
