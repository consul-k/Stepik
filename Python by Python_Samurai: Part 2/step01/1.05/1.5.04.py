n, m = map(int, input().split())
lst = []

for i in range(n):
    s = []
    for j in range(m):
        s.append('?')
    lst.append(s)

print(lst)
