def get_words_with_position(words):
    return [(j,i) for i,j in enumerate(words.split(), start=1)]
