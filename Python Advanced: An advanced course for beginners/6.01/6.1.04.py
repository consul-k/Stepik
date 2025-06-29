a = tuple(map(int, input().split()))
print(min(a), max(a))
b = tuple(i for i in a if i!=min(a) and i!=max(a))
print(b)
