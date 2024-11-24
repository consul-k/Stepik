n = int(input())

base_7 = ''
is_negative = n < 0
n = abs(n)

if n == 0:
    base_7 = '0'
else:
    while n > 0:
        base_7 = str(n % 7) + base_7
        n //= 7

if is_negative:
    base_7 = '-' + base_7

print(base_7)
