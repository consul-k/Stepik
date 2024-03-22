num = int(input())
binary = ""

while num > 0:
    binary = str(num % 2) + binary
    num //= 2

print(binary)
