def convert_to(values, type_to=int):
    return list(map(lambda x: type_to(x), numbers))
