book1 = input().strip()
book2 = input().strip()

def parse_book(s):
    spells = {}
    pairs = s.split(',')  # Разделяем по запятым
    for pair in pairs:
        if ':' in pair:
            name, power = pair.split(':', 1)  # Разделяем только по первому двоеточию
            spells[name.strip()] = int(power.strip())
    return spells

dict1 = parse_book(book1)
dict2 = parse_book(book2)

if dict1 == dict2:
    print("Книги идентичны")
else:
    print("Книги отличаются")
