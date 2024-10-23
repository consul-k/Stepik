def convert_to_python_case(text):
    result = []
    for char in text:
        if char.isupper():
            if result:
                result.append('_')
            result.append(char.lower())
        else:
            result.append(char)
    return ''.join(result)

input_text = input()
output_text = convert_to_python_case(input_text)
print(output_text)
