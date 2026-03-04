n = input()

max_digit = int(n[0])
min_digit = int(n[0])

i = 1
while i < len(n):
    current_digit = int(n[i])
    if current_digit > max_digit:
        max_digit = current_digit
    if current_digit < min_digit:
        min_digit = current_digit
    i += 1
    
print(f"Максимальная цифра равна {max_digit}")
print(f"Минимальная цифра равна {min_digit}")
