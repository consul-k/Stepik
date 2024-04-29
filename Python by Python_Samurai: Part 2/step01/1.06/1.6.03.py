x1, x2 = map(int, input().split())
print([i**2 for i in range(x1, x2 - 1, -1)] if x1 > x2 else [i**3 for i in range(x1, x2 + 1)])
