matrix = []
for i in range(5):
    line = input()
    row = [int(s) for s in line.split()]
    matrix.append(row)

averages = []
for col in range(5):
    column_sum = 0
    for row in matrix:
        column_sum += row[col]
    averages.append(column_sum / 5)

for avg in averages:
    print(avg)
