a = int(input())
b = int(input())
min = b + 1
for i in range(a, b + 1):
    if i % 12 == 0 and i % 14 == 0 and i < min:
        min = i
print(min)
