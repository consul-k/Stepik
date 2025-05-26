def countdown(N):
    count = 0

    def inner():
        nonlocal count
        if count < N:
            print(N - count)
            count += 1
        else:
            print(f"Превышен лимит, вы вызвали более {N} раз")

    return inner
