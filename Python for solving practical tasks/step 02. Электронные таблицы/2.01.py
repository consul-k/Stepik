'''

Вася планирует карьеру и переезд. Для это составил таблицу, в которой для каждого региона записал зарплаты для разных интересные ему профессий. 
Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245267/salaries.xlsx. 
Выведите название региона с самой высокой медианной зарплатой (медианой называется элемент, стоящий в середине массива после его упорядочивания) и, 
через пробел, название профессии с самой высокой средней зарплатой по всем регионам. 

'''

import openpyxl
import statistics

book = openpyxl.open('salaries.xlsx', read_only=True)
sheet = book.active

city = {}
profession = {}

#города
for i in range(2,10):
    data = []
    for j in range(1,8):
        data.append(sheet[i][j].value)
    city[sheet[i][0].value] = statistics.median(data)
    
city_data_comp = []
for data in city.values():
    city_data_comp.append(data)

for key, value in city.items():
    if value == max(city_data_comp):
        print(key)

#профессии
for i in range(1,8):
    data = []
    for j in range(2,10):
        data.append(sheet[j][i].value)
    profession[sheet[1][i].value] = statistics.mean(data)
    
profession_data_comp = []
for data in profession.values():
    profession_data_comp.append(data)

for key, value in profession.items():
    if value == max(profession_data_comp):
        print(key)
