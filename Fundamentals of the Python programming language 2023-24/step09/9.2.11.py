def counter(text):
    words = text.split()
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    result = [(count, word) for word, count in word_counts.items()]
    result.sort(key=lambda x: (x[0], x[1]))

    return result
