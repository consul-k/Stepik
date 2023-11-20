'''

Напишите функцию count_letter(text, letter), которая принимает два параметра:

    text – текст, в котором нужно посчитать сколько раз появилась буква letter, учитывая регистр буквы;
    letter – буква, количество которой мы должны посчитать в text.

Функция count_letter должна выводить на экран найденное количество букв  letter в тексте text

Ваша задача дописать только тело функции count_letter

Sample Input 1:

to be or not to be
b

Sample Output 1:

2

Sample Input 2:

did you pray desdemona
d

Sample Output 2:

4

Sample Input 3:

did you pray desdemona
D

Sample Output 3:

0

'''

def count_letter(text, letter):
    cnt = 0
    for i in text:
        if i == letter:
            cnt += 1
    print(cnt)

text = input()
symbol = input()

count_letter(text, symbol)
