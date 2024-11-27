def prime(number):
    n = number
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
    return 1 if counter == 2 else 0

print(prime(int(input())))
