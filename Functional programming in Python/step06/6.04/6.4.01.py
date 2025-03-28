def filter_numbers(numbers):
    return list(filter(lambda x: x%2==0 or abs(x)>100, numbers))
