n = int(input())
phrases = [input().split() for _ in range(n)]

word_counts = {}
for phrase in phrases:
    for word in phrase:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1

result = sum(1 for count in word_counts.values() if count == n)
print(result)
