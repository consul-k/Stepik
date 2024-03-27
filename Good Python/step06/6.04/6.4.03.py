password = input()
if len(password) >= 8 and password.lower() != password and password.upper() != password:
    print("YES")
else:
    print("NO")
