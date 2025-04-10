def find_keys(**kwargs):
    res = []
    for key, value in kwargs.items():
        if type(value) in [list, tuple]:
            res.append(key)
    return sorted(res, key = str.lower)
