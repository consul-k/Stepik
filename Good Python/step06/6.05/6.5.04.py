text = input()
n = int(len(text) / 2)
print(text[:n].capitalize(), text[n:].capitalize(), sep='')
