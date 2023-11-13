'''

Программа принимает на вход одно натуральное число и выводит его цифры в столбик в обратном порядке.

Sample Input 1:

412

Sample Output 1:

2
1
4

Sample Input 2:

8942

Sample Output 2:

2
4
9
8

'''

n = int(input())
while n > 0:
    print(n%10)
    n//=10
