def flatten_matrix(nested_list):
    for sublist in nested_list:
        yield from sublist
