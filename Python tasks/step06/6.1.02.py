def p(x, n):
    if n == 0:
        return 1
    elif n > 0:
        res = x
        for _ in range(n-1):
            res *= x
        return res
    else:
        res = x
        for _ in range(abs(n)-1):
            res *= x
        return 1 / res

x = int(input())
n = int(input())
print(p(x, n))
