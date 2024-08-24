res = []
for _ in range(int(input())):
    res.append(int(input()))
res.remove(max(res))
res.remove(min(res))
for n in res:
    print(n)
