test1 = '''
with open('people_names.txt', encoding='utf-8') as names:
    print(names.readline(), end='')
    print(names.readline(), end='')
    names.seek(0)
    print(names.readline(), end='')
'''
