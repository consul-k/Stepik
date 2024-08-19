text = input()

first_h = text.find('h')

last_h = text.rfind('h')
result = text[:first_h] + text[last_h+1:]

print(result)
