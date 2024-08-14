def number_to_words(number):
    digit_to_word = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }

    number_str = str(number)
    words = [digit_to_word[digit] for digit in number_str]
    return ' '.join(words)

number = input()

print(number_to_words(number))
