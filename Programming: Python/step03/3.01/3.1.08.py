a = int(input())
b = int(input())
if a % b == 0:
    print('YES')
    print(a//b)
else:
    print('NO')
    print(int(a/b))
    print(a%b)
