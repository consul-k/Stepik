def double_it(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)*2
    return wrapper
