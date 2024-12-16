zero = 0
plus = 0
minus = 0

for _ in range(int(input())):
    i = int(input())
    if i == 0:
        zero += 1
    elif i > 0:
        plus += 1
    else:
        minus += 1
        
print(zero, plus, minus)  
