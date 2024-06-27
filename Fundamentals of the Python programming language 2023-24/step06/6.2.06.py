def area(a, b, c=1):
    p = (a + b + c) / 2
    if c!=1:
        return (p*(p-a)*(p-b)*(p-c))**0.5
    else:
        return a*b
