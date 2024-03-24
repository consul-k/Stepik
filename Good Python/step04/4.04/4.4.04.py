n = int(input())
n, d = str(n), int(n)
if d < 0:
    print('NO')
elif len(n) <= 4 and '9' in n and '3' in n:
    print('YES')
else:
    print('NO')
