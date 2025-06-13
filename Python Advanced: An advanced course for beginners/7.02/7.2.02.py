hunters_power = {
    "Джин": 85,
    "Дон": 90,
    "Сим": 88,
    "Андрей": 70,
    "Богги": 95,
    "Кастиель": 95,
    "Ребекка": 80,
    "Люцифер": 100,
    "Микаэль": 98,
    "Габриэль": 92
}

name = input()
if name not in hunters_power:
    print("Такой охотник не найден в архиве.")
else:
    print(f'Уровень силы {name}: {hunters_power[name]}')
