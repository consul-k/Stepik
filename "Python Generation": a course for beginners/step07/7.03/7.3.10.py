check = True
for i in range(10):
    i = int(input())
    if i%2 != 0:
        check = False
        break
if check:
    print('YES')
else:
    print('NO')
