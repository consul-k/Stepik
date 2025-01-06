def check_login_password(login, password, check_login='admin', check_password='admin'):
    authorization = None
    if login == check_login and password == check_password:
        authorization = True
    else:
        authorization = False
    return authorization

print(check_login_password(input(), input()))
