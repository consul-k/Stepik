'''

Подвиг 4. Вводятся данные по книге в виде строки через запятую в формате (некоторые значения могут отсутствовать):

id, автор, название, цена, год издания

с помощью команд:

t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]

Например, при вводе:

"1, Балакирев С.М., Python, 2100, 2023"

получим список:

book = [1, 'Балакирев С.М.', 'Python', 2100.0, 2023]

А при вводе:

"1, Балакирев С.М., Python"

список:

book = [1, 'Балакирев С.М.', 'Python']

И так далее.

С помощью оператора match/case необходимо определить шаблоны для выделения следующей информации:

автор, название
автор, название, цена
автор, название, год издания
автор, название, цена, год издания

Первый шаблон срабатывает, если есть только автор и название; второй, если появляется еще и цена; третий, если есть автор, 
название, год издания, но нет цены; последний, если имеются все данные.

При срабатывании шаблона вывести на экран строку "Yes". Если ни один из шаблонов не сработал, то вывести строку "No".

Sample Input 1:

1, Балакирев С.М., Python, 2100.0, 2023

Sample Output 1:

Yes

Sample Input 2:

2, Зингаро. Д, Python без проблем, 1000.0, 2022

Sample Output 2:

Yes

Sample Input 3:

3, Бейдер Дэн

Sample Output 3:

No

Sample Input 4:

4

Sample Output 4:

No

Sample Input 5:

5, Яворски Михаил, Python. Лучшие практики и инструменты, 1500.1, 2021

Sample Output 5:

Yes

'''

t = (int, str, str, float, int)
book = [t[i](x) for i, x in enumerate(input().split(", "))]

match book:
    case (_,author, title):
        print('Yes')
    case (_,author, title, float() | int() as price):
        print('Yes')
    case (_,author, title, int() as year):
        print('Yes')    
    case (_,author, title, float() | int() as price, int() as year):
        print('Yes')
    case _:
        print("No")
