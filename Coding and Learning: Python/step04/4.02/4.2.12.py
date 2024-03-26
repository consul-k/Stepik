input_str = input()
words = input_str.split()

longest_word = max(words, key=len)
print(longest_word)
