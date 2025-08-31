text = input()

words = text.split()

longest_word = max(words, key=len)

print(longest_word)
