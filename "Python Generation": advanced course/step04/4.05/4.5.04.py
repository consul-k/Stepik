'''

Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести YES, если матрица симметрична относительно главной диагонали, и слово NO в противном случае.
Тестовые данные 🟢

Sample Input 1:

3
0 1 2
1 2 3
2 3 4

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

'''

matrix = [list(map(int, input().split())) for i in range(int(input()))]
zipped_rows = zip(*matrix)
t_matrix = [list(row) for row in zipped_rows]


if t_matrix == matrix:
    print('YES')
else:
    print('NO')
