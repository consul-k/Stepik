'''

На вход вашей программы подается две строки t1t1​ и t2t2​ со временем в формате ISO 8601. 
Посчитайте, сколько времени прошло между t1t1​ и t2t2​. Время дается в разном порядке в рамках одного дня.

Sample Input 1:

12:00:00
15:00:00

Sample Output 1:

03:00:00

Sample Input 2:

10:00:00
15:00:00

Sample Output 2:

05:00:00

Sample Input 3:

23:59:59
12:39:39

Sample Output 3:

11:20:20

Sample Input 4:

23:09:29
12:39:39

Sample Output 4:

10:29:50

Sample Input 5:

23:03:03
23:59:02

Sample Output 5:

00:55:59

'''

from datetime import time,timedelta

t1 = time.fromisoformat(input())
t2 = time.fromisoformat(input())

delta = timedelta(hours=t2.hour, minutes=t2.minute, seconds=t2.second) - timedelta(hours=t1.hour, minutes=t1.minute, seconds=t1.second)

seconds = int(abs(delta).total_seconds())

print(time(hour=seconds // 3600, minute=seconds % 3600 // 60, second=seconds % 60).isoformat())
