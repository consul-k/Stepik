data = input()

stones = data.split(',')

stone_power = {}

for stone in stones:
    stone = stone.strip()
    stone_type, power = stone.rsplit(' ', 1)
    power = int(power)

    if stone_type in stone_power:
        stone_power[stone_type] += power
    else:
        stone_power[stone_type] = power
      
for stone_type, total_power in stone_power.items():
    print(f"Общая сила {stone_type} камень: {total_power}")
