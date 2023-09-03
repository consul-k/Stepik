'''

Симметричная матрица

Напишите программу проверки симметричности квадратной матрицы относительно побочной диагонали.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы.

Формат выходных данных
Программа должна вывести YES, если матрица симметрична, и слово NO в противном случае.
Тестовые данные 🟢

Sample Input 1:

3
0 3 10
4 9 3
7 4 0

Sample Output 1:

YES

Sample Input 2:

3
0 1 2
1 2 7
2 3 4

Sample Output 2:

NO

Sample Input 3:

2
1 2
3 4

Sample Output 3:

NO

Sample Input 4:

2
4 2
3 4

Sample Output 4:

YES

'''

matrix = [list(map(int, input().split())) for i in range(int(input()))]
matrix = list(reversed(matrix))
zipped_rows = zip(*matrix)
t_matrix = [list(row) for row in zipped_rows]

if t_matrix == matrix:
    print('YES')
else:
    print('NO')
