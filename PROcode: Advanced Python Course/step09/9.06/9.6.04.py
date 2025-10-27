code = input().strip()

unique_digits = sorted(set(int(char) for char in code))

sums_set = set()
for i in range(len(unique_digits)):
    for j in range(i + 1, len(unique_digits)):
        sums_set.add(unique_digits[i] + unique_digits[j])
sums_set = sorted(sums_set)

squares_set = sorted([digit * digit for digit in unique_digits if digit > 5])

print(f"Уникальные цифры кода: {{{', '.join(map(str, unique_digits))}}}")
print(f"Возможные суммы двух цифр: {{{', '.join(map(str, sums_set))}}}")
print(f"Квадраты цифр > 5: {{{', '.join(map(str, squares_set))}}}")
