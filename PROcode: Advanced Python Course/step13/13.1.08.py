def is_diagonal_layer_balance(matrix):
    n = len(matrix)
    
    for row in matrix:
        if len(row) != n:
            return "Матрица не подходит"
    
    if n % 2 == 0:
        return "Матрица не подходит"
    
    layers = n // 2 + 1
    
    for k in range(layers):
        len_layer = n - 2 * k
        
        sum_main = 0
        sum_secondary = 0
        
        for i in range(len_layer):
            sum_main += matrix[k + i][k + i]
            
            sum_secondary += matrix[k + i][(n - 1 - k) - i]
        
        if sum_main != sum_secondary:
            return False
    
    return True
