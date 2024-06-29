def perevorot(n):
    if n < 10:
        print(n, end='')
    else:
        print(n % 10, end='')
        perevorot(n // 10)
