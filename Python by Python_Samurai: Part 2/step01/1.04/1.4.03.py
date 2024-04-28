a = list(map(int, input().split()))
m = a[0]
s = [0, a[0]]
for i, v in enumerate(a):
    if v < m:
        m = v
        s = [i, v]
print(s[0])
