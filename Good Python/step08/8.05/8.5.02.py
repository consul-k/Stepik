n=int(input())
m=int(input())
matrix=[[0 for i in range(m)] for _ in range(n)]
count =1
for i in range(n):
    for j in range(m):
        matrix[i][j] += count
        count+=1
for i in range(n):
    if i%2==0:
        print(*matrix[i])
    else:
        matrix[i].reverse()
        print(*matrix[i])
