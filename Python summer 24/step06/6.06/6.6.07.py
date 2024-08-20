a = list(map(int, input().split()))
res = []
for i in a:
    if i%2 == 0:
        if i**2%10!=4:
            res.append(i**2)
print(*res)
