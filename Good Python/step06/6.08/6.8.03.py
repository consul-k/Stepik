def replace_vowels(s):
    vowels = ['а', 'о', 'у', 'э', 'ы', 'и', 'е', 'ё', 'я', 'ю']
    s_copy = ""
    for char in s:
        if char.lower() in vowels:
            s_copy += 'у'
        else:
            s_copy += char
    return s_copy
s = input()
print(replace_vowels(s))
