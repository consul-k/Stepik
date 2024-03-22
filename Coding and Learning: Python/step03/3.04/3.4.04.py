color = input()
pedestrians = input()

if color == "Зеленый" and pedestrians == "Нет":
    print("Ехать")
elif color == "Зеленый" and pedestrians == "Да":
    print("Ожидать")
else:
    print("Остановиться")
