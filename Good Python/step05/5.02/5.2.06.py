b = int(input())
n = int(input())
ans = 0
for i in range(len(str(n))):
    ans += b ** i * (n % 10)
    n //= 10
print(ans)
