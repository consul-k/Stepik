def determinant_3x3(matrix):
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("Функция работает только для матриц 3x3")
    
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
   
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
