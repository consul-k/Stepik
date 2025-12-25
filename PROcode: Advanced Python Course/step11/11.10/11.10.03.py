for attempt in range(1, 6):
    print(f"Попытка {attempt} из 5")
    
    user_input = input()
    
    if user_input == "777":
        print("Обнаружен секретный код! Доступ получен без проверки.")
        break
    
    try:
        number = int(user_input)
        
        if number % 15 == 0:
            print("Врата открываются... Добро пожаловать!")
            break
        elif attempt < 5:
            print("Неверный код. Он не открывает врата.")
    
    except ValueError:
        print("Ошибка: ввод должен быть целым числом.")
    
    if attempt == 5:
        print("Попытки исчерпаны. Вы остаетесь в лабиринте навсегда.")

print("Сессия завершена.")
