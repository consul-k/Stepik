import copy
import functools

def no_side_effects_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Делаем глубокие копии аргументов
        args_copy = copy.deepcopy(args)
        kwargs_copy = copy.deepcopy(kwargs)
        
        # Выполняем функцию
        result = func(*args_copy, **kwargs_copy)

        return result
    return wrapper
