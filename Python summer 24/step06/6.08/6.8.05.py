n = int(input())
m = int(input())
matrix = [[i * m + j + 1 for j in range(m)] for i in range(n)]
for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()
