def validate_all_args_str(func):
    def wrapper(*args, **kwargs):
        if all(isinstance(arg, str) for arg in args):
            return func(*args, **kwargs)
        else:
            print("Все аргументы должны быть строками")
            return None
    return wrapper
