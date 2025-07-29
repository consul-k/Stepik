n = int(input())

prices = []
for i in range(n):
    price = float(input())
    prices.append(price)

discounted_prices = list(map(lambda x: round(x * 0.9, 2), prices))

print(discounted_prices)
