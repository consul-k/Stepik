'''

Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter, 
где Letter – заглавная буква английского алфавита, Number – число от 0 до 99 (включительно).

Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный почтовый индекс Латверии.

Примечание 1. Пример правильного (неправильного) индекса Латверии:

AB23_56VG          # правильный
V3F_231GT          # неправильный

Примечание 2. Обратите внимание на символ _ в почтовом индексе.

Примечание 3. Вызывать функцию generate_index() не нужно, требуется только реализовать.

'''

def generate_index():
    import random
    import string
    post = ''
    letter = ''
    number = []
    for i in range(4):
        i = random.choice(string.ascii_uppercase)
        letter += i
    for i in range(2):
        i = random.randint(0,99)
        number.append(i)
    post += letter[:2] + str(number[0]) + '_' + str(number[1]) + letter[2:] 
    return post
