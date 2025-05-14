def filter_even(func):
    def wrapper(*args, **kwargs):
        new_args = []
        for arg in args:
            if isinstance(arg, int) and arg % 2 == 0:
                new_args.append(arg)
            elif arg is False:
                new_args.append(arg)
            elif isinstance(arg, (list, tuple, set, dict, str)) and len(arg) % 2 == 0:
                new_args.append(arg)
        return func(*new_args, **kwargs)
    return wrapper

def delete_short(func):
    def wrapper(*args, **kwargs):
        new_kwargs = {k: v for k, v in kwargs.items() if len(k) > 4}
        return func(*args, **new_kwargs)
    return wrapper
