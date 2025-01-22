import string

def check_password(password):
    for char in password:
        if char not in string.ascii_letters and char not in string.digits:
            print(False)
            return
    print(True)

user_password = input()
check_password(user_password)
