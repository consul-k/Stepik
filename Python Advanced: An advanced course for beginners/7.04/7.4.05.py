signal = input()

words = signal.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

max_count = max(frequency.values())
most_frequent_words = [word for word, count in frequency.items() if count == max_count]
result = max(most_frequent_words)

print(result)
