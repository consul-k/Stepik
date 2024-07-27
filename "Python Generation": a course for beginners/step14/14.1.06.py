# объявление функции
def is_magic(date):
    day, month, year = map(int, date.split('.'))
    return day * month == int(str(year)[-2:])
    
# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))
