import sys
lst = sys.stdin.readlines()
lst = [list(map(int, i.split())) for i in lst]

# продолжите решение здесь(в lst будет приходить матрица)
def diagonal_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    return sum
print(diagonal_sum(lst))
