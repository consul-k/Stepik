def nod2(a, b):
    if b == 0:
        return a
    return nod2(b, a % b)

def nod3(a, b, c):
    return nod2(nod2(a, b), c)
