num1 = int(input())
num2 = int(input())

operation = input()

if operation == '+':
    result = num1 + num2
    print(result)
elif operation == '-':
    result = num1 - num2
    print(result)
elif operation == '*':
    result = num1 * num2
    print(result)
elif operation == '/':
    if num2 == 0:
        print("На ноль делить нельзя!")
    else:
        result = num1 / num2
        print(result)
else:
    print("Неверная операция")
