def multu_recursive(lst):
    result = 1
    
    for element in lst:
        if isinstance(element, int):
            result *= element
        elif isinstance(element, list):
            result *= multu_recursive(element)
    
    return result
