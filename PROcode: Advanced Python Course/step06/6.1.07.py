def process_letters(input_string):
    letters = tuple(input_string.split())

    letter_list = list(letters)

    unique_letters = list(set(letter_list))
    removed_count = len(letter_list) - len(unique_letters)

    unique_letters.sort()

    result_tuple = tuple(unique_letters)

    print(result_tuple)
    print(removed_count)

input_str = input()
process_letters(input_str)
