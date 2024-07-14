import re

def is_palindrome(text):
    text = text.lower()
    cleaned_text = re.sub(r'[^a-zа-яё]', '', text)
    return cleaned_text == cleaned_text[::-1]

txt = input()

print(is_palindrome(txt))
