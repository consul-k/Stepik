matrix = [list(map(int, input().split())) for i in range(int(input()))]
up = []
right = []
down = []
left = []

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i > j and i < len(matrix) - 1 - j:
            left.append(matrix[i][j])
        if i < j and i > len(matrix) - 1 - j:
            right.append(matrix[i][j])
        if i < j and i < len(matrix) - 1 - j:
            up.append(matrix[i][j])
        if i > j and i > len(matrix) - 1 - j:
            down.append(matrix[i][j])

print('Верхняя четверть:',sum(up))
print('Правая четверть:',sum(right))
print('Нижняя четверть:',sum(down))
print('Левая четверть:',sum(left))
