def func(**kwargs):
    keys = tuple(kwargs.keys())
    values = tuple(kwargs.values())
    return [keys, values]
