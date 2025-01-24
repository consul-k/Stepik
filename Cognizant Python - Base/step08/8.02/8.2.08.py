test1 = '''
new_data = {'вертолёт': 40, 'поезд': 50, 'катер': 60}
with open('magazine.txt', 'a', encoding='utf-8') as file:
    for key, value in new_data.items():
        file.write(f'{key} = {value}\n')
'''
