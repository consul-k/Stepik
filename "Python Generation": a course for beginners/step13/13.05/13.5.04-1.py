# объявление функции
def convert_to_python_case(text):
    result = []
    for i, char in enumerate(text):
        if char.isupper():
            if i > 0:
                result.append('_')
            result.append(char.lower())
        else:
            result.append(char)
    return ''.join(result)

txt = input()

print(convert_to_python_case(txt))
