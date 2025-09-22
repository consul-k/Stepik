import ast

input_data = input().strip()

ants = ast.literal_eval(input_data)

res = []
for i in ants:
    if i['phone'][-1] == '1':
        res.append(i['name'])
        
print(*sorted(res))
