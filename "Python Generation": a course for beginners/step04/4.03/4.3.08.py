n = int(input())
if n == 0:
    print('зеленый')
elif n >= 1 and n <= 10:
    if n % 2 != 0:
        print('красный')
    else:
        print('черный')
elif n >= 11 and n <= 18:
    if n % 2 != 0:
        print('черный')
    else:
        print('красный')
elif n >= 19 and n <= 28:
    if n % 2 != 0:
        print('красный')
    else:
        print('черный')
elif n >= 29 and n <= 36:
    if n % 2 != 0:
        print('черный')
    else:
        print('красный')
else:
    print('ошибка ввода')
