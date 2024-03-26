A, B = map(int, input().split())

res = 1

for i in range(A, B+1):
    res *= i
    
print(res)
