# Вводим час
hour = int(input())

# Определяем, чем занят работник
if 8 <= hour < 12 or 13 <= hour < 17:
    print("Работать")
elif hour == 12:
    print("Обедать")
else:
    print("Отдыхать")
