n = int(input())

if n == 0:
    print(0)
else:
    binary_digits = []
    while n > 0:
        binary_digits.append(str(n % 2))
        n //= 2
    
    binary = ''.join(reversed(binary_digits))
    print(binary)
