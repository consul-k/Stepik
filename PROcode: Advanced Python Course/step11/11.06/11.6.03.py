def data_converter(tp):
    def inner(s):
        numbers = map(int, s.split())
        if tp == "list":
            return list(numbers)
        elif tp == "tuple":
            return tuple(numbers)
    return inner
