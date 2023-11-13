'''

Программа принимает на вход одно натуральное число и выводит на экран минимальную и максимальную цифры данного числа в отдельных строчках

Sample Input 1:

480

Sample Output 1:

0
8

Sample Input 2:

123

Sample Output 2:

1
3

Sample Input 3:

99

Sample Output 3:

9
9

'''

n = int(input())
s = []
while n > 0:
    s.append(n%10)
    n//=10
print(min(s))
print(max(s))
