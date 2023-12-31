'''

На вход программе подаются два натуральных числа n и m, каждое на отдельной строке — количество строк и столбцов в матрице. 
Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы сначала первой строки, затем второй, и т.д.

Напишите программу, которая считывает элементы матрицы один за другим, выводит их в виде матрицы, выводит пустую строку, и снова ту же матрицу, 
но уже поменяв местами строки со столбцами: первая строка выводится как первый столбец, и так далее.

Формат входных данных
На вход программе подаются два числа nn и mm — количество строк и столбцов в матрице, далее идут n×mn×m слов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести считанную матрицу, за ней пустую строку, и ту же матрицу, но поменяв местами строки со столбцами. 
Элементы матрицы разделять одним пробелом.

Тестовые данные 🟢

Sample Input 1:

4
2
и
швец
и
жнец
и
на
дуде
игрец

Sample Output 1:

и швец
и жнец
и на
дуде игрец

и и и дуде
швец жнец на игрец

Sample Input 2:

2
3
не
в
бровь
а
в
глаз

Sample Output 2:

не в бровь
а в глаз

не а
в в
бровь глаз


'''

n = int(input())
m = int(input())
matrix = []

for i in range(n):
    p = []
    for j in range(m):
        p.append(input())
    matrix.append(p)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()

print()

matrix_c = list(zip(*matrix))
for i in matrix_c:
    for j in i:
        print(j, end= ' ')
    print()
