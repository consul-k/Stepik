'''

Подвиг 7. Вводятся целые числа в одну строчку через пробел (не менее четырех). 
еобходимо найти три наименьших числа в этой последовательности чисел и вывести их на экран в порядке возрастания. 
Реализовать программу без использования условного оператора.

Sample Input:

8 11 -5 10 -1 0 7

Sample Output:

-5 -1 0

'''

s = list(map(int, input().split()))
s = sorted(s)
print(*s[:3])
