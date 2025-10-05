def read_columns(matrix):
    if not matrix or not matrix[0]:
        return ''
    
    rows = len(matrix)
    cols = len(matrix[0])
    result = ''

    for col in range(cols):
        for row in range(rows):
            result += matrix[row][col]
    
    return result
