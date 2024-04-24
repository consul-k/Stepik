a, b = map(float, input().split())
s = input()
if s == '+':
    print(a + b)
elif s == '-':
    print(a - b)
elif s == '*':
    print(a * b)
elif s == '/':
    if b == 0:
        print('Некорректная операция')
    else:
        print(a / b)
else:
    print('Некорректная операция')
