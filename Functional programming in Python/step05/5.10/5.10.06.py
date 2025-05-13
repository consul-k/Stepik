def validate_all_args_str(func):
    def wrapper(*args, **kwargs):
        if all(isinstance(arg, str) for arg in args):
            return func(*args, **kwargs)
        else:
            print("Все аргументы должны быть строками")
            return None
    return wrapper

def validate_all_kwargs_int_pos(func):
    def wrapper(*args, **kwargs):
        if all(isinstance(value, int) and value > 0 for value in kwargs.values()):
            return func(*args, **kwargs)
        else:
            print("Все именованные аргументы должны быть положительными числами")
            return None
    return wrapper
