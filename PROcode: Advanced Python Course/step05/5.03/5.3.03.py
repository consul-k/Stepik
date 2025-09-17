bandits = ("Vitorio Zanzara", "Джек", "Dagdarion Dark", "Артур", "Алекс Глозман", "Рик", "Dark Horse")

name = input()
if name in bandits:
    print(f'{name} в сборе!')
else:
    print(f'{name} не найден в списке!')
