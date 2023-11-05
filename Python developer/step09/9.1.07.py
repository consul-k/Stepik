'''

На вход вашей программе поступают строка с датой, временем и часовым поясом в формате ISO 8601. 
Переведите время в часовой пояс UTC-03:46 и "Europe/Moscow" и выведите каждое время в новой строке.

Sample Input 1:

2022-01-01T03:44:56+04:40

Sample Output 1:

2021-12-31T19:18:56-03:46
2022-01-01T02:04:56+03:00

Sample Input 2:

2022-01-01T05:33:56+00:00

Sample Output 2:

2022-01-01T01:47:56-03:46
2022-01-01T08:33:56+03:00

Sample Input 3:

2022-04-05T23:33:56+03:00

Sample Output 3:

2022-04-05T16:47:56-03:46
2022-04-05T23:33:56+03:00

Sample Input 4:

2022-04-05T23:33:56-03:46

Sample Output 4:

2022-04-05T23:33:56-03:46
2022-04-06T06:19:56+03:00

'''

from datetime import datetime, time, timezone, timedelta
from zoneinfo import ZoneInfo

date = datetime.fromisoformat(input())
tz = timezone(offset=timedelta(hours=-3, minutes=-46))
moskow_tz = ZoneInfo("Europe/Moscow")

utc = date.astimezone(tz)
moscow = date.astimezone(moskow_tz)
print(datetime.isoformat(utc))
print(datetime.isoformat(moscow))
