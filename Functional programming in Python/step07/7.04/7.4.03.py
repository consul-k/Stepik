def get_max_recursive(lst):
    max_val = float('-inf')
    for item in lst:
        if isinstance(item, list):
            max_val = max(max_val, get_max_recursive(item))
        else:
            max_val = max(max_val, item)
    return max_val
