def get_letters(string):
    return list(map(lambda x: (x[0].upper(), x[0].lower()), string))
