def is_double_diagonal_equal(matrix):
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            return "Матрица не квадратная"
    
    main_diagonal = []
    secondary_diagonal = []
    
    for i in range(n):
        main_diagonal.append(matrix[i][i])
        secondary_diagonal.append(matrix[i][n - 1 - i])
    
    return main_diagonal == secondary_diagonal
