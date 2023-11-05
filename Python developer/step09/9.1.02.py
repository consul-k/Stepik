'''

Вашей программе на вход идут два числа – первый и второй год. Посчитайте количество високосных годов между ними включительно.

Sample Input 1:

2020
2028

Sample Output 1:

3

Sample Input 2:

2020
2020

Sample Output 2:

1

Sample Input 3:

2020
2023

Sample Output 3:

1

Sample Input 4:

2020
2024

Sample Output 4:

2

Sample Input 5:

2019
2024

Sample Output 5:

2

'''

import calendar

year1, year2 = int(input()), int(input())
print(calendar.leapdays(year1, year2+1))
