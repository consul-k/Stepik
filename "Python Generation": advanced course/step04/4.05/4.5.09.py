'''

Магическим квадратом порядка nn называется квадратная таблица размера n×nn×n, составленная из всех чисел 1,2,3,…,n**2 (то есть все числа разные) так, 
что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. 
Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы: nn строк, по nn чисел в каждой, 
разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.
Тестовые данные 🟢

Sample Input 1:

3
8 1 6
3 5 7
4 9 2

Sample Output 1:

YES

Sample Input 2:

3
8 2 6
3 5 7
4 9 1

Sample Output 2:

NO

Sample Input 3:

3
4 9 2
3 5 7
8 1 6

Sample Output 3:

YES

'''

matrix = [list(map(int, input().split())) for i in range(int(input()))]

matrix_num = [int(i) for i in range(1,len(matrix)**2 + 1)]
matrix_check = []

for group in matrix:
    matrix_check.extend(group)

row = [sum(i) for i in matrix]
columns = [sum(col) for col in zip(*matrix)]

matrix_md = [] 
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == j:
            matrix_md.append(matrix[i][j])

matrix_sd = []
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if j == len(matrix) - i - 1:
            matrix_sd.append(matrix[i][j])
           
if sorted(matrix_check) == matrix_num and row == columns and sum(matrix_md) == sum(matrix_sd):
    print('YES')
else:
    print('NO')
