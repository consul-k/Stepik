def positive(func):
    def wrapper(*args):
        result = func(*args)
        if result > 0:
            return result
        else:
            return 0
    return wrapper
