def create_accumulator():
    total = 0  # начальная сумма

    def accumulator(value):
        nonlocal total  # используем переменную из внешнего замыкания
        total += value
        return total

    return accumulator
