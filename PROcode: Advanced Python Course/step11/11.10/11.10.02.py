for attempt in range(1, 4):
    print(f"Попытка {attempt} из 3")
    
    try:
        user_input = input()
        number = int(user_input)
        
        if number % 7 == 0:
            print("Врата открываются... Доступ получен!")
            break
        else:
            print("Неверный код. Он не открывает врата.")
            
    except ValueError:
        print("Ошибка: это не число.")
        
else:
    print("Попытки исчерпаны. Врата остаются закрытыми.")
