'''

Даны два натуральных числа A и B. Требуется найти их наименьшее общее кратное (НОК).

Sample Input 1:

6 15

Sample Output 1:

30

Sample Input 2:

14 21

Sample Output 2:

42

'''

a, b = map(int, input().split())
a1 = a
b1 = b
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(int((a1*b1)/a))
