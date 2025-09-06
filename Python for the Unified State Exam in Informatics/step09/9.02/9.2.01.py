def product(n):
    if n <= 1:
        return 1
    else:
        return n % 10 * product(n // 10)
