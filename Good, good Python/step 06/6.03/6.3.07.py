'''

Подвиг 9. Имеется двумерный кортеж, размером 5 x 5 элементов:

t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))

Вводится натуральное число N (N < 5). Необходимо на основе кортежа t сформировать новый аналогичный кортеж t2 размером N x N элементов. 
Результат вывести на экран в виде таблицы чисел.

Sample Input:

3

Sample Output:

1 0 0
0 1 0
0 0 1

'''

# put your python code here
t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))
t2 = []
n = int(input())
for i in range(n):
    s = []
    for j in range(n):
        s.append(t[i][j])
    t2.append(tuple(s))
t2 = tuple(t2)
for i in t2:
    print(*i)
