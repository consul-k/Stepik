n = int(input())

max1 = int(input())
max2 = int(input())

if max2 > max1:
    max1, max2 = max2, max1

for _ in range(n - 2):
    num = int(input())
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num

print(max1)
print(max2)
