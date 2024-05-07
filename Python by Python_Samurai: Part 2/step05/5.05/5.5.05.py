def func(*dicts):
    """Функция для объединения произвольного количества словарей"""
    result = {}
    for d in dicts:
        result.update(d)
    return result
