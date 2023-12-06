'''

Задана целочисленная квадратная матрица размером N x N. 
Необходимо обойти элементы этой матрицы сверху вниз слева направо и вывести элементы именно в таком порядке в виде таблицы. 

Программа принимает на вход натуральное число N – количество строк и столбцов матрицы. 
В каждой из последующих N строк записаны N целых чисел – элементы матрицы. Все числа во входных данных не превышают 100 по абсолютной величине.

Sample Input 1:

5
3 4 9 1 2
8 2 0 5 1
4 7 4 8 7
7 1 3 3 8
5 6 3 7 0

Sample Output 1:

3 8 4 7 5
4 2 7 1 6
9 0 4 3 3
1 5 8 3 7
2 1 7 8 0

Sample Input 2:

2
6 7
9 0

Sample Output 2:

6 9
7 0

'''

matrix = [input().split() for _ in range(int(input()))]
t_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        t_matrix[j][i] = matrix[i][j]
for i in t_matrix:
    print(*i)
