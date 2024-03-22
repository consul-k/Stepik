n = int(input())
res = 1
if n == 0:
    print(0)
else:
    for i in range(n):
        i = int(input())
        res *= i
    print(res)
