def filter_words(lst):
    return list(filter(lambda x: len(x) == 4 or x.startswith('S'), lst))
