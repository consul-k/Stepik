'''

Подвиг 3. Вводится  матрица чисел из трех строк. В каждой строке числа разделяются пробелом. 
Необходимо вывести на экран последний столбец этой матрицы в виде строки из трех чисел через пробел.

Sample Input:

8 11 12 1
9 4 36 -4
1 12 49 5

Sample Output:

1 -4 5

'''

lst = []
for i in range(3):
    i = list(map(int, input().split()))
    lst.append(i)
lst1 = [i[-1] for i in lst]    
print(*lst1)
