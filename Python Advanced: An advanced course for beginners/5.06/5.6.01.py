old_passwords = ('qwerty', '123456', 'abc123')

print("Старый кортеж:", old_passwords)

password_list = list(old_passwords)

new_password = input()  # например: galaxy123

password_list.append(new_password)

new_passwords = tuple(password_list)

print("Новый кортеж:", new_passwords)
