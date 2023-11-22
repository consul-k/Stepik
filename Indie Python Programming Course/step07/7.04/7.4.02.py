'''

Напишите функцию first_repeated_word , которая принимает строку, состоящую из нескольких слов, слова разделяются между собой пробелом. 
Функция должна найти первое повторяющееся слово и вернуть его в качестве результата. 
Если передана строка, в которой все слова различны, функция first_repeated_word должна вернуть None

Регистр букв при сравнении нужно учитывать

first_repeated_word("ab ca bc ab") => "ab"
first_repeated_word("ab ca bc Ab cA aB bc") => "bc"
first_repeated_word("ab ca bc ca ab bc") => "ca"
first_repeated_word("ab ca bc") => None

Для функции first_repeated_word нужно добавить док-строку  Находит первый дубль в строке

и не забудьте проаннотировать аргументы и возврат функции

Нужно написать только определение функции first_repeated_word 

Sample Input 1:

hello hi hello

Sample Output 1:

hello

Sample Input 2:

hello hi Hello

Sample Output 2:

None

Sample Input 3:

ab ca bc ab

Sample Output 3:

ab

Sample Input 4:

ab ca bc Ab cA aB bc

Sample Output 4:

bc

'''

def first_repeated_word(string):
    'Находит первый дубль в строке'
    string = string.split()
    rep = []
    for i in string:
        if i not in rep:
            rep.append(i)
        else:
            return i
    return None
