def find_level_element(value, lst, level=1):
    for element in lst:
        if element == value:
            return level
        elif isinstance(element, list):
            found_level = find_level_element(value, element, level + 1)
            if found_level != -1:
                return found_level
    return -1
