def sum_numbers(data):
    total = 0
    for item in data:
        if isinstance(item, (int, float)):
            total += item
    return total

result = sum_numbers(data)
print(result)
