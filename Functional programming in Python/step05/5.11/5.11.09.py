import functools

def check_count_args(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        total_args = len(args) + len(kwargs)
        if total_args < 2:
            print("Not enough arguments")
        elif total_args > 2:
            print("Too many arguments")
        else:
            return func(*args, **kwargs)
    return wrapper
