n = int(input())
res = 0
while n != 0:
    if 100 <= n <= 999:
        res += n
    n = int(input())
print(res)
