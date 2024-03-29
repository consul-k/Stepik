n, m = map(int, input().split())
res = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(0)
    res.append(row)
    
for i in res:
    print(*i)
