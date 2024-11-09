def cycle_generator(lst, n):
    while n > 0:
        for i in lst:
            yield i
        n -= 1
