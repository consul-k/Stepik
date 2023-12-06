'''

Задана целочисленная квадратная матрица размером N x N. 
Необходимо обойти элементы этой матрицы снизу вверх справа налево и вывести элементы именно в таком порядке в виде таблицы. 

Программа принимает на вход натуральное число N – количество строк и столбцов матрицы. 
В каждой из последующих N строк записаны N целых чисел – элементы матрицы. 

Sample Input 1:

5
3 4 9 6 2
8 2 0 5 1
4 7 4 8 7
7 1 3 3 8
5 6 3 7 0

Sample Output 1:

0 8 7 1 2
7 3 8 5 6
3 3 4 0 9
6 1 7 2 4
5 7 4 8 3

Sample Input 2:

3
5 4 1
6 7 9
9 3 0

Sample Output 2:

0 9 1
3 7 4
9 6 5

Sample Input 3:

4
6 8 4 3
9 1 6 5
0 5 3 9 
5 3 4 7 

Sample Output 3:

7 9 5 3
4 3 6 4
3 5 1 8
5 0 9 6

'''

matrix = [input().split() for _ in range(int(input()))]
t_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        t_matrix[j][i] = matrix[i][j]
for i in t_matrix[::-1]:
    print(*reversed(i))
