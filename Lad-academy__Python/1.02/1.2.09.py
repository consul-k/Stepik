number = int(input())

if 99 <= number <= 999:
    first_digit = number // 100
    middle_digit = (number // 10) % 10
    last_digit = number % 10

    if first_digit + last_digit == middle_digit:
        print("YES")
    else:
        print("NO")
else:
    print('NO')
