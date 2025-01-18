test1 = '''
with open('people_names.txt', encoding='utf-8') as names:
    my_list = [line.strip() for line in names]
    print(my_list)
'''
