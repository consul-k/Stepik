def log_calls(func):
    def wrapper(*args):
        result = func(*args)
        print(f"Вызов с аргументами {args}. Результат: {result}")
        return result
    return wrapper
