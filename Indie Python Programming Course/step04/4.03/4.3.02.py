'''

Программа принимает на вход одно натуральное число и выводит на экран сумму цифр данного числа

Sample Input 1:

123

Sample Output 1:

6

Sample Input 2:

891101

Sample Output 2:

20

'''

n = int(input())
s = 0
while n > 0:
    s+=n%10
    n//=10
print(s)
