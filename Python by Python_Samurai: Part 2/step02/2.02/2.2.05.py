a = input()
res = {letter:a.count(letter) for letter in a if letter.isalpha()}
print(res)
