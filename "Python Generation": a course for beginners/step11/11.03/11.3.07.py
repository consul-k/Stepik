res = []
for _ in range(int(input())):
    res.append(int(input()))
del res[1::2]
print(res)
