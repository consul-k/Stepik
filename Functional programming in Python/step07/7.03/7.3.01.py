def is_member(value, lst):
    if not lst:
        return False
    if lst[0] == value:
        return True
    return is_member(value, lst[1:])
