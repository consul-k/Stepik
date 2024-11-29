def bigger(x, y):
    if x > y:
        return(x)
    elif y > x:
        return(y)
    else:
        return(x)

x, y = map(int, input().split())
print(bigger(x, y))
