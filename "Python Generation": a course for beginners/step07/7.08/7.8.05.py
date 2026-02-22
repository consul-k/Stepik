n = int(input())
max_digit = -1
has_zero = False
while n > 0:
    digit = n % 10
    if digit == 0:
        has_zero = True
    if digit % 3 == 0 and digit > max_digit:
        max_digit = digit
    n = n // 10
if max_digit == -1:
    if has_zero:
        print(0)
    else:
        print('NO')
else:
    print(max_digit)
