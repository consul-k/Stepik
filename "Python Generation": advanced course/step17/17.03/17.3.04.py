'''

Вам доступен текстовый файл numbers.txt, каждая строка которого может содержать одно или несколько целых чисел, разделенных одним или несколькими пробелами.

Напишите программу, которая вычисляет сумму чисел в каждой строке и выводит эту сумму на экран (для каждой строки выводится сумма чисел в этой строке).

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести сумму чисел в каждой строке.

Примечание 1. Если бы файл numbers.txt содержал строки:

2 1
     3    4
 1       7

то результатом было бы:

3
7
8

'''

with open('numbers.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        numbers = [int(i) for i in line.split()]
        print(sum(numbers))
