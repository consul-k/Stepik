n = int(input())

is_composite = False

for i in range(2, n):
    if n % i == 0:
        is_composite = True
        break

if is_composite:
    print("Составное")
else:
    print("Простое")
