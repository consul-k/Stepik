def is_member(value, lst):
    return value in lst

def overlapping(lst1, lst2):
    for i in lst1:
        if is_member(i, lst2):
            return True
    else:
        return False
