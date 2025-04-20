def gen_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        yield factorial
