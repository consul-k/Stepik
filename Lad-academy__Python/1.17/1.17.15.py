numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
result = {a: [n for n in range(1,a+1) if a%n == 0] for a in numbers}
print(result)
