text = input().replace(' ','').replace(',','')
text = text.upper()
if text == text[::-1]:
    print('Тайна разгадана')
else:
    print('Тайна не разгадана')
