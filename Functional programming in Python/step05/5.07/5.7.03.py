def compute(args, *num):
    l = []
    for j in num:
        for i in args:
            j = i(j)
        l.append(j)
    return l
