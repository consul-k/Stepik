def analyze_text(text):
    words = text.split()
    unique_words = set(words)
    sorted_unique = sorted(unique_words)
    return len(unique_words), sorted_unique
