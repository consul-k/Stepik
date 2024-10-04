def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_next_prime(num):
    i = num + 1
    while True:
        if is_prime(i):
            return i
        i += 1

n = int(input())

print(get_next_prime(n))
