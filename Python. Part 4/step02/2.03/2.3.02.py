def add_to_number(n):
    def inner_add(x):
        return n + x
    return inner_add
