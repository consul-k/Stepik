while True:
    user_input = input()
    try:
        code = int(user_input)
        
        if code == 0:
            print("Ошибка: код не может быть равен нулю. Попробуйте снова.")
            continue
        
        result = code * 2
        print(f"Доступ разрешён. Удвоенный код: {result}")
        break

    except ValueError:
        print("Ошибка: это не число. Попробуйте снова.")
