def log(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            args_str = ', '.join(map(str, args))
            print(f"{level}: аргументы: {args_str} результат: {result}")
            return result
        return wrapper
    return decorator
