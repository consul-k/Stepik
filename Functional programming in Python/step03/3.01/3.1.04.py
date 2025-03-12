def is_palindrome(string):
    if string.replace(' ', '').lower() == string.replace(' ', '').lower()[::-1]:
        return True
    else:
        return False
