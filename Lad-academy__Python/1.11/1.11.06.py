def bank(a, years):
    for _ in range(years):
        a += a * 0.1
    return int(a)

data = list(map(int, input().split()))
print(bank(data[0], data[1]))
