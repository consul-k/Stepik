n = int(input())
m = int(input())
mult = []

for i in range(n):
    p = []
    for j in range(m):
        p.append(i * j)
    mult.append(p)

for i in mult:
    for j in i:
        print(str(j).ljust(3), end = ' ')
    print()
