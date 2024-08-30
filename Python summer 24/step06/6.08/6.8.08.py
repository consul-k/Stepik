n = int(input())
m = int(input())
k = int(input())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

result_matrix = []
for row in matrix:
    result_row = [element * k for element in row]
    result_matrix.append(result_row)

for row in result_matrix:
    print(''.join(str(element).ljust(3) for element in row))
