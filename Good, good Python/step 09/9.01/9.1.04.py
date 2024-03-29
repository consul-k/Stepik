'''

Подвиг 6. Вводится целое положительное число a. Необходимо определить генератор, 
который бы возвращал модули чисел в диапазоне [-a; a], а затем еще один, который бы вычислял кубы чисел (возведение в степень 3), 
возвращаемых первым генератором.

Вывести в одну строчку через пробел первые четыре значения. (Полагается, что генератор выдает, как минимум четыре значения).

Sample Input:

3

Sample Output:

27 8 1 0

'''

# put your python code here
a = int(input())
first = (abs(x) for x in range(-a,a+1))
second = tuple(x**3 for x in first)
print(*second[:4])
