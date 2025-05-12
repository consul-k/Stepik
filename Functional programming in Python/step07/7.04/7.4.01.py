def sum_recursive(nested_list):
    total = 0
    for element in nested_list:
        if isinstance(element, list):
            total += sum_recursive(element)  # Рекурсивный вызов для вложенного списка
        elif isinstance(element, int):
            total += element  # Суммируем целые числа
    return total
