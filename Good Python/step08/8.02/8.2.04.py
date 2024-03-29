n = int(input())
m = int(input())
res = []
for i in range(n):
    row = []
    for j in range(1,m+1):
        row.append(j)
    res.append(row)
    
for i in res:
    print(*i)
