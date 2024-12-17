n, m = map(int, input().split())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(n):
    for j in range(m):
        matrix[i][j] += 1

for row in matrix:
    print(' '.join(map(str, row)))
