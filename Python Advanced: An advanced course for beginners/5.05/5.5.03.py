n = int(input())

profits = [1, 1, 1]

if n <= 3:
    print(' '.join(str(profits[i]) for i in range(n)))
else:
    for i in range(3, n):
        next_profit = profits[i-1] + profits[i-2] + profits[i-3]
        profits.append(next_profit)
    print(' '.join(map(str, profits)))
