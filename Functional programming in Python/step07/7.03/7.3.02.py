def power(a: int, n: int) -> int:
    if n == 0:
        return 1
    return a * power(a, n - 1)
