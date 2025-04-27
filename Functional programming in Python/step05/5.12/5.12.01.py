import functools

def multiply_result_by(N):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * N
        return wrapper
    return decorator
