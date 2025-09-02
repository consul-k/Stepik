n = int(input())

positive = []
negative = []

for _ in range(n):
    profit = int(input())
    if profit > 0:
        positive.append(profit)
    elif profit < 0:
        negative.append(profit)

print(' '.join(map(str, positive)))
print(' '.join(map(str, negative)))
