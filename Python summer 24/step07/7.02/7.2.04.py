def get_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return len(factors)

print(get_factors(int(input()))) 
