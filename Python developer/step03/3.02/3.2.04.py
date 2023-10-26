'''

Попробуйте Decimal в деле! Вашей программе на вход подаются два числа с плавающей точкой a и b. Посчитайте для них формулу a+ba

​+b c точностью 60 знаков.

Sample Input 1:

0.1234567
0.2345678

Sample Output 1:

0.585931856215202524804768125339566833405267249656346739662007

Sample Input 2:

123.1234567
12.2345678

Sample Output 2:

23.3306687683582097440712331926237579283266849866240727886380

Sample Input 3:

1000.2
100.3

Sample Output 3:

131.925938721245888103055929826241434277666284422468123947553

Sample Input 4:

1.0
2.0

Sample Output 4:

3.0

'''

from decimal import Decimal, getcontext

getcontext().prec = 60

a,b = Decimal(input()), Decimal(input())
print(a.sqrt() + b)
