res = 0
n = int(input())
for _ in range(n):
    i = int(input())
    if (i//10)*(i%10) > 35:
        res += i
print(res)
