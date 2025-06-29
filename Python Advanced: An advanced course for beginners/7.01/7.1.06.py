import ast

# Вводим строку с данными
input_data = input().strip()

# Преобразуем строку в список словарей
ants = ast.literal_eval(input_data)

# далее ваш код
res = []
for i in ants:
    if i['phone'][-1] == '1':
        res.append(i['name'])
        
print(*sorted(res))
