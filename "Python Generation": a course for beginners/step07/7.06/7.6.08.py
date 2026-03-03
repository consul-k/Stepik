n = input().strip()

even_digits = []
for digit in n:
    if int(digit) % 2 == 0:
        even_digits.append(digit)

if not even_digits:
    print("Четных цифр в числе нет")
else:
    for i, digit in enumerate(even_digits, 1):
        print(f"{i}-я четная цифра равна {digit}")
