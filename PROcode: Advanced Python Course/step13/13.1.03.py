def matrix_add(a, b):
    if len(a) != len(b):
        return "Матрицы разного размера - сложение невозможно."

    result = []

    for row_a, row_b in zip(a, b):
        if len(row_a) != len(row_b):
            return "Матрицы разного размера - сложение невозможно."

        result_row = [x + y for x, y in zip(row_a, row_b)]
        result.append(result_row)

    return result
