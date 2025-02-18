a, b = float(input()), float(input())
s = input()
if s == '+' or s == '-' or s == '*' or s == '/':
    if s == '+':
        print(a + b)
    elif s == '-':
        print(a - b)
    elif s == '*':
        print(a * b)
    elif s == '/':
        if b == 0:
            print('Неизвестно')
        else:
            print(a / b)
else:
    print('Неизвестно')
