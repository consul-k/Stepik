a = int(input())
b = int(input())
a1 = int(input())
b1 = int(input())
if (a==a1 and b!=b1) or (a!=a1 and b==b1) or abs(a-a1) == abs(b-b1):
    print('YES')
else:
    print('NO')
