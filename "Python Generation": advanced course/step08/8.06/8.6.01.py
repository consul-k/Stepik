'''

На вход программе подаются две строки текста, содержащие числа. 
Напишите программу, которая определяет количество чисел, которые есть как в первой строке, так и во второй.

Формат входных данных
На вход программе подаются две строки текста, содержащие числа, отделенные символом пробела.

Формат выходных данных
Программа должна вывести количество чисел, содержащихся одновременно как в первой строке, так и во второй.
Тестовые данные 🟢

Sample Input 1:

1 3 2
4 3 2

Sample Output 1:

2

Sample Input 2:

1 2 6 4 5 7
10 2 3 4 8

Sample Output 2:

2

Sample Input 3:

1 7 3 8 10 2 5
6 5 2 8 4 3 7

Sample Output 3:

5

'''

s1 = set([int(s) for s in input().split()])
s2 = set([int(s) for s in input().split()])

print(len(s1.intersection(s2)))
