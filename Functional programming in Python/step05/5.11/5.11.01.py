def upper(func):
    def inner(*args, **kwargs):
        """
        Внутренняя функция декоратора
        """
        return func(*args, **kwargs).upper()
    
    # Сохраняем оригинальные имя и докстроку функции
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    
    return inner


@upper
def concatenate(*args):
    """
    Возвращает конкатенацию переданных строк
    """
    return ', '.join(args)

print(concatenate.__name__)
print(concatenate.__doc__.strip())
