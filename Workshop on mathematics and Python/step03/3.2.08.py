def front_x(words):
    x_words = []
    other_words = []

    for word in words:
        if word.startswith('x'):
            x_words.append(word)
        else:
            other_words.append(word)

    x_words.sort()
    other_words.sort()
    return x_words + other_words
