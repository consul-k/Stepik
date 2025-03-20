def print_args(a, b, c, d):
    print(a, b, c, d)

dct = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
print_args(**dct)
