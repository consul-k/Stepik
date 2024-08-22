phone = {'1':['.',',','?','!',':'],
        '2':['A','B','C'],
        '3':['D','E','F'],
        '4':['G','H','I'],
        '5':['J','K','L'],
        '6':['M','N','O'],
        '7':['P','Q','R','S'],
        '8':['T','U','V'],
        '9':['W','X','Y','Z'],
        '0':[' ']}

text = [str(i) for i in input().upper()]

for s in text:
     for key, value in phone.items():
            if s in value:
                p = value.index(s)
                print(key * (p + 1), end='')
