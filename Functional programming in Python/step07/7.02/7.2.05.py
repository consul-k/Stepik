def double_fact(n):
    if n <= 0:  # условие выхода из рекурсии
        return 1
    return n * double_fact(n - 2)  # рекурсивный вызов для n-2
