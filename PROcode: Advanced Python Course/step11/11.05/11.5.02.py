res = list(map(int, input().split()))
a = filter(lambda x: x % 3 == 0, res)
b = map(lambda x: x * 2, a)
print(sorted(b))
