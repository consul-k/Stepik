import functools

def cache_result(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            result = cache[key]
            print(f"[FROM CACHE] Вызов {func.__name__} = {result}")
            return result
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper
