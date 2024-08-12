a = list(range(10))
s1 = {int(i) for i in input()}
s2 = {int(i) for i in input()}
for i in a:
    if i not in s1.union(s2):
        print('NO')
        break
else:
    print('YES')
