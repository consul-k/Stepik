def filter_magic_numbers(*args):
    res = []
    for i in args:
        if i%2==0:
            res.append(i)
    return res
