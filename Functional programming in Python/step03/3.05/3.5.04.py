def lstrip(lst, value):
    i = 0
    while i < len(lst) and lst[i] == value:
        i += 1
    
    return lst[i:]
