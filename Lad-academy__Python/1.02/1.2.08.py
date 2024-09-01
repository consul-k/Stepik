n = int(input())
if 10 <= n < 100 and (n // 10) % 2 == 0 and (n % 10) % 2 == 0:
    print('YES')
else:
    print('NO')
