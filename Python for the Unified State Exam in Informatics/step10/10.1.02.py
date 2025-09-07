def factorial(x):
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

n = int(input())
total = 0

for i in range(1, n + 1):
    total += factorial(i)

print(total)
