import string

def count_unique_words(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    unique_words = set(words)
    return len(unique_words)

input_text = input()
print(count_unique_words(input_text))
