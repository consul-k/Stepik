# кортеж паролей
old_passwords = ('qwerty', '123456', 'abc123')

# выводим старый кортеж
print("Старый кортеж:", old_passwords)

# преобразуем кортеж в список
password_list = list(old_passwords)

# ввод нового пароля
new_password = input()  # например: galaxy123

# добавляем новый пароль в список
password_list.append(new_password)

# преобразуем список обратно в кортеж
new_passwords = tuple(password_list)

# выводим новый кортеж
print("Новый кортеж:", new_passwords)
