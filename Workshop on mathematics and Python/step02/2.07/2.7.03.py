def dfactorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * dfactorial(n - 2)
