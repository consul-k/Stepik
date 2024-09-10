s1 = input()
s2 = input()
comp = set(s1+s2)
c = []

for i in range(10):
    c.append(str(i))

if set(c) == comp:
    print('YES')
else:
    print('NO')
