text = input()

char_positions = {}

for index, char in enumerate(text):
    if char in char_positions:
        char_positions[char].append(index)
    else:
        char_positions[char] = [index]

print(char_positions)
