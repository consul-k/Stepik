'''

Программа принимает на вход одно натуральное число и выводит на экран произведение цифр данного числа

Sample Input 1:

415

Sample Output 1:

20

Sample Input 2:

102

Sample Output 2:

0

'''

n = int(input())
s = 1
while n > 0:
    s*=n%10
    n//=10
print(s)
