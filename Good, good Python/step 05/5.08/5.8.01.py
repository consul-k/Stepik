'''

Подвиг 1. Вводятся вещественные числа в строку через пробел. Н
еобходимо на их основе сформировать список lst с помощью list comprehension (генератора списков) из модулей введенных чисел 
(в списке должны храниться именно числа, а не строки). Результат вывести на экран в виде списка командой:

print(lst)

Sample Input:

5.56 -8.7 1.0 3.14 77.845

Sample Output:

[5.56, 8.7, 1.0, 3.14, 77.845]

'''

lst = [abs(float(s)) for s in input().split()]
print(lst)
