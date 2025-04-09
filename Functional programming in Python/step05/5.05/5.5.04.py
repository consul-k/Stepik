def count_strings(*args):
    res = 0
    for i in args:
        if type(i) is str:
            res += 1
    return res
