n = int(input())
prices = [int(input()) for _ in range(n)]
x = int(input())

result = [price for price in prices if price > x]

print(*result)
