res = []
word = input()
while word != 'стоп' and word != 'хватит' and word != 'достаточно':
    res.append(word)
    word = input()
print(len(res))
