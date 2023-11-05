'''

Вам на вход поступает две даты в формате ISO 8601. Поменяйте в них местами годы если это возможно. Например на вход дано 2 даты:

2023-01-01
2020-12-12

В качестве ответа программа должна вернуть:

2020-01-01
2023-12-12

В случае если это сделать невозможно выведите:

Год изменить невозможно

Sample Input 1:

2023-01-01
2020-12-12

Sample Output 1:

2020-01-01
2023-12-12

Sample Input 2:

2020-02-29
2021-12-12

Sample Output 2:

Год изменить невозможно

Sample Input 3:

2021-01-01
2021-12-12

Sample Output 3:

2021-01-01
2021-12-12

Sample Input 4:

2020-02-29
2020-12-12

Sample Output 4:

2020-02-29
2020-12-12

Sample Input 5:

2020-02-29
2024-12-12

Sample Output 5:

2024-02-29
2020-12-12

Sample Input 6:

2020-02-28
2021-12-12

Sample Output 6:

2021-02-28
2020-12-12

'''

from datetime import date

d1 = date.fromisoformat(input())
d2 = date.fromisoformat(input())

try:
    year1, year2 = d1.year, d2.year
    d1 = d1.replace(year=year2)
    d2 = d2.replace(year=year1)
    print(d1,d2,sep='\n')
except ValueError:
    print("Год изменить невозможно")
