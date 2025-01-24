test1 = '''
data = {'велосипед': 10, 'самокат': 20, 'мопед': 30}
with open('magazine.txt', 'w', encoding='utf-8') as file:
    for key, value in data.items():
        file.write(f'{key} = {value}\n')
'''
