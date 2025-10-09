import json

obj = json.loads(input())
print(f'Артефакт {obj["id"]} содержит {len(obj["components"])} компонента(ов).')
json_data = json.dumps(obj, indent=4)
print(json_data)
