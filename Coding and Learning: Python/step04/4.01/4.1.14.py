phrase = input()
words = 1
i = 0

while i < len(phrase):
    if phrase[i] == " ":
        words += 1
    i += 1

print(words)
