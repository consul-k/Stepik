count = 0
for a1 in range(10):
    for a2 in range(10):
        for a3 in range(10):
            for a4 in range(10):
                if a1 % 2 + a2 % 2 + a3 % 2 + a4 % 2 == 2:
                    count += 1
print(count)
