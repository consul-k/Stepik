true_password = input()
count = 0

while True:
    check_password = input()
    if check_password == true_password:
        print("вошли в почту")
        break
    else:
        count += 1
        if count % 3 == 0:
            print("три раза уже неправильно, соберись!")
        else: 
            print("неправильный пароль")
