def summa(N):
    if N == 1:
        return 1
    else:
        return N + summa(N - 1)
