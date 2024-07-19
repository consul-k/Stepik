a = int(input())
b = int(input())
a1 = int(input())
b1 = int(input())
if (abs(a-a1) == 1 and abs(b-b1) == 2) or (abs(a-a1) == 2 and abs(b-b1) == 1):
    print('YES')
else:
    print('NO')
