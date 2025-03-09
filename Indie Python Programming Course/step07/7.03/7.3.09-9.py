def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

def trailing_zeros(n):
    fact = factorial(n)
    count = 0
    while fact % 10 == 0:
        count += 1
        fact //= 10
    return count
