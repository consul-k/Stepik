def conditional_map(func, condition, lst):
    return [func(x) if condition(x) else x for x in lst]
