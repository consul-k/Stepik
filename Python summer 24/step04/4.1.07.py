m, p, n = int(input()), int(input()), int(input())
for i in range(1, n + 1):
    print(i, float(m))
    m += m * (p / 100)
