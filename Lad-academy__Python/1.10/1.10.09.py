l = list(map(int, input().split()))
m = list(map(int, input().split()))
res = []
for i in range(len(l)):
    res.append(l[i]+m[i])
print(*res)
