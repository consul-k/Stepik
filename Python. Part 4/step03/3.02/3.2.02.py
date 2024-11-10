def limit_calls(limit):
    def decorator(func):
        count = 0  # Переменная для отслеживания количества вызовов

        def wrapper(*args, **kwargs):
            nonlocal count  # Используем nonlocal, чтобы изменять переменную count
            if count < limit:
                count += 1
                return func(*args, **kwargs)
            else:
                print("Лимит вызовов исчерпан")

        return wrapper
    return decorator
