def add_starting_balance(start):
    def decorator(func):
        def wrapper(data):
            return func(data) + start
        return wrapper
    return decorator

@add_starting_balance(start=5)
def calculate_expenses(data):
    numbers = map(float, data.split())
    return int(sum(numbers))
