n = list(map(int, input().split()))
res = []
for i in n:
    s = []
    for _ in range(n.count(i)):
        s.append(i)
    if s not in res:
        res.append(s)
print(sorted(res))
