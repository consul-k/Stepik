'''

Подвиг 4. Вводятся оценки студента в одну строчку через пробел. 
Необходимо определить, имеется ли в этом списке хотя бы одна оценка ниже тройки.
Если это так, то вывести на экран строку "отчислен", иначе - "учится".

Задачу реализовать с использованием одной из функций: any или all.

Sample Input:

3 3 3 2 3 3

Sample Output:

отчислен

'''

lst = list(map(int, input().split()))
res = all(map(lambda x: x>=3, lst))
if res:
    print('учится')
else:
    print('отчислен')
