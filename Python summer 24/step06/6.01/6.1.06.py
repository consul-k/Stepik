n = int(input())
res = []
for _ in range(n):
    res.append(int(input()))
print(*res[::-1])
