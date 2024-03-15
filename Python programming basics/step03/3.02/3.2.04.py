n = int(input(""))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True
    
if is_prime(n):
    print(f'Число {n} составное')
else:
    print(f'Число {n} простое')
