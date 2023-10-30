'''

На вход вашей программе поступает список целых чисел через пробел.

Найдите медиану этого списка. (медиана это значение по центру в отсортированном списке, причем если длина четная то возьмите среднее арифметическое двух значений)

В случае если ответом является дробное число – округлите его до одного знака после запятой. Если ответ – целое число, выведите его без дробной части.

Ввод:

Список целых чисел через пробел

Вывод:

res – медиана списка

Sample Input 1:

6 2 3

Sample Output 1:

3

Sample Input 2:

1 2 3 4

Sample Output 2:

2.5

Sample Input 3:

0 0 0

Sample Output 3:

0

Sample Input 4:

1 1 1

Sample Output 4:

1

Sample Input 5:

1 10 1000

Sample Output 5:

10

Sample Input 6:

1 10 20 30

Sample Output 6:

15

Sample Input 7:

1 2 5 4

Sample Output 7:

3

Sample Input 8:

1 1 1 30

Sample Output 8:

1

Sample Input 9:

7 5 2 1

Sample Output 9:

3.5

'''

import statistics

n = [int(i) for i in input().split()]
res = statistics.median(n)
if int(str(res).split('.')[-1]) == 0:
    print(int(res))
else:
    print(round(res,1))
