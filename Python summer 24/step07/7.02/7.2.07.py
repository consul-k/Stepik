def arithmetic(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Деление на ноль невозможно"
    else:
        return "Неизвестная операция"

a = int(input())
b = int(input())
operation = input()

print(arithmetic(a, b, operation))
