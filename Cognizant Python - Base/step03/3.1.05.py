def check_password(password):
    if len(password) < 3:
        return False

    if ' ' in password:
        return False

    if not password[0].isupper():
        return False

    if not password[-1].isdigit():
        return False

    return True

password = input()
if check_password(password):
    print("True")
else:
    print("False")
