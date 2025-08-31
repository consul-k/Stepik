n = int(input())  # Читаем количество строк
strings = [input() for _ in range(n)]  # Сохраняем все строки в список

# Находим строку с максимальной длиной
max_str = max(strings, key=len)

# Умножаем её на 33 и выводим результат
print(max_str * 3)
