res = {}

for i in d.keys():
    if d[i] > threshold:
        res[i] = d[i]
print(res)
