s = float(input())
p = float(input())
n = int(input())
for _ in range(n - 1):
    s += s * (p / 100)

print("%.3f" % s)
