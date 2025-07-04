def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input())
num2 = int(input())

result = gcd(num1, num2)

print("Наибольший общий делитель чисел равен:", result)
