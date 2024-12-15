lst = list(map(int, input().split()))
res = [i for i in lst if i > 0]
print(min(res))
