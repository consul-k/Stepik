a = [i for i in input().split()]
if set(a[0]) == set(a[1]) and set(a[1]) == set(a[2]):
    print('YES')
else:
    print('NO')
