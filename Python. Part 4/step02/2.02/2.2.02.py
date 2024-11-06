def apply_multiple(funcs, value):
    for func in funcs:
        value = func(value)
    return value
