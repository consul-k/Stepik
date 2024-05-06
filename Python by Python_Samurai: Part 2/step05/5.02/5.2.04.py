a = list(map(int, input().split()))

def func(a):
    for i in a:
        if a.count(i) == 1:
            return i
    return -1

print(func(a))
