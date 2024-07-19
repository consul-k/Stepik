n = int(input())
if n%2 == 0 and n > 20:
    print('NO')
elif n%2 == 0 and n in range(6,21):
    print('YES')
elif n%2 == 0 and n in range(2,6):
    print('NO')
elif n%2!=0:
    print('YES')
