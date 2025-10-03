import math

def validate_positive(func):
    def wrapper(n):
        if n > 0:
            return func(n)
        else:
            return "Ошибка: число должно быть больше нуля!"
    return wrapper

@validate_positive
def square_root(n):
    return round(math.sqrt(n), 2)
