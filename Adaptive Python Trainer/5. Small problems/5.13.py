text = input().split()
res = dict()

for word in text:
    l = len(word)
    if l in res:
        res[l] += 1
    else:
        res[l] = 1

for k in sorted(res.keys()):
    print(f'{k}: {res[k]}')
