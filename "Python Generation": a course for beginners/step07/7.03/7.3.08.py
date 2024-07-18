n = int(input())
res = 1
for i in range(2, n+1):
    if n == 1:
        break
    else:
        if i % 2 == 0:
            res -= i
        else:
            res += i
print(res)
