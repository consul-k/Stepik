'''

Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно, составив справочник продуктов с указанием калорийности на 100 грамм, 
а также содержание белков, жиров и углеводов на 100 грамм продукта. 
Ему не удалось найти всю информацию, поэтому некоторые ячейки остались незаполненными (можно считать их значение равным нулю). 
Также он использовал какой-то странный офисный пакет и разделял целую и дробную часть чисел запятой. 
Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking3.xlsx

Вася составил раскладку по продуктам на весь поход (она на листе "Раскладка") с указанием номера дня, названия продукта и его количества в граммах. 
Для каждого дня посчитайте 4 числа: суммарную калорийность и граммы белков, жиров и углеводов. 
Числа округлите до целых вниз и введите через пробел. Информация о каждом дне должна выводиться в отдельной строке.

'''

import openpyxl
import math

book = openpyxl.open('trekking3.xlsx', read_only=True)
sheet = book.worksheets[0]

products = {}

all_days = {}
for i in range(1,10):
    all_days[i] = {'ККал': 0, 'Б': 0, 'Ж': 0, 'У': 0}

#продукты 
for j in range(2,39):
    data = []
    for i in range(1,5):
        if sheet[j][i].value is None:
            data.append(0)
        else:
            data.append(sheet[j][i].value)
    products[sheet[j][0].value] = data

#продукты на один день
sheet_2 = book.worksheets[1]

for j in range(2,101):
    products_one_day = {}
    data = sheet_2[j][2].value / 100
    if sheet_2[j][1].value in products_one_day:
        products_one_day[sheet_2[j][1].value] += data
    else:
        products_one_day[sheet_2[j][1].value] = data

#расчеты
    for key, value in products_one_day.items():
        all_days[sheet_2[j][0].value]['ККал'] += products[key][0] * value
        all_days[sheet_2[j][0].value]['Б'] += products[key][1] * value
        all_days[sheet_2[j][0].value]['Ж'] += products[key][2] * value
        all_days[sheet_2[j][0].value]['У'] += products[key][3] * value

for day in all_days.values():
    for value in day.values():
        print(math.floor(value), end=' ')
    print()
