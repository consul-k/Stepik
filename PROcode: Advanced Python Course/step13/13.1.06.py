def matrix_multiply(a, b):
    # Проверка, что обе матрицы не пусты
    if not a or not b or not a[0] or not b[0]:
        return "❌ Матрицы несовместимы - нельзя перемножить"

    # Количество столбцов в a и строк в b
    cols_a = len(a[0])
    rows_b = len(b)

    # Проверка совместимости
    if cols_a != rows_b:
        return "❌ Матрицы несовместимы - нельзя перемножить"

    # Инициализация результирующей матрицы нулями
    rows_a = len(a)
    cols_b = len(b[0])
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    # Перемножение матриц
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]

    return result
