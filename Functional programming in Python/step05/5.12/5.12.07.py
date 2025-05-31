def compose(*funcs):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            for f in funcs:
                result = f(result)
            return result
        return wrapper
    return decorator
