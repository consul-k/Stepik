a = list(map(int, input().split()))
for i in a:
    for j in range(i):
        print('*',end='')
    print()
