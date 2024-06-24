s = 0
for i in range(1000, int(input())):
    if i % 400 == 0 or (i % 4 == 0 and i % 100 != 0):
        s += 1
print(s)
