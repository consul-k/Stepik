bandits = ("Vitorio Zanzara", "Джек", "Dagdarion Dark", "Артур", "Алекс Глозман", "Рик", "Dark Horse")

n = int(input())
s = 0

if n % len(bandits) == 0:
    print(f'Каждый бандит получит: {n // len(bandits)} монет.')
else:
    print('Общая сумма добычи не делится поровну между бандитами.')
