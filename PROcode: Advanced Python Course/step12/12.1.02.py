def загрузить_груз(**kwargs):
    data = []
    
    for key, value in kwargs.items():
        number_str = ""
        for char in key:
            if char.isdigit():
                number_str += char

        data.append((int(number_str), value))
    
    data.sort()
    
    result_lines = []
    for num, content in data:
        result_lines.append(f'Контейнер {num}: {content}')
    
    return "\n".join(result_lines)
