def multiply(x):
    def inner(y):
        return x * y
    return inner
