morse_ru_reverse = {
    '.-': 'А', '-...': 'Б', '.--': 'В', '--.': 'Г', '-..': 'Д', '.': 'Е',
    '...-': 'Ж', '--..': 'З', '..': 'И', '.---': 'Й', '-.-': 'К', '.-..': 'Л',
    '--': 'М', '-.': 'Н', '---': 'О', '.--.': 'П', '.-.': 'Р', '...': 'С',
    '-': 'Т', '..-': 'У', '..-.': 'Ф', '....': 'Х', '-.-.': 'Ц', '---.': 'Ч',
    '----': 'Ш', '--.-': 'Щ', '--.--': 'Ъ', '-.--': 'Ы', '-..-': 'Ь',
    '..-..': 'Э', '..--': 'Ю', '.-.-': 'Я', '-.-.-': ' '
}

def decode_morse(morse_code):
    words = morse_code.strip().split('   ')
    decoded_words = []

    for word in words:
        symbols = word.strip().split()
        decoded_letters = []
        for symbol in symbols:
            letter = morse_ru_reverse.get(symbol, '?')
            decoded_letters.append(letter)
        decoded_words.append(''.join(decoded_letters))

    return ' '.join(decoded_words)

encoded = input()
print(decode_morse(encoded))
