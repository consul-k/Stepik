a = set(input().split())
b = set(input().split())
c = a - b
d = b - a
print(*sorted(c))
print(*sorted(d))
