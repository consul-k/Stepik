'''

Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно, составив справочник продуктов с указанием калорийности на 100 грамм, 
а также содержание белков, жиров и углеводов на 100 грамм продукта. Ему не удалось найти всю информацию, 
поэтому некоторые ячейки остались незаполненными (можно считать их значение равным нулю). 
Также он использовал какой-то странный офисный пакет и разделял целую и дробную часть чисел запятой. 
Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx 

Вася составил раскладку по продуктам на один день (она на листе "Раскладка") с указанием названия продукта и его количества в граммах. 
Посчитайте 4 числа: суммарную калорийность и граммы белков, жиров и углеводов. Числа округлите до целых вниз и введите через пробел.

'''

import openpyxl
import math

book = openpyxl.open('trekking2.xlsx', read_only=True)
sheet = book.worksheets[0]

products = {}
total = {'ККал': 0, 'Б': 0, 'Ж': 0, 'У': 0}

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

products_one_day = {}

for j in range(2,14):
    data = sheet_2[j][1].value / 100
    if sheet_2[j][0].value in products_one_day:
        products_one_day[sheet_2[j][0].value] += data
    else:
        products_one_day[sheet_2[j][0].value] = data

#расчеты
for key, value in products_one_day.items():
    total['ККал'] += products[key][0] * value
    total['Б'] += products[key][1] * value
    total['Ж'] += products[key][2] * value
    total['У'] += products[key][3] * value

for value in total.values():
    print(math.floor(value),end=' ')
