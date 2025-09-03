a = input()

for char in ',.?!;:':
    a = a.replace(char, '')

words = a.split()

max_length = 0
longest_word = ''

for word in words:
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word

print(longest_word)
