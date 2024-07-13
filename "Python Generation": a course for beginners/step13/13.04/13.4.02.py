# объявление функции
def get_days(month):
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    return m[month-1]

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))
