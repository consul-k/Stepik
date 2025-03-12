def create_palindrome(string):
    if string.lower() == string.lower()[::-1]:
        return string.lower()
    else:
        return f'{string.lower()}_i_{string.lower()[::-1]}'
