n = int(input())
if (n < 10 or n > 100) or (n//10 + n%10 <= 10):
    print('NO')
else:
    print('YES')
