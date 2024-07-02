def strange_sorter(text):
    words = set(text.split())
    sorted_words = sorted(words, key=lambda x: (-len(x), x))
    return sorted_words
