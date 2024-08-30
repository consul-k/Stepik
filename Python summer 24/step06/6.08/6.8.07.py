def read_matrix(n, m):
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

n = int(input())
m = int(input())

matrix1 = read_matrix(n, m)
matrix2 = read_matrix(n, m)

result_matrix = []
for i in range(n):
    result_row = []
    for j in range(m):
        result_row.append(matrix1[i][j] + matrix2[i][j])
    result_matrix.append(result_row)

for row in result_matrix:
    print(" ".join(map(str, row)) + " ")
