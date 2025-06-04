# Список оружия
weapons = ['нож', 'пистолет', 'дробовик', 'мачете']

# Ниже напишите код
w1 = []
other = []

for i in range(7):
    i = input()
    if i in weapons:
        w1.append(i)
    else:
        other.append(i)
        
print('Оружие:', w1)
print('Другие предметы:', other)
