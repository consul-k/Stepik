import functools

def explicit_args(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args:
            print("Вы не можете передать позиционные аргументы. Используйте именованный способ передачи значений")
            return
        return func(**kwargs)
    return wrapper
