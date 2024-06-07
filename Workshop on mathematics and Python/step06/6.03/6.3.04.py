import numpy as np

def create_matrix(input_str):
    parts = input_str.split()

    if parts[-1].isdigit() or parts[-1].replace('.', '', 1).isdigit():
        shape = tuple(map(int, parts))
        dtype = np.float64
    else:
        shape = tuple(map(int, parts[:-1]))
        dtype = parts[-1]
    Z = np.zeros(shape, dtype=dtype)
    return Z

input_str1 = input()
Z = create_matrix(input_str1)
