password = input()

if (
    len(password) >= 8 and
    password[0].isalpha() and
    password.isalnum()
):
    print("Пароль принят!")
else:
    print("Пароль не принят!")
