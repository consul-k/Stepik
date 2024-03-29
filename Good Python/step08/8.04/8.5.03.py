n = int(input())
a = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            a[i][j] = 1
for row in a:
    print(*row)
