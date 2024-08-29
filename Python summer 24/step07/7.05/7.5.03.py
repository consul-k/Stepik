def c_v(text):
    vowels = 'аеёиоуыэюя'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

text = input().lower()
print(c_v(text))
