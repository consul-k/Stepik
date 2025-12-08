message = input()

words = message.lower().split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

for i in range(min(3, len(sorted_words))):
    word, count = sorted_words[i]
    print(f"{word} {count}")
