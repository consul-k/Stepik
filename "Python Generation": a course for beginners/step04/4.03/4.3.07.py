a = input()
b = input()
colors = ['красный', 'синий', 'зеленый', 'желтый']
if a not in colors or b not in colors:
    print('ошибка цвета')
elif (a == 'красный' and b == 'синий') or (b == 'красный' and a == 'синий'):
    print('фиолетовый')
elif (a == 'красный' and b == 'желтый') or (b == 'красный' and a == 'желтый'):
    print('оранжевый')
elif (a == 'синий' and b == 'желтый') or (b == 'синий' and a == 'желтый'):
    print('зеленый')
elif a == b:
    print(a)
