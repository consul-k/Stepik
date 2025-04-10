def decorator(func):
    def wrapper(*args):
        print('---Start calculation---')
        result = func(*args)
        print(f'---Finish calculation. Result is {result}---')
        return result
    return wrapper


@decorator
def add(a, b):
    return a + b
