a, b = map(int, input().split())
time = a
while a >= b:
    time += 1
    a -= b
    a += 1
print(time)
