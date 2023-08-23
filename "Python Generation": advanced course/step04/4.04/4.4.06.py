'''

Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.

Примечание. Элементы диагоналей также учитываются.
Тестовые данные 🟢

Sample Input 1:

3
1 4 5
6 7 8
1 1 6

Sample Output 1:

8

Sample Input 2:

4
0 1 4 6
0 0 2 5
0 0 0 7
0 0 0 0

Sample Output 2:

7

Sample Input 3:

2
6 0
7 9

Sample Output 3:

9

'''

matrix = [list(map(int, input().split())) for i in range(int(input()))]
first = []
second = []

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i >= j and i <= len(matrix) - 1 - j:
            first.append(matrix[i][j])
        if i <= j and i >= len(matrix) - 1 - j:
            second.append(matrix[i][j])

first.extend(second)
print(max(first))
