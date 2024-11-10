def skip_if_less_than(limit):
    def decorator(func):
        def wrapper(value, *args, **kwargs):
            if value <= limit:
                return func(value, *args, **kwargs)
            else:
                print(f"Значение {value} больше или равно {limit}")
        return wrapper
    return decorator
