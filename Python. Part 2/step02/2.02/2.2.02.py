res = []
for i in matrix:
    s = 0
    for j in i:
        s += j
    res.append(s)
print(res)
