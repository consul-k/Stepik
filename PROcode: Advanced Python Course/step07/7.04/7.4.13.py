mapping = {
    '1': '.,!?:', '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL',
    '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ', '0': ' '
}

char_to_keys = {}
for key, chars in mapping.items():
    for i, char in enumerate(chars):
        char_to_keys[char] = key * (i + 1)

text = input()

result = []
for char in text.upper():
    if char in char_to_keys:
        result.append(char_to_keys[char])

print(''.join(result))
