def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        min_rest = find_min(lst[1:])
        return lst[0] if lst[0] < min_rest else min_rest
