def register(name, position="Студент", city="Неизвестен"):
    if position == ' ':
        position = 'Студент'
    elif city == ' ':
        city = 'Неизвестен'
    print(f'Участник {name} зарегистрирован как {position} из города {city}.')
