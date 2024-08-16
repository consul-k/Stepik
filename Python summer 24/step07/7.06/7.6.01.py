def min(a, b):
    if a < b:
        return a
    else:
        return b

a, b, c, d = map(int, input().split())

result = min(min(a, b), min(c, d))

print(result)
