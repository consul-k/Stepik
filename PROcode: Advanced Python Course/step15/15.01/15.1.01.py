text = input().strip().lower()

russian_vowels = "аеёиоуыэюя"
english_vowels = "aeiou"
all_vowels = russian_vowels + english_vowels

count = 0
for char in text:
    if char in all_vowels:
        count += 1

print(count)
