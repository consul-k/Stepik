time_of_day = input().lower()
answer = input().lower()

if time_of_day == "день":
    if answer == "да":
        print("Людоеды съели вас.")
    elif answer == "нет":
        print("Вы прошли в деревню.")
    else:
        print("Некорректный ответ.")
elif time_of_day == "ночь":
    if answer == "да":
        print("Людоеды поймали вас.")
    elif answer == "нет":
        print("Вы прошли в деревню.")
    else:
        print("Некорректный ответ.")
else:
    print("Некорректное время суток.")
