a = int(input())
b = int(input())
a1 = int(input())
b1 = int(input())
if ((a + b) % 2 == 0 and (a1 + b1) % 2 == 0) or ((a + b) % 2 != 0 and (a1 + b1) % 2 != 0):
    print('YES')
else:
    print('NO')
