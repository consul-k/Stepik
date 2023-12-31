'''

В архитектуре компьютера важную роль играют числа, являющиеся степенями двойки: 1, 2, 4, 8 и так далее. 
Напишите программу, которая проверяет, является ли введённое натуральное число степенью двойки. 
Если да, то выводится сама эта степень; если нет, выводится «НЕТ»

Разбор Youtube Patreon Boosty

Sample Input 1:

8

Sample Output 1:

3

Sample Input 2:

9

Sample Output 2:

НЕТ

'''

n = int(input())

st = 0
while n%2 == 0:
    st += 1
    n //= 2
if n == 1:
    print(st)
else:
    print('НЕТ')
