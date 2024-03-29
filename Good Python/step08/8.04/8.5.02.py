n = int(input())
a = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = 1
        elif i < j:
            a[i][j] = 0
        else:
            a[i][j] = 2
for row in a:
    print(*row)
