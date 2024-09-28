matrix = [list(map(int, input().split())) for i in range(int(input()))]
first = []
second = []

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i >= j and i <= len(matrix) - 1 - j:
            first.append(matrix[i][j])
        if i <= j and i >= len(matrix) - 1 - j:
            second.append(matrix[i][j])

first.extend(second)
print(max(first))
