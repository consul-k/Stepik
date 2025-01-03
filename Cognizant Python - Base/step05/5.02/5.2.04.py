text = input()

words = text.split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

sorted_word_count = dict(sorted(word_count.items()))

print(sorted_word_count)
