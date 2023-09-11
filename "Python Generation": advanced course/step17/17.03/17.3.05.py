'''

Вам доступен текстовый файл nums.txt. В файле могут быть записаны целые неотрицательные числа и все, что угодно. 
Числом назовем последовательность одной и более цифр, идущих подряд (число всегда неотрицательно).

Напишите программу, которая вычисляет сумму всех чисел, записанных в файле.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести сумму всех чисел, записанных в файле.

Примечание 1. Если бы файл nums.txt содержал строки:

 123   jhjk
bhjip456qwerty
1x2y3 4 5 6
sfsd 0 dfgfd
10abc20de30pop5 5 5 5

то результатом было бы:

680

'''

with open('nums.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    total = 0
    for line in lines:
        s = ''
        for i in line:
            if i.isdigit():
                s+=i
            else:
                s+=' '
        numbers = [int(i) for i in s.split()]
        total+= sum(numbers)
    print(total)
