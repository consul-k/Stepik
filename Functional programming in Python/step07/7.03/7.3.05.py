def get_arith_progression(n):
    if n == 1:
        return 1
    return get_arith_progression(n - 1) + 7
