n = input()
i = 0

while i < len(n)-1:
    if n[i] != n[i+1]:
        print('NO')
        break
    i+=1
else:
    print('YES')
