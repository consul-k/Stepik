a = input()
i = 0
res = 0

while i < len(str(a)):
    res += int(str(a[i]))
    i += 1
print(f'Сумма цифр числа: {res}')
