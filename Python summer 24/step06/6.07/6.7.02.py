n = int(input())
m = int(input())
matrix = []

for i in range(n):
    p = []
    for j in range(m):
        p.append(input())
    matrix.append(p)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()

print()

matrix_c = list(zip(*matrix))
for i in matrix_c:
    for j in i:
        print(j, end= ' ')
    print()
