# Считываем цвета платьев подруг
first = input().strip()
second = input().strip()

# Все возможные цвета
colors = {"Розовое", "Красное", "Синее"}

# Выбираем доступный Кате цвет, учитывая её предпочтения
available = list(colors - {first, second})

# Упорядочим предпочтения Кати: от самого желаемого к наименее
preferences = ["Розовое", "Красное", "Синее"]

for color in preferences:
    if color in available:
        katyas_dress = color
        break

# Определяем цвет туфель
shoes = {
    "Розовое": "Белые",
    "Красное": "Черные",
    "Синее": "Голубые"
}

# Выводим результат
print(shoes[katyas_dress])
