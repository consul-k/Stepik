n = int(input())
res = 0
for i in range(n+1):
    if i%5==0 and i%3!=0:
        res += i

print(res)
