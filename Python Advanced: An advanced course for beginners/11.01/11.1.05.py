def lex_min(a, b):
    return a if a < b else b

def lex_min3(a, b, c):
    return lex_min(lex_min(a, b), c)

def lex_min4(a, b, c, d):
    return lex_min(lex_min3(a, b, c), d)
