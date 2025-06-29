a = tuple(map(int, input().split(',')))
print(sum(a))
b = tuple(sum(a)-i for i in a)
print(b)
