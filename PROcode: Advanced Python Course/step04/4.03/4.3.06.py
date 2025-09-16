def create_profile(name, power_level, ability="Неизвестная суперспособность"):
    if not name or name.strip() == "":
        print("Ошибка: имя не может быть пустым")
        return

    if not isinstance(power_level, (int, float)) or power_level <= 0:
        print("Ошибка: уровень силы должен быть положительным числом")
        return

    if not ability or ability.strip() == "":
        ability = "Неизвестная суперспособность"

    print(f"Герой: {name}")
    print(f"Уровень силы: {power_level}")
    print(f"Суперспособность: {ability}")
