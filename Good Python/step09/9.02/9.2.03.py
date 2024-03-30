def line(n):
    if n > 0:
        print('+' * n)
    if n < 0:
        print('-' * abs(n))

line(int(input()))
