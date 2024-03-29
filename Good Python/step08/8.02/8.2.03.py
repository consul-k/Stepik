flag = []

n = int(input())

for i in range(n):
    row = []
    for j in range(n):
        if j < (n//2):
            row.append(1)
        else:
            row.append(0)
    flag.append(row)
    
for i in flag:
    print(*i)
