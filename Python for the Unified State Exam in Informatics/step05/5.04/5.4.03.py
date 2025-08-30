h = 0
for x in range(1000 // 11):
    for y in range(1000 // 20):
        if 11 * x + 20 * y == 1000:
            j = x + y
            h += j
print(h)
