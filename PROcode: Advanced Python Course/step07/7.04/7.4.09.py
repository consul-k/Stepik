n = int(input())

phonebook = {}

for _ in range(n):
    number, name = input().split()
    name_lower = name.lower()
    
    if name_lower not in phonebook:
        phonebook[name_lower] = []
    
    phonebook[name_lower].append(number)

m = int(input())

for _ in range(m):
    query = input().lower()
    
    if query in phonebook:
        print(' '.join(phonebook[query]))
    else:
        print('абонент не найден')
