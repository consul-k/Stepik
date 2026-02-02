n = int(input())
encoded = input()

result = []
for char in encoded:
    if char.isalpha():
        shifted = ord(char) - n
        if shifted < ord('a'):
            shifted += 26
        result.append(chr(shifted))
    else:
        result.append(char)

print(''.join(result))
