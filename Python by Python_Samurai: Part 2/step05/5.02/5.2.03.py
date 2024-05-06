a = input().split()

def func(a):
    res = {}
    for s in range(len(a)):
        if a[s].isdigit():
            res[int(a[s])] = a[s-1]
    return res

print(func(a))
