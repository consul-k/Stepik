a = list(map(int, input().split()))
k = int(input())
res = []
for i in a:
    if i % k != 0:
        res.append(i)
for j in sorted(res):
    print(j)
