a, b = input(), input()
a1 = {}
b1 = {}
for i in a:
    a1[i] = a.count(i)
for i in b:
    b1[i] = b.count(i)
if a1 == b1:
    print('YES')
else:
    print('NO')
