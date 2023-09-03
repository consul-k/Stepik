'''

Латинским квадратом порядка n называется квадратная матрица размером n×n, каждая строка и каждый столбец которой содержат все числа от 1 до n. 
Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы: n строк, по n чисел в каждой, 
разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является латинским квадратом, и слово NO, если не является.
Тестовые данные 🟢

Sample Input 1:

4
2 3 4 1
3 4 1 2
4 1 2 3
1 2 3 4

Sample Output 1:

YES

Sample Input 2:

3
1 2 3
3 2 1
2 3 4

Sample Output 2:

NO

'''

n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
test_list = [i for i in range(1,n+1)]

check = True

for i in range(n):
    if set(matrix[i]) != set(test_list):
        check = False
        
zipped_rows = zip(*matrix)
t_matrix = [list(row) for row in zipped_rows]

for i in range(n):
    if set(t_matrix[i]) != set(test_list):
        check = False

if check:
    print('YES')
else:
    print('NO')
