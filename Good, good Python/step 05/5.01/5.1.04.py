'''

Подвиг 5. На каждой итерации цикла пользователь вводит целое число. Цикл продолжается, пока не встретится число 0. 
Необходимо вычислить сумму введенных в цикле чисел и вывести результат на экран. Программу реализовать при помощи цикла while.

Sample Input:

8
11
2
-4
0

Sample Output:

17

'''

s = 0
n = int(input())

while n != 0:
    s+=n
    n = int(input())

print(s)
