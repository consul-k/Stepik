a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = sorted(a - b)
print(*c)
