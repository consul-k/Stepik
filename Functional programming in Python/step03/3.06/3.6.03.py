def multiply(*args):
    res = 1
    if args:
        for i in args:
            res *= i
        return res
    else:
        return res
