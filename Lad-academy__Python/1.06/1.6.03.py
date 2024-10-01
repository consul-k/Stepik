x = int(input())
a, b = 1, 1

for i in range(1, x + 1):
    print(a, end = ' ')
    a, b = b, a + b
