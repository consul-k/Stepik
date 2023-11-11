'''

На вход программе поступает целое число

Ваша задача сохранить в переменную text  строку Even, если введенное число четное, иначе сохраните строку Odd

В качестве ответа необходимо вывести переменную text

Sample Input 1:

8

Sample Output 1:

Even

Sample Input 2:

7

Sample Output 2:

Odd

'''

text = 'Even' if int(input()) % 2 == 0 else 'Odd'
print(text)
