while True:
    login = input()
    if len(login) < 6:
        print("Логин должен содержать не менее 5 символов")
        continue

    password = input()
    if len(password) < 8 or "%" not in password or "#" not in password:
        print("Пароль менее 8 символов, либо не содержит символы \"%#\"")
        continue

    print("Регистрация завершена!")
    break
