'''

Перед вами кортеж words_tuple 

При помощи цикла for обойдите слова, хранящиеся в кортеже words_tuple, и для каждого элемента выведите строку вида

Длина слова {word} = {len_word}

Например, для кортежа words_tuple=('hi', 'world') ответ был бы таким:

Длина слова hi = 2
Длина слова world = 5

Sample Input:

Sample Output:

Длина слова quaint = 6
Длина слова leftovers = 9
Длина слова thesis = 6
Длина слова density = 7
Длина слова retired = 7
Длина слова weak = 4
Длина слова tolerate = 8
Длина слова sensitivity = 11
Длина слова primary = 7
Длина слова definition = 10
Длина слова determine = 9
Длина слова bring = 5
Длина слова monstrous = 9
Длина слова hurl = 4
Длина слова timetable = 9
Длина слова month = 5
Длина слова advocate = 8
Длина слова provoke = 7
Длина слова stress = 6
Длина слова omission = 8

'''

words_tuple = ('quaint', 'leftovers', 'thesis', 'density', 'retired', 'weak', 'tolerate',
               'sensitivity', 'primary', 'definition', 'determine', 'bring', 'monstrous',
               'hurl', 'timetable', 'month', 'advocate', 'provoke', 'stress', 'omission')
for word in words_tuple:
    print(f'Длина слова {word} = {len(word)}')
