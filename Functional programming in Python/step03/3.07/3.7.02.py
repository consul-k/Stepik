def concatenate(**kwargs):
    res = ''
    for i in kwargs.values():
        res += str(i)
    return res
