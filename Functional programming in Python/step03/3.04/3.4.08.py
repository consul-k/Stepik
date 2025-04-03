def create_matrix(size=3, up_fill=0, down_fill=0):
    matrix = [[0] * size for _ in range(size)]
    
    for i in range(size):
        matrix[i][i] = i + 1
    
    for i in range(size):
        for j in range(i + 1, size):
            matrix[i][j] = up_fill
    
    for i in range(size):
        for j in range(i):
            matrix[i][j] = down_fill
    
    return matrix
