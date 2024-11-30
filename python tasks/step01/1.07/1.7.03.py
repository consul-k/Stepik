def check_number(number):
    if number % 2 == 0 and number > 10:
        print(1)
    elif number % 2 != 0 or number < 0:
        print(-1)
    else:
        print(0)

n = int(input())
check_number(n)
