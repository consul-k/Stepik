n = int(input())
m = int(input())
matrix = []

for i in range(n):
    p = [int(s) for s in input().split()]
    matrix.append(p)

m = max(max(matrix, key=max))
res = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == m:
            res.append((i,j))

print(*res[0])
