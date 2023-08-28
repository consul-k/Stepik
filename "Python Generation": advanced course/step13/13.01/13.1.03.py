'''

Дополните приведенный код, чтобы он вывел сумму наибольшей и наименьшей цифры Decimal числа.

Тестовые данные 🟢

Sample Input 1:

12.1244354689

Sample Output 1:

10

Sample Input 2:

0.1244354689

Sample Output 2:

9

'''

from decimal import *
num = Decimal(input())
num_tuple = num.as_tuple()

numbers = [n for n in num_tuple.digits]
if int(num) == 0:
    print(max(num_tuple.digits))
else:
    print(min(numbers)+max(numbers))
