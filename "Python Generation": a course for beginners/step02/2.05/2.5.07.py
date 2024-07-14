n = input()
a = 0
b = 1
for i in n:
    a += int(i)
    b *= int(i)
print(f'Сумма цифр = {a}')
print(f'Произведение цифр = {b}')
