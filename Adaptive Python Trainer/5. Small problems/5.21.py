n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

transposed = [[matrix[i][j] for i in range(n)] for j in range(m)]

for row in transposed:
    print(*row)
