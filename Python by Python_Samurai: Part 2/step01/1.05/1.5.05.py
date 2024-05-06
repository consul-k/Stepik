weights = [1, 2, 4, 8, 16, 32, 64]
target = int(input())

result = []
for weight in reversed(weights):
    while target >= weight:
        result.append(weight)
        target -= weight

print(result)
