n = int(input())

current_number = 1

for i in range(1, n + 1):
    for j in range(i):
        print(current_number, end=' ')
        current_number += 1
    print()
