num = list(map(int, input().split()))
res = []
for i in range(1, num[0]+1):
    if i % num[1] == 0:
        res.append(i)
print(res)
