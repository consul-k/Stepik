while True:
    number = input()
    if not number.isdigit():
        print("Вы ввели не число")
    else:
        number = int(number)
        if number == 13:
            print("Вы всё таки ввели 13, а я думал мы друзья...")
            break
        else:
            print("Вы ввели число:", number)
