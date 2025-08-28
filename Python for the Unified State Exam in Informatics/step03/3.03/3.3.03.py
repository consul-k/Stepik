n = int(input())  # количество минут

# Рассчитываем часы и минуты
hours = n // 60
minutes = n % 60

# Выводим результат
print(f"{hours}:{minutes}")
