'''

Задача на программирование

Определите, сколько прошло времени между двумя моментами во времени.

На вход программе идут две строки в формате ISO 8601, содержащие дату и время. Определите сколько между ними секунд.

Sample Input 1:

2020-02-20T12:00:00
2023-01-02T20:01:33

Sample Output 1:

90489693

Sample Input 2:

2023-01-02T20:01:33
2020-02-20T12:00:00

Sample Output 2:

90489693

Sample Input 3:

2020-01-02T20:01:33
2020-02-20T12:00:00

Sample Output 3:

4204707

Sample Input 4:

2020-06-02T19:01:36
2010-12-20T14:05:03

Sample Output 4:

298270593

'''

from datetime import datetime

d1 = datetime.fromisoformat(input())
d2 = datetime.fromisoformat(input())

print(int(abs(d2-d1).total_seconds()))
