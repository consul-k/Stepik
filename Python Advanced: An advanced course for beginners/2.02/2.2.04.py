def determine_type(token):
    if token.startswith('"') and token.endswith('"'):
        return "str"
    if token == "True" or token == "False":
        return "bool"
    try:
        int(token)
        return "int"
    except:
        pass
    try:
        float(token)
        return "float"
    except:
        pass
    return "Неверный тип данных"

# Ввод
input_str = input()
tokens = input_str.split()

# Вывод типов
for token in tokens:
    print(determine_type(token))
