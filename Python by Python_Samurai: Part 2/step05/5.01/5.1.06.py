def func(password):
    digits = any(char.isdigit() for char in password)
    lower = any(char.islower() for char in password)
    upper = any(char.isupper() for char in password)
    special = any(char in "!@#$%*" for char in password)
    length = len(password) >= 8

    if all((digits, lower, upper, special, length)):
        print("Шикарный пароль!")
    else:
        print("Плохо. Но я уверен ты сможешь! Наверное...")
