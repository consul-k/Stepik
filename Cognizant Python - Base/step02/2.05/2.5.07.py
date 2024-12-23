password = input()
test1 = password.istitle()
test2 = password.isidentifier()
check_password = test1 + test2
print(check_password == 2)
