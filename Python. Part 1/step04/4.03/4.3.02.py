a = float(input())
b = float(input())
op = input()
if op == '+':
    print(f"Результат: {a+b}")
elif op == '-':
    print(f"Результат: {a-b}")
elif op == '*':
    print(f"Результат: {a*b}")
elif op == '/':
    if b == 0:
        print("Ошибка: Деление на ноль невозможно.")
    else:
        print(f"Результат: {a/b}")
