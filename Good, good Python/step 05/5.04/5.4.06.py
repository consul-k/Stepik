'''

Подвиг 6. Вводится список в виде вещественных чисел в одну строку через пробел. 
С помощью цикла for необходимо найти наименьшее значение в этом списке. Полученный результат вывести на экран.  
Реализовать программу без использования функции min, max и сортировки.

Sample Input:

8.6 9.11 -4.567 -10.0 1.45

Sample Output:

-10.0

'''

a = list(map(float, input().split()))
m = 0
m = a[0]
for i, v in enumerate(a):
    if v < m:
        m = v
print(m)
