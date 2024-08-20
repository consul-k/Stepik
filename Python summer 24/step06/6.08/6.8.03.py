matrix = [list(map(int, input().split())) for i in range(int(input()))]
zipped_rows = zip(*matrix)
t_matrix = [list(row) for row in zipped_rows]


if t_matrix == matrix:
    print('YES')
else:
    print('NO')
