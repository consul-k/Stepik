n = int(input())
prices = []
for _ in range(n):
  prices.append(int(input()))

min_price = min(prices)
max_price = max(prices)

print(min_price + max_price)
