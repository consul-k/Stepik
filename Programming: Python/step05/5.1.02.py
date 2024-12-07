s = input()
for c in s:
    if c.isdigit():
        print('Цифра')
        break
else:
    print('Цифр нет')
