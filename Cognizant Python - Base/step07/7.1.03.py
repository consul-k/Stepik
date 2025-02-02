# Создайте функцию-генератор:
def infinite_double_generator(n):
    while True:
        n *= 2
        yield n

# Приняли число от пользователя:
number = int(input())

# Создайте генератор gen:
gen = infinite_double_generator(number)

# Код ниже не удаляйте:
for i in range(number):
    print(next(gen))
