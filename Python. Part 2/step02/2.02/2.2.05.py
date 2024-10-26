num_rows = len(matrix)
num_cols = len(matrix[0])

column_sums = [0] * num_cols

for col in range(num_cols):
    for row in range(num_rows):
        column_sums[col] += matrix[row][col]

print(column_sums)
