text = input()

first_h_index = text.find('h')
last_h_index = text.rfind('h')

before_h = text[:first_h_index + 1]
middle_h = text[first_h_index + 1:last_h_index]
after_h = text[last_h_index:]

reversed_middle_h = middle_h[::-1]

result = before_h + reversed_middle_h + after_h

print(result)
