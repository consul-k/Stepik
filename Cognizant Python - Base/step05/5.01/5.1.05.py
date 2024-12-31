def count_repeated_words(text):
    words = text.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    repeated_words = [word for word, count in word_count.items() if count > 1]

    return len(repeated_words)

# Пример использования
text = input()
result = count_repeated_words(text)
print(result)
