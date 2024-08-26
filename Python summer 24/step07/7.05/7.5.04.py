def s(a, n):
    res = 1
    for _ in range(n):
        res *= a
    return res

a = int(input())
n = int(input())
print(s(a, n))
