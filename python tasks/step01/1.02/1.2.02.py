import math

def check_sqrt(n):
    s = int(math.sqrt(n))
    if s * s == n:
        return s
    else:
        return -1

n = int(input())

res = check_sqrt(n)
print(res)
