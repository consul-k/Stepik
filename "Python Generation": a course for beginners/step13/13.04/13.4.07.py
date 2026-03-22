def get_unique(numbers):
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result

numbers = eval(input())

print(get_unique(numbers))
