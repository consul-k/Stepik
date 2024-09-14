n = [int(i) for i in input().split()]
n = sorted(n)

def isort(n):
    return sum([int(i) for i in str(n)])

print(*sorted(n, key=isort))
