n=int(input())
p=[]
l=[]
for i in range(n):
    i=int(input())
    p.append(i)
p.sort()
d=p[1]-p[0]
for j in range(len(p)-1):
    if p[j+1]-p[j]==d:
        l.append('+')
    else:
        l.append('-')
if '-' not in l:
    print('YES')
else:
    print('NO')
