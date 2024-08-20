matrix = []
s = []

for i in range(int(input())):
    matrix.append(input().split())
    
for i in range(len(matrix)):
    s.append(int(matrix[i][i]))
    
print(sum(s))
