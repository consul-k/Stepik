sizes = list(map(int, input().split()))

energy_levels = {size ** 2 for size in sizes}

large_crystals = {size for size in sizes if size % 2 == 0 and size > 10}

unique_digits = {int(digit) for size in sizes for digit in str(size)}

print(f"Энергетические уровни: {{{', '.join(map(str, sorted(energy_levels)))}}}")
print(f"Крупные кристаллы: {{{', '.join(map(str, sorted(large_crystals)))}}}")
print(f"Уникальные цифры: {{{', '.join(map(str, sorted(unique_digits)))}}}")
