def gen_factorial():
    factorial = 1
    i = 1
    while True:
        factorial *= i
        yield factorial
        i += 1
