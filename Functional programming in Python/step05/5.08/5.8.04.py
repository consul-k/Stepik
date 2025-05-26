def create_accumulator(initial_value=0):
    total = initial_value  # начальное значение, по умолчанию 0

    def accumulator(value):
        nonlocal total  # используем переменную из внешнего замыкания
        total += value
        return total

    return accumulator
