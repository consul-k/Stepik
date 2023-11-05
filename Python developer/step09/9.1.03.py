'''

Вам дано 2 даты: start_date и end_date, где start_date <= end_date. 
Посчитайте, сколько между этими датами дней (включая даты), причём если end_date переходит на следующий месяц или ещё дальше – посчитайте, 
сколько дней между start_date и последним днём её месяца.

Ввод:

start_date – начальная дата

end_date – конечная дата

Вывод:

Количество дней между датами, ограниченное максимальным количеством дней в месяце.

Sample Input 1:

2022-08-01
2022-08-14

Sample Output 1:

14

Sample Input 2:

2022-08-20
2022-09-05

Sample Output 2:

12

Sample Input 3:

2022-08-30
2022-09-05

Sample Output 3:

2

Sample Input 4:

2022-02-01
2022-02-28

Sample Output 4:

28

Sample Input 5:

2022-02-01
2022-09-28

Sample Output 5:

28

Sample Input 6:

2022-02-10
2022-02-28

Sample Output 6:

19

Sample Input 7:

2022-08-01
2023-08-01

Sample Output 7:

31

'''

from datetime import date
import calendar
d1, d2 = [date.fromisoformat(input()) for _ in range(2)]
d2 = min(d2, d1.replace(day=calendar.monthrange(d1.year, d1.month)[1]))
print((d2-d1).days + 1)
