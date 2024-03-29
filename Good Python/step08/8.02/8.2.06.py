n = int(input())
m = int(input())

l = []
for i in range(n):
    l.append(input().split())
    for j in range(m):
        l[i][j] = int(l[i][j])

print(l)
