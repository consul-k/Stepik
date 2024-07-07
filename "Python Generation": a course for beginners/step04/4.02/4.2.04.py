n = int(input())
if (n >= 1000 and n <= 9999) and (n % 7 == 0 or n % 17 == 0):
    print('YES')
else:
    print('NO')
