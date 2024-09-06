a = int(input())
b = int(input())
res = 0

for i in range(a, b+1):
    if 10 <= i <= 99 and i%2 == 0 and ((i//10) + (i%10) < 12):
        res += i
print(res)
