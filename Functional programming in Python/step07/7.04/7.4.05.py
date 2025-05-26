def is_member(value, lst):
    for element in lst:
        if isinstance(element, list):
            if is_member(value, element):
                return True
        elif element == value:
            return True
    return False
