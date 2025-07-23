def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    transposed = []

    for col in range(cols):
        new_row = []
        for row in range(rows):
            new_row.append(matrix[row][col])
        transposed.append(new_row)

    return transposed
