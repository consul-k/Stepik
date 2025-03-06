n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
summ = 0
for i in range(n):
    for j in range(n):
        if i == j: summ += matrix[i][j]
print(summ)
