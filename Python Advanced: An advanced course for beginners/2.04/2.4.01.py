def choose_weapon(power_level, battle_experience):
    if power_level < 50:
        print("Выберите меч!")
    elif 50 <= power_level <= 100:
        if battle_experience < 20:
            print("Выберите лук и стрелы!")
        else:
            print("Выберите магический посох!")
    else:
        print("Выберите любое оружие на ваш выбор!")

power = int(input())
experience = int(input())
choose_weapon(power, experience)
