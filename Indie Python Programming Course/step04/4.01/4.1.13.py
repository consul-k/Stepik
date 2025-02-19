n, m = map(int, input().split())
days = n
while n >= m:
    days += 1
    n -= m
    n += 1
print(days)
