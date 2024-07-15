res = []
for _ in range(3):
    res.append(int(input()))
res = sorted(res, reverse=True)
for n in res:
    print(n)
