def create_dict():
    data = {}
    count = 0

    def inner(value):
        nonlocal count
        count += 1
        data[count] = value
        return data

    return inner
