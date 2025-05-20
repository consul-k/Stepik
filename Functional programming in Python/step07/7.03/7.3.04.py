def is_palindrome(word):
    word = word.lower()  # игнорируем регистр
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])
