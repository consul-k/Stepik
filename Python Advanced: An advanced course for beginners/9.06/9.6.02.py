s = input()

digits = sorted({ch for ch in s if ch.isdigit()})
letters = sorted({ch for ch in s if ch.isalpha()})

print(f'Уникальные цифры: {{{", ".join(digits)}}}')
print(f'Уникальные буквы: {{{", ".join(letters)}}}')
