n = int(input())
m = int(input())
matrix = [['.'] for _ in range(n * m)]
for i in range(1, len(matrix), 2):
    matrix[i][0] = '*'

for r in range(n):
    for c in range(m):
        print(matrix[r + c][0], end = ' ')
    print()
