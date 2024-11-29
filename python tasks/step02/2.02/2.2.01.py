l = []
res = []

for _ in range(int(input())):
    l.append(int(input()))

for i in l:
    if l.count(i) > 1 and i not in res:
        res.append(i)
print(*sorted(res))
