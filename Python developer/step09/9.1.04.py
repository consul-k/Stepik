'''

Определите количество дней между двумя годами. Вам на вход поступает два числа – первый год и второй. Нужно определить количество дней между ними.

В качестве ответа выведите количество дней между годами.

Sample Input 1:

2024
2020

Sample Output 1:

1461

Sample Input 2:

2020
2024

Sample Output 2:

1461

Sample Input 3:

2020
2021

Sample Output 3:

366

Sample Input 4:

2000
1965

Sample Output 4:

12783

Sample Input 5:

1950
2023

Sample Output 5:

26663

'''

from datetime import date

d1 = date(year = int(input()), month=1, day=1)
d2 = date(year = int(input()), month=1, day=1)

delta = abs(d2 - d1)
print(delta.days)
