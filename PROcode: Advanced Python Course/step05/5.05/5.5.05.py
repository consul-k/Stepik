numbers = (
    3, 1, 4, 1, 5, 9, 2, 6, 5, 3,
    5, 8, 9, 7, 9, 3, 2, 3, 8, 4,
    6, 2, 6, 4, 3, 3, 8, 3, 2, 7,
    9, 5, 0, 2, 8, 8, 4, 1, 9, 7,
    1, 6, 9, 3, 9, 9, 3, 7, 5, 1
)

# Читаем ввод
x = int(input().strip())
start = int(input().strip())
end = int(input().strip())

found_index = -1  # маркер, если не найдено

# Перебор в диапазоне
for i in range(start, end):
    if 0 <= i < len(numbers) and numbers[i] == x:
        found_index = i
        break

# Вывод результата
if found_index != -1:
    print(f"Первое вхождение числа {x} в диапазоне от {start} до {end} находится на индексе: {found_index}")
else:
    print(f"Число {x} не найдено в диапазоне от {start} до {end}.")
