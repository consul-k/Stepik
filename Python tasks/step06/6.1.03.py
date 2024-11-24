a = int(input())
b = int(input())
c = int(input())

count = 0
for x in range(c // a + 1):
    remaining = c - x * a
    if remaining >= 0 and remaining % b == 0:
        count += 1

print(count)
