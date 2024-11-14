class TumbaUmba:
    pass

def func(n):
    result = []
    for i in range(n):
        obj = TumbaUmba()
        if (i + 1) % 3 == 0:
            obj.warrior = False
        else:
            obj.warrior = True
        result.append(obj)
    return result
