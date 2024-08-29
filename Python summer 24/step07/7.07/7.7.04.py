def palindrome(data):
    data = data.replace(' ','').lower()
    return 'TRUE' if data == data[::-1] else 'FALSE'

print(palindrome(input()))
