a = [i for i in input() if i.isdigit()]
b = {i for i in a if a.count(i)>=2}
if not b:
    print('NO')
else:
    print(*sorted(list(b)))
