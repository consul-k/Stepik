a = int(input())
b = int(input())
op = input()
if op == '/' and b == 0:
    print('На ноль делить нельзя!')
elif op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
else:
    print('Неверная операция')
