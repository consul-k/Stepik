def is_pangram(s: str):
    alpha = set('abcdefghijklmnopqrstuvwxyz')
    return alpha <= set(s.lower())
