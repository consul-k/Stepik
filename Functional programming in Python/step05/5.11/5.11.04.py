import functools

def add_args(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        new_args = ("begin",) + args + ("end",)
        return func(*new_args, **kwargs)
    return wrapper
