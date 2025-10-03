security_level = 0

def hack_system():
    global security_level
    security_level = 5  # Меняем глобальную переменную

    defense_level = 0  # Локальная переменная во внешней функции

    def defend_system():
        nonlocal defense_level
        defense_level = 10

    defend_system() 
    return defense_level
