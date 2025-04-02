def compute(lst, *args):
    res = []
    for func in lst:
        for i in args:
            res.append(func(i))
    return res
