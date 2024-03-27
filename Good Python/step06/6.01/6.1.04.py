a = input()
if len(a)%2==0:
    print('Нет центрального символа')
else:
    middle_index = len(a) // 2
    middle_symbol = a[middle_index]
    print(middle_symbol)
