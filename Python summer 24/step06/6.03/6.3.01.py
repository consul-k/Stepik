n = int(input())
res = []
for _ in range(n):
    res.append(int(input()))
for i in res:
    print(i)
print()
for j in res:
    print(j**2+2*j+1)
