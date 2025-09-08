from math import sqrt

n = int(input())
res = 0

for i in range(1,n+1):
    res += sqrt(i)
    
print(res)
