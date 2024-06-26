matrix = []
for i in range(5):
    line = input()
    row = [int(s) for s in line.split()]
    matrix.append(row)

transposed_matrix = [[matrix[j][i] for j in range(5)] for i in range(5)]

for row in transposed_matrix:
    print(" ".join(map(str, row)))
