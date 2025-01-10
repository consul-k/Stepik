# put your python code here
login = input()
password = input()
if login != 'admin':
    print(f'Пользователь {login}')
else:
    if password == 'read':
        print('Редактор в режиме чтения')
    elif password == 'edit':
        print('Редактор в режиме редактирования')
    elif password != 'read' and password != 'edit':
        print('Неправильный пароль')
