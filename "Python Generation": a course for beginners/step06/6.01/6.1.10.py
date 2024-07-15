number = int(input())

a = number // 100
b = (number // 10) % 10
c = number % 10

digits = sorted([a, b, c])

if digits[2] - digits[0] == digits[1]:
    print("Число интересное")
else:
    print("Число неинтересное")
