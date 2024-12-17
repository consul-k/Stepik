input_string = input().lower()

vowels = "аеёиоуыэюя"
consonants = "бвгджзйклмнпрстфхцчшщ"

vowel_count = 0
consonant_count = 0

for char in input_string:
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonant_count += 1

print(f"Гласных - {vowel_count}")
print(f"Согласных - {consonant_count}")
