n = int(input())

count_red = 0

for _ in range(n):
    color = input().strip()  # Считываем цвет машины
    if color == "красный":
        count_red += 1

print(count_red)
