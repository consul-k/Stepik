def generate_dict_from_even_indices(input_string):
    numbers = list(map(int, input_string.split(',')))

    result_dict = {i: numbers[i] for i in range(len(numbers)) if i % 2 == 0}

    return result_dict

input_string = input()
result = generate_dict_from_even_indices(input_string)
print(result)
