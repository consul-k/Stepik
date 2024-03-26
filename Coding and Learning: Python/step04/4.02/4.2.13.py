a = input()
letters = 0
digits = 0

for i in a:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1
        
print(f'Letters: {letters}\nDigits: {digits}')
