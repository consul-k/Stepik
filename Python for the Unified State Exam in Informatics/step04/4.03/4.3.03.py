# Вводим три целых числа
a = int(input())
b = int(input())
c = int(input())

# Считаем количество положительных чисел
positive_count = sum(x > 0 for x in (a, b, c))

# Применяем соответствующие преобразования
if positive_count == 3:
    a *= 2
    b *= 2
    c *= 2
elif positive_count == 2:
    a *= 3
    b *= 3
    c *= 3
elif positive_count == 1:
    a = a**2
    b = b**2
    c = c**2
# если положительных нет — ничего не делаем

# Выводим результаты
print(a)
print(b)
print(c)
