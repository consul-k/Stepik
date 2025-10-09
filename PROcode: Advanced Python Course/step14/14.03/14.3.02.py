import json

data = json.loads(input())
count = 0
for key, value in data.items():
    print(f'Модуль: {key}, количество: {value}')
    count += value
print(f'Всего модулей: {count}')
