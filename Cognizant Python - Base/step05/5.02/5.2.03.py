a = input().split()
res = {}
for i in range(len(a)):
    l = list(map(int, input().split()))
    res[a[i]] = l
print(res)
