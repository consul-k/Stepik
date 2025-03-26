def lstrip(lst, value):
    while lst and lst[0] == value:
        lst.pop(0)
