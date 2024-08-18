n = int(input())
res = [1]

for i in range(2, n+1):
    if n%i == 0:
        res.append(i)
print(*res)
