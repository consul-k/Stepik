def process_symbols(input_string):
    symbols = tuple(input_string.split())

    sun_count = symbols.count('☀️')

    unique_index = -1
    for idx, symbol in enumerate(symbols):
        if symbols.count(symbol) == 1:
            unique_index = idx
            break

    return (sun_count, unique_index)

input_str = input()
result = process_symbols(input_str)
print(result)
