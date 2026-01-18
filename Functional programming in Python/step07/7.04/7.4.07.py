def reversed_recursive(lst):
    result = []
    for item in reversed(lst):
        if isinstance(item, list):
            result.append(reversed_recursive(item))
        else:
            result.append(item)
    return result
