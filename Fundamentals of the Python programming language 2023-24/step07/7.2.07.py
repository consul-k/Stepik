N = int(input())

harvest = {}

for _ in range(N):
    data = input()
    month, quantity = data.split()
    quantity = int(quantity)

    harvest[month] = harvest.get(month, 0) + quantity

max_month = max(harvest, key=harvest.get)

print(max_month)
