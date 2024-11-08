def wrap_result(func):
    def wrapper(*args):
        result = {'result': func(*args)}
        return result
    return wrapper
