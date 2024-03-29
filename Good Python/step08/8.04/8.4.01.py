n = int(input())
a = [[0]*n for _ in range(n)]
for i in range(len(a)):
    a[i][i] = 1
for j in a:
    print(*j)
