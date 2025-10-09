data = input().strip()

pairs = data.split(',')

magic_keys = {}

for pair in pairs:
    code_part, name_part = pair.split(':', 1)
    code = int(code_part.strip())
    name = name_part.strip().strip('"').strip()
    magic_keys[code] = name

print(f"Сумма всех ключей: {sum(magic_keys.keys())}")
print(f"Минимальный ключ: {min(magic_keys.keys())}")
print(f"Максимальный ключ: {max(magic_keys.keys())}")
