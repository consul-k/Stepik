num = int(input())

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Составное")
            break
    else:
        print("Простое")
else:
    print("Составное")
